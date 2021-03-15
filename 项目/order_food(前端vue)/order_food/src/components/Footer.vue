<template>
    <el-row>
      <el-col :span="20">
          <div class="bg-dark-green">
            选择菜品{{this.$store.state.count_food}}件，价格{{this.$store.state.sum_price}}元。
          </div>
      </el-col>
      <el-col :span="4">
          <div class="bg-dark-red">
            结算
          </div>
      </el-col>
    </el-row>
</template>

<script>
    export default {
        name: "Footer",
        props:["myvalue","mytotal"]
    }
</script>

<style scoped>
  .bg-dark-green{
    background-color:darkgreen;
    color:white;
    height:60px;
    line-height:60px;
  }
  .bg-dark-red{
    background-color:darkred;
    color:white;
    height:60px;
    line-height:60px;
  }
  .bg-dark-red:hover{
    background-color:purple;
    color:white;
    height:60px;
    line-height:60px;
  }
</style>
