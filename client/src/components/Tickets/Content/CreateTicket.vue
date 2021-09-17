<template>
  <div>
    <NewHeader />
    <TicketSideBar />
    <CreateService />
  </div>
</template>

<script>
import NewHeader from "../../layouts/NewHeader";
import TicketSideBar from "../../layouts/TicketSideBar";
import CreateService from "../AddTicket";

export default {
  name: "CreateTicket",
  components: {
    NewHeader,
    TicketSideBar,
    CreateService
  }
};
</script>

<style scoped></style>
