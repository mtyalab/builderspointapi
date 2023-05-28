import { NgModule } from '@angular/core';
import {RouterModule, Routes} from "@angular/router";
import {DashboardComponent} from "./dashboard/dashboard.component";
import {MaterialComponent} from "./material/material.component";
import {OrderComponent} from "./order/order.component";
import {PurchaseComponent} from "./purchase/purchase.component";
import {TruckComponent} from "./truck/truck.component";
import {RatingComponent} from "./rating/rating.component";
import {UserComponent} from "./user/user.component";
import {LoginComponent} from "./login/login.component";


const routes: Routes = [
  {path: '', component: LoginComponent},
  {path: 'dashboard', component: DashboardComponent},
      {path: 'material', component: MaterialComponent},
      {path: 'order', component: OrderComponent},
      {path: 'purchase', component: PurchaseComponent},
      {path: 'truck', component: TruckComponent},
      {path: 'rating', component: RatingComponent},
      {path: 'user', component: UserComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
