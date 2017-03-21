/*
 * Angular Imports
 */
import {
  NgModule,
  Component
} from '@angular/core';
import {BrowserModule} from '@angular/platform-browser';
import {platformBrowserDynamic} from '@angular/platform-browser-dynamic';
import { // 加载路由的相关模块
  RouterModule,
  Routes
} from '@angular/router';
import {LocationStrategy, HashLocationStrategy} from '@angular/common';

/*
 * Components
 */
import {HomeComponent} from 'components/HomeComponent';
import {AboutComponent} from 'components/AboutComponent';
import {ContactComponent} from 'components/ContactComponent';

/*
 * Webpack
 */
require('css/styles.css');

// 在模板中使用 router-outlet 元素定义路由内容的放置位置，
// 即路由链接的内容都会呈现在这个元素内
//
// 使用 <a href="/#/home">Home</a> 也可以定义链接，但是这样的话，
// 当点击链接时，页面会重加载，不适合在 SPA 中使用
// Angular2 中使用 [routerLink] 指令来建立路由链接，这样创建的
// 链接点击时页面不会重加载。
// [routerLink] 指令右侧的表达式是一个数据，其中第一个元素指的是
// 对应的路由路径，其它的元素可以是子元素，路由参数等。
@Component({
  selector: 'router-app',
  template: `
  <div>
    <nav>
      <a>Navigation:</a>
      <ul>
        <li><a [routerLink]="['home']">Home</a></li>
        <li><a [routerLink]="['about']">About</a></li>
        <li><a [routerLink]="['contact']">Contact Us</a></li>
      </ul>
    </nav>

    <router-outlet></router-outlet>
  </div>
  `
})
class RoutesDemoApp {
}

// 定义应用的路由：
// + path: 指定该路由要处理的 URL
// + component: 关联该路由的处理组件
// + redirectTo(可选): 用于将某个路径重定向到现存的路由
const routes: Routes = [
  { path: '', redirectTo: 'home', pathMatch: 'full' },
  { path: 'home', component: HomeComponent },
  { path: 'about', component: AboutComponent },
  { path: 'contact', component: ContactComponent },
  { path: 'contactus', redirectTo: 'contact' },
];

// 在应用的 @NgModule 中的 imports 区域，通过 RouterModule.forRoot 来安装路由
@NgModule({
  declarations: [
    RoutesDemoApp,
    HomeComponent,
    AboutComponent,
    ContactComponent
  ],
  imports: [
    BrowserModule,
    RouterModule.forRoot(routes) // <-- 通过这里安装路由
  ],
  bootstrap: [ RoutesDemoApp ],
  providers: [
    { provide: LocationStrategy, useClass: HashLocationStrategy }
  ]
})
class RoutesDemoAppModule {}

platformBrowserDynamic().bootstrapModule(RoutesDemoAppModule)
  .catch((err: any) => console.error(err));
