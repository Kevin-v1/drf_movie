import { createStore } from 'vuex'

export default createStore({
  state: {
    isLogin: false,
    token: ''
  },
  getters: {
  },
  mutations: {
    initializeStore(state) {
      if (localStorage.getItem('token')) {
        state.isLogin = true
        state.token = localStorage.getItem('token')
      }
      else {
        state.isLogin = false
        state.token = ''
      }
    },
    setLoginStatus(state, status) {
      state.isLogin = status
    },
    setToken(state, token) {
      state.token = token
    },
    removeToken(state, token) {
      state.token = ''
    },

  },
  actions: {
  },
  modules: {
  }
})

