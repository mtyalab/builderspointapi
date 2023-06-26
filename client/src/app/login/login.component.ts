import {Component, OnInit} from '@angular/core';
import { Router } from '@angular/router';
import {FormBuilder, FormGroup, Validators} from "@angular/forms";
import {UsersService} from "../services/users.service";

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {
    loginForm: FormGroup;
    constructor(private router: Router,
                private fb: FormBuilder,
                  private userService: UsersService) {
    }

    ngOnInit() {
        this.loginForm = this.fb.group({
            email: ['', Validators.required],
            password: ['', Validators.required]
        });
    }

    onSubmit(): void {
        this.userService.login(
            this.loginForm.value['email'],
            this.loginForm.value['password'])
            .subscribe((data) => {
                if (data['role'] === 'CLIENT') {
                    alert('Unauthorized access');
                  return;
                } else {
                    if(data['status_code'] === 400) {
                        alert(data['detail']);
                    } else {
                       this.router.navigate(['/dashboard']);
                    }
                }
              }, err => {
                alert(err.message);
            });
    }
}
