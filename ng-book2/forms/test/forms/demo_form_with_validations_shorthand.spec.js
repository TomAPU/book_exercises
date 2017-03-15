"use strict";
var testing_1 = require('@angular/core/testing');
var testing_2 = require('@angular/core/testing');
var forms_1 = require('@angular/forms');
var by_1 = require('@angular/platform-browser/src/dom/debug/by');
var demo_form_with_validations_shorthand_1 = require('../../app/ts/forms/demo_form_with_validations_shorthand');
var util_1 = require('../util');
testing_1.describe('DemoFormWithValidationsShorthand', function () {
    var originalConsole, fakeConsole;
    var el, input, form;
    beforeEach(function () {
        fakeConsole = new util_1.ConsoleSpy();
        originalConsole = window.console;
        window.console = fakeConsole;
        testing_1.addProviders([
            forms_1.disableDeprecatedForms(),
            forms_1.provideForms(),
            forms_1.FormBuilder
        ]);
    });
    afterAll(function () { return window.console = originalConsole; });
    function createComponent(tcb) {
        return tcb.createAsync(demo_form_with_validations_shorthand_1.DemoFormWithValidationsShorthand)
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
            input.value = 'XYZ';
            util_1.dispatchEvent(input, 'input');
            fixture.detectChanges();
            var msgs = el.querySelectorAll('.ui.error.message');
            testing_1.expect(msgs.length).toEqual(0);
        });
    })));
    testing_1.it('logs the correct form value to console', testing_1.inject([testing_2.TestComponentBuilder], testing_1.fakeAsync(function (tcb) {
        createComponent(tcb).then(function (fixture) {
            input.value = 'XYZ';
            util_1.dispatchEvent(input, 'input');
            testing_1.tick();
            fixture.detectChanges();
            util_1.dispatchEvent(form, 'submit');
            testing_1.tick();
            testing_1.expect(fakeConsole.logs).toContain('you submitted value: XYZ');
        });
    })));
});
