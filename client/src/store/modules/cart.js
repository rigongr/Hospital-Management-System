// import router from "../../router";
import axios from 'axios';

export const state = {
  carts: [],
};

export const getters = {
  allCarts: (state) => state.carts,
};

const actions = {
  getAllCarts({ commit }) {
    axios
      .get('http://localhost:5000/api/cart')
      .then((res) => {
        console.log(res);
        commit('setCarts', res.data);
      })
      .catch((err) => {
        console.log(err);
      });
  },

  deleteCart({ commit }, cart) {
    axios
      .delete('http://localhost:5000/api/cart/' + cart)
      .then((res) => {
        console.log(res);
        axios
          .get('http://localhost:5000/api/cart')
          .then((res) => {
            commit('setCarts', res.data);
            // commit("setUsers", res.data);
          })
          .catch((err) => {
            console.log(err);
          });
      })
      .catch((err) => {
        console.log(err);
      });
  },

  addCart({ commit }, data) {
    axios
      .post(`http://localhost:5000/api/cart`, data)
      .then((response) => {
        //   axios
        //     .get("http://localhost:5000/api/services")
        //     .then((res) => {
        //       commit("setServices", res.data);
        //       console.log(res);
        //     })
        //     .catch((err) => {
        //       console.log(err);
        //     });
        commit('setCarts', response.data);
      })
      .catch((err) => {
        console.log(err);
      });
  },

  updateCart({ commit }, cart) {
    axios
      .put(`http://localhost:5000/api/cart/` + cart._id, cart)
      .then((response) => {
        commit('setCarts', response.data);
      })
      .catch((err) => {
        console.log(err);
      });
  },
};

const mutations = {
  setCarts: (state, carts) => (state.carts = carts),
};

export default {
  state,
  getters,
  actions,
  mutations,
};
