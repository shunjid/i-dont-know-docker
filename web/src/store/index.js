import Vue from "vue";
import Vuex from "vuex";
import axios from "axios";

Vue.use(Vuex);

const api = "http://localhost:5051/api";

export default new Vuex.Store({
  state: {
    users: [],
  },
  mutations: {
    SET_USERS(state, value) {
      state.users = value;
    },
  },
  actions: {
    getUsers(context) {
      axios
        .get(`${api}/users`)
        .then((res) => {
          context.commit("SET_USERS", res.data.data);
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
});
