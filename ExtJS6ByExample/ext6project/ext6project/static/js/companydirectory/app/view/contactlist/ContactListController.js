Ext.define('CD.view.contactlist.ContactListController', {
    extend: 'Ext.app.ViewController',
    alias: 'controller.contactlist',
    views: ['CD.view.contactlist.ContactList', 'CD.view.contactlist.Add'],
    requires: ['CD.store.ContactList', 'CD.view.contactlist.Add'],
    // stores: ['newstore'],
    init: function(){
        var me = this;
    },
    onSave: function() {
        Ext.get('contactList').save();
    },
    onSelectionChange: function(){
        this.lookupReference('btnRemoveContact').enable();
    },
    onRemove: function(){
        var grid = this.lookupReference('contactListGrid');
        var sm = grid.getSelectionModel();
        grid.plugins[0].cancelEdit();
        grid.getStore().remove(sm.getSelection());
        if(grid.getStore().getCount()>0){
            sm.select(0);
        }
    },
    onCreate: function(){
        var grid = this.lookupReference('contactListGrid');
        grid.plugins[0].cancelEdit();

        var r = Ext.create('Contact');
        grid.getStore().insert(0, r);
        grid.plugins[0].startEdit(0, 0);
        
//        var win = Ext.create('CD.view.ContactList.Add').show().getEl()
//        .alignTo(Ext.getBody(), 'tr-tr', [0, -40]);
//        Ext.EventManager.onWindowResize(function(w, h){
//            if(win)
//            {
//                win.alignTo(Ext.getBody(), 'tr-tr', [0, -40]);
//            }
//        });

    }
});
