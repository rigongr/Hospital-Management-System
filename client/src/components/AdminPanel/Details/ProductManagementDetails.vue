<template>
  <div>
    <NewHeader />
    <AdminSideBar />
    <div v-for="product in allProducts" :key="product._id">
      <b-card-group deck style="margin: 20px 50px 0 400px" v-if="product._id === productId">
        <b-card header="Product Details">
          <b-row>
            <b-col>
              <label for="example1">Name</label>
              <input type="text" id="name" class="form-control" v-model="name" />
              <label for="example1">Description</label>
              <input type="text" id="description" class="form-control" v-model="description" />
              <label for="example1">Status</label>
              <b-form-select v-model="selected" :options="options"></b-form-select>
              <label for="example1">Priority</label>
              <b-form-select v-model="selectedP" :options="optionsP"></b-form-select>
            </b-col>
            <b-col>
              <label for="example1">Category</label>
              <input type="text" id="category" class="form-control" v-model="category" />
              <label for="example1">Assigned</label>
              <input type="text" id="example1" class="form-control" :value="product.assigned" />
              <b-form-checkbox
                id="checkbox-1"
                v-model="overdue"
                name="checkbox-1"
                value="accepted"
                unchecked-value="not_accepted"
                style="margin-top: 40px"
              >Overdue</b-form-checkbox>
              <b-form-checkbox
                id="checkbox-2"
                v-model="closed"
                name="checkbox-2"
                value="accepted"
                unchecked-value="not_accepted"
                style="margin-top: 40px"
              >Close Product</b-form-checkbox>
            </b-col>
          </b-row>
          <br />
          <b-button size="sm" variant="primary" @click="handleUpdateProduct">Save</b-button>
          <b-button size="sm" variant="danger" @click="$router.go(-1)">Close</b-button>
        </b-card>
      </b-card-group>
    </div>
  </div>
</template>

<script>
import router from "../../../router";
import NewHeader from "../../layouts/NewHeader";
import AdminSideBar from "../../layouts/AdminSideBar";
import axios from "axios";
import { mapGetters, mapActions } from "vuex";

export default {
  name: "ProductManagementDetails",
  data() {
    return {
      productId: {},
      selected: null,
      options: [
        { value: null, text: "Please select an option" },
        { value: "a", text: "To do" },
        { value: "b", text: "Doing" },
        { value: "c", text: "Done" }
      ],
      selectedP: null,
      optionsP: [
        { value: null, text: "Please select an option" },
        { value: "a", text: "Low" },
        { value: "b", text: "Medium" },
        { value: "c", text: "High" }
      ],
      name: "",
      description: "",
      status: "",
      priority: "",
      category: ""
    };
  },
  methods: {
    ...mapActions(["getAllProducts"]),
    ...mapActions(["updateProduct"]),
    handleUpdateProduct(evt) {
      evt.preventDefault();

      let bodyData = {
        _id: this.productId,
        title: this.name,
        img: "",
        description: this.description,
        status: this.status,
        priority: this.priority,
        category: this.category,
        assigned: true,
        unassigned: false,
        overdue: false,
        closed: false
      };
      this.updateProduct(bodyData);
      router.go(-1);
    }
  },
  computed: mapGetters(["allProducts"]),
  mounted() {
    this.productId = this.$route.params.prodId;
    this.value = axios
      .get("http://localhost:5000/api/products/" + this.productId)
      .then(response => {
        this.name = response.data.title;
        this.description = response.data.description;
        this.category = response.data.category;
      });
    this.getAllProducts();
    this.updateProduct();
  },
  components: {
    NewHeader,
    AdminSideBar
  }
};
</script>

<style scoped>
</style>