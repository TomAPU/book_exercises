import { Injectable } from '@angular/core';
import { CanActivate } from '@angular/router';
import { AuthService } from 'services/AuthService';

@Injectable()
export class LoggedInGuard implements CanActivate { // 实现 CanActivate 接口
  // 构造器中 AuthService 注入
  constructor(private authService: AuthService) {}

  // 由于路由的 `canActive` 挂钩配置为了该类，
  // 那么当路由被激活时会调用 canActivate 方法
  canActivate(): boolean {
    return this.authService.isLoggedIn();
  }
}
