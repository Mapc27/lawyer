<template>
	<div id="header">
			<div class="top">
				<div class="mbox">
					<header class="header">
						<div class="sliders">
							<div class="logo-part">
								<div class="logo"></div>
								<div class="slogan">Квалифицированная юридическая помощь в сфере товарных знаков</div>
							</div>
							<div class="contacts-part">
								<div class="contacts">
									<div class="phone">+7 986 923 5153</div>
									<div class="text">С 9:00 до 21:00 Без выходных</div>
								</div>
							</div>
						</div>
					</header>
				</div>
			</div>
			<div class="center">
				<div class="mbox">
					<div class="sliders">

						<div class="text-part">
							<p>Попали в спорную ситуацию, связанную с товарным знаком и считаете, что Вы правы?</p>
							<ul>
								<li>Страховая занижает или отказывает в выплате?</li>
								<li>Попали в ДТП, но у виновника нет страховки?</li>
								<li>Выявили дефект после покупки авто в салоне?</li>
								<li>Или любая другая проблема связаная с авто</li>
							</ul>
							<h1>Юрист авто-подбор.рф с многолетней практикой работы поможет с решением задачи</h1>
						</div>
						<div class="form-part">
							<div class="form">
								<div class="title">
									<h3 class="title-text">Оставьте заявку</h3>
                  <p class="title-subtitle">Получите первичную бесплатную консультацию</p>
								</div>
								<div class="inputer">
									<div class="label">Номер телефона*</div>
									<vue-mask id="phone_number" class="form-input" mask="+7 (999) 999 99 99" :options="options" v-model="phone_number" :raw="true" type="text" name="phone_number"></vue-mask>
								</div>
								<div class="inputer">
									<div class="label">Ваше имя</div>
									<input class="form-input" v-model="person_name" v-on:input="name_input" type="tel" name="person_name" required="" aria-required="true" aria-invalid="false">
								</div>
								<div class="inputer">
									<div class="label">Опишите ситуацию</div>
									<textarea class="form-input" v-model="description" name="description" placeholder="С какой проблемой столкнулись?" rows="3"></textarea>
								</div>
								<div class="submiter">
									<button v-on:click="send_application">
										<span>Оставить заявку</span>
									</button>
								</div>
							</div>
							{{this.message}}
						</div>

					</div>
				</div>
			</div>
			<div class="bottom"></div>
	</div>
</template>

<script>
import vueMask from 'vue-jquery-mask';

export default {
	name: "Header",
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

<style scoped>
#header{
  background-color: darkgrey;
  color: #ffffff;
}
.mbox{
  max-width: 1250px;
  margin: 0 auto;
  padding: 0 50px;
}
.top{
	padding: 30px 0;
}
.sliders{
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
}
.center{
	padding: 30px 0;
  align-content: center;
}
.form{
  margin: 0 0 0 20px;
	padding: 30px;

  max-width: 360px;
  width: 100%;
  background-color: #ffffff;

  font-family: 'Roboto', arial, sans-serif;
  font-size: 16px;
  color: #3D3D3D;

  border-radius: 3px;
}
.title-text{
  margin: 0 0 10px;
  color: #000000;
  font-size: 33px;
}
.title-subtitle{
  color: #636363;
  font-size: 13px;
  margin: 0;
}
.inputer{
  padding: 10px 0;
  width: 100%;
  position: relative;

}
.label{
  margin: 0 0 10px;
}

.form-input{
  border: 1px solid #FFCD02;
  padding: 18px 20px;
  margin: 0;
}

@media screen and (max-width: 1480px) {
  .first-wrap .texter {max-width: 800px;margin-left: 20px;}
  .form {margin: 0 0 0 20px;}
}</style>