const state = {
  checked: JSON.parse(localStorage.getItem("changeChecked"))
};

const getters = {
  getChecked: state => state.checked
};

const actions = {
  setChecked({ commit }) {
    commit("changeChecked");
    localStorage.setItem("changeChecked", state.checked);
  }
};

const mutations = {
  changeChecked: state => (state.checked = !state.checked)
};

export default {
  state,
  getters,
  actions,
  mutations
};
