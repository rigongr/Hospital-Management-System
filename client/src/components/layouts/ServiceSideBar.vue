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
          href: "/services/dashboard",
          title: "Dashboard",
          icon: "fa fa-user"
        },
        {
          href: "/services",
          title: "Services",
          icon: "fa fa-chart-area",
          child: [
            {
              href: "/services/create-services",
              title: "Create Service"
            },
            {
              href: "/services/all-services",
              title: "All Services"
            },
            {
              href: "/services/my-services",
              title: "My Services"
            },
            {
              href: "/services/open-services",
              title: "Unassigned"
            },
            {
              href: "/services/overdue-services",
              title: "Overdue"
            },
            {
              href: "/services/closed-services",
              title: "Closed"
            }
          ]
        },
        {
          href: "/services/all-services",
          title: "Tools",
          icon: "fa fa-user"
        },
        {
          href: "/services/all-services",
          title: "Reports",
          icon: "fa fa-chart-area"
        },
        {
          href: "/services/all-services",
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