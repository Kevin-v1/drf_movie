<template>
    <div id="container" class="text-white text-sm bg-primary-300 min-h-screen pb-4"> 
        <Header/>
        <div id="main" class="bg-primary-300 p-6 text-black">
            <div class="rounded bg-white mx-4 my-4 py-6 ">
                <div class="px-6">
                    <h1 class="text-lg font-semibold">我的收藏</h1>
                </div>
            </div>
            <div class="rounded bg-white mx-4 mt-4 py-6 "> 
                <div v-if="info">
                    <div id="movie-list" class="p-2 grid grid-cols-2 md:grid-cols-4 lg:grid-cols-6 gap-4">
                        <div class="movie" v-for="movie in info">
                            <a :href="'/movie/' + movie.id"> 
                            <div class="relative">
                                <div v-if="movie.image_url" class="cover">
                                    <img :src="movie.image_url"  alt="" class="rounded h-full w-full">
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
            <div v-else class="text-center text-2xl">
                暂无收藏电影
            </div>
        </div>
        </div>
        <Footer/>
    </div>
</template>

<script>
import Header from '@/components/Header.vue'
import Footer from '@/components/Footer.vue'
import axios from 'axios'


export default {
    name: 'Collect',
    data: function(){
        return {
            info: ''
        }
    },
    components: { Header, Footer },
    mounted() {
        this.get_cellect_movie()
    },
    methods: {
        get_cellect_movie(){
            const accessToken = window.localStorage.getItem('token'); 
            axios
                .get('/api/collects/',{
                    headers: {
                        'Authorization': `JWT ${accessToken}` 
                    }
                })
                .then( response => {
                    this.info = response.data
                    console.log(this.info)
                })
                .catch(error => {
                    console.log(error)
                })
        }
    },
}
</script>