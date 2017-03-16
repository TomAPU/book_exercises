// 使用 ngForm 和 ngControl 隐含地创建 FormControl 和 FormGroup 虽然方便，
// 但是不能进行过多设置。
// FormBuilder 是一种更加灵活的配置表单的方式。
// FormBuilder 类似于工厂对象(factory)，可以用来创建 FormControl 和 FormGroup。
import { Component } from '@angular/core';
import { // 导入这些类，以便在模板中使用 formGroup 和 formControl 指令。
  FormBuilder,
  FormGroup
} from '@angular/forms';

// 在上例中，因为导入了 FormsModule，所以 ngForm 会自动关联到每一个 form 标签，
// 并为它们创建各自的 FormGroup 对象。
//
// 本例中，我们不想让 ngForm 为我们创建 FormGroup 对象，需要使用自己通过
// FormBuilder 创建的 myForm 对象。
// 只需 '<form [formGroup]="myForm"`，即将 formGroup 指令添加到 form 标签上即可。
// 这是因为 ngForm 的选择子实际是 `form:not([ngNotForm]):not([formGroup]),ngForm,[ngForm]`，
// 因此，当 form 标签上加上 [formGroup] 或 [ngNotForm] 等属性后，ngForm 指令不会
// 应用到这些表单上。
//
// 绑定 FormControl 到 input 标签： `[formControl]="myForm.controls['sku']"`。
// 使用了 formControl 指令，同时，访问 FormGroup 对象中的 FormControl 对象，
// 用了 myForm.controls['sku']。
@Component({
  selector: 'demo-form-sku-builder',
  template: `
  <div class="ui raised segment">
    <h2 class="ui header">Demo Form: Sku with Builder</h2>
    <form [formGroup]="myForm" 
          (ngSubmit)="onSubmit(myForm.value)"
          class="ui form">

      <div class="field">
        <label for="skuInput">SKU</label>
        <input type="text" 
               id="skuInput" 
               placeholder="SKU"
               [formControl]="myForm.controls['sku']">
      </div>

    <button type="submit" class="ui button">Submit</button>
    </form>
  </div>
  `
})
export class DemoFormSkuBuilder {
  myForm: FormGroup;

  // 通过在构造器中加入该参数，从而注入(inject)了 FormBuilder
  // 在注入过程中，会创建一个 FormBuilder 实例，并赋给 fb 变量。
  // FormBuilder 中有两个主要函数：
  //   + control: 用于创建 FormControl
  //   + group: 用于创建 FormGroup
  constructor(fb: FormBuilder) {
    // 创建的 FormGroup 实例存储在组件属性 myForm 中。
    // 同时，该 FormGroup 实例中只有一个 FormControl 对象 'sku', 其值为 'ABC123'。
    // 这里创建 FormControl 的参数是一个数组，这是因为还可以添加 Validator 等参数。
    this.myForm = fb.group({
      'sku': ['ABC123']
    });
  }

  onSubmit(value: string): void {
    console.log('you submitted value: ', value);
  }
}
