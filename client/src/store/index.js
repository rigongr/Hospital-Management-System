import Vue from 'vue';
import Vuex from 'vuex';
import users from './modules/users';
import global from './modules/global';
import product from './modules/product';
import service from './modules/service';
import ticket from './modules/ticket';
import cart from './modules/cart';

Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
    product,
    global,
    users,
    service,
    ticket,
    cart,
  },
});
