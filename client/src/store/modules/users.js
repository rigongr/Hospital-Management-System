// import axios from "axios";
// import router from "../../router";
import axios from "axios";

export const state = {
  users: [],
  logedIn: false,
  userData: null,
};

export const getters = {
  allUsers: (state) => state.users,
  getLogedIn: (state) => state.logedIn,
  getUser: (state) => state.userData,
};

const setLocalStorage = (data) => {
  localStorage.setItem(
    "userData",
    JSON.stringify({
      userId: data.userId,
      email: data.email,
      token: data.token,
    })
  );
};

const actions = {
  logedInTrue({ commit }, data) {
    commit("setLogedInToTrue");
    if (data.user) {
      localStorage.setItem("email", JSON.stringify(data.user.email));
      commit("setUser", data);
    } else {
      commit("setUser", null);
    }
  },

  getEmailFromLocalStorage({ commit }) {
    const userData = JSON.parse(localStorage.getItem("userData"));
    if (userData) {
      commit("setUser", userData);
      commit("setLogedInToTrue");
    }
  },

  logedInFalse({ commit }) {
    localStorage.removeItem("userData");
    commit("setLogedInToFalse");
    commit("setUserNull");
  },

  getAllUsers({ commit }) {
    axios
      .get("http://localhost:5000/api/users")
      .then((res) => {
        console.log(res);
        commit("setUsers", res.data);
      })
      .catch((err) => {
        console.log(err);
      });
  },

  deleteUsr({ commit }, user) {
    axios
      .delete("http://localhost:5000/api/users/" + user._id)
      .then((res) => {
        console.log(res);
        axios
          .get("http://localhost:5000/api/users")
          .then((res) => {
            console.log(res);
            commit("deleteUser", res.data);
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
  login({ commit }, data) {
    axios
      .post(`http://172.18.0.4:5000/login`, data)
      .then((response) => {
        console.log(response.data.access_token);
        setLocalStorage(response.data);
        commit("setUser", response.data);
      });
    setLocalStorage(data);
    commit("setUser", data);
  },
  signup({ commit }, data) {
    axios
      .post(`http://172.18.0.4:5000/register`, data)
      .then((response) => {
        setLocalStorage(response.data);
        commit("setUser", response.data);
        console.log(response, "SIGNUP");
      });
  },
};

const mutations = {
  setUsers: (state, users) => (state.users = users),
  setLogedInToTrue: (state) => (state.logedIn = true),
  setLogedInToFalse: (state) => (state.logedIn = false),
  setUser: (state, data) => {
    state.userData = data;
  },
  setUserNull: (state) => {
    state.userData = null;
  },
  deleteUser: (state, users) => (state.users = users),
};

export default {
  state,
  getters,
  actions,
  mutations,
};
