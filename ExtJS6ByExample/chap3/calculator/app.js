// we simply create the Main view and show it as a floating, movable window
Ext.application({
    name: 'Calc',
    launch: function(){
        Ext.create('Calc.view.main.Main').show();
    }
});
