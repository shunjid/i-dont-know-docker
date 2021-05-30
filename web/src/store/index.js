import Vue from "vue";
import Vuex from "vuex";
import axios from "axios";

Vue.use(Vuex);

const api = "http://localhost:5051/api";

export default new Vuex.Store({
  state: {
    users: [],
    snackbarText: "",
    snackbarColor: "",
    isPosting: false,
    isFetching: false,
  },
  mutations: {
    SET_USERS(state, value) {
      state.users = value;
    },
    SHOW_SNACKBAR(state, value) {
      state.snackbarText = value.text;
      state.snackbarColor = value.color;
    },
    SET_IS_POSTING(state, value) {
      state.isPosting = value;
    },
    SET_IS_FETCHING(state, value) {
      state.isFetching = value;
    },
  },
  actions: {
    getUsers(context) {
      context.commit("SET_IS_FETCHING", true);

      axios
        .get(`${api}/users`)
        .then((res) => {
          context.commit("SET_USERS", res.data.data);
        })
        .catch(() => {
          context.commit("SHOW_SNACKBAR", {
            text: "Something went wrong",
            color: "error",
          });
        })
        .finally(() => {
          context.commit("SET_IS_FETCHING", false);
        });
    },
    addUser(context, payload) {
      context.commit("SET_IS_POSTING", true);

      axios
        .post(`${api}/users`, payload)
        .then(() => {
          context.dispatch("getUsers");

          context.commit("SHOW_SNACKBAR", {
            text: "User added successfully",
            color: "primary",
          });
        })
        .catch((error) => {
          context.commit("SHOW_SNACKBAR", {
            text: error.response
              ? error.response.data.message
              : "Something went wrong",
            color: "error",
          });
          console.log(error);
        })
        .finally(() => {
          context.commit("SET_IS_POSTING", false);
        });
    },
    updateUser(context, payload) {
      const id = payload.id;

      const body = {
        emailAddress: payload.email,
        firstName: payload.firstName,
        lastName: payload.lastName,
        mobileNumber: payload.mobile,
      };

      axios
        .put(`${api}/users/${id}`, body)
        .then(() => {
          context.commit("SHOW_SNACKBAR", {
            text: "Contact updated successfully",
            color: "primary",
          });
        })
        .catch((error) => {
          context.commit("SHOW_SNACKBAR", {
            text: error.response
              ? error.response.data.message
              : "Something went wrong",
            color: "error",
          });
          context.dispatch("getUsers");
        });
    },
  },
});
