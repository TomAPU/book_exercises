/*
 * host 就是代表当前组件关联到的元素。这里设置将
 * 每个 app-article 标签上都加个 'row' 类。通过 host，
 * 我们可以在组件内对元素标签进行配置
 */
import { Component, OnInit, Input } from '@angular/core';
import { Article } from './article.model.ts';

@Component({
  selector: 'app-article',
  templateUrl: './article.component.html',
  styleUrls: ['./article.component.css']
  host: {
      class: 'row'
  }
})
export class ArticleComponent implements OnInit {
  // 这些属性可以在组件模板中引用
  @Input() article: Article;

  // 这些函数可以在组件模板中引用
  voteUp(): boolean {
      this.article.voteUp();
      return false;
  }

  voteDown(): boolean {
      this.article.voteDown();
      return false;
  }

  ngOnInit() {
  }

}
