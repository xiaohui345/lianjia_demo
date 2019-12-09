<template>
  <div class="lunbo-house">
    <div class="row">
      <div v-for="(item,index) in housedata">
        <div class="col-md-4">
          <div class="thumbnail">
            <img :src=item.img :alt=item.title style="width: 400px;height: 250px">
            <div class="bg"></div>
            <div class="title">
              {{item.title}}
              <p><label> {{item.price}}元/平</label></p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    name: "lubo2",
    data() {
      return {
        house_list: this.$store.state.house_data.newhouse
      }
    },
    methods:{
    },
    computed: {
      housedata() {
        return this.house_list
      }
    }
  }
</script>

<style scoped>
  .lunbo-house {
    height: 300px;
    background-color: white;
  }

  .thumbnail {
    padding: 0;
    border: 0;
    margin-left: 20px;
  }

  .row {
    margin-top: 20px;
  }

  .bg {
    background: #000;
    opacity: .1;
    width: 360px;
    height: 250px;
    position: absolute;
    left: 0;
    bottom: 0;
    margin-left: 35px;
    margin-bottom: 20px;
  }

  .title {
    font-size: 25px;
    color: #fff;
    position: absolute;
    bottom: 25px;
    width: 350px;
    font-weight: 800;
    height: 260px;
    left: 50%;
    top: 50%;
    margin-left: -170px;
    text-align: center;
    margin-top: -50px;
    text-shadow: 0 1px 4px rgba(0, 0, 0, 0.6);
  }

  label {
    font-weight: 700;
    color: #fff2ab;
    font-size: 20px;
    position: relative;
    top: 1px;
  }
</style>
