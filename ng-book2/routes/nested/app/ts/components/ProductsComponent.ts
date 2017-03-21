/*
 * Angular
 */
import {
  NgModule,
  Component
} from '@angular/core';
import {
  RouterModule,
  ActivatedRoute,
  Router,
  Routes
} from '@angular/router';

/*
 * Components
 */
import {MainComponent} from 'components/products/MainComponent';
import {InterestComponent} from 'components/products/InterestComponent';
import {SportifyComponent} from 'components/products/SportifyComponent';
import {ByIdComponent} from 'components/products/ByIdComponent';

@Component({
  selector: 'products',

  // 模板中的本地路由用 `./` 作为前缀，例如 ['./main']，
  // 从而表明这些路由是相对于父路由路径的。
  // 我们也可以写成 ['products', 'main']，明确写出父路由，
  // 但是这样写后，子路由就需要了解父路由，当父路由修改
  // 名字后，子路由中也需要跟着修改。
  template: `
  <h2>Products</h2>

  <div class="navLinks">
    <a [routerLink]="['./main']">Main</a> |
    <a [routerLink]="['./interest']">Interest</a> |
    <a [routerLink]="['./sportify']">Sportify</a> |
    Enter id: <input #id size="6">
    <button (click)="goToProduct(id.value)">Go</button>
  </div>

  <!-- 这里的 router-outlet 是为子路由使用的 -->
  <div class="products-area">
    <router-outlet></router-outlet>
  </div>
  `
})

export class ProductsComponent {
  constructor(private router: Router, private route: ActivatedRoute) {
  }

  goToProduct(id:string): void {
    // 这里使用了相对路由
    this.router.navigate(['./', id], {relativeTo: this.route});
  }
}

// 本组件定义了自己的路由
export const routes: Routes = [
  // 当访问 /products 时，会重定向到 /products/main
  { path: '', redirectTo: 'main', pathMatch: 'full' },

  { path: 'main', component: MainComponent },

  // URL 中在 `/products/` 后的数据都会抽取后保存在路由的 id 参数中
  // 如果 id 值与本路由配置中明确定义的 id 值都不同，即
  // 不等于 main, interest, sportify 后，才会激活本条路由
  { path: ':id', component: ByIdComponent },

  { path: 'interest', component: InterestComponent },
  { path: 'sportify', component: SportifyComponent },
];

@NgModule({
  declarations: [
    ProductsComponent,
    MainComponent,
    InterestComponent,
    SportifyComponent,
    ByIdComponent
  ],
  exports: [
    ProductsComponent,
    MainComponent,
    InterestComponent,
    SportifyComponent,
    ByIdComponent
  ],
  imports: [ RouterModule ]
})
export class ProductsComponentModule {}

