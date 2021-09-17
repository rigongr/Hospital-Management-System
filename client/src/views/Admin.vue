<template>
  <div>
    <NewHeader />
    <AdminSideBar />
  </div>
</template>

<script>
import NewHeader from "../components/layouts/NewHeader";
import AdminSideBar from "../components/layouts/AdminSideBar";

export default {
  name: "Service",
  components: {
    NewHeader,
    AdminSideBar
  }
};
</script>

<style scoped></style>
