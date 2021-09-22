<template>
  <div>
    <NewHeader />
    <PatientSideBar />
    <h1 style="margin-left: 350px">Departamentet</h1>
    <b-row style="margin-left: 350px">
      <b-col>
        <b-card v-for="item in data" :key="item.id">
          <!-- <h1 :to="{ name: '/patient/department', params: { id: item.id } }">{{item.name}}</h1> -->
          <h1 @click="patientDepartment(item.id)">{{item.name}}</h1>
          <h3>{{item.description}}</h3>
        </b-card>
        <br />
        <!-- <b-card>
          <h3>Closed Services</h3>
          <h1>{{closed}}</h1>
        </b-card> -->
      </b-col>
      <!-- <b-col>
        <b-card>
          <h3>Unassigned Services</h3>
          <h1>{{unassigned}}</h1>
        </b-card>
        <br />
        <b-card>
          <h3>My Services</h3>
          <h1>{{my}}</h1>
        </b-card>
      </b-col>
      <b-col style="margin-right: 20px">
        <b-card>
          <h3>Overdue Services</h3>
          <h1>{{overdue}}</h1>
        </b-card>
        <br />
        <b-card>
          <h3>Total Services</h3>
          <h1>{{total}}</h1>
        </b-card>
      </b-col> -->
    </b-row>
  </div>
</template>

<script>
import NewHeader from "../layouts/NewHeader";
import PatientSideBar from "../layouts/PatientSideBar.vue";
// import { mapGetters, mapActions } from "vuex";
// import axios from "axios";

export default {
  name: "Dashboard",
  data() {
    return {
      data: [{
      id: 'asd123',
      name: 'Kirurgji',
      description: 'Departamenti per Kirurgji'
    },
    {
      id: 'asd321',
      name: 'Stomatologji',
      description: 'Departamenti per Stomatologji'
    }]
      // total: {},
      // unassigned: {},
      // overdue: {},
      // closed: {},
      // my: 1
    };
  },
  methods: {
    // ...mapActions(["getAllServices"])
    patientDepartment(id) {
      this.$router.push(`/patient/department/${id}`)
    }
  },
  // computed: mapGetters(["allServices"]),
  mounted() {
    // this.getAllServices();
    // axios.get("http://localhost:5000/api/services").then(response => {
    //   this.total = response.data.length;
    //   let countUn = 0;
    //   let countOver = 0;
    //   let countClose = 0;
    //   response.data.forEach(el => {
    //     if (el.unassigned === true) {
    //       countUn++;
    //     }
    //     if (el.overdue === true) {
    //       countOver++;
    //     }
    //     if (el.closed === true) {
    //       countClose++;
    //     }
    //   });
    //   this.unassigned = countUn;
    //   this.overdue = countOver;
    //   this.closed = countClose;
    // });
  },
  components: {
    NewHeader,
    PatientSideBar
  }
};
</script>

<style scoped></style>
