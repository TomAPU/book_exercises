/*
 * Angular
 */
import {
  Component,
  ReflectiveInjector,
} from '@angular/core';
import { NgModule } from "@angular/core";
import { BrowserModule } from "@angular/platform-browser";
import { platformBrowserDynamic } from "@angular/platform-browser-dynamic";

/*
 * Webpack
 */
require('css/styles.css');

// 先创建一个只返回一个字符串的服务：
class MyService {
  getValue(): string {
    return 'a value';
  }
}

// 应用组件
@Component({
  selector: 'di-sample-app',
  template: `
  <button (click)="invokeService()">Get Value</button>
  `
})
class DiSampleApp {
  myService: MyService;

  constructor() {
      // 使用静态方法 ReflectiveInjector.resolveAndCreate 来创建 Injector 实例
      // 传入的参数是一个数组，包含所有该 Injector 实例需知道的
      // 可注入对象，这里我们只想让它知道
      // MyService 这个可注入对象
      // ReflectiveInjector 是 Injector 的一个具体实现
      // 它是最常的 Injector 类
    let injector: any = ReflectiveInjector.resolveAndCreate([MyService]);
    this.myService = injector.get(MyService);

      // 需要注意的是：注入的是一个单例实例
      // 因此，这里输出是 "Same instance? true"
    console.log('Same instance?', this.myService === injector.get(MyService));
  }

  invokeService(): void {
    console.log('MyService returned', this.myService.getValue());
  }
}

// 由于使用了自己的 Injector 实现，因此无需和以前那样
// 将 MyService 放入 NgModule 的 providers 列表中
// no need to add injectables here
@NgModule({
  declarations: [ DiSampleApp ],
  imports: [ BrowserModule ],
  bootstrap: [ DiSampleApp ]
})
class DiSampleAppModule {}

platformBrowserDynamic().bootstrapModule(DiSampleAppModule);

