<template>
  <div>
    <NewHeader />
    <TicketSideBar />
    <TicketContent />
  </div>
</template>

<script>
import NewHeader from "../components/layouts/NewHeader";
import TicketContent from "../components/Tickets/TicketContent";
import TicketSideBar from "../components/layouts/TicketSideBar";

export default {
  name: "Ticket",
  components: {
    NewHeader,
    TicketContent,
    TicketSideBar
  }
};
</script>

<style scoped></style>
