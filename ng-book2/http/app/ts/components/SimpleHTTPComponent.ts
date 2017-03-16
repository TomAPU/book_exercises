import {Component} from '@angular/core';

// 导入 HTTP 库中的相关对象
import {Http, Response} from '@angular/http';

@Component({
  selector: 'simple-http',

  // 模板中，data 是一个对象，在调试时可通过
  // json 过滤器来显示
  template: `
  <h2>Basic Request</h2>
  <button type="button" (click)="makeRequest()">Make Request</button>
  <div *ngIf="loading">loading...</div>
  <pre>{{data | json}}</pre>
`
})
export class SimpleHTTPComponent {
  data: Object;
  // 通过与模板中的 ngIf 指令结合，可以在数据加载时显示 "loading..."
  loading: boolean;

  // 构造器体是空的，但是当参数是 `private http: Http` 时，
  // TypeScript 将会把 http 赋值给 this.http，实现上等同于：
  //  private http: Http;
  //
  //  constructor(http: Http){
  //     this.http = http
  //  }
  constructor(private http: Http) {
  }

  makeRequest(): void {
    this.loading = true; // 先显示 加载中 ...
    // Http.request 发送一个 GET 请求，返回的是
    // 一个 Observable 对象，可以通过 subscribe
    // 添加侦听者。subscribe(successFn, failureFn, completedFn)。
    // Http.request 返回数据后，会发送一个 Response 对象，
    // 我们可以在 subscribe 的回调函数中进处理。
    this.http.request('http://jsonplaceholder.typicode.com/posts/1')
      .subscribe((res: Response) => {
        this.data = res.json();
        this.loading = false;
      });
  }
}

