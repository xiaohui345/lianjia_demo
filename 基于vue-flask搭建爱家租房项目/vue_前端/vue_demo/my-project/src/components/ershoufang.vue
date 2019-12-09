<template>
  <div>
    <Vheader></Vheader>
    <div class="container">
      <h2>二手房</h2>
      <div class="row">
        <div v-for="(item,index) in house_old_data">
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
    name: "ershoufang",
    data() {
      return {
        house_old_list: '',
        house_city:this.$store.state.city,
      }
    },
    components: {
      Vheader,
      Footer
    },
    mounted() {
      var that = this;
      this.$axios.request({
        url: 'http://127.0.0.1:5000/ershoufang/'+that.house_city,
        method: 'get'
      }).then(function (arg) {
        if (arg.data.code === 1000) {
          that.house_old_list = arg.data.data.ershoufang;
          console.log(arg.data.data.ershoufang)
        }
      })
    },
    computed: {
      house_old_data() {
        return this.house_old_list
      }
    }
  }
</script>

<style scoped>

</style>
