<template>
  <div>
    <Header />
    <CartContent style="margin: 100px 100px 0 0" />
    <ProductContent />
    <Footer />
  </div>
</template>

<script>
import Header from "../components/layouts/Header";
import Footer from "../components/layouts/Footer";
import CartContent from "../components/Cart/CartContent";
import ProductContent from "../components/Products/ProductContent";

export default {
  name: "Cart",
  components: {
    Header,
    Footer,
    CartContent,
    ProductContent
  }
};
</script>

<style scoped>
</style>