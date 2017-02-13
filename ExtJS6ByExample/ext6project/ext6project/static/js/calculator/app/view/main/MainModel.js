/*
 * This ViewModel has just one property display. This is used to bind the
 * display value of the calculator. Here, we will not create a model
 * separately with a set of fields
 */
Ext.define('Calc.view.main.MainModel', {
    extend: 'Ext.app.ViewModel',
    alias: 'viewmodel.main',
    data: {
        display: 0.0
    }
});
