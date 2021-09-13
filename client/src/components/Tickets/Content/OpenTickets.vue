<template>
  <div>
    <NewHeader />
    <TicketSideBar />
    <b-card-group deck style="margin: 20px 50px 0 400px">
      <b-card header="Open Tickets">
        <b-list-group v-for="ticket in allTickets" :key="ticket._id">
          <b-list-group-item
            :to="{ name: 'ticket-details', params: { prodId: ticket._id } }"
            v-if="ticket.unassigned === true"
          >{{ticket.title}}</b-list-group-item>
        </b-list-group>

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
import TicketSideBar from "../../layouts/TicketSideBar";
import { mapGetters, mapActions } from "vuex";

export default {
  name: "OpenTickets",
  methods: {
    ...mapActions(["getAllTickets"])
  },
  computed: mapGetters(["allTickets"]),
  mounted() {
    this.getAllTickets();
  },
  components: {
    NewHeader,
    TicketSideBar
  }
};
</script>

<style scoped></style>
