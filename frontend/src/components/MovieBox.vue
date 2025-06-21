<template>

<div class="flex items-center justify-center">
    <div class="w-full px-2" style="max-width:1440px;">
        <div id="main" class="bg-primary-300 p-6 text-black">
            <div class="flex rounded bg-white mx-4 py-6">
                <div class="mx-6" >
                    <div class="" style="min-height: 259px; max-height: 300px;height: 274px;">
                    <img :src="movie.image_url" class="h-full w-full">
                    </div>
                    <button v-on:click="collect_or_cancle(movie.id)" id="collect" class="copy text-white w-full px-4 py-1 mt-2 text-sm bg-blue-500 rounded border">
                        {{ collectMessage }}
                    </button>
                </div>
                <div id="info" data-movie-id="443">
                <ul>
                    <li class="text-lg font-semibold"> {{ movie.movie_name }}</li>
                    <li>导演: {{ movie.director }} </li>
                    <li>编剧: {{ movie.scriptwriter}}</li>
                    <li>主演: {{ movie.actors }}</li>
                    <li>语言: {{ movie.language }}</li>
                    
                    <li>首播: 2022年7月5日 </li>
                    <li>集数: 27</li>
                    
                    <li>类型: {{ movie.types }} </li>
                    <li>制片国家/地区: 
                        <span v-if="movie.region === 1">中国大陆</span>
                        <span v-else-if="movie.region === 2">中国香港</span>
                        <span v-else-if="movie.region === 3">中国台湾</span>
                        <span v-else-if="movie.region === 4">美国</span>
                        <span v-else-if="movie.region === 5">韩国</span>
                        <span v-else-if="movie.region === 6">日本</span>
                        <span v-else>其他</span>
                    </li>
                    <li>又名: {{ movie.alternate_name }} </li>
                    <li>豆瓣评分: {{ movie.rate }}</li>
                </ul>
                </div>
            </div>
            <div class="rounded bg-white mx-4 my-4 py-6 ">
                <div class="px-6">
                    <h1 class="text-lg mb-6 font-semibold">简介</h1>
                    <p>
                        {{ movie.review }}
                    </p>
                </div>
            </div>
            <div id="download_info" class="rounded bg-white mx-4 mt-4 py-6 "> 
                <h1 class="text-lg mb-6 font-semibold px-6">网盘地址</h1>

                <div v-if="movie.download_info" class="px-6">
                    <div v-if="download_info">
                        {{ movie.download_info }}
                    </div>
                    <div v-else class="flex flex-col items-center justify-center mx-6 rounded h-28 bg-gradient-to-r from-blue-500 to-purple-500">
                        <button v-on:click="check_member_status" id="check_member" class="rounded-center text-white">获取网盘地址</button>
                    </div>
                </div>
                <div v-else class="px-6">
                        暂无下载地址
                    </div>
            </div>
        </div>
    </div>
</div>
</template>

<script>
import axios from 'axios'
import showMessage from '@/utils/message.js'

export default {
    name: 'MovieBox',
    data: function() {
        return {
            movie: {},
            isCollected: false,
            collectMessage: '添加收藏',
            download_info: false,
            userInfo:'',
        }
    },
    mounted() {
        const movie_id = this.$route.params.id
        // 获取电影详细信息
        this.get_movie_detail(movie_id)
        if (!this.$store.state.isLogin) {
            this.collectStatus = '添加收藏'
        }
        else {
            this.get_collect_status(movie_id)
        }

    },
    methods: {
        get_movie_detail(movie_id) {
            axios
                .get('/api/movie/' + movie_id)
                .then(response => (this.movie = response.data))
        },

        get_collect_status(movie_id) {
            axios
                .get('/api/collects/'+movie_id+'/is_collected/')
                .then(response => {
                    this.collectStatus = response.data.is_collected
                    if (this.collectStatus) {
                        this.collectMessage = '取消收藏'
                    }
                    else {
                        this.collectMessage = '添加收藏'
                    }
                })
        },

        collect_or_cancle(movie_id) {
            const isLogin = this.$store.state.isLogin;
            // 判断登录
            if (!isLogin) {
                showMessage('请先登录！', 'error', ()=>{
                    this.$router.push({ name: "Login" });
                })
                return 
            } 
            if (this.collectStatus) {
                this.cancle_collet_movie(movie_id)
            } 
            else {
                this.collet_movie(movie_id)
            }
            
        },

        collet_movie(movie_id) {
            axios
                .post('/api/collects/', {movie_id: movie_id})
                .then(response => {
                    showMessage('收藏成功','info')
                    this.collectStatus = true
                    this.collectMessage = '取消收藏'
                })
                .catch(error => {
                    showMessage('收藏失败')
                })
        },

        cancle_collet_movie(movie_id) {
            axios
                .delete('/api/collects/'+movie_id)
                .then(response => {
                    showMessage('取消成功','info')
                    this.collectStatus = false
                    this.collectMessage = '添加收藏'
                })
                .catch(error => {
                    showMessage('取消失败')
                })
        },
        // 判断用户状态
        check_member_status() {
            if(!this.$store.state.isLogin) {
                showMessage('请先登录！', 'error', ()=>{
                    this.$router.push({ name: "Login" });
                })
                return 
            }
            axios
                .get('/api/users/me/')
                .then(response => {
                    this.userInfo = response.data
                    if (this.userInfo.profile.is_upgrade) {
                        this.download_info = true
                    }
                    else {
                        showMessage('请先升级会员！', 'error', ()=>{
                            this.$router.push({ name: "MemberCard" });
                        })
                    }
                })
                .catch(error => {
                    showMessage('获取用户状态失败')
                })
        }
    }
    
}
</script>