<template>
  <div id="app">
    <!--<Vheader></Vheader>-->
    <router-view/>
  </div>
</template>

<script>
import Vheader from '@/components/Vheader'
export default {
  name: 'App',
  components:{
    Vheader
  }
}

</script>



<style>

</style>
