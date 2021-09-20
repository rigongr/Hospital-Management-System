<template>
  <div>
    <NewHeader />
    <DoctorSideBar />
  </div>
</template>

<script>
import NewHeader from "../components/layouts/NewHeader";
import DoctorSideBar from "../components/layouts/DoctorSideBar";

export default {
  name: "Service",
  components: {
    NewHeader,
    DoctorSideBar
  }
};
</script>

<style scoped></style>
