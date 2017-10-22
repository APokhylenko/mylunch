<template>
    <div class="box">
        <div class="media">
            <div class="media-left">
                <h2 class="subtitle">Имя</h2>
            </div>
            <div class="media-content">
                <h2 class="subtitle has-text-centered">Заказ</h2>
            </div>
            <div class="media-right">
                <h2 class="subtitle">Оплата</h2>
            </div>
        </div>
        <div v-for="(person, index) in people" class="media">
            <div class="media-left">
                {{ person.first_name }} {{ person.last_name[0] }}.
            </div>
            <div class="media-content ">
                <orders-modal-window v-if="showProductsModal">
                    <template slot="header">Выберите продукты</template>
                    <template>
                    	<div class="select">
                        <select v-model="selectedProduct">
                            <option v-for="product in products" :value="{ name:product.name, price:product.price }">
                                {{ product.name }}
                            </option>
                        </select>
                        </div>
                        <button class="button" 
                        	v-on:click="addProduct(selectedProduct.name, selectedProduct.price)">
                            Добавить
                        </button>
                        <ul>
                            <li v-for="(product, index) in userProducts">
                            	<hr>
                                {{ product.name }} - {{ product.price }} грн
                                <button class="button is-small is-danger" v-on:click="deleteProduct(index, product.price)" style="float:right;">
                                    X
                                </button>
                            </li>
                        </ul>
                    </template>
                    <template slot="buttons">
                        <button class="button is-success" @click="sendUserOrder(userProducts)">ОК</button>
                        <button class="button is-danger"  @click="sendUserOrder([{name: 'deleteOrder',}]), userTotalPrice=0, userProducts=[]">Удалить заказ</button>
                        <span><strong>Всего: {{ userTotalPrice }} грн</strong></span>
                    </template>
                </orders-modal-window>
                <ul>
                    <li v-for="food in person.order">
                        {{ food.name }}
                    </li>
                </ul>
                <template v-if="person.last_name == lastName">
                    <button class="button is-small is-info is-outlined" @click="productsModal=true">Добавить еще</button>
                    
                </template>
            </div>
            <div class="media-right">
                <p>X</p>
            </div>
        </div>
        <hr>
    </div>
</template>
<script>
import { eventBus } from '../main'

import ModalWindow from './ModalWindow.vue'
export default {
    mounted() {
            this.getProducts(),
            this.getPeople()
        },
        props: ['userId','lastName'],
        data() {
            return {
                people: '',
                products: [],
                productsModal: false,
                selectedProduct: [],
                userLastName: '',
                userProducts: [],
                userTotalPrice: 0,
            }
        },
        methods: {
            getProducts() {
                this.$http.get('http://localhost:8000/api/v1/products/')
                    .then(response => {
                        this.products = response.data
                    })
                    .catch(error => {
                        console.log(error)
                    })
            },
            getPeople() {
                this.$http.get('http://localhost:8000/api/v1/users/')
                    .then(response => {
                        this.people = response.data;
                        var orders = this.people.map(p => p.order).filter(p => {
                            return p.length > 0
                    })
                        eventBus.$emit('people', orders)
                    })
                    .catch(error => {
                        console.log(error)
                    })
            },
            addProduct(product, price) {
                    this.userProducts.push({
                        name: product,
                        price: price
                    })
                this.userTotalPrice += price
            },
            deleteProduct(index, price) {
                this.userProducts.splice(index, 1)
                this.userTotalPrice -= price
            },
            updateOrder(index) {
                let m = this.people.pop(index)
                this.people.unshift(m)
            },
            sendUserOrder(products) {
            	this.productsModal = false
            	let token = "JWT " + localStorage.getItem("token")
            	this.$http({ 
            		method: 'patch',
            		headers: {
            			Authorization: token
            		},
            		url: '/users/' + this.userId + '/',  
            		data: { order: products }
            	})
                    .then(response => {
                    	console.log(response)
                        this.getPeople()
                    })
                    .catch(error => {
                        console.log(error)
                    });
            }
        },
        computed: {
            showProductsModal() {
                eventBus.$on('showModal', (data) => {
                    this.productsModal = data
                })
                return this.productsModal
            },
        },
        components: {
            'ordersModalWindow': ModalWindow,
        }
}
</script>
<style scoped>
.box {
    max-height: 300px;
    overflow: auto;
}

.media-left {
    width: 100px;
}

.media-right {
    min-width: 60px;
    text-align: center;
    margin-top: auto;
    margin-bottom: auto;
}
</style>
