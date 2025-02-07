// 该组件当用户登录后显示用户信息和退出链接，
// 用户未登录时显示登录表单
import {Component} from '@angular/core';

/*
 * Services
 */
import {AuthService} from 'services/AuthService';

@Component({
  selector: 'login',
  template: `
  <div class="alert alert-danger" role="alert" *ngIf="message">
    {{ message }}
  </div>

  <!-- 在用户未登录时显示 -->
  <form class="form-inline" *ngIf="!authService.getUser()">
    <div class="form-group">
      <label for="username">User:</label>
      <input class="form-control" name="username" #username>
    </div>

    <div class="form-group">
      <label for="password">Password:</label>
      <input class="form-control" type="password" name="password" #password>
    </div>

    <a class="btn btn-default" (click)="login(username.value, password.value)">
      Submit
    </a>
  </form>

  <!-- 在用户登录后显示 -->
  <div class="well" *ngIf="authService.getUser()">
    Logged in as <b>{{ authService.getUser() }}</b>
    <a href (click)="logout()">Log out</a>
  </div>
  `
})
export class LoginComponent {
  message: string;

  constructor(private authService: AuthService) {
    this.message = '';
  }

  login(username: string, password: string): boolean {
    this.message = '';
    if (!this.authService.login(username, password)) {
      this.message = 'Incorrect credentials.';
      setTimeout(function() {
        this.message = '';
      }.bind(this), 2500);
    }
    return false;
  }

  logout(): boolean {
    this.authService.logout();
    return false;
  }
}
