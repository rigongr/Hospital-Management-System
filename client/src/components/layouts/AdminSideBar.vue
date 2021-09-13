<template>
  <sidebar-menu :menu="menu" />
</template>

<script>
export default {
  data() {
    return {
      menu: [
        {
          header: true,
          title: "Main Navigation",
          hiddenOnCollapse: true
        },
        {
          href: "/admin/dashboard",
          title: "Dashboard",
          icon: "fa fa-user"
        },
        {
          href: "/admin",
          title: "Admin",
          icon: "fa fa-chart-area",
          child: [
            {
              href: "/admin/products",
              title: "Products"
            },
            {
              href: "/admin/services",
              title: "Services"
            },
            {
              href: "/admin/tickets",
              title: "Tickets"
            },
            {
              href: "/admin/users",
              title: "Users"
            }
          ]
        },
        {
          href: "/admin",
          title: "Tools",
          icon: "fa fa-user"
        },
        {
          href: "/admin",
          title: "Reports",
          icon: "fa fa-chart-area"
        },
        {
          href: "/admin",
          title: "Sign Out",
          icon: "fa fa-user"
        }
      ]
    };
  }
};
</script>

<style scoped>
</style>