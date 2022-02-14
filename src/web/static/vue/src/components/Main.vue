<template>
	<div id="main">
		<div class="form">
			<div class="inputer">
				<div class="label">Номер телефона*</div>
				<vue-mask id="phone_number" mask="+7 (999) 999 99 99" :options="options" v-model="phone_number" type="text" name="phone_number"></vue-mask>
			</div>
			<div class="inputer">
				<div class="label">Ваше имя</div>
				<input v-model="person_name" v-on:input="name_input" type="tel" name="person_name" required="" aria-required="true" aria-invalid="false">
			</div>
			<div class="inputer">
				<div class="label"> Опишите ситуацию </div>
        <textarea v-model="description" name="description" placeholder="С какой проблемой столкнулись?" rows="3"></textarea>
			</div>
			<div class="submiter">
				<button v-on:click="send_application">
					<span>Оставить заявку</span>
        </button>
			</div>
			<div class="result">
				{{message}}
			</div>
		</div>
	</div>
</template>

<script>
import vueMask from 'vue-jquery-mask';


export default {
	name: "Main",
	components: {
		vueMask,
	},
	data(){
		return {
			phone_number: '',
			person_name: '',
			description: '',
			message: '',
			options: {
          placeholder: '+7(XXX) XXX-XX-XX',
        },
			regex: /^(\+7|8|)([0-9]{10})$/
		}
	},
	methods: {
		name_input(){
			this.person_name = this.person_name[0].toUpperCase() + this.person_name.slice(1);
		},
		check_input_data() {
			if (this.phone_number.match(this.regex) === null){
				this.message = 'Номер телефона имеет неверный формат'
				return false;
			}
			if (this.description === ''){
				this.message = 'Добавьте описание'
				return false
			}
			if (this.person_name === ''){
				this.message = 'Введите Ваше имя'
				return false
			}
			return true
		},
		send_application(){
			if (!this.check_input_data()) return
			fetch( `/api/applications/`,
					{
						method: 'POST',
						headers: {"Content-Type": "application/json"},
						body: JSON.stringify({'phone_number': this.phone_number, 'person_name': this.person_name, 'description': this.description})
					})
			.then(response => response.json())
			.then((data) => (self.message = data));
			console.log( JSON.stringify({'phone_number': this.phone_number, 'person_name': this.person_name, 'description': this.description}))
		}
	},
}
</script>

<style scoped lang="scss">

</style>