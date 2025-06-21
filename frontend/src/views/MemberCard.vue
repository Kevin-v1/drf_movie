<template>

<div id="container" class="text-white text-sm bg-primary-300 min-h-screen pb-4"> 
    <Header/>
        <div id="main" class="bg-primary-300 p-12 text-black">
            <div class="grid grid-cols-3 gap-3">
                
                <div v-for="card in info.results" v-bind="card" class="flex flex-col justify-center items-center bg-white rounded-lg px-6 max-w-xl">
                    <div class="text-4xl text-center">
                        {{ card.card_name }}
                    </div>
                    <div class="text-4xl text-center">
                        ￥{{ card.card_price }} 元
                    </div>
                    <button v-on:click="pay(card)"  data-pay_type="alipay" class="card w-24 rounded-3xl bg-purple-600 text-white text-lg p-2 mx-8 my-2">购买</button>
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
    name: 'MemberCard',
    data: function() {
        return {
            info: '',
            pay_url: ''
        }
    },
    components: { Header, Footer},
    mounted() {
        this.get_card_info()
    },
    methods: {
        get_card_info() {
            axios
                .get('/api/cards')
                .then(response => {
                    this.info = response.data
                    console.log(this.info)
                })
        },
        pay(card) {
            console.log(card)
            console.log(card.id)
            alert('购买' + card.id)
            const url = '/api/alipay/?card_id='+card.id
            axios
                .get(url, {card_id: card.id})
                .then(response => {
                    // this.pay_url = response.data
                    console.log(this.pay_url)
                    // that.$router.push({ name: "home" });
                    window.location.href = response.data
                })
        }
    },
}
</script>