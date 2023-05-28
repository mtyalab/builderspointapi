import { BrowserModule } from '@angular/platform-browser';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';
import { InputTextModule } from 'primeng/inputtext';
import { InputTextareaModule } from 'primeng/inputtextarea';
import { InputNumberModule } from 'primeng/inputnumber';
import { ButtonModule } from 'primeng/button';
import { TableModule } from 'primeng/table';
import { DialogModule } from 'primeng/dialog';
import { ConfirmDialogModule } from 'primeng/confirmdialog';
import { DropdownModule } from 'primeng/dropdown';
import { RadioButtonModule } from 'primeng/radiobutton';
import { RatingModule } from 'primeng/rating';
import { ToolbarModule } from 'primeng/toolbar';
import { ConfirmationService } from 'primeng/api';

import { AppComponent } from './app.component';
import { DemoComponent } from './demo/demo.component';
import { LoginComponent } from './login/login.component';
import {CheckboxModule} from "primeng/checkbox";
import {RippleModule} from "primeng/ripple";
import {RouterOutlet} from "@angular/router";
import {StyleClassModule} from "primeng/styleclass";
import { DashboardComponent } from './dashboard/dashboard.component';
import { MaterialComponent } from './material/material.component';
import { OrderComponent } from './order/order.component';
import { PurchaseComponent } from './purchase/purchase.component';
import { RatingComponent } from './rating/rating.component';
import { TruckComponent } from './truck/truck.component';
import { UserComponent } from './user/user.component';
import {AppRoutingModule} from "./app-routing.module";
import {MenuModule} from "primeng/menu";
import {ChartModule} from "primeng/chart";
import {AppLayoutModule} from "./layout/app.layout.module";
import {AppConfigModule} from "./layout/config/config.module";
import {ToggleButtonModule} from "primeng/togglebutton";
import {SplitButtonModule} from "primeng/splitbutton";


@NgModule({
    declarations: [
        AppComponent,
        DemoComponent,
        LoginComponent,
        DashboardComponent,
        MaterialComponent,
        OrderComponent,
        PurchaseComponent,
        RatingComponent,
        TruckComponent,
        UserComponent,
    ],
    imports: [
        BrowserModule,
        BrowserAnimationsModule,
        FormsModule,
        TableModule,
        HttpClientModule,
        InputTextModule,
        DialogModule,
        ToolbarModule,
        ConfirmDialogModule,
        RatingModule,
        InputNumberModule,
        InputTextareaModule,
        RadioButtonModule,
        DropdownModule,
        ButtonModule,
        CheckboxModule,
        RippleModule,
        RouterOutlet,
        StyleClassModule,
        AppRoutingModule,
        MenuModule,
        ChartModule,
        AppLayoutModule,
        AppConfigModule,
        ToggleButtonModule,
        SplitButtonModule
    ],
    providers: [ConfirmationService],
    bootstrap: [AppComponent]
})
export class AppModule { }
