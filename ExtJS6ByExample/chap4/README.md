Ext.Loader.setConfig({
    enabled : true,
    paths   : {
        DT : "http://servername/path/to/js/folder/extjs-4.1.1/apps/dt"
    } 
});


Ext.application({
	name: 'DT',
	appFolder: 'app',
	
	requires: ['DT.view.user.List'],
	
	launch: function(){
		console.log('application started');	
		Ext.create("Ext.container.Viewport", {
			layout: "fit",
			items: [
				{
					xtype: 'userlist'
				}
			]
		});
	}
});
