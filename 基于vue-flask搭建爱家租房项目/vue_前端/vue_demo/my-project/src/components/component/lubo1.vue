<template>
  <div class="lunbo-house">
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
</template>

<script>
  export default {
    name: "lubo1",
    data() {
      return {
        house_old_list: this.$store.state.house_data.oldhouse
      }
    },
    computed: {
      house_old_data() {
        return this.house_old_list
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

  .tip-price {
    position: absolute;
    right: 0;
    bottom: 0;
    font-size: 16px;
    color: #FA5741;
    letter-spacing: 0;
  }

  .caption .position {
    font-size: 18px;
    color: #101D37;
    letter-spacing: 0;
    line-height: 24px;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
    margin: 0;
  }

  .caption {
    padding: 0;
    margin-top: 20px;
    margin-left: 2px;
  }
</style>
