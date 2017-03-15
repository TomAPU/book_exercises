"use strict";
var dom_adapter_1 = require('@angular/platform-browser/src/dom/dom_adapter');
function dispatchEvent(element, eventType) {
    dom_adapter_1.getDOM().dispatchEvent(element, dom_adapter_1.getDOM().createEvent(eventType));
}
exports.dispatchEvent = dispatchEvent;
var ConsoleSpy = (function () {
    function ConsoleSpy() {
        this.logs = [];
    }
    ConsoleSpy.prototype.log = function () {
        var args = [];
        for (var _i = 0; _i < arguments.length; _i++) {
            args[_i - 0] = arguments[_i];
        }
        this.logs.push(args.join(' '));
    };
    ConsoleSpy.prototype.warn = function () {
        var args = [];
        for (var _i = 0; _i < arguments.length; _i++) {
            args[_i - 0] = arguments[_i];
        }
        this.log.apply(this, args);
    };
    return ConsoleSpy;
}());
exports.ConsoleSpy = ConsoleSpy;
