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
          href: "/tickets/dashboard",
          title: "Dashboard",
          icon: "fa fa-user"
        },
        {
          href: "/tickets",
          title: "tickets",
          icon: "fa fa-chart-area",
          child: [
            {
              href: "/tickets/create-tickets",
              title: "Create Ticket"
            },
            {
              href: "/tickets/all-tickets",
              title: "All Tickets"
            },
            {
              href: "/tickets/my-tickets",
              title: "My Tickets"
            },
            {
              href: "/tickets/open-tickets",
              title: "Unassigned"
            },
            {
              href: "/tickets/overdue-tickets",
              title: "Overdue"
            },
            {
              href: "/tickets/closed-tickets",
              title: "Closed"
            }
          ]
        },
        {
          href: "/tickets/all-tickets",
          title: "Tools",
          icon: "fa fa-user"
        },
        {
          href: "/tickets/all-tickets",
          title: "Reports",
          icon: "fa fa-chart-area"
        },
        {
          href: "/tickets/all-tickets",
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