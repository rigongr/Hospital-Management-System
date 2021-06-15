<template>
  <div class="container">
    <h1> The data below is coming from backend </h1>
    <p> {{ msg }} </p>
    <ul>
      <li v-for="(item, index) in msg" :key="index">{{ item }} {{ index }}</li>

    </ul>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Ping',
  data() {
    return {
      msg: '',
    };
  },
  methods: {
    getMessage() {
      const path = 'http://localhost:5000/ping';
      axios.get(path)
        .then((res) => {
          this.msg = res.data;
          console.log('This is response data: ', res.data);
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
  },
  created() {
    this.getMessage();
  },
};
</script>
