<template>
  <div>
    <NewHeader />
    <PatientSideBar />
  </div>
</template>

<script>
import NewHeader from "../components/layouts/NewHeader";
import PatientSideBar from "../components/layouts/PatientSideBar";

export default {
  name: "Service",
  components: {
    NewHeader,
    PatientSideBar
  }
};
</script>

<style scoped></style>
