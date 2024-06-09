# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

{
	'name': "Product cooperator On Invoice/Vendor Bill Line",
	'version': "15.0.0.0",
	'category': "Accounting",
	'license':'OPL-1',
	'summary': "Display product cooperator on invoice line print product cooperator on invoice report print cooperator on invoice line product cooperator print product cooperator on invoice line product cooperator in invoice line print Product cooperator on vendor bill line",
	'description': """
						
			Display product cooperator on invoice/vendor bill line. It will also display product cooperator on invoice/vendor bill report. 
			
			Product cooperator On Invoice/Vendor Bill Line in odoo,
			Invoice/Vendor bill report with product cooperator in odoo,
			Product cooperator on invoice/vendor bill line and invoice/vendor bill report in odoo,
			Identify product via cooperator in odoo,
			Identify priduct via cooperator on invoice/vendor bill report in odoo,

	""",
	'author': "Fall Lewis YOMBA",
    'depends': ['base', 'account'],
	'data': [
			'report/invoice_report.xml',
			'views/view_invoice.xml',
			],
	'installable': True,
	'auto_install': False,
	'application': False,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
