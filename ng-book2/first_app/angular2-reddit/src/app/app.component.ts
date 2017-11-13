import { Component } from '@angular/core';
import { Article } from './article/article.model';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
    // 将 articles 定义为是 Article 的数组，
    // 也可以写成 articles: Array<Article>
    articles: Article[];

    constructor(){
        this.articles = [
            new Article('Angular 2', 'http://angular.io', 3),
            new Article('Fullstack', 'http://fullstack.io', 2),
            new Article('Angular Homepage', 'http://angular.io', 1)
        ];
    }

    // 方法声明的格式为：
    // functionName(propertyName1: typeName, propertyName2: typeName): returnTypeName
    // 这些参数需要在响应事件时传入
    addArticle(title: HTMLInputElement, link: HTMLInputElement): boolean {
        // 这里又用 ` 来包围字符串，在 ES6 中，这种字符串能扩展里面的变量值
        console.log(`Adding article title: ${title.value} and link: ${link.value}`);
        this.articles.push(new Article(title.value, link.value, 0));

        // 值清空后，其绑定的 Input 标签上的值也会清空
        title.value = '';
        link.value = '';
        return false;
    }

    sortedArticles(): Article[] {
        return this.articles.sort((a: Article, b: Article) => b.votes - a.votes);
    }
}
