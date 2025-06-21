<template>
    <div id="main-body" class="bg-primary-100 flex justify-center h-screen">
    <section class="container flex justify-center items-center rounded ">
        <div class="hidden md:block">
          <img src="../assets/images/bg.png" alt="" class="rounded-l max-h-[500px]">
        </div>
        <div class="rounded-r w-80 h-[500px] my-8 px-2 py-4 bg-white shadow shadow-gray-300">
          <div class="text-center text-lg py-6">用户注册</div>
          <form id="register_form" class="px-4">
            <div class="flex justify-left items-center relative h-10 px-4  my-2 rounded border-solid border border-gray-400">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 text-gray-300 mr-2" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                <path stroke-linecap="round" stroke-linejoin="round" d="M5.121 17.804A13.937 13.937 0 0112 16c2.5 0 4.847.655 6.879 1.804M15 10a3 3 0 11-6 0 3 3 0 016 0zm6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
              </svg>
              <input v-model="username" type="text"  placeholder="请输入用户名" class="outline-0 text-sm">
            </div>
            <div class="flex justify-left items-center relative h-10 px-4  my-2 rounded border-solid border border-gray-400">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 text-gray-300 mr-2" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                <path stroke-linecap="round" stroke-linejoin="round" d="m19 2-8.4 7.05a1 1 0 0 1-1.2 0L1 2m18 0a1 1 0 0 0-1-1H2a1 1 0 0 0-1 1m18 0v12a1 1 0 0 1-1 1H2a1 1 0 0 1-1-1V2" />
              </svg>
              <input v-model="email" type="text"  placeholder="请输入邮箱" class="outline-0 text-sm">
            </div>
            <div class="flex justify-left items-center relative h-10 px-4  my-2 rounded border-solid border border-gray-400">

              <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 text-gray-300 mr-2" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                <path stroke-linecap="round" stroke-linejoin="round" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z" />
              </svg>
              <input v-model="password" type="password"  placeholder="请输入密码" class="outline-0 text-sm">
            </div>
            <div class="flex justify-left items-center relative h-10 px-4  my-2 rounded border-solid border border-gray-400">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 text-gray-300 mr-2" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                <path stroke-linecap="round" stroke-linejoin="round" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z" />
              </svg>
              <input v-model="password2" type="password" placeholder="确认密码" class="outline-0 text-sm">
            </div>
            <div class="flex items-center">
              <div class="flex  items-center relative h-10 w-32 px-4  my-2 rounded border-solid border border-gray-400">
                  <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 text-gray-300 mr-2" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z" />
                  </svg>
                  <input type="text" id="vcode" name="vcode" placeholder="请输入验证码" class="outline-0 text-sm w-24">
              </div>
              <img id="signInVcodeImg" src="" onclick="refreshVcode()" />
            </div>
            <div class="pt-6">
              <button v-on:click.prevent="submitForm" id="login" class="rounded bg-green-500 w-full h-8 text-white">注册</button>
            </div>
            <div class="text-center text-sm my-2">
              已有账号
              <a class="text-blue-500" href="/login">去登录</a>
            </div>
          </form>
        </div>
    </section>
</div>

</template>

<script>
import axios from 'axios'
import showMessage from '@/utils/message.js'

export default {
    name: 'Register',
    data: function(){
        return {
            username: '',
            password: '',
            password2: '',
            email: '',
        }
    },
    methods: {
        submitForm() {
          if (this.username === '') {
            showMessage('用户名不能为空')
            return 
          }

          if (this.email === '') {
            showMessage('不能为空')
            return 
          }

          if (this.password === '') {
            showMessage('密码不能为空')
            return 
          }

          if (this.password !== this.password2) {
            showMessage('2次密码不一致')
            return 
          } 
          // 没有错误，提交表单

            const formData = {
              username: this.username,
              email: this.email,
              password: this.password
            }
          // const that = this;
            axios
              .post('/api/users/', formData)
              .then(response => {
                  // 登录成功后回到登录页面
                  showMessage('注册完成，请到邮箱中激活账号')
                  that.$router.push({name: 'Login'});
              })
              .catch( error => {
                // 遍历所有错误信息
                const errorData = error.response.data
                const errorMessages = Object.values(errorData).flat(); 
                for (let i = 0; i < errorMessages.length; i++) {
                  showMessage(errorMessages[i])
                }
              })
        }
    }
}
</script>



