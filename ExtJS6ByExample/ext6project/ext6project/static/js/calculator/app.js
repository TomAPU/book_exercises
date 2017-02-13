// we simply create the Main view and show it as a floating, movable window
Ext.application({
    name: 'Calc',
    appFolder: '/static/js/calculator/app',
    launch: function(){
        Ext.Loader.setPath('Calc', '/static/js/calculator/app');
        Ext.create('Calc.view.main.Main').show();
    }
});
