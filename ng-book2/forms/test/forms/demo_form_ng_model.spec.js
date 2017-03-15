"use strict";
var testing_1 = require('@angular/core/testing');
var forms_1 = require('@angular/forms');
var testing_2 = require('@angular/core/testing');
var demo_form_ng_model_1 = require('../../app/ts/forms/demo_form_ng_model');
testing_1.describe('DemoFormNgModel', function () {
    beforeEach(function () {
        testing_1.addProviders([
            forms_1.disableDeprecatedForms(),
            forms_1.provideForms(),
            forms_1.FormBuilder
        ]);
    });
    testing_1.it('requires product name', testing_1.async(testing_1.inject([testing_2.TestComponentBuilder], function (tcb) {
        return tcb.createAsync(demo_form_ng_model_1.DemoFormNgModel)
            .then(function (fixture) {
            var comp = fixture.debugElement.componentInstance;
            var el = fixture.debugElement.nativeElement;
            comp.productName = '';
            fixture.detectChanges();
            expect(el.querySelector('.ui.error.message').innerHTML)
                .toContain('Form is invalid');
            comp.productName = 'something';
            fixture.detectChanges();
            expect(el.querySelector('.ui.error.message')).toBeNull();
        });
    })));
});
