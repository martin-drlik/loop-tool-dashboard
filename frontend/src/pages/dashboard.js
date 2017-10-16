import moment from 'moment';
import Plotly from 'plotly';
import Vue from 'vue';
import { get } from '../api';

const init = async (
    initialData,
) => {
    new Vue({
        el: '#course-dashboard',
        data: {
            weekNum: 0,
            courseId: initialData.courseId,
            numWeeks: initialData.numWeeks,
            courseStart: initialData.courseStart,
            topUsers: {},
            topContent: [],
            topCommunications: [],
            topAssessments: [],
        },
        mounted: async function mounted() {
            this.getOverallDashboard();
        },
        computed: {
            weekStart: function() {
                return moment(this.courseStart).add(this.weekNum - 1, 'weeks').format('MMM D, YYYY');
            },
            weekEnd: function() {
                return moment(this.courseStart).add(this.weekNum, 'weeks').add(-1, 'days').format('MMM D, YYYY');
            },
        },
        methods: {
            async getOverallDashboard() {
                this.getTopContent();
                this.getTopCommunications();
                this.getTopAssessments();
                this.getTopUsers();
                this.plotOverallGraph();
                this.plotHistogram();
            },
            async getWeekDashboard(weekNum) {
                this.getTopContent(weekNum);
                this.getTopCommunications(weekNum);
                this.getTopAssessments(weekNum);
                this.getTopUsers(weekNum);
                this.plotPerWeekGraph(weekNum);
                this.plotWeekMetrics(weekNum);
                this.plotHistogram(weekNum);
            },
            async getTopContent(weekNum = null) {
                this.topContent = await get(`${this.courseId}/top_content/${weekNum ? weekNum + '/' : ''}`);
            },
            async getTopCommunications(weekNum = null) {
                this.topCommunications = await get(`${this.courseId}/top_communication/${weekNum ? weekNum + '/' : ''}`);
            },
            async getTopAssessments(weekNum = null) {
                this.topAssessments = [
                    {page_id: 21, title: 'Page 21', module: 'module', user_views: 6, average_score: 65, attempts: 12},
                    {page_id: 22, title: 'Page 22', module: 'module', user_views: 4, average_score: 86, attempts: 23},
                    {page_id: 23, title: 'Page 23', module: 'module', user_views: 2, average_score: 23, attempts: 32},
                    {page_id: 24, title: 'Page 24', module: 'module', user_views: 7, average_score: 37, attempts: 31},
                    {page_id: 25, title: 'Page 25', module: 'module', user_views: 7, average_score: 87, attempts: 13},
                    {page_id: 26, title: 'Page 26', module: 'module', user_views: 4, average_score: 23, attempts: 12},
                    {page_id: 27, title: 'Page 27', module: 'module', user_views: 3, average_score: 56, attempts: 14},
                    {page_id: 28, title: 'Page 28', module: 'module', user_views: 6, average_score: 45, attempts: 23},
                ];
            },
            async getTopUsers(weekNum = null) {
                // This is getting top users with page views filtered by week
                this.topUsers = await get(`${this.courseId}/top_users`);
            },
            async plotHistogram(weekNum = null) {
            },
            async plotOverallGraph() {
            },
            async plotPerWeekGraph(weekNum) {
                const data = [{
                    x: [1, 2, 3, 4, 5],
                    y: [1, 2, 4, 8, 16]
                }];
                Plotly.plot('graph_container', data, {margin: {t: 0}});
            },
            async plotWeekMetrics(weekNum) {
            },
        },
        watch: {
            weekNum: function (val) {
                if (val >= 1) {
                    this.getWeekDashboard(val)
                } else {
                    this.getOverallDashboard();
                }
            },
        },
    });
};

window.pages = window.pages || {};
window.pages.dashboard = {};
window.pages.dashboard.init = init;
