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
body {
	margin: 0;
  min-height: 100%;
  width: 100%;
  min-width: 320px;
  font-family: 'Roboto', arial,sans-serif;
  background: #fff;
  color: #3d3d3d;
  position: relative;
  font-size: 16px;
  line-height: 1;
  overflow-x: hidden; }
</style>
