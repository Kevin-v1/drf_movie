<template>
  <div class="flex items-center justify-center">
    <div class="w-full px-2" style="max-width:1440px;">
        <div id="movie-list" class="p-2 grid grid-cols-2 md:grid-cols-4 lg:grid-cols-6 gap-4">
            <div class="movie" v-for="movie in info.results" :key="movie.id">
                <a :href="'/movie/' + movie.id"> 
                <div class="relative">
                    <div v-if="movie.image_url" class="cover">
                        <img :src="movie.image_url" referrerPolicy="no-referrer" alt="" class="rounded h-full w-full">
                    </div>
                    <div v-else>
                        <img src="@/assets/images/nopicture.jpg" alt="" class="rounded h-full w-full">
                    </div>
                    <div v-if="movie.is_top" class="rounded absolute top-0 bg-purple-600 px-1 text-sm">
                        置顶
                    </div>
                    <div v-if="movie.quality === 1" class="rounded absolute bottom-0 right-0 bg-blue-500 px-1 text-sm ">
                        720p
                    </div>
                    <div v-else-if="movie.quality === 2" class="rounded absolute bottom-0 right-0 bg-blue-500 px-1 text-sm ">
                        1080p
                    </div>
                    <div v-else-if="movie.quality === 3" class="rounded absolute bottom-0 right-0 bg-blue-500 px-1 text-sm ">
                        4k
                    </div>
                </div>
                <p> {{ movie.movie_name }}({{movie.release_year}})</p>
                <p class="text-sm text-primary-200">{{movie.language}}</p>
                </a>
            </div>
        </div>  
    </div>
  </div>
    <!-- 添加Page组件，并将info数据作为props传递给Page组件 -->
    <Page :info="info"></Page>

</template>

<script>
    import axios from 'axios';
    import Page from '@/components/Page.vue'

    export default {
        name: 'MovieListView',
        components: { Page },
        data: function () {
            return {
                info: ''
            }
        },
        mounted() {
            this.get_movie_data()
        },
        methods: {
            // 获取电影列表数据
            get_movie_data: function () {
                let url = '/api/movie';
                const page = Number(this.$route.query.page);
                const search = this.$route.query.search;
                const category = this.$route.query.category;
                const region = this.$route.query.region;
                const params = new URLSearchParams(); // 创建一个URLSearchParams对象
                // 拼接参数
                if (page) {
                    params.append('page', page);
                }
                if (search) { 
                    params.append('movie_name', search);
                }
                if (category) {
                    params.append('category_id', category);
                }
                if (region) {
                    params.append('region', region);
                }
                url = url + '?' + params.toString()
                console.log(url)
                // 发送请求
                axios
                    .get(url)
                    .then(response => (this.info = response.data))
            }
        },
        watch: {
            // 监听路由是否有变化
            $route() {
                this.get_movie_data()
            }
        }
    }
</script>


