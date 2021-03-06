import Vue from 'vue';
import { get } from '../api';
import RangeGraph from '../components/range_graph.vue';
import HistogramGraph from '../components/histogram_graph.vue';

const init = async (
    initialData,
) => {
    const RESOURCE_NUM_HISTOGRAM_BINS = window.__APP_CONTEXT__.RESOURCE_NUM_HISTOGRAM_BINS;

    new Vue({
        el: '#resource-page',
        data: {
            courseId: initialData.courseId,
            courseStart: initialData.courseStart,
            numWeeks: initialData.numWeeks,
            resourceId: initialData.resourceId,
            resourceType: initialData.resourceType,
            histogramNumBins: RESOURCE_NUM_HISTOGRAM_BINS,
        },
        asyncComputed: {
            notViewedStudents() {
                return get(`${this.courseId}/resource/${this.resourceId}/not_viewed_students`);
            },
        },
        components: {
            RangeGraph,
            HistogramGraph,
        },
    });
};

window.pages = window.pages || {};
window.pages.resourcePage = {};
window.pages.resourcePage.init = init;
