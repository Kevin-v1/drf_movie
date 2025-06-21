<template>
    <div id="container" class="text-white text-sm bg-primary-300 min-h-screen pb-4"> 
        <Header/>
        <MovieBox/>
        <Footer/>
    </div>
</template>

<script>
import Header from '@/components/Header.vue'
import Footer from '@/components/Footer.vue'
import MovieBox from '@/components/MovieBox.vue'


export default {
    name: 'MovieDetail',
    components: {Header, Footer, MovieBox}
}
</script>