'use strict';

const { argv } = require('yargs');

function getClientEnvironment(publicUrl) {
    const node_env = process.env.NODE_ENV || 'development';
    var processEnv = Object
        .keys(process.env)
        .reduce((env, key) => {
            env[key] = JSON.stringify(process.env[key]);
            return env;
        },
        {
            // Useful for determining whether we’re running in production mode.
            NODE_ENV: JSON.stringify(node_env),
            // Useful for resolving the correct path to static assets in `public`.
            // For example, <img src={process.env.PUBLIC_URL + '/img/logo.png'} />.
            // This should only be used as an escape hatch. Normally you would put
            // images into the `src` and `import` them in code to get their paths.
            PUBLIC_URL: JSON.stringify(publicUrl),
        });
    return {
        'process.env': processEnv,
    };
}

module.exports = ({
    // one of 'development' or 'production'
    environment,

    // undefined (use default), true (more verbose default), or webpack 'devtool' setting
    sourceMap = undefined,

    // Include settings for bootstrap-sass?
    bootstrap = true,
    // Add bootstrap to the sass includePath?
    // allows you to do cleaner imports, eg
    //      @import 'bootstrap/buttons';
    // Not done by default because it breaks IDE discoverability
    bootstrapSassIncludePath = false,

    // Include settings for jQuery?
    jQuery = true,

    // Enable webpack HMR?
    hot = true,

    // Dev server config
    serverHost = '0.0.0.0',
    serverPort = '3011',

} = {}) => {
    // NOTE: We are using require() here to be consistent as some of these may
    // be optional
    const BundleTracker = require('webpack-bundle-tracker');
    const CaseSensitivePathsPlugin = require('case-sensitive-paths-webpack-plugin');
    const ExtractTextPlugin = require('extract-text-webpack-plugin');
    const assert = require('assert');
    const autoprefixer = require('autoprefixer');
    const path = require('path');
    const fs = require('fs');
    const webpack = require("webpack");

    const isDev = environment != 'production';
    const FRONTEND_DIR = './';
    const NODE_MODULES_DIR = path.join(FRONTEND_DIR, 'node_modules') + '/';
    const OUTPUT_DIR_BASE = path.join(FRONTEND_DIR, 'dist') + '/';
    const OUTPUT_DIR_RELATIVE = `/${environment}/`;
    // In dev assets are served from dev server, otherwise filesystem
    const PUBLIC_PATH = isDev ? `http://${serverHost}:${serverPort}/` : '/static/dist' + OUTPUT_DIR_RELATIVE;
    const INLINE_BINARY_DATA_LIMIT = 8192;

    assert(['development', 'production'].indexOf(environment) >= 0, '"environment" option is not valid');

    if (sourceMap === true)      sourceMap = isDev ? 'eval-source-map' : 'source-map';
    if (sourceMap === undefined) sourceMap = isDev ? 'eval-source-map' : 'hidden-source-map';

    const srcRoot = './src/';

    const entry = [
        `${srcRoot}index.js`,
    ];

    if (isDev && hot) {
        // HMR related loaders must come first
        entry.unshift(`webpack-hot-middleware/client?path=http://${serverHost}:${serverPort}/__webpack_hmr`);
    }

    // ----------------------------------------------------------------------
    // Base config
    let conf = {
        devtool: sourceMap,
        entry,
        output: {
            path: path.join(__dirname, OUTPUT_DIR_BASE, OUTPUT_DIR_RELATIVE),
            // TODO: chunkhash to provide cache busting. can be removed when we have
            // support in django-webpack-loader to include assets with
            // timestamp query parameter.
            filename: isDev ? "[name].bundle.js" : "[name].[chunkhash].bundle.js",
            publicPath: PUBLIC_PATH,
        },
        module: {
            rules: [],
            noParse: /jquery/,
        },
        plugins: [
            new webpack.DefinePlugin(getClientEnvironment(PUBLIC_PATH)),
            // Require case to match on imports - prevents builds breaking on
            // case sensitive filesystems
            new CaseSensitivePathsPlugin(),
            new webpack.LoaderOptionsPlugin({
                options: {
                    // Autoprefixing is done with postcss - postcss-loader
                    // included in getCssLoader
                    postcss: function() {
                        return [
                            autoprefixer({
                                browsers: [
                                    '>1%',
                                    'last 4 versions',
                                    'Firefox ESR',
                                    'not ie < 9',
                                ]
                            }),
                        ];
                    },
                    eslint: {
                        // Allow build to continue in dev, just emit warnings
                        emitWarning: isDev,
                        // Prevent production builds is linting fails
                        failOnWarning: !isDev,
                        failOnError: !isDev,
                    },
                },
            }),
            new BundleTracker({
                filename: OUTPUT_DIR_BASE + (isDev ? '/webpack-stats-dev.json' : '/production/webpack-stats.json'),
            }),
        ],
        resolve: {
            alias: {},
        },
    };

    if (isDev) {
        if (hot) {
            conf.plugins.push(...[
                // Enables HMR
                new webpack.HotModuleReplacementPlugin(),
                // Prints readable module names on HMR updates rather than a
                // number
                new webpack.NamedModulesPlugin(),
            ]);
        }
    } else {
        conf.plugins.push(...[
            // TODO: Remove chunkhash once we have cache busting
            // using query parameters going
            new ExtractTextPlugin('[name].[chunkhash].css'),
        ]);
    }

    // ------------------------------------------------------------------
    // Config that may be modified by options
    let sassIncludePaths = [];
    let babelPresets = [
        ['es2015', {
            // This enables webpack2 tree-shaking
            modules: false,
        }],
    ];
    let babelPlugins = [
        'transform-async-to-generator',
        'transform-runtime',
        'transform-class-properties',
        'transform-object-rest-spread',
    ];
    let babelPluginsProd = [];

    // ----------------------------------------------------------------------
    // jQuery
    if (jQuery) {
        conf.plugins.push(new webpack.ProvidePlugin({
            $: "jquery",
            jQuery: "jquery"
        }));
    }

    // ----------------------------------------------------------------------
    // bootstrap (sass version)
    if (bootstrap) {
        if (bootstrapSassIncludePath) {
            const bootstrapAssetsPath = path.resolve(NODE_MODULES_DIR, './bootstrap-sass/assets');
            sassIncludePaths += [
                bootstrapAssetsPath + '/stylesheets/',
                bootstrapAssetsPath + '/fonts/',
            ];
        }
        conf.entry.push('bootstrap-sass/assets/javascripts/bootstrap.js');
    }


    // ------------------------------------------------------------------

    // Binary files
    conf.module.rules.push({
        test: /\.(jpg|jpeg|png|gif|eot|svg|ttf|woff|woff2)$/,
        loader: 'url-loader',
        options: { limit: INLINE_BINARY_DATA_LIMIT }
    });

    // ------------------------------------------------------------------
    // JS
    conf.module.rules.push({
        test: /\.(js|jsx)$/,
        loader: 'babel-loader',
        exclude: [
            path.resolve(NODE_MODULES_DIR),
            /node_modules/,
            // path.resolve(BUILD_DIR),
        ],
        options: {
            presets: babelPresets,
            plugins: babelPlugins,
            env: {
                development: {
                    plugins: [],
                    presets: [],
                },
                production: {
                    plugins: babelPluginsProd,
                    presets: [],
                },
            },
            babelrc: false,
            cacheDirectory: false
        },
    });

    conf.module.rules.push({
        test: /\.json$/,
        loader: 'json-loader'
    });


    // ------------------------------------------------------------------
    // Vue / Client / Plotly application setup
    const pagesRoot = path.resolve(`${srcRoot}pages`);
    const files = fs.readdirSync(pagesRoot);
    files.forEach(filename => {
      const entryName = filename.replace('.js', '');
      conf.entry.push(path.resolve(pagesRoot, entryName));
    });

    // See https://vuejs.org/v2/guide/installation.html#Standalone-vs-Runtime-only-Build
    conf.resolve.alias['vue$'] = "vue/dist/vue.js";
    // Setup support for .vue files
    let vueConfig = {
      test: /\.vue$/,
      loader: 'vue-loader',
      // vue-loader options goes here
      options: {}
    };
    if (!isDev) {
      vueConfig.options.loaders = {
        css: ExtractTextPlugin.extract({
          loader: 'css-loader',
          fallbackLoader: 'vue-style-loader',
        }),
      };
    }
    conf.module.rules.push(vueConfig);

    conf.resolve.alias['plotly$'] = "plotly.js/dist/plotly.js";
    conf.resolve.alias['moment$'] = "moment/moment.js";


    // ------------------------------------------------------------------
    // CSS/SCSS
    const getCssLoader = (includeSass) => {
        const cssUse = [
            {
                loader: 'css-loader',
                options: {
                    modules: false,
                    localIdentName: '[name]__[local]__[hash:base64:5]',
                },
            },
            // postcss is just used for autoprefixing; see plugins section for setup
            'postcss-loader',
        ];
        if (includeSass) {
            let sassLoader = {
                loader: 'sass-loader',
                options: {
                    includePaths: sassIncludePaths,
                },
            };
            // make things a little cleaner
            if (!sassLoader.options.includePaths.length) delete sassLoader.options.includePaths;
            if (!Object.keys(sassLoader.options).length) delete sassLoader.options;
            cssUse.push(sassLoader);
        }
        // In production css extracted to file, dev uses style-loader to load
        // it from js
        return !isDev ? ExtractTextPlugin.extract({ use: cssUse }) : ['style-loader', ...cssUse];
    };

    const cssRule = {
        test: /\.(css)$/,
        use: getCssLoader(false),
    };
    const sassRule = {
        test: /\.(scss)$/,
        use: getCssLoader(true),
    };
    conf.module.rules.push(cssRule);
    conf.module.rules.push(sassRule);

    return conf;
};
