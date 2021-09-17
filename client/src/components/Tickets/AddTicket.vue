<template>
  <div>
    <div class="card mx-auto mt-4 customwidth">
      <article class="card-body">
        <p class="text-left">
          <router-link :to="{name: 'ticket-management'}">Home</router-link>
        </p>
        <h4 class="card-title text-center mb-4 mt-1">Add Ticket</h4>
        <hr />
        <p class="text-success text-center">{{ error }}</p>
        <form>
          <div class="form-group">
            <div class="input-group">
              <input
                v-model="title"
                id="title"
                class="form-control"
                placeholder="Title"
                type="text"
              />
            </div>
          </div>

          <div class="form-group">
            <div class="input-group">
              <div class="input-group-prepend">
                <input
                  type="file"
                  id="image"
                  title="image"
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
                  titleError ||
                  categoryError
              "
              type="submit"
              @click="handleAddTicket"
              class="btn btn-dark w-50 mt-4"
            >Add Ticket</button>
          </div>
        </form>
      </article>
    </div>
  </div>
</template>

<script>
import router from "../../router";
import { mapActions } from "vuex";

export default {
  title: "AddTicket",
  data() {
    return {
      title: "",
      description: "",
      status: "",
      priority: "",
      category: "",
      error: "",
      descriptionError: true,
      statusError: true,
      priorityError: true,
      titleError: true,
      categoryError: true
    };
  },

  updated() {
    this.validateDescription();
    this.validateStatus();
    this.validatePriority();
    this.validateTitle();
    this.validateCategory();
    console.log(
      this.descriptionError,
      this.statusError,
      this.priorityError,
      this.titleError,
      this.categoryError
    );
  },
  methods: {
    ...mapActions(["addTicket"]),

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

    validateTitle() {
      var re = new RegExp("^([a-z0-9]{5,})$");

      if (re.test(this.title)) {
        this.titleError = false;
      } else {
        this.titleError = true;
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

    handleAddTicket(evt) {
      evt.preventDefault();

      var bodyFormData = new FormData();
      let image = document.getElementById("image");

      bodyFormData.set("title", this.title);
      bodyFormData.append("image", image.files[0]);
      bodyFormData.set("description", this.description);
      bodyFormData.set("status", this.status);
      bodyFormData.set("priority", this.priority);
      bodyFormData.set("category", this.category);

      this.addTicket(bodyFormData);
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
