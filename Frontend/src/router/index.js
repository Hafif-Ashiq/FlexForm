import { createRouter, createWebHistory } from "vue-router";
import Dashboard from "@/views/Dashboard.vue";
import Tables from "@/views/Tables.vue";
import CreateForm from "@/views/CreateForm.vue";
import ResponseTable from "@/views/ResponseTable.vue";
// import Billing from "@/views/Billing.vue";
import VirtualReality from "@/views/VirtualReality.vue";
import Profile from "@/views/Profile.vue";
// import Rtl from "@/views/Rtl.vue";
import SignIn from "@/views/SignIn.vue";
import SignUp from "@/views/SignUp.vue";
import BarCodeScanner from "@/views/BarCodeScanner.vue"



// import auth from '../middleware/auth.js';
// import log from '../middleware/log.js';


const routes = [
  {
    path: "/sign-in",
    name: "Sign In",
    component: SignIn,

  },
  {
    path: "/barcode-scanner",
    name: "Barcode Scanner",
    component: BarCodeScanner,

  },
  {
    path: "/sign-up",
    name: "Sign Up",
    component: SignUp,

  },
  {
    path: "/form/:id",
    name: "Form",
    component: VirtualReality,
    props: true,
  },
  {
    path: "/",
    name: "/",
    redirect: "/dashboard",
    beforeEnter : (to, from, next) => {

      
        if(!localStorage.getItem('token')){
          return next({name: 'Sign In'})
        }
      
    
      return next();
    } 

  },
  {
    path: "/dashboard",
    name: "Dashboard",
    component: Dashboard,
    beforeEnter : (to, from, next) => {
     
        if(!localStorage.getItem('token')){
          return next({name: 'Sign In'})
        }
      
    
      return next();
    } 

  },
  {
    path: "/workspace",
    name: "WorkSpace",
    component: Tables,
    beforeEnter : (to, from, next) => {
  
        if(!localStorage.getItem('token')){
          return next({name: 'Sign In'})
        }
      
    
      return next();
    } 

  },
  {
    path: "/workspace/create-form/:id",
    name: "Create Form",
    props: true,
    component: CreateForm,
    beforeEnter : (to, from, next) => {
  
        if(!localStorage.getItem('token')){
          return next({name: 'Sign In'})
        }
      
    
      return next();
    } 

  },
  {
    path: "/workspace/form-responses/:id",
    name: "Form Response",
    props: true,
    component: ResponseTable,
    beforeEnter : (to, from, next) => {
  
        if(!localStorage.getItem('token')){
          return next({name: 'Sign In'})
        }
      
    
      return next();
    } 

  },
  
  {
    path: "/profile",
    name: "Profile",
    component: Profile,
    beforeEnter : (to, from, next) => {

      
        if(!localStorage.getItem('token')){
          return next({name: 'Sign In'})
        }
      
    
      return next();
    } 

  },
  
  
  
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
  linkActiveClass: "active",
});



  

  
   

export default router;
