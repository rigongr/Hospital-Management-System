// import router from "../../router";
import axios from 'axios';

export const state = {
  products: [],
};

export const getters = {
  allProducts: (state) => state.products,
};

const actions = {
  getAllProducts({ commit }) {
    axios
      .get('http://localhost:5000/api/products')
      .then((res) => {
        commit('setProducts', res.data);
      })
      .catch((err) => {
        console.log(err);
      });
  },

  getProduct({ commit }, product) {
    axios
      .get('http://localhost:5000/api/products/' + product._id)
      .then((res) => {
        commit('setProducts', res.data);
      })
      .catch((err) => {
        console.log(err);
      });
  },

  deleteProduct({ commit }, product) {
    axios
      .delete('http://localhost:5000/api/products/' + product._id)
      .then((res) => {
        console.log(res);
        axios
          .get('http://localhost:5000/api/products')
          .then((res) => {
            commit('setProducts', res.data);
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

  addProduct({ commit }, data) {
    axios
      .post(`http://localhost:5000/api/products`, data)
      .then((response) => {
        //   axios
        //     .get("http://localhost:5000/api/products")
        //     .then((res) => {
        //       commit("setProducts", res.data);
        //       console.log(res);
        //     })
        //     .catch((err) => {
        //       console.log(err);
        //     });
        commit('setProducts', response.data);
      })
      .catch((err) => {
        console.log(err);
      });
  },
};

const mutations = {
  setProducts: (state, products) => (state.products = products),
};

export default {
  state,
  getters,
  actions,
  mutations,
};
