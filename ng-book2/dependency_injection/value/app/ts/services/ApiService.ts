import { Inject } from '@angular/core';

// 定义一个常量，将用作 API URL 注入依赖的标识 (token)，
// 即 Angular 将用字符串 'API_URL' 来存储 URL 的信息。
export const API_URL: string = 'API_URL';

export class ApiService {
  // NgModule 中定义的注入依赖 API_URL 的值将注入这里
  constructor(@Inject(API_URL) private apiUrl: string) {
  }

  get(): void {
    console.log(`Calling ${this.apiUrl}/endpoint...`);
  }
}
