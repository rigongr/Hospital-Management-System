<template>
  <div>
    <NewHeader />
    <AdminSideBar />
    <h1 style="margin-left: 350px">Dashboard</h1>
    <b-row style="margin-left: 350px">
      <b-col>
        <b-card>
          <h3>Users</h3>
          <h1>{{users}}</h1>
        </b-card>
        <br />
        <b-card>
          <h3>Tickets</h3>
          <h1>{{tickets}}</h1>
        </b-card>
      </b-col>
      <b-col>
        <b-card>
          <h3>Services</h3>
          <h1>{{services}}</h1>
        </b-card>
        <br />
        <b-card>
          <h3>Overdue Services</h3>
          <h1>15</h1>
        </b-card>
      </b-col>
      <b-col style="margin-right: 20px">
        <b-card>
          <h3>Products</h3>
          <h1>{{products}}</h1>
        </b-card>
        <br />
        <b-card>
          <h3>Total Services</h3>
          <h1>15</h1>
        </b-card>
      </b-col>
    </b-row>
  </div>
</template>

<script>
import NewHeader from "../layouts/NewHeader";
import AdminSideBar from "../layouts/AdminSideBar";
import { mapGetters, mapActions } from "vuex";
import axios from "axios";

export default {
  name: "AdminDashboard",
  data() {
    return {
      services: {},
      users: {},
      products: {},
      tickets: {}
    };
  },
  methods: {
    ...mapActions(["getAllServices"]),
    ...mapActions(["getAllProducts"]),
    ...mapActions(["getAllUsers"]),
    ...mapActions(["getAllTickets"])
  },
  computed: mapGetters([
    "allServices",
    "allProducts",
    "allUsers",
    "allTickets"
  ]),
  mounted() {
    this.getAllServices();
    this.getAllProducts();
    this.getAllUsers();
    this.getAllTickets();
    axios.get("http://localhost:5000/api/services").then(response => {
      this.services = response.data.length;
    });
    axios.get("http://localhost:5000/api/tickets").then(response => {
      this.tickets = response.data.length;
    });
    axios.get("http://localhost:5000/api/users").then(response => {
      this.users = response.data.length;
    });
    axios.get("http://localhost:5000/api/products").then(response => {
      this.products = response.data.length;
    });
  },
  components: {
    NewHeader,
    AdminSideBar
  }
};
</script>

<style scoped></style>
