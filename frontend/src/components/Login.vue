<template>
    <div>
        <login-modal-window @close="">
            <h2 slot="header">Login</h2>
            <div v-if="!checkIfLogged" @keyup.enter="login" class="login-form">
                <div class="field">
                    <div class="info" v-if="infoError">Ошибка входа. Повторите попытку.</div>
                    <p class="control has-icons-left has-icons-right">
                        <input v-model="email" class="input" type="text" placeholder="Email" required>
                        <span class="icon is-small is-left">
					<i class="fa fa-envelope"></i>
				</span>
                        <span class="icon is-small is-right">
					<i class="fa fa-check"></i>
				</span>
                    </p>
                </div>
                <div class="field">
                    <p class="control has-icons-left">
                        <input v-model="password" class="input" type="password" placeholder="Password" required>
                        <span class="icon is-small is-left">
					<i class="fa fa-lock"></i>
				</span>
                    </p>
                </div>
            </div>
            <div v-else>
                <p style="text-align: center;">Вход выполнен
                    <i class="fa fa-check" aria-hidden="true"></i>
                </p>
            </div>
            <div slot="buttons" class="field">
                <p class="control">
                    <button v-if="!logged" @click="login" class="button is-success">
                        Login
                    </button>
                </p>
                <button v-if="logged" @click="logout" class="button move-right">
                    Logout
                </button>
            </div>
        </login-modal-window>
    </div>
</template>
<script>
import { eventBus } from '../main'
import ModalWindow from './ModalWindow.vue'
export default {
	props: ['isLogged'],
    data() {
            return {
                infoError: false,
                email: '',
                password: '',
                logged: ''
            }
        },
        methods: {
            login() {
                this.infoError = false
                this.$http.post('http://localhost:8000/auth/login', {
                        username: this.email,
                        password: this.password,
                    })
                    .then(response => {
                        this.logged = true
                        localStorage.setItem('token', response.data.token)
                        eventBus.$emit('getUserData', {
                            id: response.data.user.id,
                            first_name: response.data.user.first_name,
                            last_name: response.data.user.last_name
                        })
                        setTimeout(function() {
                                eventBus.$emit('showModal', false)
                            }, 1100)
                    })
                    .catch(error => {
                        console.log(error)
                        this.infoError = true
                        this.password = ''
                    });
            },
            logout() {
            	eventBus.$emit('userIsLogged', false)
                this.logged = false
                localStorage.removeItem('token')
                location.reload()
            }
        },
        computed: {
        	checkIfLogged() {
        		this.logged = this.isLogged
        		return this.logged
        	}
        },
        components: {
            loginModalWindow: ModalWindow
        },

}
</script>
<style></style>
