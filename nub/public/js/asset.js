frappe.ui.form.on("Asset", {
  barcode_serial_number(frm) {
    let barcode_value = $("input[data-fieldname='barcode_serial_number']").val()
    frm.set_value("barcode", barcode_value)
    frm.refresh_field("barcode")
  }
});
