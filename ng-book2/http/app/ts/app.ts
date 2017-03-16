/*
 * Angular
 */
import {
  Component
} from '@angular/core';
import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { platformBrowserDynamic } from '@angular/platform-browser-dynamic';
// 导入 HTTP 模块
import { HttpModule } from '@angular/http';

/*
 * Components
 */
import { SimpleHTTPComponent } from 'components/SimpleHTTPComponent';
import { MoreHTTPRequests } from 'components/MoreHTTPRequests';
import {
  YouTubeSearchComponent,
  SearchBox,
  SearchResultComponent
} from 'components/YouTubeSearchComponent';

/*
 * Injectables
 */
// 先导入可注入的定义体
import { youTubeServiceInjectables } from 'components/YouTubeSearchComponent';

/*
 * Webpack
 */
require('css/styles.css');

@Component({
  selector: 'http-app',
  template: `
  <div class="container">
    <simple-http></simple-http>
    <hr/>
    <more-http></more-http>
    <hr/>
    <youtube-search></youtube-search>
  </div>
  `
})
class HttpApp {
}

@NgModule({
  declarations: [
    HttpApp,
    SimpleHTTPComponent,
    MoreHTTPRequests,
    YouTubeSearchComponent,
    SearchBox,
    SearchResultComponent
  ],
  // 将 HTTP 模块放入应用的依赖中，
  // 它能将 Http(及其它一些模块）注入(inject) 我们的组件中
  // 在组件定义中，将 Http 服务这样注入使用：
  //  class MyFooComponent {
  //     constructor(public http: Http){
  //        // 无需定义和赋值，就自动为组件创建了一个 this.http
  //     }
  // 
  //     makeRequest(): void {
  //        // do something with this.http ...
  //     }
  //  }
  imports: [
    BrowserModule,
    HttpModule // <--- right here
  ],
  bootstrap: [ HttpApp ],
  providers: [ // 设置 youTubeServiceInjectables 中的变量注入到全局应用时，即可在应用的所有组件定义中使用
    youTubeServiceInjectables
  ]
})
class HttpAppModule {}

platformBrowserDynamic().bootstrapModule(HttpAppModule)
  .catch((err: any) => console.error(err));
