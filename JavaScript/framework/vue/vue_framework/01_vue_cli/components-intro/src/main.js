import Vue from 'vue'
import App from './App.vue'

// For main can acess the another components, is necessaire register the component here
// import counterButton from './counterButton.vue'
import Counters from './Counters.vue'

Vue.config.productionTip = false

// Vue.component('testComponent', counterButton)
Vue.component('counters', Counters)

new Vue({
  render: h => h(App),
}).$mount('#app')
