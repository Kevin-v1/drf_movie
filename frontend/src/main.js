import { createApp } from 'vue' // 创建应用
import App from './App.vue' // 入口文件
import router from './router' // 路由
import store from './store' // 状态管理
import './assets/css/tailwind.css' // 样式

createApp(App).use(store).use(router).mount('#app')
