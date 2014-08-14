# -*- encoding: utf-8 -*-
##############################################################################
#
#    FreeSWITCH Click2dial module for OpenERP
#    Copyright (C) 2010-2014 Alexis de Lattre <alexis@via.ecp.fr>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################


{
    'name': 'FreeSWITCH Click2dial',
    'version': '0.4',
    'category': 'Phone',
    'license': 'AGPL-3',
    'summary': 'FreeSWITCH-OpenERP connector',
    'description': """This module adds 3 functionalities :

1) It adds a 'dial' button in the partner form view so that users can directly dial a phone number through FreeSWITCH. This feature is usually known as 'click2dial'. Here is how it works :
. In OpenERP, the user clicks on the 'dial' button next to a phone number field in the partner view.
. OpenERP connects to the FreeSWITCH Manager Interface and FreeSWITCH makes the user's phone ring.
. The user answers his own phone (if he doesn't, the process stops here).
. FreeSWITCH dials the phone number found in OpenERP in place of the user.
. If the remote party answers, the user can talk to his correspondent.

2) It adds the ability to show the name of the calling party on the screen of your IP phone on incoming phone calls if the presented
phone number is present in the partner/leads/employees/... of OpenERP. Here is how it works :
. On incoming phone calls, the FreeSWITCH dialplan executes an AGI script "set_name_incoming_timeout.sh".
. The "set_name_incoming_timeout.sh" script calls the "set_name_agi.py" script with a short timeout.
. The "set_name_agi.py" script will make an XML-RPC request on the OpenERP server to try to find the name of the person corresponding to the phone number presented by the calling party.
. If it finds the name, it is set as the CallerID name of the call, so as to be presented on the IP phone of the user.
It also works on outgoing calls, so as to display the name of the callee on the SIP phone of the caller. For that, you should use the script "set_name_outgoing_timeout.sh".

3) It adds a button "Open calling partner" in the menu "Sales > Address book" to get the partner corresponding to the calling party in one click. Here is how it works :
. When the user clicks on the "Open calling partner" button, OpenERP sends a query to the FreeSWITCH Manager Interface to get a list of the current phone calls
. If it finds a phone call involving the user's phone, it gets the phone number of the calling party
. It searches the phone number of the calling party in the Partners of OpenERP. If a record matches, it shows the name of the related Partner and proposes to open it, or open its related sale orders or invoices. If no record matches, it proposes to create a new Contact with the presented phone number as 'Phone' or 'Mobile' number or update an existing Contact.
It is possible to get a pop-up of the partner corresponding to the calling party without any action from the user via the module *freeswitch_popup*.

A detailed documentation for this module is available on the Akretion Web site : http://www.akretion.com/en/products-and-services/openerp-freeswitch-voip-connector """,
    'author': 'Akretion',
    'website': 'http://www.akretion.com/',
    'depends': ['base_phone'],
    'external_dependencies': {'python': ['phonenumbers', 'ESL']},
    'data': [
        'freeswitch_server_view.xml',
        'res_users_view.xml',
        'res_partner_view.xml',
        'wizard/open_calling_partner_view.xml',
        'security/ir.model.access.csv',
        ],
    'demo': ['freeswitch_click2dial_demo.xml'],
    'images': [
        'images/sshot-click2dial.jpg',
        'images/sshot-open_calling_party.jpg',
        ],
    'application': True,
    'installable': True,
    'active': False,
}