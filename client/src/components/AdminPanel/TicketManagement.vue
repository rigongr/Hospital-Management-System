<template>
  <div>
    <NewHeader />
    <AdminSideBar />
    <b-card-group deck style="margin: 20px 50px 0 400px">
      <b-card header="All Tickets">
        <b-list-group v-for="ticket in allTickets" :key="ticket._id">
          <b-list-group-item
            :to="{ name: 'ticket-management-details', params: { prodId: ticket._id } }"
          >
            {{ticket.title}}
            <b-button
              size="sm"
              @click="removeTicket(ticket)"
              :to="{ name: 'ticket-management'}"
              class="float-right"
              variant="danger"
            >Remove</b-button>
          </b-list-group-item>
        </b-list-group>
        <b-button size="sm" class="float-left" variant="success" :to="{ name: 'add-ticket'}">Create</b-button>

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
import NewHeader from "../layouts/NewHeader";
import AdminSideBar from "../layouts/AdminSideBar";
import { mapGetters, mapActions } from "vuex";

export default {
  name: "TicketManagement",
  methods: {
    ...mapActions(["getAllTickets"]),
    ...mapActions(["deleteTicket"]),
    removeTicket(ticket) {
      this.deleteTicket(ticket);
    }
  },
  computed: mapGetters(["allTickets"]),
  mounted() {
    this.getAllTickets();
  },
  components: {
    NewHeader,
    AdminSideBar
  }
};
</script>

<style scoped>
</style>
