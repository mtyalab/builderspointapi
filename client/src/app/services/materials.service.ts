import { Injectable } from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {Observable} from "rxjs";
import {environment} from "../../environments/environment";

const baseUrl = `${environment.serverUrl}/material`;
@Injectable({
  providedIn: 'root'
})
export class MaterialsService {



  constructor(private http: HttpClient) {
  }


  getMaterials(): Observable<any>{
    return this.http.get(`${baseUrl}/all`);
  }
}
