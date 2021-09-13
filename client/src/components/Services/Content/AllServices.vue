<template>
  <div>
    <NewHeader />
    <ServiceSideBar />
    <b-card-group deck style="margin: 20px 50px 0 400px">
      <b-card header="All Services">
        <b-list-group v-for="service in allServices" :key="service._id">
          <b-list-group-item
            :to="{ name: 'service-details', params: { prodId: service._id } }"
          >{{service.name}}</b-list-group-item>
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
import ServiceSideBar from "../../layouts/ServiceSideBar";
import { mapGetters, mapActions } from "vuex";

export default {
  name: "AllServices",
  methods: {
    ...mapActions(["getAllServices"])
  },
  computed: mapGetters(["allServices"]),
  mounted() {
    this.getAllServices();
  },
  components: {
    NewHeader,
    ServiceSideBar
  }
};
</script>

<style scoped>
</style>
