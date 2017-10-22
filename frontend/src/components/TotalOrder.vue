<template>
    <div class="box">
        <h2 class="subtitle has-text-centered">Общий заказ</h2>
        <hr>
        <div class="media">
                <div class="media-left">
					<ul>
						<li v-for="product in productsList.name">{{ product }}</li>
					</ul>
                </div>
                <div class="media-content">
                    <ul>
						<li v-for="i in productsList.name.length">1 шт</li>
					</ul>
                </div>
                <div class="media-right">
                	<ul>
						<li v-for="product in productsList.price">{{ product }} грн</li>
					</ul>
                </div>
            <div class="media-right vertical-center">
                <h2 class="title"> {{ totalPrice }} грн </h2>
            </div>
        </div>
    </div>
</template>
<script>
import {
    eventBus
} from '../main'
export default {
    data() {
            return {
                products: {
                	name: [],
                	price: []
                },
                totalPrice: 0
            }
        },
        computed: {
            productsList() {
                eventBus.$on('people', (data) => {
                	this.products = {name:[],price:[]}
                	this.totalPrice = 0
                    for (var i=0; i < data.length; i++) {
                    	data[i].forEach(product => {
                    		this.totalPrice += product.price
                    		this.products['name'].push(product.name)
                    		this.products['price'].push(product.price)
                    	})                    	
                    }
                })
                return this.products
            }
        }
}
</script>
<style scoped>
.vertical-center {
    align-self: center;
    flex-grow: 0.4;
    text-align: right;
}

.box {
    max-height: 300px;
    overflow: auto;
}
</style>
