# Copyright (c) 2023, safvan and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import cstr
from frappe.utils.csvutils import (UnicodeWriter,
                                   read_csv_content_from_attached_file)


class CheckSalesOrderStatus(Document):
	@frappe.whitelist()
	def read_file(self):
		rows = read_csv_content_from_attached_file(self)
		if not rows:
			frappe.throw(_("Please select a csv file"))
		error_row = []
		order = []
		data = []
		try:
			for i, d in enumerate(rows):
				if not i or not d:
					continue
				id=d[0]
				if frappe.db.exists('Sales Order', id):
					order.append(id)
				else:
					error_row.append(id)
			data = frappe.db.get_all('Sales Order', filters={
				'name': ['in', order]
			}, fields=['name', 'grand_total', 'status'])
			return {'data': data, 'error_row': error_row}
		except Exception:
			frappe.log_error(str(frappe.get_traceback()), "Read File")




@frappe.whitelist()
def get_template():
	w = UnicodeWriter()
	w = add_header(w)

	frappe.response["result"] = cstr(w.getvalue())
	frappe.response["type"] = "csv"
	frappe.response["doctype"] = "selling_management"


def add_header(w):
	w.writerow(
		["ID"]
	)
	return w

