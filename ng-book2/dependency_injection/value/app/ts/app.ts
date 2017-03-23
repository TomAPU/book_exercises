/*
 * Angular
 */
import {
  Component
} from '@angular/core';
import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { platformBrowserDynamic } from '@angular/platform-browser-dynamic';

/*
 * Services
 */
import {ApiService, API_URL} from 'services/ApiService';

/*
 * Webpack
 */
require('css/styles.css');

@Component({
  selector: 'di-value-app',
  template: `
  <button (click)="invokeApi()">Invoke API</button>
  `
})
class DiValueApp {
  constructor(private apiService: ApiService) {
  }

  invokeApi(): void {
    this.apiService.get();
  }
}

// 可以通过 WebPack 或 .env 文件来定义这些环境变量值
const isProduction: boolean = true;

@NgModule({
  declarations: [ DiValueApp ],
  imports: [ BrowserModule ],
  bootstrap: [ DiValueApp ],
  providers: [
    { provide: ApiService, useClass: ApiService },

    // 根据环境变量设置不同的值
    {
      provide: API_URL,
      useValue: isProduction ?
        'https://production-api.sample.com' :
        'http://dev-api.sample.com'
    }
  ]
})
class DiValueAppAppModule {}

platformBrowserDynamic().bootstrapModule(DiValueAppAppModule)
  .catch((err: any) => console.error(err));
