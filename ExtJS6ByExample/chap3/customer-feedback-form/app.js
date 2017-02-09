Ext.application({
    name: 'MyApp',
    /*
     * ExtJS calls `launch` after page loaded.
     */
    launch: function(){ 
        // we place all components in Viewport. This is a specialized container
        // that represents the browser's application  view area.
        Ext.create('Ext.container.Viewport', {
            scrollable: true, // Instead of true or false, can also take x or y as value
                              // to enable only horizontal or vertical scroll
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
                            xtype: 'form',
                            bodyPadding: 20,
                            maxWidth: 700,
                            // set flex to make the form panel to fill the parent container's
                            // with and at the same time we're limiting the max with of the form
                            flex: 1,
                            title: 'Customer Feedback',
                            items: [
                                {
                                    xtype: 'fieldcontainer',
                                    // Here field container is used with hbox layout to put
                                    // both the first name and last name under a sinle label
                                    layout: 'hbox',
                                    fieldLabel: 'Name',
                                    combineErrors: true,

                                    // By setting defaultType at the container level we can
                                    // avoid repeating xtype for the child components of this
                                    // container. So by default all child which doesn't set
                                    // xtype will default to textfield
                                    defaultType: 'textfield',

                                    // The defaults config allows you to set any config which
                                    // will be set as default for all the child componets.
                                    defaults: {
                                        allowBlank: false, // make as required fields
                                        flex: 1 // make child components' with equal to the container's width
                                    },
                                    items: [
                                        {
                                            name: 'firstName',
                                            emptyText: 'First Name'
                                        },
                                        {
                                            name: 'lastName',
                                            margin: '0 0 0 5',
                                            emptyText: 'Last Name'
                                        }
                                    ]
                                },
                                {
                                    xtype: 'datefield',
                                    fieldLabel: 'Date of Birth',
                                    name: 'dob',
                                    maxValue: new Date() // Prevent entering the future date
                                },
                                {
                                    fieldLabel: 'Email Address',
                                    name: 'email', vtype: 'email',
                                    allowBlank: false
                                },
                                {
                                    fieldLabel: 'Phone Number',
                                    labelWidth: 100,
                                    name: 'phone',
                                    width: 200,
                                    emptyText: 'xxx-xxx-xxxx',
                                    maskRe: /[\d\-]/, // available input chars
                                    regex: /^\d{3}-\d{3}-\d{4}$/, // valid input format
                                    regexText: 'The format must be xxx-xxx-xxxx'
                                },
                                {
                                    xtype: 'numberfield',
                                    name: 'productsPurchased',
                                    fieldLabel: 'How many times have you purchased our products?',
                                    value: 0,
                                    maxValue: 100,
                                    minValue: 0
                                },
                                {
                                    xtype: 'radiogroup',
                                    fieldLabel: 'How satisfied with our service?',
                                    vertical: true,
                                    columns: 1,
                                    items: [
                                        {
                                            boxLabel: 'Very satisfied',
                                            name: 'rb',
                                            inputValue: '1'
                                        },
                                        {
                                            boxLabel: 'satisfied',
                                            name: 'rb',
                                            inputValue: '2'
                                        },
                                        {
                                            boxLabel: "Didn't care",
                                            name: 'rb',
                                            inputValue: '3'
                                        },
                                        {
                                            boxLabel: 'Dissatisfied',
                                            name: 'rb',
                                            inputValue: '4'
                                        },
                                        {
                                            boxLabel: 'Very dissatisfied',
                                            name: 'rb',
                                            inputValue: '5'
                                        }
                                    ]
                                },
                                {
                                    xtype: 'checkboxgroup',
                                    fieldLabel: 'Which of these words would you use to describe our products? Select all that apply',
                                    vertical: true,
                                    columns: 1,
                                    items: [
                                        {
                                            boxLabel: 'Reliable',
                                            name: 'ch',
                                            inputValue: '1'
                                        },
                                        {
                                            boxLabel: 'High quality',
                                            name: 'ch',
                                            inputValue: '2'
                                        },
                                        {
                                            boxLabel: 'Good value for money',
                                            name: 'ch',
                                            inputValue: '3'
                                        },
                                        {
                                            boxLabel: 'Overpriced',
                                            name: 'ch',
                                            inputValue: '4'
                                        },
                                        {
                                            boxLabel: 'Poor quality',
                                            name: 'ch',
                                            inputValue: '5'
                                        }
                                    ]
                                },
                                {
                                    xtype: 'radiogroup',
                                    fieldLabel: 'How likely is it that you would recommend this company to a friend or colleague?',
                                    vertical: false,
                                    defaults: {
                                        padding: 20
                                    },
                                    items: [
                                        {
                                            boxLabel: '1',
                                            name: 'recommend',
                                            inputValue: '1'
                                        },
                                        {
                                            boxLabel: '2',
                                            name: 'recommend',
                                            inputValue: '2'
                                        },
                                        {
                                            boxLabel: '3',
                                            name: 'recommend',
                                            inputValue: '3'
                                        },
                                        {
                                            boxLabel: '4',
                                            name: 'recommend',
                                            inputValue: '4'
                                        },
                                        {
                                            boxLabel: '5',
                                            name: 'recommend',
                                            inputValue: '5'
                                        }
                                    ]
                                },
                                {
                                    xtype: 'textareafield',
                                    fieldLabel: 'Comments',
                                    labelAlign: 'top',
                                    name: 'comments',
                                    width: 400,
                                    height: 100
                                }
                            ],
                            buttons: [
                                {
                                    text: 'Submit',
                                    handler: function(){
                                        var form = this.up('form').getForm();
                                        if (form.isValid()){
                                            form.submit({
                                                url: 'customer/feedback',
                                                success: function(){
                                                },
                                                failure: function(){
                                                }
                                            });
                                        } else {
                                            Ext.Msg.alert('Error', 'Fix the erros in the form');
                                        }
                                    }
                                }
                            ]
                        }
                    ]
                }
            ]
        });
    }
});
