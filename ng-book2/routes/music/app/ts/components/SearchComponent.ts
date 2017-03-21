// 导入
import {Component, OnInit} from '@angular/core';
import {
  Router,
  ActivatedRoute,
} from '@angular/router';

// 导入我们实现的 SpotifyService
import {SpotifyService} from 'services/SpotifyService';

@Component({
  selector: 'search',
  template: `
  <h1>Search</h1>

  <!--
  搜索框部分，
  这里定义当 input 元素的 (keydown.enter) 事件，即当在 input 元素中
  输入回车键时也能触发 form 提交。
  -->
  <p>
    <input type="text" #newquery
      [value]="query"
      (keydown.enter)="submit(newquery.value)">
    <button (click)="submit(newquery.value)">Search</button>
  </p>

  <!--
  显示搜索结果部分，
  使用 ngFor 指令来遍历搜索结果
  -->
  <div *ngIf="results">
    <div *ngIf="!results.length">
      No tracks were found with the term '{{ query }}'
    </div>

    <div *ngIf="results.length">
      <h1>Results</h1>

      <div class="row">
        <div class="col-sm-6 col-md-4" *ngFor="let t of results">
          <div class="thumbnail">
            <div class="content">
              <img src="{{ t.album.images[0].url }}" class="img-responsive">
              <div class="caption">
                <h3>
                  <!--
                  通过数组的第 2 个元素传入路由的参数
                  -->
                  <a [routerLink]="['/artists', t.artists[0].id]">
                    {{ t.artists[0].name }}
                  </a>
                </h3>
                <br>
                <p>
                  <a [routerLink]="['/tracks', t.id]">
                    {{ t.name }}
                  </a>
                </p>
              </div>
              <div class="attribution">
                <h4>
                  <a [routerLink]="['/albums', t.album.id]">
                    {{ t.album.name }}
                  </a>
                </h4>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  `
})
export class SearchComponent implements OnInit {
  query: string;
  results: Object;

  // 注入 SpotifyService, Router, ActivatedRoute 对象，
  // 以成为组件的属性
  constructor(private spotify: SpotifyService,
              private router: Router,
              private route: ActivatedRoute) {
    // this.route.queryParams 和 this.route.params 不同：
    // + this.route.queryParams 将 URL 参数组织成对象，
    //   例如在 URL http://localhost/#/search?query=cats&order=asc 中，
    //   queryParams['query'] 值为 'cats'
    // + this.route.params 将路由的参数组织成对象
    this.route
      .queryParams
      // 将查询参数保存为组件的属性，以便在刷新时可使用
      .subscribe(params => { this.query = params['query'] || ''; });
  }

  // 在页面加载时进行搜索，
  // 即当我们直接访问带有 query 参数的该 URL 时，也进行搜索操作
  // 组件的构造器中适合对值进行初始化操作，但是要想编写出
  // 好的易测试的代码，那么应该尽可能减少构造器中的代码量，
  // 而最好将组件的初始化逻辑放在下面的挂钩(hook) 方法中。
  // ngOnInit 是 OnInit 接口中的方法
  ngOnInit(): void {
    this.search();
  }

  // 提交表单后进行搜索操作
  // 同时，当访问带有 query 参数的该 URL 时（共享了一个链接或收藏了页面后），
  // 也会进行搜索操作
  submit(query: string): void {
    // 手动告诉路由，导航到 search 路由，并提供了一个 query 参数，
    // 然后再执行实际的搜索。
    // 这种方式有个很大的好处：当浏览器重新加载页面时，可以看到相同的搜索结果。
      // 这就是 "pesisting the search term on the URL"
    this.router.navigate(['search'], { queryParams: { query: query } })
      .then(_ => this.search() );
  }

  // 实际的搜索操作
  search(): void {
    console.log('this.query', this.query);
    if (!this.query) {
      return;
    }

    this.spotify
      .searchTrack(this.query)
      .subscribe((res: any) => this.renderResults(res));
  }

  // 我们将 results 定义为了组件属性，当它的值有修改后，
  // Angular 会自动为我们更新与其关联的视图
  renderResults(res: any): void {
    this.results = null;
    if (res && res.tracks && res.tracks.items) {
      this.results = res.tracks.items;
    }
  }
}
