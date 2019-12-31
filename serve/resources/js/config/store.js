import Vue from 'vue'
import Vuex from 'vuex'
import createPersistedState from 'vuex-persistedstate'

Vue.use(Vuex)

export default new Vuex.Store({
  plugins: [
    createPersistedState({
      key: "bce072b8c4399e048f58a4PCS"
    })
  ],
  strict: process.env.NODE_ENV !== 'production',
  state: {
    user: {},
  },
  mutations: {
    SET_CURRENT_USER (state, data) {
      state.user = data
    },
  },
  actions: {
    login ({ commit }, obj) {
      commit('SET_CURRENT_USER', obj)
    },

    logout ({ commit }) {
      commit('SET_CURRENT_USER', {})
    },
  },
  getters: {
    isLogged: state => state.user != {},
    getCurrentUser: state => state.user,
  }
})
