import { OnInit } from '@angular/core';
import { Component } from '@angular/core';
import { LayoutService } from './service/app.layout.service';

@Component({
    selector: 'app-menu',
    templateUrl: './app.menu.component.html'
})
export class AppMenuComponent implements OnInit {

    model: any[] = [];

    constructor(public layoutService: LayoutService) { }

    ngOnInit() {
        this.model = [
            {
                items: [
                    { label: 'Dashboard', icon: 'pi pi-fw pi-home', routerLink: ['/dashboard'] },
                     { label: 'Materials', icon: 'pi pi-fw pi-circle', routerLink: ['/material'] },
                     { label: 'Orders', icon: 'pi pi-fw pi-shopping-cart', routerLink: ['/order'] },
                     { label: 'Purchases', icon: 'pi pi-fw pi-money-bill', routerLink: ['/purchase'] },
                     { label: 'Trucks', icon: 'pi pi-fw pi-truck', routerLink: ['/truck'] },
                     { label: 'Ratings', icon: 'pi pi-fw pi-star', routerLink: ['/rating'] },
                     { label: 'Users', icon: 'pi pi-fw pi-user', routerLink: ['/user'] }
                ]
            },
        ];
    }
}
