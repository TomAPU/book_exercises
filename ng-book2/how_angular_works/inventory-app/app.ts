/**
 *  Copyright (c) 2015, Fullstack.io
 *  All rights reserved.
 *
 * This source code is licensed under the license found in the
 * LICENSE file in the root directory of this source tree.
 */

import {
  Component,
  EventEmitter
} from '@angular/core';

import { NgModule } from "@angular/core";
import { BrowserModule } from "@angular/platform-browser";
import { platformBrowserDynamic } from "@angular/platform-browser-dynamic";

/**
 * 用一个简单类来提供 `Product` 对象，该类与 Angular 没有任何关联
 */
class Product {
  constructor(
    public sku: string,
    public name: string,
    public imageUrl: string,
    public department: string[],
    public price: number) {
  }
}

/**
 * @ProductImage: 显示单个产品图片的组件
 */
@Component({
  selector: 'product-image',
  host: {class: 'ui small image'},
  inputs: ['product'],

  // 这里 img 的 src 是通过 [src] 来设置的！
  // 如果像 <img src="{{ product.imageUrl }}"> 写是错误的，
  // 这是因为有时浏览器会在 Angular 运行前加载了模板，而
  // 那时图片的 URL 是 "{{ product.imageUrl }}"，从而出现
  // 404 错误。
  // 故一定要用 [src] 属性来设置，让 Angular 来替换相应的值
  template: `
  <img class="product-image" [src]="product.imageUrl">
  `
})
class ProductImage {
  product: Product;
}

/**
 * @ProductDepartment: 显示产品部门信息的组件
 * Product's department
 */
@Component({
  selector: 'product-department',
  inputs: ['product'],

  // 这里的 ngFor 指令中，通过 `let i=index;` 将每次的遍历索引赋给了 i
  template: `
  <div class="product-department">
    <span *ngFor="let name of product.department; let i=index">
      <a href="#">{{ name }}</a>
      <span>{{i < (product.department.length-1) ? '>' : ''}}</span>
    </span>
  </div>
  `
})
class ProductDepartment {
  product: Product;
}

/**
 * @PriceDisplay: 显示产品单价的组件
 */
@Component({
  selector: 'price-display',
  inputs: ['price'],

  // 这里对 $ 进行转义，从而避免了对变量的解析扩展
  template: `
  <div class="price-display">\${{ price }}</div>
  `
})
class PriceDisplay {
  price: number;
}

/**
 * @ProductRow: 显示单个产品的组件
 */
@Component({
  selector: 'product-row',
  inputs: ['product'],

  // 为组件的匹配标签添加 "item" 类
  host: {'class': 'item'},

  // 模板中可见，该组件调用了 3 个子组件
  template: `
  <product-image [product]="product"></product-image>
  <div class="content">
    <div class="header">{{ product.name }}</div>
    <div class="meta">
      <div class="product-sku">SKU #{{ product.sku }}</div>
    </div>
    <div class="description">
      <product-department [product]="product"></product-department>
    </div>
  </div>
  <price-display [price]="product.price"></price-display>
  `
})
class ProductRow {
  // 该属性设置为了输入项，因此能通过外部组件传入，故这里不
  // 需要一个构造器
  product: Product;
}

/**
 * @ProductsList: 该组件显示所有的产品列
 * 并存储当前选中的产品
 */
@Component({
  selector: 'products-list',

  // inputs 用来定义该组件的输入绑定，这里的每个参数都要对应本组件类中的一个实例变量。
  // 当 inputs 中的参数是普通的字符串名时，例如 `inputs: ['productList']`，则 productList 直接映射到实例变量 productList。
  // 定义输入绑定也可以通过 @Input() 实现，即直接在组件类中的属性定义中添加 @Input annotation，比如：
  //     class ProductsList {
  //        @Input() productList: Product[];
  // 输入项也可以实现名字的更改，即将组件属性名转成不同的导出属性名供外部使用，
  // inputs 中的参数的一般格式为 'componentProperty: exposedProperty'，因此，
  // 如果用 `inputs: ['productList: products']`，则外部就能通过 [products]="..." 来传入数据了。
  // 这种映射，如果用 @Input() 实现，则为：
  //     class ProductsList {
  //        @Input('products') productList: Product[];
  inputs: ['productList'],


  // 定义组件的公开事件，外部组件可对其进行侦听
  // 在外部组件的模板中，可用 (outputevent)="action" 的语法来绑定。
  // 内置的事件有 click, dbl-click, mousedown 等，而创建自定义事件需要做 3 件事：
  //   1. 在 @Component 的 outputs 中指定事件名，如 'onProductSelected'
  //   2. 事件名 'onProductSelected' 对应组件类中的一个属性 onProductSelected，
  //      该属性需要设置为 EventEmitter 类型，如本例中为 
  //      `onProductSelected: EventEmitter<Product>;`，表示产生该事件时，同时抛出一个
  //      Product 对象。并对其初始化，本例中是在构造器中进行初始化。
  //   3. 在适当的时候，通过 EventEmitter.emit 发送事件，如本例中：
  //       `this.onProductSelected.emit(product);`
  //
  // EventEmitter 对象有助于我们实现观察者模式，即它能维护一组注册者，并向他们发送事件。
  // 使用示例如下：
  //   let ee = new EventEmitter();
  //   ee.subscribe((name: string) => console.log(`Hello ${name}`));
  //   ee.emit('Nate');  // -> "Hello Nate"
  //
  // 当将 EventEmitter 赋给 outputs 后，Angular 会自动处理注册的流程
  outputs: ['onProductSelected'],

  // 使用 ngFor 指令来遍历调用 ProductRow 组件来显示每个产品信息
  //
  // [class.selected]="isSelected(myProduct)"> 的作用是根据条件为当前标签设置 "selected" 类，当函数 isSelected(myProduct) 值为 true 时设置，当值为 false 时不设置。
  template: `
  <div class="ui items">
    <product-row 
      *ngFor="let myProduct of productList" 
      [product]="myProduct" 
      (click)='clicked(myProduct)'
      [class.selected]="isSelected(myProduct)">
    </product-row>
  </div>
  `
})
class ProductsList {
  /**
   * @input productList - the Product[] passed to us
   * 外部传入该产品数组
   */
  productList: Product[];

  /**
   * @output onProductSelected - 
   *         当选中一个产品时，会触发该事件
   */
  onProductSelected: EventEmitter<Product>;

  /**
   * @property currentProduct - 保存当前选中的产品的一个本地状态。
   * 也称为 local component state
   */
  private currentProduct: Product;

  constructor() {
    this.onProductSelected = new EventEmitter();
  }

  clicked(product: Product): void {
    this.currentProduct = product;
    this.onProductSelected.emit(product);
  }

  isSelected(product: Product): boolean {
    if (!product || !this.currentProduct) {
      return false;
    }
    return product.sku === this.currentProduct.sku;
  }

}

/**
 * @InventoryApp: 这是应用的最顶层组件
 */
// @Component 就是注解 annotation，它将 metadata 加入到紧跟其后的类（这里是 InventoryApp) 中。
@Component({
  // selector 定义该组件在 HTML 中的匹配标签。它类似于 CSS 或 XPath 选择子。
  // 之后，可以在 HTML 中用 <inventory-app></inventory-app> 来调用组件;
  // 不过也可以用 div 和属性的方式调用，如 <div inventory-app></div>
  selector: 'inventory-app',

  // 模板也可以通过 templateUrl 来定义
  // 本组件调用了 ProductsList 来呈现所有的产品信息。
  // 在调用 ProductsList 组件时，用到了组件的一个关键特性：输入和输出。
  // 数据通过输入绑定 (input bindings) 流入你的组件，而你的组件中的事件
  // 则通过输出绑定 (output bindings) 流出。
  // 输入 Inputs:
  //     [productList]="products" 是输入部分，表示将当前组件中的变量值 products 
  //     传给 ProductsList 组件的 productList 属性
  // 输出 Outputs:
  //     (onProductSelected)="productWasSelected($event)"> 是输出部分，
  //     左侧的 onProductSelected 是 ProductsList 组件触发的事件，
  //     右侧的 productWasSelected 是定义在本组件中的回调函数
  //     而 $event 是 ProductsList 组件在产生 onProductSelected 事件时抛出的事件值
  template: `
  <div class="inventory-app">
    <products-list 
      [productList]="products"
      (onProductSelected)="productWasSelected($event)">
    </products-list>
  </div>
  `
})
class InventoryApp { // 类定义体实现了该组件的控制器 Controller
  products: Product[]; // 该属性存储所有的产品列表，可以在本组件的模板中使用

  constructor() {
    this.products = [
      new Product(
        'MYSHOES',
        'Black Running Shoes',
        '/resources/images/products/black-shoes.jpg',
        ['Men', 'Shoes', 'Running Shoes'],
        109.99),
      new Product(
        'NEATOJACKET',
        'Blue Jacket',
        '/resources/images/products/blue-jacket.jpg',
        ['Women', 'Apparel', 'Jackets & Vests'],
        238.99),
      new Product(
        'NICEHAT',
        'A Nice Black Hat',
        '/resources/images/products/black-hat.jpg',
        ['Men', 'Accessories', 'Hats'],
        29.99)
      ];
  }

  // 当用户选中了某个产品时，可以回调下面的方法来处理
  productWasSelected(product: Product): void {
    console.log('Product clicked: ', product);
  }
}

@NgModule({
  declarations: [ 
    InventoryApp,
    ProductImage, 
    ProductDepartment, 
    PriceDisplay,
    ProductRow,
    ProductsList
  ],
  imports: [ BrowserModule ],
  bootstrap: [ InventoryApp ]
})
class InventoryAppModule {}

platformBrowserDynamic().bootstrapModule(InventoryAppModule);

