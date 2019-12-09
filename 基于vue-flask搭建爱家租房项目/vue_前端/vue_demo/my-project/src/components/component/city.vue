<template>
  <div>
    <Vheader></Vheader>
    <div>
      <h2>选择你要选的城市</h2>
      <ul>
        <li @click="changecity('北京')" >北京</li>
        <li @click="changecity('上海')" >上海</li>
        <li @click="changecity('武汉')" >武汉</li>
        <li @click="changecity('深圳')" >深圳</li>
      </ul>
    </div>
    <Footer></Footer>
  </div>

</template>

<script>
  import Vheader from '@/components/Vheader'
  import Footer from '@/components/component/footer'

  export default {
    name: "city",
    data(){
      return{
      }
    },
    components: {
      Vheader,
      Footer
    },
    methods:{
      changecity(cityname){
          console.log("cityname",cityname);
          this.$store.dispatch('city',cityname);
          this.$router.push({
                path: '/'
              })
      }
    }
  }
</script>

<style scoped>

</style>
