<template>
  <div>
    <b-card-group deck style="margin: 20px 50px 0 300px">
      <b-card header="Cart">
        <b-list-group v-for="cart in allCarts" :key="cart._id">
          <b-list-group-item v-if="cart.user === userId">
            <p class="float-left anash text-muted">{{cart.name}}</p>
            <b-button
              variant="primary"
              size="sm"
              class="float-right"
              @click="removeItem(cart._id)"
            >Remove</b-button>
            <p class="float-right shtyje text-muted">{{cart.price}}</p>
          </b-list-group-item>
        </b-list-group>

        <b-button variant="primary" size="sm" @click="buyAll">Buy</b-button>
      </b-card>
    </b-card-group>
  </div>
</template>

<script>
import { mapGetters, mapActions } from "vuex";
import axios from "axios";

export default {
  name: "CartContent",
  data() {
    return {
      userId: {},
      total: {}
    };
  },
  methods: {
    ...mapActions(["getAllCarts"]),
    ...mapActions(["deleteCart"]),
    removeItem(cartId) {
      this.deleteCart(cartId);
    },
    buyAll() {
      this.total = this.total.filter(response => {
        return response.user === this.userId;
      });

      this.total.forEach(el => {
        this.deleteCart(el._id);
      });
    }
  },
  computed: mapGetters(["allCarts"]),
  mounted() {
    this.userId = this.$route.params.userId;
    this.getAllCarts();
    axios.get("http://localhost:5000/api/cart").then(response => {
      this.total = response.data;
    });
  }
};
</script>

<style scoped>
p {
  display: inline;
  margin: 0;
}

.shtyje {
  margin-right: 30px;
  margin-top: 10px;
}

.anash {
  margin-top: 10px;
}
</style>