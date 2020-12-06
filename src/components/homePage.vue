<template>
<div>
<div id="header" class="d-flex">
<p style="padding-top:15px; padding-left:10px; font-family:Helvetica;">Welcome to Lip2Text</p>
<p style="padding-top:15px; padding-right:10px; font-family:Helvetica;" class="ml-auto">Capstone Project 2020</p>
</div>

<div class="d-flex justify-content-center" id="body">
  <div id="input_area">
    <div class="d-flex">
    <p style="padding-top:20px;font-size:50px;font-family:Helvetica;">Upload</p>
    <input type="file" ref="video_upload" style="display:none;">
    <button type="text" @click="$refs.video_upload.click()">
      <v-icon large color="green" style="font-size:100px;">mdi-arrow-up-bold-box-outline</v-icon>
    </button>
  </div>
   <v-select
   style="width:250px;"
    v-model="dataset_type_chosen"
          :items="dataset_type"
          label="Type"
          solo
        ></v-select>
     <v-btn
   style="width:250px;"
        >Begin</v-btn>
  </div>
  <div id="middle_line"></div>
  <div id="output_area">
    <div class="d-flex"><p style="font-size:30px; padding-top:10px; padding-right:10px;">Trimming</p><v-icon large :color="trimming_icon" style="font-size:50px;">mdi-check-circle</v-icon></div>
    <div class="d-flex"><p style="font-size:30px; padding-top:10px; padding-right:10px;">Splitting</p><v-icon large :color="splitting_icon" style="font-size:50px;">mdi-check-circle</v-icon></div>
    <div class="d-flex"><p style="font-size:30px; padding-top:10px; padding-right:10px;">Calculating Area</p><v-icon large :color="area_icon" style="font-size:50px;">mdi-check-circle</v-icon></div>
    <div class="d-flex" v-if="dataset_type_chosen=='Training'"><p style="font-size:30px; padding-top:10px; padding-right:10px;">Training</p><v-icon large :color="area_icon" style="font-size:50px;">mdi-check-circle</v-icon></div>
    <div class="d-flex" v-if="dataset_type_chosen=='Prediction'"><p style="font-size:30px; padding-top:10px; padding-right:10px;">Analysing</p><v-icon large :color="area_icon" style="font-size:50px;">mdi-check-circle</v-icon></div>
  </div>
</div>
<hr style="width:50%; margin-left:25%;margin-top:2%">
<div id="results_body">

</div>

</div>
</template>
<script>
// import axios from "axios";
export default {
  data() {
    return {
      dataset_type:["Training", "Prediction","Signature"],
      dataset_type_chosen: "Training",
      trimming_icon: "gray",
      splitting_icon: "gray",
      area_icon: "gray",
    };
  },
  methods: {
    clicked() {
      this.trimming_icon = "green";
      this.splitting_icon = "green";
      this.area_icon = "green";
    }
    
  },
  created() {
    
  }
};
</script>

<style scoped>

</style>
