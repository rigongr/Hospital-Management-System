<template>
  <div>
    <NewHeader />
    <ServiceSideBar />
    <AddService />
  </div>
</template>

<script>
import NewHeader from "../../layouts/NewHeader";
import ServiceSideBar from "../../layouts/ServiceSideBar";
import AddService from "../AddService";

export default {
  name: "CreateService",
  components: {
    NewHeader,
    ServiceSideBar,
    AddService
  }
};
</script>

<style scoped></style>
