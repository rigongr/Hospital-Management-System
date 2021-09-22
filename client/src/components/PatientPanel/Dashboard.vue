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
          href: "/patient/dashboard",
          title: "Dashboard",
          icon: "fa fa-user"
        },
        {
          href: "/patient",
          title: "Patient",
          icon: "fa fa-chart-area",
          child: [
            {
              href: "/patient/departments",
              title: "Departments"
            },
            {
              href: "/patient/doctors",
              title: "Doctors"
            },
            {
              href: "/patient/appointments",
              title: "Appointments"
            },
            {
              href: "/patient/recipes",
              title: "Recipes"
            },
            {
              href: "/patient/drugs",
              title: "DrugStore"
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
          href: "/patient",
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