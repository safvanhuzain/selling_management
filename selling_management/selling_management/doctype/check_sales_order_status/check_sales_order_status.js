// Copyright (c) 2023, safvan and contributors
// For license information, please see license.txt

frappe.ui.form.on('Check Sales Order Status', {
	refresh(frm){
		frm.set_df_property("order_status", "hidden", 1);
	},
	upload: function(frm) {
		frm.set_df_property("order_status", "hidden", 0);
		frm.call({
			method: "read_file",
			doc: frm.doc,
			callback: function (r){
				var table = document.getElementById("myTable");
				r.message.data.forEach(element =>{
						var row = table.insertRow(-1);
                        var cell1 = row.insertCell(0);
                        var cell2 = row.insertCell(1);
                        var cell3 = row.insertCell(2);
                        cell1.innerHTML = `<a href="javascript:frappe.set_route('Form', 'Sales Invoice', '${element.name}')">` + element.name +"</b>";
                        cell2.innerHTML = element.status
                        cell3.innerHTML = element.grand_total
				})
			}
		})
	},
	get_template(frm) {
		window.location.href = repl(frappe.request.url +
			'?cmd=%(cmd)s', {
			cmd: "selling_management.selling_management.doctype.check_sales_order_status.check_sales_order_status.get_template",
		});
	},
});
