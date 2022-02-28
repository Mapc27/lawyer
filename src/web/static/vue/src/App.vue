<template>
	<div id="app">
		<Base></Base>
	</div>
</template>

<script>
import Base from './components/Base.vue'

export default {
  name: 'App',
  components: {
		Base,
	}
}
</script>

<style>
body{
  margin: 0;
  min-width: 320px;
}
</style>
