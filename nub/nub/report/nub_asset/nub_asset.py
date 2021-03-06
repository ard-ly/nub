# Copyright (c) 2013, Anvil Team and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _


def execute(filters=None):
	columns, data = get_columns(), get_data(filters)
	return columns, data


def get_data(filters):
	conds = get_conditions(filters)
	result = frappe.db.sql("""
		SELECT name as asset_id, asset_name, asset_category, location, is_available, barcode
		FROM `tabAsset` 
		{}
	""".format(conds))
	if filters.get('barcode', False):
		if result:
			print(len(result[0]))
			if len(result[0])==6:
				if result[0][5] == filters.get('barcode', False):
					if result[0][4] == 0:
						doc = frappe.get_doc("Asset",result[0][0])
						doc.db_set('is_available', 1)
						row = list(result[0])
						row[4] = 1
						x = []
						x.append(tuple(row))
						result = tuple(x)
						frappe.db.commit()
	return result


def get_columns():
	return [
		{
			"label": _('Asset'),
			"options": 'Asset',
			"fieldname": "asset_id",
			"fieldtype": "Link",
			"width": 140
		},
		{
			'fieldname': "asset_name",
			'label': _("Asset Name"),
			'fieldtype': "Data",
			'width': 200
		},
		{
			'fieldname': "asset_category",
			'label': _("Asset Category"),
			'fieldtype': "Link",
			'options': "Asset Category",
			'width': 200
		},
		{
			'fieldname': "location",
			'label': _("Location"),
			'fieldtype': "Link",
			'options': "Location",
			'width': 200
		},
		{
			'fieldname': "is_available",
			'label': _("Asset Status"),
			'fieldtype': "Check",
			'width': 200
		},
		{
			'fieldname': "barcode",
			'label': _("barcode"),
			'fieldtype': "data",
			'width': 200
		}
		
	]


def get_conditions(filters):
	conds = []
	if filters.get('company', False):
		conds.append(" company='{}' ".format(filters.get('company')))
	
	if filters.get('asset_name', False):
		conds.append(" asset_name LIKE '%{}%' ".format(filters.get('asset_name')))
	
	if filters.get('asset_category', False):
		conds.append(" asset_category='{}' ".format(filters.get('asset_category')))
	
	if filters.get('location', False):
		conds.append(" location='{}' ".format(filters.get('location')))
	
	is_available = filters.get('available', False)
	if is_available:
		is_available = 1 if is_available=='Yes' else 0
		conds.append(" is_available={}".format(is_available))
	
	if filters.get('barcode', False):
		conds.append(" barcode = '{}' ".format(filters.get('barcode')))

	if filters.get('from_date', False):
		conds.append(" creation >= '{}' ".format(filters.get('from_date')))
	
	if filters.get('to_date', False):
		conds.append(" creation <= '{}' ".format(filters.get('to_date')))
	
	if conds:
		return " WHERE {}".format(" AND ".join(conds))
	return ""
