<template>
  <div>
    <Vheader></Vheader>
    <div class="container">
      <h2>新房</h2>
      <div class="row">
        <div v-for="(item,index) in house_new_data">
          <div class="col-md-4">
            <div class="thumbnail">
              <img :src=item.img :alt=item.title style="width: 400px;height: 230px">
              <div class="caption">
                <p class="position">{{item.title}}</p>
                <p class="position">{{item.area}}</p>
                <p class="tips"><span>{{item.type}}·{{item.size}}平米</span>
                  <span class="tip-price">{{item.price}}万</span>
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <Footer></Footer>
  </div>


</template>

<script>
  import Vheader from '@/components/Vheader'
  import Footer from '@/components/component/footer'
  export default {
    name: "xinfang",
    data() {
      return {
        house_new_list: ''
      }
    },
    components:{
      Vheader,
      Footer
    },
    mounted() {
      var that = this;
      this.$axios.request({
        url: 'http://127.0.0.1:5000/xinfang',
        method: 'get'
      }).then(function (arg) {
        if (arg.data.code === 1000) {
          that.house_new_list = arg.data.data.xinfang;
          console.log(arg.data.data.xinfang)
        }
      })
    },
    computed: {
      house_new_data() {
        return this.house_new_list
      }
    }
  }
</script>

<style scoped>

</style>
