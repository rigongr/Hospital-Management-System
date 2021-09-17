<template>
  <div>
    <div class="card mx-auto mt-4 customwidth">
      <article class="card-body">
        <p class="text-left">
          <router-link :to="{name: 'product-management'}">Home</router-link>
        </p>
        <h4 class="card-title text-center mb-4 mt-1">Add Product</h4>
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
                v-model="supplier"
                id="supplier"
                class="form-control"
                placeholder="Supplier"
                type="text"
              />
            </div>
          </div>

          <div class="form-group">
            <div class="input-group">
              <input
                v-model="details"
                id="details"
                class="form-control"
                placeholder="Details"
                type="text"
              />
            </div>
          </div>

          <div class="form-group">
            <div class="input-group">
              <input v-model="type" id="type" class="form-control" placeholder="Type" type="text" />
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
                  supplierError ||
                  nameError ||
                  categoryError
              "
              type="submit"
              @click="handleAddProduct"
              class="btn btn-dark w-50 mt-4"
            >Add Product</button>
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
  name: "AddProduct",
  data() {
    return {
      details: "",
      type: "",
      supplier: "",
      name: "",
      category: "",
      error: "",
      detailsError: true,
      typeError: true,
      supplierError: true,
      nameError: true,
      categoryError: true
    };
  },

  updated() {
    this.validateDetails();
    this.validateType();
    this.validateSupplier();
    this.validateName();
    this.validateCategory();
    console.log(
      this.typeError,
      this.detailsError,
      this.supplierError,
      this.nameError,
      this.categoryError
    );
  },
  methods: {
    ...mapActions(["addProduct"]),

    validateDetails() {
      var re = new RegExp("^([a-z0-9]{5,})$");
      if (re.test(this.details)) {
        this.detailsError = false;
      } else {
        this.detailsError = true;
      }
    },

    validateType() {
      var re = new RegExp("^([a-z0-9]{5,})$");
      if (re.test(this.type)) {
        this.typeError = false;
      } else {
        this.typeError = true;
      }
    },

    validateSupplier() {
      var re = new RegExp("^([a-z0-9]{5,})$");
      if (re.test(this.supplier)) {
        this.supplierError = false;
      } else {
        this.supplierError = true;
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

    handleAddProduct(evt) {
      evt.preventDefault();

      var bodyFormData = new FormData();
      let image = document.getElementById("image");

      bodyFormData.set("name", this.name);
      bodyFormData.append("image", image.files[0]);
      bodyFormData.set("details", this.details);
      bodyFormData.set("type", this.type);
      bodyFormData.set("supplier", this.supplier);
      bodyFormData.set("category", this.category);

      this.addProduct(bodyFormData);
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
