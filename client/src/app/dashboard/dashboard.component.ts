import {Component, OnInit} from '@angular/core';
import {Product} from "../domain/product";
import {MenuItem} from "primeng/api";
import {Subscription} from "rxjs";
import {ProductService} from "../services/productservice";
import {LayoutService} from "../layout/service/app.layout.service";
import {OrdersService} from "../services/orders.service";
import {MaterialsService} from "../services/materials.service";

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})
export class DashboardComponent implements OnInit {
   items!: MenuItem[];

    subscription!: Subscription;
    ordersCount: number;
    materialsCount: number;

    constructor(public layoutService: LayoutService,
                private orderService: OrdersService,
                private materialService: MaterialsService) {

    }

    ngOnInit() {
     this.getOrdersCount();
     this.getMaterialsCount();
    }

    getOrdersCount() {
        this.orderService.getOrders().subscribe((response)=> {
            this.ordersCount = response.length;
        }, err => {
            alert(err);
        });
    }


    getMaterialsCount() {
        this.materialService.getMaterials().subscribe((response)=> {
            this.materialsCount = response['data'].length;
        }, err => {
            alert(err);
        });
    }


    ngOnDestroy() {
        if (this.subscription) {
            this.subscription.unsubscribe();
        }
    }


       get containerClass() {
        return {
            'layout-theme-light': this.layoutService.config.colorScheme === 'light',
            'layout-theme-dark': this.layoutService.config.colorScheme === 'dark',
            'layout-overlay': this.layoutService.config.menuMode === 'overlay',
            'layout-static': this.layoutService.config.menuMode === 'static',
            'layout-static-inactive': this.layoutService.state.staticMenuDesktopInactive && this.layoutService.config.menuMode === 'static',
            'layout-overlay-active': this.layoutService.state.overlayMenuActive,
            'layout-mobile-active': this.layoutService.state.staticMenuMobileActive,
            'p-input-filled': this.layoutService.config.inputStyle === 'filled',
            'p-ripple-disabled': !this.layoutService.config.ripple
        }
    }

}
