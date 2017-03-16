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
        // 在使用 JSON API 时，API 返回通常不会有类型定义，
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
// 这里我们指定将可注入的 YOUTUBE_API_KEY 绑定到值 YOUTUBE_API_KEY（YOUTUBE_API_URL 也一样），将可注入的 YouTubeService 绑定到类 YouTubeService。
// 所有我们将 youTubeServiceInjectables 导出了，所以可以在主入口文件 app.ts 等中使用。
export var youTubeServiceInjectables: Array<any> = [
  {provide: YouTubeService, useClass: YouTubeService},
  {provide: YOUTUBE_API_KEY, useValue: YOUTUBE_API_KEY},
  {provide: YOUTUBE_API_URL, useValue: YOUTUBE_API_URL}
];

/**
 * SearchBox 显示搜索框，并基于搜索结果发送出事件。
 * 它是 UI 和 YouTubeService 之间的中介。
 * 它实现：
 *   1. 监听 input 上的 keyup 事件，向 YouTubeService 提供一次查询
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
  loading: EventEmitter<boolean> = new EventEmitter<boolean>();
  results: EventEmitter<SearchResult[]> = new EventEmitter<SearchResult[]>();

  constructor(private youtube: YouTubeService,
              private el: ElementRef) {
  }

  ngOnInit(): void {
    // convert the `keyup` event into an observable stream
    Observable.fromEvent(this.el.nativeElement, 'keyup')
      .map((e: any) => e.target.value) // extract the value of the input
      .filter((text: string) => text.length > 1) // filter out if empty
      .debounceTime(250)                         // only once every 250ms
      .do(() => this.loading.next(true))         // enable loading
      // search, discarding old events if new input comes in
      .map((query: string) => this.youtube.search(query))
      .switch()
      // act on the return of the search
      .subscribe(
        (results: SearchResult[]) => { // on sucesss
          this.loading.next(false);
          this.results.next(results);
        },
        (err: any) => { // on error
          console.log(err);
          this.loading.next(false);
        },
        () => { // on completion
          this.loading.next(false);
        }
      );

  }
}

@Component({
  inputs: ['result'],
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

@Component({
  selector: 'youtube-search',
  template: `
  <div class='container'>
      <div class="page-header">
        <h1>YouTube Search
          <img
            style="float: right;"
            *ngIf="loading"
            src='${loadingGif}' />
        </h1>
      </div>

      <div class="row">
        <div class="input-group input-group-lg col-md-12">
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
