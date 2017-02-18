Ext.define('Contact', {
    extend: 'Ext.data.Model',
    fields: ['first_name', 'last_name', 'email', 'address','city', 'state','phone','work_type']
});

Ext.define('CD.store.ContactList', {
    extend: 'Ext.data.Store',
    storeId: 'contactList',
    model: 'Contact',
    pageSize: 5,
proxy: {
        type: 'rest',
        url: '/companydirectory/employees/', // url that will load data with respect to start and limit params
        reader: {
            type: 'json',
            rootProperty: 'results',
            totalProperty: 'total'
        }
    }
});

Ext.create('CD.store.ContactList').load();
