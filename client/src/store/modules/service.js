// import router from "../../router";
import axios from 'axios';

export const state = {
  services: [],
};

export const getters = {
  allServices: (state) => state.services,
};

const actions = {
  getAllServices({ commit }) {
    axios
      .get('http://localhost:5000/api/services')
      .then((res) => {
        console.log(res);
        commit('setServices', res.data);
      })
      .catch((err) => {
        console.log(err);
      });
  },

  deleteService({ commit }, service) {
    axios
      .delete('http://localhost:5000/api/services/' + service._id)
      .then((res) => {
        console.log(res);
        axios
          .get('http://localhost:5000/api/services')
          .then((res) => {
            commit('setServices', res.data);
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

  addService({ commit }, data) {
    axios
      .post(`http://localhost:5000/api/services`, data)
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
        commit('setServices', response.data);
      })
      .catch((err) => {
        console.log(err);
      });
  },

  updateService({ commit }, service) {
    axios
      .put(`http://localhost:5000/api/services/` + service._id, service)
      .then((response) => {
        commit('setServices', response.data);
      })
      .catch((err) => {
        console.log(err);
      });
  },
};

const mutations = {
  setServices: (state, services) => (state.services = services),
};

export default {
  state,
  getters,
  actions,
  mutations,
};
