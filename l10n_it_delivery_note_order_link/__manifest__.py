# Copyright 2014-2019 Dinamiche Aziendali srl (http://www.dinamicheaziendali.it/)
# @author: Andrea Piovesana <andrea.m.piovesana@gmail.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

# noinspection PyStatementEffect
{
    'name': 'ITA - Documento di Trasporto link from purchase order',
    'summary': 'Delivery Note link from purchase order',
    'author': 'Openindustry.it Sas',
    'website': 'https://openindustry.it/',
    'version': '12.0.1.0.0',
    'category': 'Localization',
    'depends': [
        'purchase_stock',
        'sale_stock',
        'l10n_it_delivery_note',
    ],
    'data': [
        'views/purchase_order.xml',
        'views/sale_order.xml',
    ],
}
