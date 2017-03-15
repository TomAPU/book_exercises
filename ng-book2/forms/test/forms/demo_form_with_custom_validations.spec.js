"use strict";
var testing_1 = require('@angular/core/testing');
var forms_1 = require('@angular/forms');
var testing_2 = require('@angular/core/testing');
var util_1 = require('../util');
var by_1 = require('@angular/platform-browser/src/dom/debug/by');
var demo_form_with_custom_validations_1 = require('../../app/ts/forms/demo_form_with_custom_validations');
testing_1.describe('DemoFormWithCustomValidations', function () {
    var el, input, form;
    var providerArr;
    beforeEach(function () {
        testing_1.addProviders([
            forms_1.disableDeprecatedForms(),
            forms_1.provideForms(),
            forms_1.FormBuilder
        ]);
    });
    function createComponent(tcb) {
        return tcb.overrideProviders(demo_form_with_custom_validations_1.DemoFormWithCustomValidations, providerArr)
            .createAsync(demo_form_with_custom_validations_1.DemoFormWithCustomValidations)
            .then(function (fixture) {
            el = fixture.debugElement.nativeElement;
            input = fixture.debugElement.query(by_1.By.css("input")).nativeElement;
            form = fixture.debugElement.query(by_1.By.css("form")).nativeElement;
            fixture.detectChanges();
            return fixture;
        });
    }
    testing_1.it('displays errors with no sku', testing_1.async(testing_1.inject([testing_2.TestComponentBuilder], function (tcb) {
        return createComponent(tcb).then(function (fixture) {
            input.value = '';
            util_1.dispatchEvent(input, 'input');
            fixture.detectChanges();
            var msgs = el.querySelectorAll('.ui.error.message');
            expect(msgs[0].innerHTML).toContain('SKU is invalid');
            expect(msgs[1].innerHTML).toContain('SKU is required');
            expect(msgs[2].innerHTML).toContain('SKU must begin with <tt>123</tt>');
            expect(msgs[3].innerHTML).toContain('Form is invalid');
        });
    })));
    testing_1.it('removes the required error when sku has a value', testing_1.async(testing_1.inject([testing_2.TestComponentBuilder], function (tcb) {
        return createComponent(tcb).then(function (fixture) {
            input.value = 'ABC';
            util_1.dispatchEvent(input, 'input');
            fixture.detectChanges();
            var msgs = el.querySelectorAll('.ui.error.message');
            expect(msgs[0].innerHTML).toContain('SKU is invalid');
            expect(msgs[1].innerHTML).toContain('SKU must begin with <tt>123</tt>');
            expect(msgs[2].innerHTML).toContain('Form is invalid');
        });
    })));
    testing_1.it('removes all errors when sku starts with 123', testing_1.async(testing_1.inject([testing_2.TestComponentBuilder], function (tcb) {
        return createComponent(tcb).then(function (fixture) {
            input.value = '123ABC';
            util_1.dispatchEvent(input, 'input');
            fixture.detectChanges();
            var msgs = el.querySelectorAll('.ui.error.message');
            expect(msgs.length).toEqual(0);
        });
    })));
});
