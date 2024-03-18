
import SignUp from './components/SignUp.vue'
import HomePage from './components/HomePage.vue'
import LogIn from './components/LogIn.vue'
import PolitiScope from './components/PolitiScope.vue'
import AboutPage from './components/AboutPage.vue'
import InfoCenter from './components/InfoCenter.vue'
import MyAccount from './components/MyAccount.vue'
import LogOut from './components/LogOut.vue'
import {createRouter, createWebHistory} from 'vue-router' 


const routes=[
    {
        name: 'HomePage',
        component : HomePage,
        path : '/home',
        alias: ['/']  

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

    },
    { 
        name: 'PolitiScope',
        component: PolitiScope,
        path: '/politiscope'

    },
    { 
        name: 'AboutPage',
        component: AboutPage,
        path: '/about'

    },
    { 
        name: 'InfoCenter',
        component: InfoCenter,
        path: '/infocenter'

    },
    { 
        name: 'MyAccount',
        component: MyAccount,
        path: '/myaccount'

    },
    { 
        name: 'LogOut',
        component: LogOut,
        path: '/logout'

    }
    

];


const router= createRouter({
    history:createWebHistory(),
    routes
});

export default router;