import { Injectable } from '@angular/core';
import {environment} from "../../environments/environment";
import {Observable} from "rxjs";
import {HttpClient} from "@angular/common/http";

@Injectable({
  providedIn: 'root'
})
export class OrdersService {
  baseUrl = `${environment.serverUrl}`;
  constructor(private http: HttpClient) { }

  getOrders():Observable<any> {
    return this.http.get<any>(this.baseUrl + '/purchase/all');
  }
}
