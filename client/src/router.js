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
import AdminDashboard from './components/AdminPanel/Dashboard';
import ProductManagement from './components/AdminPanel/ProductManagement';
import ServiceManagement from './components/AdminPanel/ServiceManagement';
import TicketManagement from './components/AdminPanel/TicketManagement';
import UserManagement from './components/AdminPanel/UserManagement';
import AddUser from './views/AddUser';
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
      path: '*',
      redirect: 'product',
    },
  ],
  mode: 'history',
});
