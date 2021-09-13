<template>
  <div>
    <NewHeader />
    <ServiceSideBar />
    <ServiceContent />
  </div>
</template>

<script>
import NewHeader from "../components/layouts/NewHeader";
import ServiceContent from "../components/Services/ServiceContent";
import ServiceSideBar from "../components/layouts/ServiceSideBar";

export default {
  name: "Service",
  components: {
    NewHeader,
    ServiceContent,
    ServiceSideBar
  }
};
</script>

<style scoped></style>
