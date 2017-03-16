// ngModel 指令用于将数据模型绑定到表单中。
// Angular 2 中的数据流一般是单向的（自上而下），
// 但是 ngModel 指令实现的是双向绑定。
import { Component } from '@angular/core';
import {
  FormBuilder,
  FormGroup,
  Validators
} from '@angular/forms';

@Component({
  selector: 'demo-form-ng-model',
  template: `
  <div class="ui raised segment">
    <h2 class="ui header">Demo Form: with ng-model</h2>

    <div class="ui info message">
      The product name is: {{productName}}
    </div>

    <form [formGroup]="myForm"
          (ngSubmit)="onSubmit(myForm.value)"
          class="ui form">

      <div class="field">
        <label for="productNameInput">Product Name</label>
        <!--
        由于 [] 表示输入，而 () 表示输出，
        这里 [(ngModel)] 很容易看出是双向绑定，
        实现将该 input 项的值与组件属性 productName 的值进行同步绑定
        -->
        <input type="text"
               id="productNameInput"
               placeholder="Product Name"
               [formControl]="myForm.get('productName')"
               [(ngModel)]="productName">
      </div>

      <div *ngIf="!myForm.valid"
        class="ui error message">Form is invalid</div>
      <button type="submit" class="ui button">Submit</button>
    </form>

  </div>
  `
})
export class DemoFormNgModel {
  myForm: FormGroup;
  productName: string;

  constructor(fb: FormBuilder) {
    this.myForm = fb.group({
      'productName':  ['', Validators.required]
    });
  }

  onSubmit(value: string): void {
    console.log('you submitted value: ', value);
  }
}
