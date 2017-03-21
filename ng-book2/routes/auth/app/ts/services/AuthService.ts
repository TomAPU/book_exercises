//创建登录认证服务
import { Injectable } from '@angular/core';

@Injectable()
export class AuthService {
  login(user: string, password: string): boolean {
    if (user === 'user' && password === 'password') {
      // 成功登录后，将 username 保存到 `localStorage` 
      // localStorage 是 HTML5 提供的键/值对，它能用来
      // 将持久数据保存到浏览器中。
      // API：https://developer.mozilla.org/en-US/docs/Web/API/Storage
      localStorage.setItem('username', user);
      return true;
    }

    return false;
  }

  logout(): any {
    localStorage.removeItem('username');
  }

  getUser(): any {
    return localStorage.getItem('username');
  }

  isLoggedIn(): boolean {
    return this.getUser() !== null;
  }
}

export var AUTH_PROVIDERS: Array<any> = [
  { provide: AuthService, useClass: AuthService }
];
