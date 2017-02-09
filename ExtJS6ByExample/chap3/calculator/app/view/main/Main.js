/* We will create one single view for this calculator application called Main.
 * This view contains all the buttons, the display field, and so on.
 * Events are associated with the methods of this controller.
 */

Ext.define('Calc.view.main.Main', {
    extend: 'Ext.window.Window',
    /* Marks these are required classes to be loaded before
     * loading this view */
    requires: [
        'Calc.view.main.MainController', // -> app/view/main/MainController.js
        'Calc.view.main.MainModel' // -> app/view/main/MainModel.js
    ],
    xtype: 'app-main',
    controller: 'main', // now we can use handlers defined in `controller.main` in this view

    // View model of the view
    viewModel: { type: 'main' }, // -> now we can use the data defined in `viewmodel.main`
    resizable: false,
    layout: {
        type: 'table',
        columns: 4
    },

    /* Defaults properties to be used for the child items. Any child can override it */
    defaultType: 'button',
    defaults: {
        width: 50,
        height: 50,
        cls: 'btn', // custom css class
        handler: 'onClickNumber' // handler from `controller.main`
    },
    /* we're using the header config of the Ext.window.Window to
     * display the result in the calculator. Using this header we can
     * move the floating calculator around within the browser
     */
    header: {
        items: [
            {
                xtype: 'displayfield',
                colspan: 4,
                width: 200,
                cls: 'display',
                bind: { value: '{display}'}, // value from it's ViewModel
                height: 60,
                padding: 0
            }
        ]
    },
    items: [
        {
            text: 'C',
            colspan: 2,
            width: 100,
            cls: 'btn-green',
            handler: 'onClickClear'
        },
        {
            text: '+/-',
            cls: 'btn-green',
            handler: 'onClickChangeSign'
        },
        {
            text: '&divide;',
            cls: 'btn-orange',
            handler: 'onClickOp'
        },
        { text: '7' },
        { text: '8' },
        { text: '9' },
        {
            text: '&times;',
            cls: 'btn-orange',
            handler: 'onClickOp'
        },
        { text: '4' },
        { text: '5' },
        { text: '6' },
        {
            text: '-',
            cls: 'btn-orange',
            handler: 'onClickOp'
        },
        { text: '1' },
        { text: '2' },
        { text: '3' },
        {
            text: '+',
            cls: 'btn-orange',
            handler: 'onClickOp'
        },
        {
            text: '0',
            width: 100,
            colspan: 2
        },
        {
            text: '.',
            handler: 'onClickDot'
        },
        {
            text: '=',
            cls: 'btn-orange',
            handler: 'onClickOp'
        }
    ]
});
