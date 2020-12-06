<template>
<div>
<div id="header" class="d-flex">
<p style="padding-top:15px; padding-left:10px; font-family:Helvetica;">Welcome to Lip2Text</p>
<p style="padding-top:15px; padding-right:10px; font-family:Helvetica;" class="ml-auto">Capstone Project 2020</p>
</div>

<div class="d-flex justify-content-start" id="body">
  <div id="input_area">
    <div class="d-flex">
    <p style="padding-top:20px;font-size:50px;font-family:Helvetica;">Upload</p>
    <input type="file" ref="video_upload" style="display:none;" @change="mediaUpload">
    <button type="text" @click="$refs.video_upload.click()">
      <v-icon large color="green" style="font-size:100px;">mdi-arrow-up-bold-box-outline</v-icon>
    </button>
  </div>
   <v-select
   style="width:250px;"
    v-model="operation_type_chosen"
          :items="operation_type"
          label="Type"
          solo
        ></v-select>
     <v-select
     v-if="operation_type_chosen=='Training'"
   style="width:250px;"
    v-model="word_chosen"
          :items="words"
          label="Word"
          solo
        ></v-select>

     <v-btn
     v-on:click="beginProcess()"
   style="width:250px;"
        >Begin</v-btn>
  </div>
  <div id="middle_line"></div>
  <div id="output_area">
    <div class="d-flex"><p style="font-size:30px; padding-top:10px; padding-right:10px;">Media Uploaded</p><span style="padding-top:15px;padding-left:20px;"><v-progress-circular v-if="media_icon=='gray'" indeterminate color="primary"></v-progress-circular></span><v-icon  v-if="media_icon=='green'" large :color="media_icon" style="font-size:50px;">mdi-check-circle</v-icon><v-icon  v-if="media_icon=='not_gray'" large :color="media_icon" style="font-size:50px;">mdi-check-circle</v-icon></div>
    <div class="d-flex"><p style="font-size:30px; padding-top:10px; padding-right:10px;">Trimming</p><span style="padding-top:15px;padding-left:20px;"><v-progress-circular v-if="trimming_icon=='gray'" indeterminate color="primary"></v-progress-circular></span><v-icon  v-if="trimming_icon=='green'" large :color="trimming_icon" style="font-size:50px;">mdi-check-circle</v-icon><v-icon  v-if="trimming_icon=='not_gray'" large :color="trimming_icon" style="font-size:50px;">mdi-check-circle</v-icon></div>
    <div class="d-flex"><p style="font-size:30px; padding-top:10px; padding-right:10px;">Splitting</p><span style="padding-top:15px;padding-left:20px;"><v-progress-circular v-if="splitting_icon=='gray'" indeterminate color="primary"></v-progress-circular></span><v-icon  v-if="splitting_icon=='green'" large :color="splitting_icon" style="font-size:50px;">mdi-check-circle</v-icon><v-icon  v-if="trimming_icon=='not_gray'" large :color="trimming_icon" style="font-size:50px;">mdi-check-circle</v-icon></div>
    <div class="d-flex"><p style="font-size:30px; padding-top:10px; padding-right:10px;">Calculating Area</p><span style="padding-top:15px;padding-left:20px;"><v-progress-circular v-if="area_icon=='gray'" indeterminate color="primary"></v-progress-circular></span><v-icon  v-if="area_icon=='green'" large :color="area_icon" style="font-size:50px;">mdi-check-circle</v-icon><v-icon  v-if="trimming_icon=='not_gray'" large :color="trimming_icon" style="font-size:50px;">mdi-check-circle</v-icon></div>
    <div class="d-flex" v-if="operation_type_chosen=='Training'"><p style="font-size:30px; padding-top:10px; padding-right:10px;">Training</p><span style="padding-top:15px;padding-left:20px;"><v-progress-circular v-if="training_icon=='gray'" indeterminate color="primary"></v-progress-circular></span><v-icon  v-if="training_icon=='green'" large :color="area_icon" style="font-size:50px;">mdi-check-circle</v-icon><v-icon  v-if="training_icon=='not_gray'" large :color="area_icon" style="font-size:50px;">mdi-check-circle</v-icon></div>
    <div class="d-flex" v-if="operation_type_chosen=='Prediction'"><p style="font-size:30px; padding-top:10px; padding-right:10px;">Analysing</p><span style="padding-top:15px;padding-left:20px;"><v-progress-circular v-if="prediction_icon=='gray'" indeterminate color="primary"></v-progress-circular></span><v-icon  v-if="prediction_icon=='green'" large :color="area_icon" style="font-size:50px;">mdi-check-circle</v-icon><v-icon  v-if="training_icon=='not_gray'" large :color="area_icon" style="font-size:50px;">mdi-check-circle</v-icon></div>
    <div class="d-flex" v-if="operation_type_chosen=='Signature'"><p style="font-size:30px; padding-top:10px; padding-right:10px;">Generating Image Signatures</p><span style="padding-top:15px;padding-left:20px;"><v-progress-circular v-if="signature_icon=='gray'" indeterminate color="primary"></v-progress-circular></span><v-icon  v-if="signature_icon=='green'" large :color="signature_icon" style="font-size:50px;">mdi-check-circle</v-icon><v-icon  v-if="signature_icon=='not_gray'" large :color="area_icon" style="font-size:50px;">mdi-check-circle</v-icon></div>
  </div>
</div>
<hr style="width:50%; margin-left:25%;margin-top:2%">
<div id="results_body">
<img :src="image_bytes" alt="">
</div>

</div>
</template>
<script>
import axios from "axios";

export default {
  data() {
    return {
      operation_type:["Training", "Prediction","Signature"],
      words: ["Hello", "Bye"],
      operation_type_chosen: "Training",
      word_chosen:"Hello",
      media_icon: "not_gray",
      trimming_icon: "not_gray",
      splitting_icon: "not_gray",
      area_icon: "not_gray",
      prediction_icon: "not_gray",
      training_icon: "not_gray",
      signature_icon: "not_gray",
      image_bytes:null,

      videos:[],
    };
  },
  methods: {
    async beginProcess() {

      // if(this.videos.length == 0)
      // {
      //   alert("Please upload atleast 1 video file.")
      //   return;
      // }

      this.media_icon = "gray";
      this.trimming_icon = "gray";
      this.splitting_icon = "gray";
      this.area_icon = "gray";
      this.prediction_icon = "gray",
      this.training_icon= "gray",
      this.signature_icon= "gray"

      //uploading all the videos to the database first
      // for (var i = 0; i < this.videos.length; i++) {
      //   let video = this.videos[i];
      //   var formData = new FormData();
      //   formData.append("video_tag",this.word_chosen);
      //   formData.append("video",video);
      //   await axios.post("http://localhost:5000/mediaUpload", formData, {
      //   headers: {
      //       'Content-Type': 'multipart/form-data'}})
      // }
      // this.media_icon = "green";

      // //triggering the trimmer to act on the uploaded videos
      // await axios.get("http://localhost:5000/trimming");
      // this.trimming_icon = "green";

      // //triggering the splitter to act on the uploaded videos
      // await axios.get("http://localhost:5000/splitting");
      // this.splitting_icon = "green";

      // //triggering the area calculation procedure
      // await axios.get("http://localhost:5000/areacalculation");
      // this.area_icon = "green";

      switch(this.operation_type_chosen)
      {
        case("Training"): 
        {
          await axios.get("http://localhost:5000/training");
          this.area_icon = "green";
          break;
        }
        case("Prediction"):{
          await axios.get("http://localhost:5000/prediction");
          this.area_icon = "green";
          break;
        }
        case("Signature"):{
          let url;
          if(this.word_chosen == "Hello"){
            url = "http://localhost:5000/signature?dataset=hello"
          }else{
            url = "http://localhost:5000/signature?dataset=bye"
          }
          let image_bytes = await axios.get(url);
          this.image_bytes = image_bytes.data;
          // var blob = new Blob( [ image_bytes ], { type: "image/png" } );
          // var imageUrl = URL.createObjectURL( blob );
          // console.log(imageUrl)
          
          this.signature_icon = "green";
          console.log("here",this.signature_icon)
          break;
        }
      }
    
    },

    async mediaUpload(videoEvent) {
      this.videos = videoEvent.target.files;
    },

    
  },
  created() {
    
  }
};
</script>

<style scoped>

</style>
