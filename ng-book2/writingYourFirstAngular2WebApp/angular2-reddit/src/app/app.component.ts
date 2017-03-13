import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
    // 方法声明的格式为：
    // functionName(propertyName1: typeName, propertyName2: typeName): returnTypeName
    // 这些参数需要在响应事件时传入
    addArticle(title: HTMLInputElement, link: HTMLInputElement): boolean {
        // 这里又用 ` 来包围字符串，在 ES6 中，这种字符串能扩展里面的变量值
        console.log(`Adding article title: ${title.value} and link: ${link.value}`);
        return false;
    }
}
