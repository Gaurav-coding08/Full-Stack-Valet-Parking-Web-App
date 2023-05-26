<template>
    <body>
    <div style="padding-top: 25vh">
      <video ref="videoPlayer" width="640" height="360" controls @click="togglePlay">
        <source :src="videoSource" type="video/mp4">
        Your browser does not support the video tag.
      </video>
    </div>
</body>
  </template>
  
  <script>
  export default {
    data() {
      return {
        videoSource: "/Users/gauravrastogi/Desktop/valet_parking_vue/valet/public/welcome to my desktop.mp4",
        isVideoPlaying: false
      };
    },
    methods: {
      togglePlay() {
        const videoElement = this.$refs.videoPlayer;
  
        if (this.isVideoPlaying) {
          videoElement.pause();
          this.isVideoPlaying = false;
        } else {
          videoElement.play();
          this.isVideoPlaying = true;
        }
      }
    }
  };
  </script>
  