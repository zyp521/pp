<template>

    <el-col :span="4">
      <el-menu
      background-color="darkgreen"
      text-color="white">
        <el-menu-item>
          <i class="el-icon-upload"></i>
          <span>厨师推荐</span>
        </el-menu-item>
        <el-menu-item>
          <i class="el-icon-picture"></i>
          <span>精品凉菜</span>
        </el-menu-item>
        <el-menu-item>
          <i class="el-icon-phone"></i>
          <span>特色小炒</span>
        </el-menu-item>
        <el-menu-item>
          <i class="el-icon-search"></i>
          <span>家常热菜</span>
        </el-menu-item>
        <el-menu-item>
          <i class="el-icon-star-on"></i>
          <span>营养主食</span>
        </el-menu-item>
        <el-menu-item>
          <i class="el-icon-news"></i>
          <span>调味饮料</span>
        </el-menu-item>
      </el-menu>
    </el-col>

</template>

<script>
    export default {
        name: "LeftSide"
    }
</script>

<style scoped>
.el-menu-item:hover{
  background-color:purple!important;
  color:yellow!important;
}
</style>
