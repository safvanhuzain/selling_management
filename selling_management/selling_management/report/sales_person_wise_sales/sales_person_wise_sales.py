import frappe
from erpnext.selling.report.item_wise_sales_history.item_wise_sales_history import \
    execute as item_wise_sales_history
from frappe import _


def execute(filters=None):
	columns, data, null, chart_data = item_wise_sales_history(filters)
	columns.extend(
		[
			{
				"label": _("Sales Person"),
				"fieldname": "sales_person",
				"fieldtype": "Link",
				"options": "Sales Person",
				"width": 120,
				"hidden": 1
			},
		]
	)
	for d in data:
		d["sales_person"] = frappe.db.get_value('Sales Order', d['sales_order'], 'sales_person')

	return columns, data, null, chart_data