<template>
  <div class="hello">
    <Header ></Header>
    <el-row>
      <LeftSide ></LeftSide>
      <!--<FoodMain :myvalue="count_food" @transfer="getCount" @totalprice="sumPrice"></FoodMain>-->
      <FoodMain></FoodMain>
    </el-row>
    <!--<Footer :myvalue="count_food" :mytotal="sum_price"></Footer>-->
    <Footer></Footer>
  </div>
</template>

<script>
  import Header from "./Header.vue"
  import LeftSide from "./LeftSide.vue"
  import FoodMain from "./FoodMain.vue"
  import Footer from "./Footer.vue"
export default {
  name: 'HelloWorld',
  /*把data()理解成django里面的models*/
  data () {
    return {

    }
  },
  components:{
    Header,
    LeftSide,
    FoodMain,
    Footer
  },
  methods:{
    getCount(msg){
        console.log("XXXXXXX")
        console.log(msg)
        console.log("XXXXXXXX")
        this.count_food=msg
    },
    sumPrice(msg){
      this.sum_price+=msg;
      console.log("QQQQQQQQQQQQQQQQQQQQQQQQQ")
      console.log(this.sum_price)
      console.log("QQQQQQQQQQQQQQQQQQQQQQQQ")
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
