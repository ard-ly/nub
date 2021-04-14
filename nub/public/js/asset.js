frappe.ui.form.on('Asset', {
	setup(frm) {
        console.log("setup");
        $( "[data-fieldname='barcode_serial_number']" ).filter(":input" ).hide()
	},
	load(frm) {
        console.log("load");

        $( "[data-fieldname='barcode_serial_number']" ).filter(":input" ).hide()
	},
    refresh(frm) {
        console.log("refresh");
        $( "[data-fieldname='barcode_serial_number']" ).filter(":input" ).hide()
	}

})