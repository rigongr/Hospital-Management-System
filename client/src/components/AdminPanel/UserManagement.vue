<template>
  <div>
    <NewHeader />
    <AdminSideBar />
    <b-card-group deck style="margin: 20px 50px 0 400px">
      <b-card header="All Users">
        <b-list-group v-for="user in allUsers" :key="user._id">
          <b-list-group-item
            :to="{ name: 'user-management-details', params: { prodId: user._id } }"
          >
            {{user.name}}
            <b-button
              size="sm"
              @click="removeUser(user)"
              :to="{ name: 'user-management'}"
              class="float-right"
              variant="danger"
            >Remove</b-button>
          </b-list-group-item>
        </b-list-group>
        <b-button size="sm" class="float-left" variant="success" :to="{ name: 'add-user'}">Create</b-button>

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
  name: "ProductManagement",
  methods: {
    ...mapActions(["getAllUsers"]),
    ...mapActions(["deleteUsr"]),
    removeUser(user) {
      this.deleteUsr(user);
    }
  },
  computed: mapGetters(["allUsers"]),
  mounted() {
    this.getAllUsers();
  },
  components: {
    NewHeader,
    AdminSideBar
  }
};
</script>

<style scoped>
</style>
