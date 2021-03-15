<script src="../main.js"></script>
<template>
    <el-col :span="20">
      <el-table
        :data="foodlist"
        height="335">
        <el-table-column
         prop="name"
        label="菜品名称">

        </el-table-column>
        <el-table-column
        prop="images"
        label="菜品图片">
          <template v-slot="scope">
            <img :src="scope.row.images" height="60"/>
          </template>
        </el-table-column>
        <el-table-column
        prop="price"
        label="菜品价格">

        </el-table-column>
        <el-table-column
        label="操作">
          <template v-slot="scope">
              <i class="el-icon-circle-plus" @click="plug_goods(scope.row.price)"></i>
          </template>
        </el-table-column>
      </el-table>

    </el-col>

</template>

<script>
  import axios from "axios"
    export default {
        name: "FoodMain",
        data() {
          return {
            /*加入食品列表的变量,在data()方法中赋值，这里用的冒*/
            /*
            foodlist: [
              {
                name: "地三鲜",
                images: "/static/images/disanxian.jpeg",
                price: 13.00
              },
              {
                name: "西红柿牛楠",
                images: "/static/images/niunan.jpg",
                price: 53.00
              },
              {
                name: "红烧鸡块",
                images: "/static/images/hongsaojikuai.jpg",
                price: 28.00
              },
              {
                name: "水煮肉",
                images: "/static/images/suizhurou.jpg",
                price: 35.00
              },
              {
                name: "凉拌土豆丝",
                images: "/static/images/todousi.jpg",
                price: 10.00
              }
            ] */
            foodlist:[]
          }
        },
        props:["myvalue"],
        created(){
            /*
            var _this=this
            axios.get("http://localhost:8001/").then(function(res){
              这里直接用this，其实this目标发生变化
              _this.foodlist=res.data
              console.log("1111111")
              console.log(_this.foodlist)
            })
            */
            /*axios改进写法，用到了ES6当中立即函数,箭头函数*/
            axios.get("http://localhost:8001/").then((res)=>{this.foodlist=res.data})
        },
        methods:{
            plug_goods(prices){
              /*逻辑:dispatch一个指令
*               dispatch(信号，值）*/
              this.$store.dispatch("increment",{"price":prices})
              /*
                console.log("-----------------")
                console.log(datas)
                console.log("---------------")
                datas.myvalue=datas.myvalue+1
                this.$emit("transfer",datas.myvalue)
                this.$emit("totalprice",prices)
                */
            }
        }

    }
</script>

<style scoped>

</style>
