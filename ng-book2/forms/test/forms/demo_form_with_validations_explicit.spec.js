"use strict";
var testing_1 = require('@angular/core/testing');
var testing_2 = require('@angular/core/testing');
var forms_1 = require('@angular/forms');
var by_1 = require('@angular/platform-browser/src/dom/debug/by');
var demo_form_with_validations_explicit_1 = require('../../app/ts/forms/demo_form_with_validations_explicit');
var util_1 = require('../util');
testing_1.describe('DemoFormWithValidationsExplicit', function () {
    var el, input, form;
    beforeEach(function () {
        testing_1.addProviders([
            forms_1.disableDeprecatedForms(),
            forms_1.provideForms(),
            forms_1.FormBuilder
        ]);
    });
    function createComponent(tcb) {
        return tcb.createAsync(demo_form_with_validations_explicit_1.DemoFormWithValidationsExplicit)
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
            testing_1.expect(msgs[0].innerHTML).toContain('SKU is invalid');
            testing_1.expect(msgs[1].innerHTML).toContain('SKU is required');
        });
    })));
    testing_1.it('displays no errors when sku has a value', testing_1.async(testing_1.inject([testing_2.TestComponentBuilder], function (tcb) {
        return createComponent(tcb).then(function (fixture) {
            input.value = 'ABC';
            util_1.dispatchEvent(input, 'input');
            fixture.detectChanges();
            var msgs = el.querySelectorAll('.ui.error.message');
            testing_1.expect(msgs.length).toEqual(0);
        });
    })));
});
