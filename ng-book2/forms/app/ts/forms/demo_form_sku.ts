import { Component } from '@angular/core';

// 该组件显示一个提交 SKU 的表单
@Component({
  selector: 'demo-form-sku',

  // 由于已在 @NgModule 中增加了 FormsModule 依赖，现可以在模板中使用 NgForm。
  // Angular 2 中任何指令，一旦应用到视图中时，它们都会与视图中和指令的选择子
  // 匹配的所有元素关联。由于 NgForm 指令的选择子有 form 标签，这意味着：
  // 当将 `FormsModule` 导入后， `NgForm` 指令将自动关联到视图中的所有 form 标签。
  // NgForm 提供了 2 个重要功能：
  //    1. 一个名为 ngForm 的 FormGroup 对象
  //    2. 一个 (ngSubmit) 输出
  // 下面的模板中，通过 `#f="ngForm"`，实现将表单中由 NgForm 指令自动生成的名为 ngForm 
  // 的 FormGroup 对象，创建一个本地别名变量 f。
  // 而 (ngSubmit) 也是来自 NgForm 指令，其回调函数的参数是 f.value，由于 f 是一个 FormGroup
  // 对象，因此 f.value 是一个键值对。
  //
  // NgModel 指令的选择子有 ngModel，因此，只要在 input 标签中加入 `ngModel="whatever"` 等属性时，该指令就会与此 input 关联。
  // 下面模板中添加的 ngModel 属性没有属性值，表示其属性值和 input 的 name 值相等，即也是 "sku"
  // 当在 input 上加个一个无属性值的 ngModel 属性时，表示：
  //   1. 建立一个单向数据绑定
  //   2. 根据该 input 的 name 值，创建一个同名的 FormControl 对象
  // 由 ngModel 创建的 FormControl 对象会自动添加到父 FormGroup 对象中（本例中 f），
  // 并将 DOM 元素也和新建的该 FormControl 对象绑定。
  template: `
  <div class="ui raised segment">
    <h2 class="ui header">Demo Form: Sku</h2>
    <form #f="ngForm"
          (ngSubmit)="onSubmit(f.value)"
          class="ui form">

      <div class="field">
        <label for="skuInput">SKU</label>
        <input type="text"
               id="skuInput"
               placeholder="SKU"
               name="sku" ngModel>
      </div>

      <button type="submit" class="ui button">Submit</button>
    </form>
  </div>
  `
})
export class DemoFormSku {
  onSubmit(form: any): void {
    console.log('you submitted value:', form);
  }
}
