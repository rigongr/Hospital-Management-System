<template>
  <div>
    <NewHeader />
    <AdminSideBar />
    <b-card-group deck style="margin: 20px 50px 0 400px">
      <b-card header="All Products">
        <b-list-group v-for="product in allProducts" :key="product._id">
          <b-list-group-item
            :to="{ name: 'product-management-details', params: { prodId: product._id } }"
          >
            {{product.name}}
            <b-button
              size="sm"
              @click="removeProduct(product)"
              :to="{ name: 'product-management'}"
              class="float-right"
              variant="danger"
            >Remove</b-button>
          </b-list-group-item>
        </b-list-group>
        <b-button size="sm" class="float-left" variant="success" :to="{ name: 'add-product'}">Create</b-button>

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
    ...mapActions(["getAllProducts"]),
    ...mapActions(["deleteProduct"]),
    removeProduct(productId) {
      this.deleteProduct(productId);
    }
  },
  computed: mapGetters(["allProducts"]),
  mounted() {
    this.getAllProducts();
  },
  components: {
    NewHeader,
    AdminSideBar
  }
};
</script>

<style scoped>
</style>
