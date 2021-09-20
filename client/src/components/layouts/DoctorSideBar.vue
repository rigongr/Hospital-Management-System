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
          href: "/doctor/dashboard",
          title: "Dashboard",
          icon: "fa fa-user"
        },
        {
          href: "/doctor",
          title: "Doctor",
          icon: "fa fa-chart-area",
          child: [
            {
              href: "/doctor/departments",
              title: "Departments"
            },
            {
              href: "/doctor/appointments",
              title: "Appointments"
            },
            {
              href: "/doctor/recipes",
              title: "Recipes"
            },
            {
              href: "/doctor/patients",
              title: "Patients"
            }
          ]
        },
        {
          href: "/doctor",
          title: "Tools",
          icon: "fa fa-user"
        },
        {
          href: "/doctor",
          title: "Reports",
          icon: "fa fa-chart-area"
        },
        {
          href: "/doctor",
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