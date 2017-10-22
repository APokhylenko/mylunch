<template>
    <div>
        <div>
            <div class="container box">
                <nav class="level is-marginless ">
                    <div class="level-left">
                        <div class="level-item">{{ dateToday | moment }}</div>
                    </div>
                    <div class="level-right">
                        <div class="level-item">
                            {{ getUserInfo }}
                        </div>
                        <div class="level-item">
                            <i class="fa fa-bell-o fa-1x"></i>
                        </div>
                        <div class="level-item">
                            <i @click="showLogin = true" :class="{loggedin: userIsLogged}" class="fa fa-user fa-2x"></i>
                        </div>
                    </div>
                </nav>
                <app-login v-if="showLoginForm" :isLogged="userIsLogged"></app-login>
                <app-orders :lastName="userLastName" :userId="userId"></app-orders>
                <app-total-order></app-total-order>
            </div>
        </div>
    </div>
</template>
<script>
import moment from 'moment'
import {
    eventBus
} from './main'
import Login from './components/Login.vue'
import Orders from './components/Orders'
import TotalOrder from './components/TotalOrder'

moment.locale('ru');

export default {
    name: 'app',
    data() {
        return {
            userId: Number,
            userFirstName: '',
            userLastName: '',
            userIsLogged: false,
            showLogin: false,
            dateToday: new Date(),
        }
    },
    methods: {

    },
    computed: {
        showLoginForm() {
            eventBus.$on('showModal', (data) => {
                this.showLogin = data
            })
            return this.showLogin
        },
        getUserInfo() {
            eventBus.$on('getUserData', (data) => {
                this.userId = data.id
                this.userFirstName = data.first_name
                this.userLastName = data.last_name
                this.userIsLogged = true
                // localStorage.getItem('token'))
            })
            eventBus.$on('userIsLogged', (data) => {
              this.userIsLogged = data
            })
            return this.userFirstName

        }
    },
    filters: {
        moment: function(date) {
            return moment(date).format('D MMMM YYYY');
        }
    },
    components: {
        appLogin: Login,
        appOrders: Orders,
        appTotalOrder: TotalOrder
    },
}
</script>
<style>
#app {
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
    margin-top: 60px;
}

.container {
    width: 70%;
}

.level-item {
    font-size: 30px;
    margin-bottom: 10px;
}

.media {
    justify-content: space-between;
}

.media-content {
    text-align: none;
    flex-grow: 0.2;
}

.loggedin {
    color: #199085;
}
</style>
