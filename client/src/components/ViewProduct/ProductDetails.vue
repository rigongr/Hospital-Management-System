<template>
  <!-- News jumbotron -->
  <div class="jumbotron text-center hoverable p-4 container z-depth-0">
    <!-- Grid row -->
    <div class="row">
      <!-- Grid column -->
      <div class="col-md-4 offset-md-1 mx-3 my-3">
        <!-- Featured image -->
        <div class="view overlay">
          <img
            src="https://mdbootstrap.com/img/Photos/Others/laptop-sm.jpg"
            class="img-fluid"
            alt="Sample image for first version of blog listing"
          />
          <a>
            <div class="mask rgba-white-slight"></div>
          </a>
        </div>
      </div>
      <!-- Grid column -->

      <!-- Grid column -->
      <div
        class="col-md-7 text-md-left ml-3 mt-3"
        v-for="product in allProducts"
        :key="product._id"
      >
        <!-- Excerpt -->
        <a href="#!" class="green-text" v-if="product._id === productId">
          <h6 class="h6 pb-1">
            <i class="fas fa-desktop pr-1"></i> Work
          </h6>
        </a>

        <!-- TODO: v-if to check for the interested id -->
        <h4 class="h4 mb-4" v-if="product._id === productId">{{product.name}}</h4>
        <p class="font-weight-normal" v-if="product._id === productId">{{product.details}}</p>
        <p class="font-weight-normal" v-if="product._id === productId">
          by
          <a>
            <strong>Carine Fox</strong>
          </a>, 19/08/2016
        </p>

        <a
          class="btn btn-success"
          v-if="product._id === productId"
          @click="handleAddItem"
        >Add To Cart</a>
      </div>
      <!-- Grid column -->
    </div>
    <!-- Grid row -->
  </div>
  <!-- News jumbotron -->
</template>

<script>
import { mapGetters, mapActions } from "vuex";

export default {
  name: "ProductDetails",
  data() {
    return {
      products: {},
      productId: {},
      user: "",
      name: "",
      price: null
    };
  },
  methods: {
    ...mapActions(["getAllProducts"]),
    ...mapActions(["addCart"]),
    handleAddItem(evt) {
      evt.preventDefault();

      let bodyFormData = {
        user: this.user,
        product: this.productId,
        name: this.name,
        price: this.price
      };

      this.addCart(bodyFormData);
    }
  },
  computed: {
    ...mapGetters(["getUser"]),
    ...mapGetters(["allProducts"]),
    currentProduct() {
      console.log(this.$store.getters["allProducts"]);
      return this.$store.getters["allProducts"];
    }
  },
  mounted() {
    this.user = this.$store.getters["getUser"].userId;
    this.products = this.$store.getters["allProducts"];
    this.productId = this.$route.params.prodId;
    this.products.forEach(el => {
      if (el._id === this.productId) {
        this.name = el.name;
        this.price = el.price;
      }
    });
    this.getAllProducts();
  },
  updated() {
    console.log(this.allProducts, "allproducts");
  }
};
</script>

<style scoped>
</style>