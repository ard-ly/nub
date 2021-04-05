// Copyright (c) 2016, Anvil Team and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["NUB Asset"] = {
	"filters": [
		{
			fieldname: "company",
			label: __("Company"),
			fieldtype: "Link",
			options: "Company",
			default: frappe.defaults.get_user_default("Company"),
			reqd: 1
		},
		{
			fieldname: "asset_name",
			label: __("Asset Name"),
			fieldtype: "Data"
		},
		{
			fieldname: "asset_category",
			label: __("Asset Category"),
			fieldtype: "Link",
			options: "Asset Category"
		},
		{
			fieldname: "location",
			label: __("Location"),
			fieldtype: "Link",
			options: "Location"
		},
		{
			fieldname: "from_date",
			label: __("From Date"),
			fieldtype: "Date",
			default: frappe.datetime.add_months(frappe.datetime.get_today(), -3),
		},
		{
			fieldname: "to_date",
			label: __("To Date"),
			fieldtype: "Date",
			default: frappe.datetime.get_today()
		},
		{
			fieldname: "available",
			label: __("Is Available"),
			fieldtype: "Select",
			default: '',
			options: ['', __('Yes'), __('No')]
		},
		{
			fieldname: "barcode_serial_number",
			label: __("Barcode Serial Number"),
			fieldtype: "Barcode",
		},
		
	]
};
