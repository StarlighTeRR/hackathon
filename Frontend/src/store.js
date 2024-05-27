import Vuex from 'vuex'

export const store = new Vuex.Store({
  state: {
    authToken: null
  },
  mutations: {
    setAuthToken (state, token) {
      state.authToken = token
    },
    clearAuthToken (state) {
      state.authToken = null
    }
  },
  actions: {
    saveAuthToken ({ commit }, token) {
      commit('setAuthToken', token)
    },
    removeAuthToken ({ commit }) {
      commit('clearAuthToken')
    }
  },
  getters: {
    isAuthenticated: (state) => !!state.authToken
  }
})

export default store
