<template>
  <div>
    <div
      class="card mx-auto mt-4 customwidth"
      :class="{ post: getChecked === false, postblack: getChecked === true }"
    >
      <article class="card-body">
        <p class="text-left">
          <router-link to="/"> Home </router-link>
        </p>
        <h4 class="card-title text-center mb-4 mt-1">Sign Up</h4>
        <hr />
        <p class="text-success text-center">{{ error }}</p>
        <form>
          <div class="form-group">
            <div class="input-group">
              <div class="input-group-prepend">
                <span class="input-group-text">
                  <i class="fa fa-user"></i>
                </span>
              </div>
              <input
                v-model="name"
                id="name"
                class="form-control"
                placeholder="Name"
                type="text"
              />
            </div>
          </div>
          <div class="form-group">
            <div class="input-group">
              <div class="input-group-prepend">
                <span class="input-group-text">
                  <i class="fa fa-user"></i>
                </span>
              </div>
              <input
                v-model="username"
                id="username"
                class="form-control"
                placeholder="Username"
                type="text"
              />
            </div>
          </div>

          <div class="form-group">
            <div class="input-group">
              <div class="input-group-prepend">
                <span class="input-group-text">
                  <i class="fa fa-user"></i>
                </span>
              </div>
              <input
                v-model="email"
                id="email"
                class="form-control"
                placeholder="Email"
                type="email"
              />
            </div>
          </div>
          <div class="form-group">
            <div class="input-group">
              <div class="input-group-prepend">
                <span class="input-group-text">
                  <i class="fa fa-lock"></i>
                </span>
              </div>
              <input
                v-model="password"
                id="password"
                placeholder="Password"
                class="form-control"
                type="password"
              />
            </div>
          </div>

          <div class="form-group">
            <button
              :disabled="emailError || passwordError || usernameError"
              type="submit"
              @click="onSignup"
              class="btn btn-dark w-50 mt-4"
            >
              Sign Up
            </button>
          </div>
          <p class="text-center">
            <router-link to="/login" class="btn btn-default"
              >Already have an account Log In</router-link
            >
          </p>
        </form>
      </article>
    </div>
  </div>
</template>

<script>
import router from "../../router";
import { mapActions, mapGetters } from "vuex";
// import axios from "axios";

export default {
  name: "SignUp",
  data() {
    return {
      username: "",
      email: "",
      password: "",
      name: "",
      admin: false,
      error: "",
      usernameError: true,
      passwordError: true,
      emailError: true,
      nameError: true,
    };
  },

  computed: mapGetters(["getLogedIn", "getChecked"]),
  updated() {
    this.validateName();
    this.validateUsername();
    this.validateEmail();
    this.validatePassword();
  },
  methods: {
    ...mapActions(["signup"]),
    validateName() {
      var re = new RegExp("^([a-z0-9]{5,})$");
      if (re.test(this.name)) {
        this.nameError = false;
      } else {
        this.nameError = true;
      }
    },

    validateUsername() {
      var re = new RegExp("^([a-z0-9]{5,})$");
      if (re.test(this.username)) {
        this.usernameError = false;
      } else {
        this.usernameError = true;
      }
    },

    validatePassword() {
      if (this.password.length > 5) {
        this.passwordError = false;
      } else {
        this.passwordError = true;
      }
    },

    validateEmail() {
      var re = /^(([^<>()\]\\.,;:\s@"]+(\.[^<>()\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
      if (re.test(String(this.email).toLowerCase())) {
        this.emailError = false;
      } else {
        this.emailError = true;
      }
    },

    onSignup(evt) {
      evt.preventDefault();
      const data = {
        name: this.name,
        username: this.username,
        email: this.email,
        password: this.password,
      };

      this.signup(data);
      router.replace({ name: "product" });
    },
  },
};
</script>

<style></style>
