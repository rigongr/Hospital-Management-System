<template>
  <div>
    <NewHeader />
    <PatientSideBar />
    <b-card-group deck style="margin: 20px 50px 0 400px">
      <b-card header="Recipes">
        <b-list-group v-for="item in data" :key="item.id">
          <b-list-group-item
            :to="{ name: 'service-management-details', params: { prodId: item.id } }"
          >
            {{item.name}}
            <b-button
              size="sm"
              @click="removeService(item)"
              :to="{ name: 'service-management'}"
              class="float-right"
              variant="success"
            >Appoint</b-button>
          </b-list-group-item>
        </b-list-group>
        <!-- <b-button size="sm" class="float-left" variant="success" :to="{ name: 'add-service'}">Create</b-button> -->

        <p class="card-text mt-2">
          Quis magna Lorem anim amet ipsum do mollit sit cillum voluptate ex nulla tempor. Laborum
          consequat non elit enim exercitation cillum aliqua consequat id aliqua. Esse ex consectetur
          mollit voluptate est in duis laboris ad sit ipsum anim Lorem.
        </p>
      </b-card>
    </b-card-group>
  </div>
</template>

<script>
import NewHeader from "../../layouts/NewHeader";
import PatientSideBar from "../../layouts/PatientSideBar.vue";
// import { mapGetters, mapActions } from "vuex";
// import axios from "axios";

export default {
  name: "Dashboard",
  data() {
    return {
      data: [{
      id: 'asd123',
      name: 'Doktorri 1',
      description: 'Departamenti per Kirurgji'
    },
    {
      id: 'asd321',
      name: 'Doktorri 2',
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
