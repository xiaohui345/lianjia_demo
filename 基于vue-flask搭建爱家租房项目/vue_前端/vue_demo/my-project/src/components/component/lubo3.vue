<template>
  <div class="lunbo-house">
    <div class="row">
      <div v-for="(item,index) in housedata">
        <div class="col-md-4">
          <div class="thumbnail">
            <img :src=item.img :alt=item.title style="width: 400px;height: 230px">
            <div class="bg"></div>
            <div class="title">
              <p><label>约{{item.price}}万元</label></p>
            </div>
            <div class="caption">
              <p class="country">{{item.area}}</p>
              <p class="p01">{{item.title}} </p>
              <div class="tips">
                <div class="tips-info">{{item.type}}·{{item.size}}平米</div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    name: "lubo1",
    data() {
      return {
        house_list: this.$store.state.house_data.abroad_newhouse
      }
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

  .caption .tips {
    margin-top: 11px;
    position: relative;
  }

  .caption {
    padding: 0;
    margin-top: 20px;
    margin-left: 2px;
  }

  .bg {
    background: #000;
    opacity: .1;
    width: 360px;
    height: 202px;
    position: absolute;
    left: 0;
    bottom: 0;
    margin-left: 35px;
    margin-bottom: 120px;
  }

  .title {
    font-size: 15px;
    color: #fff;
    position: absolute;
    bottom: 25px;
    width: 350px;
    font-weight: 200;
    height: 260px;
    left: 50%;
    top: 50%;
    margin-left: -60px;
    text-align: center;
    margin-top: -10px;
    text-shadow: 0 1px 4px rgba(0, 0, 0, 0.6);
  }

  label {
    font-weight: 200;
    color: #fff2ab;
    font-size: 20px;
    position: relative;
    top: 1px;
  }

  .country {
    font-size: 12px;
    line-height: 12px;
    color: #767676;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
  }

  .p01 {
    margin-top: 8px;
    font-size: 18px;
    color: #222222;
    line-height: 1.2;
    font-weight: 600;
    overflow: hidden;
  }

  .tips-info {
    float: left;
    color: #222222;
    font-size: 12px;
    max-width: 210px;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
  }
</style>
