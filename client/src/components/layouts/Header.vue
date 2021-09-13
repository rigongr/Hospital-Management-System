<template>
  <div class="w-100">
    <b-navbar
      toggleable="lg"
      class="navbar fixed-top grey lighten-4 z-depth-0"
      type="light"
      variant="light"
    >
      <b-container>
        <b-navbar-brand href="#" @click="goHome">SPITALI YT</b-navbar-brand>

        <b-nav-form>
          <b-form-input size="md" class="ml-1 w-100" placeholder="Search"></b-form-input>
        </b-nav-form>

        <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

        <b-collapse id="nav-collapse" is-nav>
          <b-navbar-nav class="ml-auto">
            <!-- BUTTON -->
            <b-button
              size="sm"
              v-if="getLogedIn === true || getUser !== null"
              :to="{ name: 'cart' , params: {userId: userId}} "
            >Cart</b-button>

            <ul class="navbar-nav">
              <li v-if="getLogedIn === false && getUser === null" class="nav-item active">
                <a class="nav-link">
                  <router-link class="links" to="/signup">Sign Up</router-link>

                  <span class="sr-only">(current)</span>
                </a>
              </li>
              <li v-if="getLogedIn === false && getUser === null" class="nav-item">
                <a class="nav-link">
                  <router-link class="links" to="/login">Log In</router-link>
                </a>
              </li>
            </ul>
            <div v-if="getLogedIn === true || getUser !== null">
              <b-nav-item-dropdown right class="ml-3">
                <!-- Using 'button-content' slot -->
                <template v-slot:button-content>User</template>
                <b-dropdown-item>Profile</b-dropdown-item>
                <b-dropdown-item @click="logedInFalse">Sign Out</b-dropdown-item>
              </b-nav-item-dropdown>
            </div>
          </b-navbar-nav>
        </b-collapse>
      </b-container>
    </b-navbar>
  </div>
</template>

<script>
import { mapGetters, mapActions } from "vuex";

export default {
  name: "Header",
  components: {},
  data() {
    return {
      search: "",
      userId: ""
    };
  },

  updated() {
    // console.log(this.getChecked);
  },
  computed: {
    ...mapGetters(["getUser", "getLogedIn"]),
    currentUser() {
      return this.$store.getters["getUser"].userId;
    }
  },
  methods: {
    ...mapActions(["logedInFalse"]),
    goHome() {
      this.$router.push("/");
    }
    // handleChecked() {
    // this.checked = !this.checked;
    // this.setChecked();
    // },
    // filterPosts($event) {
    //   console.log($event, "event");
    //   console.log(this.search);
    //   this.fetchPostsWithSearch(this.search);
    // }
  },
  mounted() {
    this.userId = this.$store.getters["getUser"].userId;
  }
};
</script>

<style scoped>
.links {
  color: black;
}
.links:hover {
  text-decoration: none;
}
.start {
  position: fixed;
  top: 0;
  width: 100%;
}
</style>
