/* tslint:disable:no-string-literal */
import { Component } from '@angular/core';

// 验证器由 Validators 模块提供，最简单的验证器是 Validators.required。
// 要使用验证器，需：
//   1. 将一个验证器赋给一个 FormControl 对象
//   2. 在视图中检查验证器的状态，然后进行相关操作
//   
//  将验证器赋给 FormControl 对象，只需将验证器作为第 2 个参数
//  传入 FormControl 构造器即可，如：
//      let control = new FormControl('sku', Validators.required);
//  或者在用 FormBuilder 创建 FormControl 时，作为参数数组的第 2 个值传入，如：
//      this.myForm = fb.group({'sku':  ['', Validators.required] });
import {
  FormBuilder,
  FormGroup,
  Validators,
  AbstractControl
} from '@angular/forms';

// 验证器在模板中使用，主要关注 4 个方面：
// 1. 检查整个表单的有效性，并显示相应消息
// 2. 检查单个项的有效性，并显示相应消息
// 3. 检查单个项的有效性，无效时设置该项颜色为红色
// 4. 检查单个项的某个特定要求，不满足时显示相应消息
@Component({
  selector: 'demo-form-with-validations-explicit',
  template: `
  <div class="ui raised segment">
    <h2 class="ui header">Demo Form: with validations (explicit)</h2>
    <form [formGroup]="myForm"
          (ngSubmit)="onSubmit(myForm.value)"
          class="ui form">

      <!-- 4. 检查单个项的某个特定要求，不满足时显示相应消息 
          当无效时，添加 error class。同时 sku.touched 确保
          只有在用户操作（如输入后再删除）过后才显示。
      -->
      <div class="field"
          [class.error]="!sku.valid && sku.touched">
        <label for="skuInput">SKU</label>
        <input type="text"
               id="skuInput"
               placeholder="SKU"
               [formControl]="sku">

         <!-- 2. 检查单个项的有效性，并显示相应消息 -->
         <div *ngIf="!sku.valid"
           class="ui error message">SKU is invalid</div>

         <!-- 4. 检查单个项的某个特定要求，不满足时显示相应消息 
              当然也可以通过 FormGroup 对象来检查，如：
              *ngIf="myForm.hasError('required', 'sku')"，它和
              下面的效果等同
         -->
         <div *ngIf="sku.hasError('required')"
           class="ui error message">SKU is required</div>
      </div>

      <!-- 1. 检查整个表单的有效性，并显示相应消息 -->
      <div *ngIf="!myForm.valid"
        class="ui error message">Form is invalid</div>

      <button type="submit" class="ui button">Submit</button>
    </form>
  </div>
  `
})
export class DemoFormWithValidationsExplicit {
  myForm: FormGroup;
  sku: AbstractControl;

  constructor(fb: FormBuilder) {
    this.myForm = fb.group({
      'sku':  ['', Validators.required] // 同时将一个验证器赋给新建的 FormControl
    });

    // 这里将创建的 FormControl 对象抽取出来存放在实例的属性 sku 中 (AbstractControl 类型),
    // 从而可以在模板中直接访问
    this.sku = this.myForm.controls['sku'];
  }

  onSubmit(value: string): void {
    console.log('you submitted value: ', value);
  }
}
