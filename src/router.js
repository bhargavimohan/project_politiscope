import SignUp from './components/SignUp.vue'
import HomePage from './components/HomePage.vue'
import LogIn from './components/LogIn.vue'
import {createRouter, createWebHistory} from 'vue-router' 

const routes=[
    {
        name: 'HomePage',
        component : HomePage,
        path : '/'

    },
    { 
        name: 'SignUp',
        component: SignUp,
        path: '/signup'

    },
    { 
        name: 'LogIn',
        component: LogIn,
        path: '/login'

    }
];

const router= createRouter({
    history:createWebHistory(),
    routes
});

export default router;