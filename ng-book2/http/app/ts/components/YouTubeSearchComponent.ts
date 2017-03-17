/**
 * YouTubeSearchComponent is a tiny app that will autocomplete search YouTube.
 */

import {
  Component,
  Injectable,
  OnInit,
  ElementRef,
  EventEmitter,
  Inject
} from '@angular/core';
import { Http, Response } from '@angular/http';
import { Observable } from 'rxjs';

/*
  This API key may or may not work for you. Your best bet is to issue your own
  API key by following these instructions:
  https://developers.google.com/youtube/registering_an_application#Create_API_Keys

  Here I've used a **server key** and make sure you enable YouTube.

  Note that if you do use this API key, it will only work if the URL in
  your browser is "localhost"
*/
// 将 YouTube 服务的 API KEY, API URL 定义为常数
// 对于这些环境变量（生产环境、开发环境下有不同的值），
// 最好使它们能可注入(injectable)
export var YOUTUBE_API_KEY: string = 'AIzaSyDOfT_BO81aEZScosfTYMruJobmpjqNeEk';
export var YOUTUBE_API_URL: string = 'https://www.googleapis.com/youtube/v3/search';

let loadingGif: string = ((<any>window).__karma__) ? '' : require('images/loading.gif');

// 用来保存查询结果
class SearchResult {
  id: string;
  title: string;
  description: string;
  thumbnailUrl: string;
  videoUrl: string;

  // obj? 是一个可选参数，用来模拟关键字参数
  constructor(obj?: any) {
    this.id              = obj && obj.id             || null;
    this.title           = obj && obj.title          || null;
    this.description     = obj && obj.description    || null;
    this.thumbnailUrl    = obj && obj.thumbnailUrl   || null;
    this.videoUrl        = obj && obj.videoUrl       ||
                             `https://www.youtube.com/watch?v=${this.id}`;
  }
}

/**
 * YouTubeService connects to the YouTube API
 * See: * https://developers.google.com/youtube/v3/docs/search/list
 */
// 由于 YouTubeService 类也要定义为可注入，所以使用了 @Injectable() 注解。
@Injectable()
export class YouTubeService {
  // 该构造器中注入了 3 个变量：
  //   1. Http 注入和上面例子中的一样，使用的是隐式注入
  //   2. YOUTUBE_API_KEY 和 YOUTUBE_API_URL 使用 @Inject，是显式注入
  // 注入后，组件中就会生成 this.http, this.apiKey, this.apiUrl 属性了。
  constructor(private http: Http,
              @Inject(YOUTUBE_API_KEY) private apiKey: string,
              @Inject(YOUTUBE_API_URL) private apiUrl: string) {
  }

  // 该方法返回一个 Observable 对象，该对象会发送
  // SearchResult 数组
  search(query: string): Observable<SearchResult[]> {
    let params: string = [
      `q=${query}`,
      `key=${this.apiKey}`,
      `part=snippet`,
      `type=video`,
      `maxResults=10`
    ].join('&');
    let queryUrl: string = `${this.apiUrl}?${params}`;


    // 这里使用 this.http.get 进行 GET 请求，将返回的 Response
    // 进行 map 处理，使每个查询结果转换成 SearchResult 类型。
    return this.http.get(queryUrl)
      .map((response: Response) => {
        // 这里的 `(<any>Response.json()).items`：告诉 TypeScrit 这里无需进行严格的类型检查
        // 在使用 JSON API 时，API 返回不会有类型定义，
        // 因此 TypeScript 不会知道返回的应用中会有 items 键，
        // 从而会抛出警告等信息
        return (<any>response.json()).items.map(item => {
          // console.log("raw item", item); // uncomment if you want to debug
          return new SearchResult({
            id: item.id.videoId,
            title: item.snippet.title,
            description: item.snippet.description,
            thumbnailUrl: item.snippet.thumbnails.high.url
          });
        });
      });
  }
}

// 将这些值做成 injectable，我们使用 {provide: ..., useValue: ...} 语法。
// 这里我们指定将可注入的 YOUTUBE_API_KEY 绑定到值 YOUTUBE_API_KEY（YOUTUBE_API_URL 也一样），
// 将可注入的 YouTubeService 绑定到类 YouTubeService。
// 将 youTubeServiceInjectables 导出后，就可以在主入口文件 app.ts 等中使用。
export var youTubeServiceInjectables: Array<any> = [
  {provide: YouTubeService, useClass: YouTubeService},
  {provide: YOUTUBE_API_KEY, useValue: YOUTUBE_API_KEY},
  {provide: YOUTUBE_API_URL, useValue: YOUTUBE_API_URL}
];

/**
 * SearchBox 显示搜索框，并基于搜索结果发送出事件。
 * 它是 UI 和 YouTubeService 之间的中介。
 * 它实现：
 *   1. 监听 input 上的 keyup 事件，向 YouTubeService 请求查询
 *   2. 当加载时发送出 loading 事件
 *   3. 当返回查询结果时发送出 results 事件
 */

@Component({
  outputs: ['loading', 'results'], // 定义输出事件
  selector: 'search-box',
  template: `
    <input type="text" class="form-control" placeholder="Search" autofocus>
  `
})
export class SearchBox implements OnInit {
  // 该类实现了 OnInit 接口，该接口中定义了 ngOnInit 方法，
  // 在里面可以做一些初始化任务（因为调用 constructor 时像组件的 input 元素
  // 等都还不能操作），只能在 ngOnInit 里操作。
    //
    // 定义及初始化 2 个输出事件
  loading: EventEmitter<boolean> = new EventEmitter<boolean>();
  results: EventEmitter<SearchResult[]> = new EventEmitter<SearchResult[]>();

  // 注入了 2 个对象，其中 el 就是该组件关联的元素，类型是 ElementRef，
  // 它是 Angular 对 HTML 元素的一个封装对象。
  constructor(private youtube: YouTubeService,
              private el: ElementRef) {
  }

  ngOnInit(): void {
      // 当然我们也可以手动侦听 input 框的 keyup 事件，不过由于它
      // 要完成下面的一系列操作，手动侦听有点难度：
      //   1. 过滤掉所有的空或很短的查询
      //   2. "debounce"，不在用户输入每个字符时都进行查询请求，只在用户
      //     输入后暂停一段时间后才去查询
      //   3. 如果用户进行了新的查询，那么只显示新的查询内容
      //
      // 因此，将 `keyup` 事件转成 Rx 的 Observable 流会更简单。
      // 使用 Rx.Observable.fromEvent 进行转换：
    Observable.fromEvent(this.el.nativeElement, 'keyup')  // this.el.nativeElement 就是本组件关联的 DOM 对象，
                                                          //转化成 keyup 事件流后，可以对流进行各种操作。
      .map((e: any) => e.target.value) // 流中的是 keyup 事件 e，e.target 就是事件关联的 input 元素，
                                        //这里的作用是将事件流转成 input 值的流
      .filter((text: string) => text.length > 1) // 过滤掉 input 值流中的空值
      .debounceTime(250)                         // 只有用户输入后暂停 250ms 后才进行查询
      .do(() => this.loading.next(true))        // `do` 操作是对流中的每个事件都进行该操作，但不对流本身进行修改，
                                                //这里是让 this.loading(EventEmitter对象）发送 true 值作为下一个事件，用来显示 'loading...'
      .map((query: string) => this.youtube.search(query)) // 为流中的每个查询值进行实际的查询操作
      .switch() // 表示当有新查询时，只关注最新的查询，忽略旧的查询
      // 查询后返回的是 SearchResult[]，因此现在是一个 SearchResult[] 流
      .subscribe( // 注册侦听流中的每个 SearchResult[] 返回值
        (results: SearchResult[]) => { // 流中出现一个正常的 SearchResult[] 时调用
          this.loading.next(false);  // 发送 false 作为下一个事件，表示隐藏 'loading...' 显示
          this.results.next(results); // 发送 SearchResult[] 作为下一个事件
        },
        (err: any) => { // 当流中出现一个错误时调用
          console.log(err);
          this.loading.next(false);
        },
        () => { // 当流中的某个事件操作完成时都会调用
          this.loading.next(false);
        }
      );

  }
}


// 该组件显示单个查询结果
@Component({
  inputs: ['result'], // 定义输入域，类型为 SearchResult
  selector: 'search-result',
  template: `
   <div class="col-sm-6 col-md-3">
      <div class="thumbnail">
        <img src="{{result.thumbnailUrl}}">
        <div class="caption">
          <h3>{{result.title}}</h3>
          <p>{{result.description}}</p>
          <p><a href="{{result.videoUrl}}"
                class="btn btn-default" role="button">
                Watch</a></p>
        </div>
      </div>
    </div>
  `
})
export class SearchResultComponent {
  result: SearchResult;
}


// 该组件用来整合所有的组件
@Component({
  selector: 'youtube-search',

  template: `
  <div class='container'>
      <div class="page-header">
        <h1>YouTube Search

          <!-- 
           loadingGif 变量来自程序中的 `require` 语句，
           这是 webpack 的图片加载功能（见 https://github.com/tcoopman/image-webpack-loader）
           这里当本地变量 'loading' 为 true 时会显示该图片
          -->
          <img
            style="float: right;"
            *ngIf="loading"
            src='${loadingGif}' />
        </h1>
      </div>

      <div class="row">
        <div class="input-group input-group-lg col-md-12">
          <!--
            绑定SerarchBox 的输出：
              1. `(loading)="loading = $event"` 表示当 SearchBox 出现 loading 事件时，
                会运行 `loading=$event` 表达式，其中的 $event 是事件发送出的值。
              2. `(results)="updateResults($event)"` 表示当 SearchBox 出现 results 事件时，
                运行组件的 updateResults 方法，其中的 $event 是事件发送出的值 (SearchResult[] 类型）
          -->
          <search-box
             (loading)="loading = $event"
             (results)="updateResults($event)"
              ></search-box>
        </div>
      </div>

      <div class="row">
        <search-result
          *ngFor="let result of results"
          [result]="result">
        </search-result>
      </div>
  </div>
  `
})
export class YouTubeSearchComponent {
  results: SearchResult[];

  updateResults(results: SearchResult[]): void {
    this.results = results;
    // console.log("results:", this.results); // uncomment to take a look
  }
}
