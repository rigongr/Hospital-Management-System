// import router from "../../router";
import axios from 'axios';

export const state = {
  tickets: [],
};

export const getters = {
  allTickets: (state) => state.tickets,
};

const actions = {
  getAllTickets({ commit }) {
    axios
      .get('http://localhost:5000/api/tickets')
      .then((res) => {
        console.log(res);
        commit('setTickets', res.data);
      })
      .catch((err) => {
        console.log(err);
      });
  },

  deleteTicket({ commit }, ticket) {
    axios
      .delete('http://localhost:5000/api/tickets/' + ticket._id)
      .then((res) => {
        console.log(res);
        axios
          .get('http://localhost:5000/api/tickets')
          .then((res) => {
            commit('setTickets', res.data);
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

  addTicket({ commit }, data) {
    axios
      .post(`http://localhost:5000/api/tickets`, data)
      .then((response) => {
        //   axios
        //     .get("http://localhost:5000/api/tickets")
        //     .then((res) => {
        //       commit("setTickets", res.data);
        //       console.log(res);
        //     })
        //     .catch((err) => {
        //       console.log(err);
        //     });
        commit('setTickets', response.data);
      })
      .catch((err) => {
        console.log(err);
      });
  },

  updateTicket({ commit }, ticket) {
    axios
      .put(`http://localhost:5000/api/tickets/` + ticket._id, ticket)
      .then((response) => {
        commit('setTickets', response.data);
      })
      .catch((err) => {
        console.log(err);
      });
  },
};

const mutations = {
  setTickets: (state, tickets) => (state.tickets = tickets),
};

export default {
  state,
  getters,
  actions,
  mutations,
};
