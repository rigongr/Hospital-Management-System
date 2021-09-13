<template>
  <div>
    <NewHeader />
    <TicketSideBar />
    <h1 style="margin-left: 350px">Dashboard</h1>
    <b-row style="margin-left: 350px">
      <b-col>
        <b-card>
          <h3>Total Tickets</h3>
          <h1>{{total}}</h1>
        </b-card>
        <br />
        <b-card>
          <h3>Closed Tickets</h3>
          <h1>{{closed}}</h1>
        </b-card>
      </b-col>
      <b-col>
        <b-card>
          <h3>Unassigned Tickets</h3>
          <h1>{{unassigned}}</h1>
        </b-card>
        <br />
        <b-card>
          <h3>My Tickets</h3>
          <h1>{{my}}</h1>
        </b-card>
      </b-col>
      <b-col style="margin-right: 20px">
        <b-card>
          <h3>Overdue Tickets</h3>
          <h1>{{overdue}}</h1>
        </b-card>
        <br />
        <b-card>
          <h3>Total Tickets</h3>
          <h1>{{total}}</h1>
        </b-card>
      </b-col>
    </b-row>
  </div>
</template>

<script>
import NewHeader from "../../layouts/NewHeader";
import TicketSideBar from "../../layouts/TicketSideBar";
import { mapGetters, mapActions } from "vuex";
import axios from "axios";

export default {
  name: "Dashboard",
  data() {
    return {
      total: {},
      unassigned: {},
      overdue: {},
      closed: {},
      my: 1
    };
  },
  methods: {
    ...mapActions(["getAllTickets"])
  },
  computed: mapGetters(["allTickets"]),
  mounted() {
    this.getAllTickets();
    axios.get("http://localhost:5000/api/tickets").then(response => {
      this.total = response.data.length;
      let countUn = 0;
      let countOver = 0;
      let countClose = 0;
      response.data.forEach(el => {
        if (el.unassigned === true) {
          countUn++;
        }
        if (el.overdue === true) {
          countOver++;
        }
        if (el.closed === true) {
          countClose++;
        }
      });
      this.unassigned = countUn;
      this.overdue = countOver;
      this.closed = countClose;
    });
  },
  components: {
    NewHeader,
    TicketSideBar
  }
};
</script>

<style scoped></style>
