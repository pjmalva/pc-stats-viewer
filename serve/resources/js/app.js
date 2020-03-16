import './config/bootstrap';
import router from './config/router'
import store from './config/store'

window.Vue = require('vue');

const app = new Vue({
    el: '#app',
    router,
    store,
});
