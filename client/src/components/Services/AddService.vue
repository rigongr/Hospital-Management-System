<template>
  <div>
    <div class="card mx-auto mt-4 customwidth">
      <article class="card-body">
        <p class="text-left">
          <router-link :to="{name: 'service-management'}">Home</router-link>
        </p>
        <h4 class="card-title text-center mb-4 mt-1">Add Service</h4>
        <hr />
        <p class="text-success text-center">{{ error }}</p>
        <form>
          <div class="form-group">
            <div class="input-group">
              <input v-model="name" id="name" class="form-control" placeholder="Name" type="text" />
            </div>
          </div>

          <div class="form-group">
            <div class="input-group">
              <div class="input-group-prepend">
                <input
                  type="file"
                  id="image"
                  name="image"
                  class="form-control-file"
                  @change="onFileChange"
                />
              </div>
            </div>
          </div>
          <div class="form-group">
            <div class="input-group">
              <input
                v-model="priority"
                id="priority"
                class="form-control"
                placeholder="Priority"
                type="text"
              />
            </div>
          </div>

          <div class="form-group">
            <div class="input-group">
              <input
                v-model="description"
                id="description"
                class="form-control"
                placeholder="Description"
                type="text"
              />
            </div>
          </div>

          <div class="form-group">
            <div class="input-group">
              <input
                v-model="status"
                id="status"
                class="form-control"
                placeholder="Status"
                type="text"
              />
            </div>
          </div>

          <div class="form-group">
            <div class="input-group">
              <input
                v-model="category"
                id="category"
                placeholder="Category"
                class="form-control"
                type="text"
              />
            </div>
          </div>

          <div class="form-group">
            <button
              :disabled="
                detailsError ||
                  typeError ||
                  priorityError ||
                  nameError ||
                  categoryError
              "
              type="submit"
              @click="handleAddService"
              class="btn btn-dark w-50 mt-4"
            >Add Service</button>
          </div>
        </form>
      </article>
    </div>
  </div>
</template>

<script>
import router from "../../router";
import { mapActions } from "vuex";
// import axios from "axios";

export default {
  name: "AddService",
  data() {
    return {
      name: "",
      description: "",
      status: "",
      priority: "",
      category: "",
      error: "",
      descriptionError: true,
      statusError: true,
      priorityError: true,
      nameError: true,
      categoryError: true
    };
  },

  updated() {
    this.validateDescription();
    this.validateStatus();
    this.validatePriority();
    this.validateName();
    this.validateCategory();
    console.log(
      this.descriptionError,
      this.statusError,
      this.priorityError,
      this.nameError,
      this.categoryError
    );
  },
  methods: {
    ...mapActions(["addService"]),

    validateStatus() {
      var re = new RegExp("^([a-z0-9]{5,})$");
      if (re.test(this.status)) {
        this.statusError = false;
      } else {
        this.statusError = true;
      }
    },

    validateDescription() {
      var re = new RegExp("^([a-z0-9]{5,})$");
      if (re.test(this.description)) {
        this.descriptionError = false;
      } else {
        this.descriptionError = true;
      }
    },

    validatePriority() {
      var re = new RegExp("^([a-z0-9]{5,})$");
      if (re.test(this.priority)) {
        this.priorityError = false;
      } else {
        this.priorityError = true;
      }
    },

    validateName() {
      var re = new RegExp("^([a-z0-9]{5,})$");

      if (re.test(this.name)) {
        this.nameError = false;
      } else {
        this.nameError = true;
      }
    },

    validateCategory() {
      var re = new RegExp("^([a-z0-9]{5,})$");
      if (re.test(this.category)) {
        this.categoryError = false;
      } else {
        this.categoryError = true;
      }
    },

    handleAddService(evt) {
      evt.preventDefault();

      var bodyFormData = new FormData();
      let image = document.getElementById("image");

      bodyFormData.set("name", this.name);
      bodyFormData.append("image", image.files[0]);
      bodyFormData.set("description", this.description);
      bodyFormData.set("status", this.status);
      bodyFormData.set("priority", this.priority);
      bodyFormData.set("category", this.category);

      this.addService(bodyFormData);
      router.replace({ name: "product" });
    },

    onFileChange(e) {
      const file = e.target.files[0];

      console.log(file);
    }
  }
};
</script>

<style></style>
