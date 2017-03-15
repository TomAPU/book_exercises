"use strict";
var testing_1 = require('@angular/core/testing');
var testing_2 = require('@angular/core/testing');
var forms_1 = require('@angular/forms');
var by_1 = require('@angular/platform-browser/src/dom/debug/by');
var demo_form_with_events_1 = require('../../app/ts/forms/demo_form_with_events');
var util_1 = require('../util');
testing_1.describe('DemoFormWithEvents (bad)', function () {
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
    testing_1.it('validates and triggers events', testing_1.inject([testing_2.TestComponentBuilder], testing_1.fakeAsync(function (tcb) {
        tcb.createAsync(demo_form_with_events_1.DemoFormWithEvents)
            .then(function (fixture) {
            var el = fixture.debugElement.nativeElement;
            var input = fixture.debugElement.query(by_1.By.css('input')).nativeElement;
            var form = fixture.debugElement.query(by_1.By.css('form')).nativeElement;
            fixture.detectChanges();
            input.value = '';
            util_1.dispatchEvent(input, 'input');
            fixture.detectChanges();
            testing_1.tick();
            var msgs = el.querySelectorAll('.ui.error.message');
            testing_1.expect(msgs[0].innerHTML).toContain('SKU is invalid');
            testing_1.expect(msgs[1].innerHTML).toContain('SKU is required');
            input.value = 'XYZ';
            util_1.dispatchEvent(input, 'input');
            fixture.detectChanges();
            testing_1.tick();
            msgs = el.querySelectorAll('.ui.error.message');
            testing_1.expect(msgs.length).toEqual(0);
            fixture.detectChanges();
            util_1.dispatchEvent(form, 'submit');
            testing_1.tick();
            testing_1.expect(fakeConsole.logs).toContain('you submitted value: XYZ');
        });
    })));
});
