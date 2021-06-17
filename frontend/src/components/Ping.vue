<template>
  <div class="container">
    <h1> The data below is coming from backend (MONGO_DB) </h1>
    <ul>
      <li v-for="(item, index) in msg" :key="index">{{ item }} {{ index }}</li>

    </ul>
    <h1> The data below is coming from Postgres and SQLAlchemy </h1>
    <p> {{ msg2 }} </p>
    <ul>
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
      msg2: '',
    };
  },
  methods: {
    getMessage() {
      const path = 'http://localhost:5000/ping';
      axios.get(path)
        .then((res) => {
          [this.msg, this.msg2] = res.data;
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
