<template>
  <div class="container" style="margin-top:75px">
    <div class="featured">
      <h4>Featured Products</h4>
    </div>
    <div class="row">
      <mdb-container>
        <mdb-row>
          <mdb-card-group deck>
            <mdb-card class="hoverable" v-for="product in allProducts" :key="product._id">
              <mdb-view hover>
                <a href="#!">
                  <mdb-card-image
                    :src="`http://localhost:5000/${product.img}`"
                    alt="Card image cap"
                  ></mdb-card-image>
                  <mdb-mask flex-center waves overlay="white-slight"></mdb-mask>
                </a>
              </mdb-view>
              <mdb-card-body>
                <mdb-card-title>{{product.name}}</mdb-card-title>
                <mdb-card-text>{{product.details}}</mdb-card-text>
                <router-link
                  :to="{ name: 'viewproduct', params: { prodId: product._id } }"
                >Go to your profile</router-link>
                <!-- <mdb-btn color="primary">Read more</mdb-btn> -->
              </mdb-card-body>
            </mdb-card>
          </mdb-card-group>
        </mdb-row>
      </mdb-container>
    </div>
  </div>
</template>

<script>
import {
  mdbContainer,
  mdbRow,
  mdbCard,
  mdbCardImage,
  mdbCardBody,
  mdbCardTitle,
  mdbCardText,
  mdbCardGroup,
  // mdbBtn,
  mdbView,
  mdbMask
} from "mdbvue";
import { mapGetters, mapActions } from "vuex";

export default {
  name: "ProductContent",
  methods: {
    ...mapActions(["getAllProducts"])
  },
  computed: mapGetters(["allProducts"]),
  mounted() {
    this.getAllProducts();
  },
  updated() {
    console.log(this.allProducts, "allproducts");
  },
  components: {
    mdbContainer,
    mdbRow,
    mdbCard,
    mdbCardImage,
    mdbCardBody,
    mdbCardTitle,
    mdbCardText,
    mdbCardGroup,
    // mdbBtn,
    mdbView,
    mdbMask
  }
};
</script>

<style scoped>
.featured {
  margin-bottom: 40px;
}
</style>
