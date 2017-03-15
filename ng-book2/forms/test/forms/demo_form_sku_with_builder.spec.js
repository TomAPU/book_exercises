"use strict";
var testing_1 = require('@angular/core/testing');
var testing_2 = require('@angular/core/testing');
var forms_1 = require('@angular/forms');
var demo_form_sku_with_builder_1 = require('../../app/ts/forms/demo_form_sku_with_builder');
testing_1.describe('DemoFormSkuBuilder', function () {
    var providerArr;
    beforeEach(function () {
        providerArr = [
            forms_1.disableDeprecatedForms(),
            forms_1.provideForms(),
            forms_1.FormBuilder
        ];
    });
    testing_1.it('initializes sku', testing_1.async(testing_1.inject([testing_2.TestComponentBuilder], function (tcb) {
        var fb = new forms_1.FormBuilder();
        return tcb.overrideProviders(demo_form_sku_with_builder_1.DemoFormSkuBuilder, providerArr)
            .createAsync(demo_form_sku_with_builder_1.DemoFormSkuBuilder)
            .then(function (fixture) {
            var comp = fixture.debugElement.componentInstance;
            var el = fixture.debugElement.nativeElement;
            fixture.detectChanges();
            testing_1.expect(comp.myForm.controls.sku.value).toEqual('ABC123');
            testing_1.expect(el.querySelector('form input').value).toEqual('ABC123');
        });
    })));
});
