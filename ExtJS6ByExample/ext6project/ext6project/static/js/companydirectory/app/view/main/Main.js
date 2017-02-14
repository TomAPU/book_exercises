Ext.define('CD.view.main.Main', {
    extend: 'Ext.panel.Panel',

    requires: [
        'CD.view.contactlist.ContactList'
    ],
    autoScroll: true,
    xtype: 'app-main',
    // cls: 'main',
    
    items: [
        {
            xtype: 'container',
            layout: {
                type: 'hbox',
                align: 'center',
                pack: 'center'
            },
            items: [
                {
                    xtype: 'container',
                    layout: 'vbox',
                    width: '100%',
                    items: [
                        {
                            html: '<h1 class="header">Hello world</h1>',
                            width: '100%'
                        },
                        {
                            xtype: 'app-contactlist',
                            width: '100%',
                            height: '100%'
                        }
                    ]
                }
            ]
        }
    ]
});
