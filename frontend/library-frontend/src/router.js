import { createRouter, createWebHistory } from 'vue-router'

import Home from './views/Home.vue'
import Books from './views/Books.vue'
import Members from './views/Members.vue'
import Transactions from './views/Transactions.vue'
import AddBooks from '@/components/AddBooks.vue'
import ImportBooks from '@/components/ImportBooks.vue'
import AddMember from './views/AddMember.vue'
import TransactionList from './components/TransactionList.vue'
import IssueTransaction from './components/IssueTransaction.vue'
import ReturnBook from './components/ReturnBook.vue'

const routes = [
  { path: '/', name: 'Home', component: Home },
  { path: '/books', name: 'Books', component: Books },
  {
    path: '/add-book',
    name: 'AddBooks',
    component: AddBooks,
  },
  {
    path: '/import-books',
    name: 'ImportBooks',
    component: ImportBooks,
  },
  { path: '/add-member', name: 'AddMember', component: AddMember },
  { path: '/members', name: 'Members', component: Members },
  { path: '/transactions', name: 'Transactions', component: TransactionList },
  { path: '/transactions/issue', name: 'IssueTransaction', component: IssueTransaction },
  { path: '/transactions/return', name: 'ReturnBook', component: ReturnBook },
  {
    path: '/edit-book/:id',
    name: 'EditBook',
    component: () => import('./views/EditBook.vue'),
  },
  {
    path: '/edit-member/:id',
    name: 'EditMember',
    component: () => import('./views/EditMember.vue'),
  },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router
