/*
 * Angular
 */

import {Component, OnInit} from '@angular/core';
import {ActivatedRoute} from '@angular/router';
import {Location} from '@angular/common';

/*
 * Services
 */
import {SpotifyService} from 'services/SpotifyService';


// angular2 中不能用 'track' 作为选择子
// 因为这是一个已存在的 HTML 元素
// https://developer.mozilla.org/en-US/docs/Web/HTML/Element/track
// 该组件显示音轨的名字，唱片封面图片，
// 并使用 HTML5 audio 标签进行预览播放
@Component({
  selector: 'theTrack',
  template: `
  <div *ngIf="track">
    <h1>{{ track.name }}</h1>

    <p>
      <img src="{{ track.album.images[1].url }}">
    </p>

    <p>
      <audio controls src="{{ track.preview_url }}"></audio>
    </p>

    <p><a href (click)="back()">Back</a></p>
  </div>
  `
})
export class TrackComponent implements OnInit {
  id: string;
  track: Object;

  constructor(private route: ActivatedRoute, private spotify: SpotifyService,
              private location: Location) {
    // 将路由的参数保存为组件的属性
    route.params.subscribe(params => { this.id = params['id']; });
  }

  // 当初始化后，获取音轨的详细信息进行显示
  ngOnInit(): void {
    this.spotify
      .getTrack(this.id)
      .subscribe((res: any) => this.renderTrack(res));
  }

  // 实现页面返回（后退）功能
  back(): void {
    this.location.back();
  }

  renderTrack(res: any): void {
    this.track = res;
  }
}

