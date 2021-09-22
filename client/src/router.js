import Vue from 'vue';
import Router from 'vue-router';
import Product from './views/Product.vue';
import Service from './views/Service.vue';
import Ticket from './views/Ticket.vue';
import Login from './views/auth/Login.vue';
import Signup from './views/auth/Signup.vue';
import AddProduct from './components/Products/AddProduct';
import AddService from './components/Services/AddService';
import AddTicket from './components/Tickets/AddTicket';
import Cart from './views/Cart';
import AllServices from './components/Services/Content/AllServices';
import OpenServices from './components/Services/Content/OpenServices';
import ClosedServices from './components/Services/Content/ClosedServices';
import CreateService from './components/Services/Content/CreateService';
import Dashboard from './components/Services/Content/Dashboard';
import MyServices from './components/Services/Content/MyServices';
import OverdueServices from './components/Services/Content/OverdueServices';
import AllTickets from './components/Tickets/Content/AllTickets';
import OpenTickets from './components/Tickets/Content/OpenTickets';
import ClosedTickets from './components/Tickets/Content/ClosedTickets';
import CreateTicket from './components/Tickets/Content/CreateTicket';
import TDashboard from './components/Tickets/Content/Dashboard';
import MyTickets from './components/Tickets/Content/MyTickets';
import OverdueTickets from './components/Tickets/Content/OverdueTickets';
import ServiceDetails from './components/Services/Content/ServiceDetails';
import TicketDetails from './components/Tickets/Content/TicketDetails';
import Admin from './views/Admin';
import Doctor from './views/Doctor';
import Patient from './views/Patient';
import AdminDashboard from './components/AdminPanel/Dashboard';
import ProductManagement from './components/AdminPanel/ProductManagement';
import ServiceManagement from './components/AdminPanel/ServiceManagement';
import TicketManagement from './components/AdminPanel/TicketManagement';
import UserManagement from './components/AdminPanel/UserManagement';
import AddUser from './views/AddUser';
/*
- Manage Departments
- Manage Doctors
- Manage Patients
- Manage Pharmacies
*/
import PatientDashboard from './components/PatientPanel/Dashboard';
import PatientDepartmentManagement from './components/PatientPanel/DepartmentManagement';
import PatientAppointmentsManagement from './components/PatientPanel/AppointmentsManagement';
import PatientRecipeManagement from './components/PatientPanel/RecipeManagement';
import PatientDoctorsManagement from './components/PatientPanel/DoctorsManagement';
// import PatientDrugsManagement from './components/PatientPanel/DrugsManagement';
import PatientDepartmentManagementDetails from './components/PatientPanel/Details/DepartmentManagementDetails';
import PatientAppointmentsManagementDetails from './components/PatientPanel/Details/AppointmentsManagementDetails';
import PatientRecipeManagementDetails from './components/PatientPanel/Details/RecipeManagementDetails';
import PatientsDoctorsManagementDetails from './components/PatientPanel/Details/DoctorsManagementDetails';
// import PatientDrugsManagementDetails from './components/PatientPanel/DrugsManagementDetails';
import DoctorDashboard from './components/DoctorPanel/Dashboard';
import DepartmentManagement from './components/DoctorPanel/DepartmentManagement';
import AppointmentsManagement from './components/DoctorPanel/AppointmentsManagement';
import RecipeManagement from './components/DoctorPanel/RecipeManagement';
import PatientsManagement from './components/DoctorPanel/PatientsManagement';
import DepartmentManagementDetails from './components/DoctorPanel/Details/DepartmentManagementDetails';
import AppointmentsManagementDetails from './components/DoctorPanel/Details/AppointmentsManagementDetails';
import RecipeManagementDetails from './components/DoctorPanel/Details/RecipeManagementDetails';
import PatientsManagementDetails from './components/DoctorPanel/Details/PatientsManagementDetails';
import ServiceManagementDetails from './components/AdminPanel/Details/ServiceManagementDetails';
import ProductManagementDetails from './components/AdminPanel/Details/ProductManagementDetails';
import TicketManagementDetails from './components/AdminPanel/Details/TicketMangementDetails';
import UserManagementDetails from './components/AdminPanel/Details/UserManagementDetails';

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/',
      name: 'product',
      component: Product,
    },
    {
      path: '/add-product',
      name: 'add-product',
      component: AddProduct,
    },
    {
      path: '/login',
      name: 'login',
      component: Login,
    },
    {
      path: '/signup',
      name: 'signup',
      component: Signup,
    },
    {
      path: '/services',
      name: 'services',
      component: Service,
    },
    {
      path: '/add-service',
      name: 'add-service',
      component: AddService,
    },
    {
      path: '/tickets',
      name: 'tickets',
      component: Ticket,
    },
    {
      path: '/add-ticket',
      name: 'add-ticket',
      component: AddTicket,
    },
    {
      path: '/cart/:userId',
      name: 'cart',
      component: Cart,
      props: true,
    },
    {
      path: '/services/all-services',
      name: 'all-services',
      component: AllServices,
    },
    {
      path: '/services/open-services',
      name: 'open-services',
      component: OpenServices,
    },
    {
      path: '/services/closed-services',
      name: 'closed-services',
      component: ClosedServices,
    },
    {
      path: '/services/create-services',
      name: 'create-services',
      component: CreateService,
    },
    {
      path: '/services/dashboard',
      name: 'dashboard',
      component: Dashboard,
    },
    {
      path: '/services/my-services',
      name: 'my-services',
      component: MyServices,
    },
    {
      path: '/services/overdue-services',
      name: 'overdue-services',
      component: OverdueServices,
    },
    {
      path: '/services/:prodId',
      name: 'service-details',
      component: ServiceDetails,
      props: true,
    },
    {
      path: '/tickets/all-tickets',
      name: 'all-tickets',
      component: AllTickets,
    },
    {
      path: '/tickets/open-tickets',
      name: 'open-tickets',
      component: OpenTickets,
    },
    {
      path: '/tickets/closed-tickets',
      name: 'closed-tickets',
      component: ClosedTickets,
    },
    {
      path: '/tickets/create-tickets',
      name: 'create-tickets',
      component: CreateTicket,
    },
    {
      path: '/tickets/dashboard',
      name: 'dashboard',
      component: TDashboard,
    },
    {
      path: '/tickets/my-tickets',
      name: 'my-tickets',
      component: MyTickets,
    },
    {
      path: '/tickets/overdue-tickets',
      name: 'overdue-tickets',
      component: OverdueTickets,
    },
    {
      path: '/tickets/:prodId',
      name: 'ticket-details',
      component: TicketDetails,
      props: true,
    },
    {
      path: '/admin',
      name: 'admin',
      component: Admin,
    },
    {
      path: '/admin/dashboard',
      name: 'admin-dashboard',
      component: AdminDashboard,
    },
    {
      path: '/admin/products',
      name: 'product-management',
      component: ProductManagement,
    },
    {
      path: '/admin/services',
      name: 'service-management',
      component: ServiceManagement,
    },
    {
      path: '/admin/tickets',
      name: 'ticket-management',
      component: TicketManagement,
    },
    {
      path: '/admin/users',
      name: 'user-management',
      component: UserManagement,
    },
    {
      path: '/doctor',
      name: 'doctor',
      component: Doctor,
    },
    {
      path: '/doctor/dashboard',
      name: 'doctor-dashboard',
      component: DoctorDashboard,
    },
    {
      path: '/doctor/departments',
      name: 'doctor-departments',
      component: DepartmentManagement,
    },
    {
      path: '/doctor/appointments',
      name: 'doctor-appointments',
      component: AppointmentsManagement,
    },
    {
      path: '/doctor/recipes',
      name: 'doctor-recipes',
      component: RecipeManagement,
    },
    {
      path: '/doctor/patients',
      name: 'doctor-patients',
      component: PatientsManagement,
    },
    {
      path: '/patient',
      name: 'patient',
      component: Patient,
    },
    {
      path: '/patient/dashboard',
      name: 'patient-dashboard',
      component: PatientDashboard,
    },
    {
      path: '/patient/departments',
      name: 'patient-departments',
      component: PatientDepartmentManagement,
    },
    {
      path: '/patient/appointments',
      name: 'patient-appointments',
      component: PatientAppointmentsManagement,
    },
    {
      path: '/patient/recipes',
      name: 'patient-recipes',
      component: PatientRecipeManagement,
    },
    {
      path: '/patient/doctors',
      name: 'patient-doctors',
      component: PatientDoctorsManagement,
    },
    // {
    //   path: '/patient/drugs',
    //   name: 'patient-drugs',
    //   component: PatientDrugsManagement,
    // },
    {
      path: '/add-user',
      name: 'add-user',
      component: AddUser,
    },
    {
      path: '/admin/service/:id',
      name: 'service-management-details',
      component: ServiceManagementDetails,
      props: true,
    },
    {
      path: '/admin/ticket/:id',
      name: 'ticket-management-details',
      component: TicketManagementDetails,
      props: true,
    },
    {
      path: '/admin/product/:id',
      name: 'product-management-details',
      component: ProductManagementDetails,
      props: true,
    },
    {
      path: '/admin/user/:id',
      name: 'user-management-details',
      component: UserManagementDetails,
      props: true,
    },
    {
      path: '/doctor/department/:id',
      name: 'department-management-details',
      component: DepartmentManagementDetails,
      props: true,
    },
    {
      path: '/doctor/appointments/:id',
      name: 'appointments-management-details',
      component: AppointmentsManagementDetails,
      props: true,
    },
    {
      path: '/doctor/recipe/:id',
      name: 'recipe-management-details',
      component: RecipeManagementDetails,
      props: true,
    },
    {
      path: '/doctor/patients/:id',
      name: 'patients-management-details',
      component: PatientsManagementDetails,
      props: true,
    },
    {
      path: '/patient/department/:id',
      name: 'department-management-details',
      component: PatientDepartmentManagementDetails,
      props: true,
    },
    {
      path: '/patient/appointments/:id',
      name: 'appointments-management-details',
      component: PatientAppointmentsManagementDetails,
      props: true,
    },
    {
      path: '/patient/recipe/:id',
      name: 'recipe-management-details',
      component: PatientRecipeManagementDetails,
      props: true,
    },
    {
      path: '/patient/doctors/:id',
      name: 'doctors-management-details',
      component: PatientsDoctorsManagementDetails,
      props: true,
    },
    // {
    //   path: '/patient/drugs/:id',
    //   name: 'drugs-management-details',
    //   component: PatientDrugsManagementDetails,
    //   props: true,
    // },
    {
      path: '*',
      redirect: 'product',
    },
  ],
  mode: 'history',
});
