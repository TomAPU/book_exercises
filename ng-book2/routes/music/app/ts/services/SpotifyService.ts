import {Injectable} from '@angular/core';
import {Http} from '@angular/http';
import {Observable} from 'rxjs/Observable';

import 'rxjs/Rx';

/**
 * SpotifyService works querying the Spotify Web API
 * https://developer.spotify.com/web-api/
 */

// 该类注解为可注入
@Injectable()
export class SpotifyService {
  static BASE_URL: string = 'https://api.spotify.com/v1';

  constructor(private http: Http) {
  }

  // 拼接参数，并实际请求 Spotify API，返回是一个 Observable，
  // 这里通过 RxJS 的 map 函数将 http.request 返回的 Response 对象
  // 转换成 JSON 对象
  query(URL: string, params?: Array<string>): Observable<any[]> {
    let queryURL: string = `${SpotifyService.BASE_URL}${URL}`;
    if (params) {
      queryURL = `${queryURL}?${params.join('&')}`;
    }

    return this.http.request(queryURL).map((res: any) => res.json());
  }

  // 使用 https://developer.spotify.com/web-api/search-item/
  // 可以根据关键字指定类型的元素，如 type=track 时搜索音轨
  search(query: string, type: string): Observable<any[]> {
    return this.query(`/search`, [
      `q=${query}`,
      `type=${type}`
    ]);
  }

  // 搜索音轨
  searchTrack(query: string): Observable<any[]> {
    return this.search(query, 'track');
  }

  // 搜索特定音轨的详情
  getTrack(id: string): Observable<any[]> {
    return this.query(`/tracks/${id}`);
  }

  // 搜索特定艺术家的详情
  getArtist(id: string): Observable<any[]> {
    return this.query(`/artists/${id}`);
  }

  // 搜索特定唱片的详情
  getAlbum(id: string): Observable<any[]> {
    return this.query(`/albums/${id}`);
  }
}

export var SPOTIFY_PROVIDERS: Array<any> = [
  {provide: SpotifyService, useClass: SpotifyService}
];
