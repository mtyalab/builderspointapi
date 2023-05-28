import {Component, OnInit} from '@angular/core';
import {MenuItem} from "primeng/api";
import {LayoutService} from "../layout/service/app.layout.service";
import {MaterialsService} from "../services/materials.service";
import {Material} from "../domain/material";
import {environment} from "../../environments/environment";

@Component({
  selector: 'app-material',
  templateUrl: './material.component.html',
  styleUrls: ['./material.component.css']
})
export class MaterialComponent implements  OnInit {

  items!: MenuItem[];
  materials!: Material[];
   dropdownItems: MenuItem[] = [];

  constructor(public layoutService: LayoutService, private materialService: MaterialsService) {

  }

  ngOnInit(): void {
        this.getAllMaterials();
          this.dropdownItems = [
            { label: 'Update', icon: 'pi pi-refresh' , url: ''},
            { label: 'Delete', icon: 'pi pi-times', url: '' },
            { separator: true },
        ];
    }

  getAllMaterials() {
    this.materialService.getMaterials().subscribe((response) => {
       this.materials = response['data'];
       console.log(this.materials);
    }, err => console.log(err));
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

   apiUrl = environment;

}
