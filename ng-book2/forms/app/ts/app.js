"use strict";
var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (this && this.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};
var core_1 = require('@angular/core');
var platform_browser_dynamic_1 = require('@angular/platform-browser-dynamic');
var forms_1 = require('@angular/forms');
require('../css/styles.css');
require('../css/semantic.min.css');
require('../images/ng-book-2-minibook.png');
require('../images/favicon-32x32.png');
require('../images/favicon.ico');
var demo_form_sku_1 = require('./forms/demo_form_sku');
var demo_form_sku_with_builder_1 = require('./forms/demo_form_sku_with_builder');
var demo_form_with_validations_shorthand_1 = require('./forms/demo_form_with_validations_shorthand');
var demo_form_with_validations_explicit_1 = require('./forms/demo_form_with_validations_explicit');
var demo_form_with_custom_validations_1 = require('./forms/demo_form_with_custom_validations');
var demo_form_with_events_1 = require('./forms/demo_form_with_events');
var demo_form_ng_model_1 = require('./forms/demo_form_ng_model');
var FormsDemoApp = (function () {
    function FormsDemoApp() {
    }
    FormsDemoApp = __decorate([
        core_1.Component({
            selector: 'forms-demo-app',
            directives: [demo_form_sku_1.DemoFormSku,
                demo_form_sku_with_builder_1.DemoFormSkuBuilder,
                demo_form_with_validations_shorthand_1.DemoFormWithValidationsShorthand,
                demo_form_with_validations_explicit_1.DemoFormWithValidationsExplicit,
                demo_form_with_custom_validations_1.DemoFormWithCustomValidations,
                demo_form_with_events_1.DemoFormWithEvents,
                demo_form_ng_model_1.DemoFormNgModel
            ],
            template: "\n<div>\n  <demo-form-ng-model></demo-form-ng-model>\n  <demo-form-with-events></demo-form-with-events>\n  <demo-form-with-custom-validations></demo-form-with-custom-validations>\n  <demo-form-with-validations-shorthand></demo-form-with-validations-shorthand>\n  <demo-form-with-validations-explicit></demo-form-with-validations-explicit>\n  <demo-form-sku-builder></demo-form-sku-builder>\n  <demo-form-sku></demo-form-sku>\n</div>\n  "
        }), 
        __metadata('design:paramtypes', [])
    ], FormsDemoApp);
    return FormsDemoApp;
}());
platform_browser_dynamic_1.bootstrap(FormsDemoApp, [
    forms_1.disableDeprecatedForms(),
    forms_1.provideForms()
])
    .catch(function (err) { return console.error(err); });
