// 每个 FormGroup 和 FormControl 对象都有 EventEmitter 这个观察者模式的对象，
// 我们可以通过该 EventEmitter 对表单或表单项进行修改情况的侦听。
// 对表单项 FormControl 的监听需要：
//   1. 通过 control.valueChanges 获取 EventEmitter 对象
//   2. 使用 `.subscribe` 添加观察者
import { Component } from '@angular/core';
import {
  FormBuilder,
  FormGroup,
  Validators,
  AbstractControl
} from '@angular/forms';

@Component({
  selector: 'demo-form-with-events',
  template: `
  <div class="ui raised segment">
    <h2 class="ui header">Demo Form: with events</h2>
    <form [formGroup]="myForm"
          (ngSubmit)="onSubmit(myForm.value)"
          class="ui form">

      <div class="field"
          [class.error]="!sku.valid && sku.touched">
        <label for="skuInput">SKU</label>
        <input type="text"
               class="form-control"
               id="skuInput"
               placeholder="SKU"
               [formControl]="sku">
         <div *ngIf="!sku.valid"
           class="ui error message">SKU is invalid</div>
         <div *ngIf="sku.hasError('required')"
           class="ui error message">SKU is required</div>
      </div>

      <div *ngIf="!myForm.valid"
        class="ui error message">Form is invalid</div>

      <button type="submit" class="ui button">Submit</button>
    </form>
  </div>
  `
})
export class DemoFormWithEvents {
  myForm: FormGroup;
  sku: AbstractControl;

  constructor(fb: FormBuilder) {
    this.myForm = fb.group({
      'sku':  ['', Validators.required]
    });

    this.sku = this.myForm.controls['sku'];

    // 对单个表单项 FormControl 的修改情况进行侦听
    this.sku.valueChanges.subscribe(
      (value: string) => {
        console.log('sku changed to:', value);
      }
    );

    // 对整个表单 FormGroup 的修改情况进行侦听
    this.myForm.valueChanges.subscribe(
      (form: any) => {
        console.log('form changed to:', form);
      }
    );

  }

  onSubmit(form: any): void {
    console.log('you submitted value:', form.sku);
  }
}
