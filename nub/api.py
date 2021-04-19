# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version
import frappe

def check_asset_barcode(doc, method):
    if doc.barcode_serial_number and doc.barcode_serial_number != '':
        doc.db_set('is_available', 1)
    doc.barcode_serial_number = doc.barcode
    frappe.db.set_value(doc.doctype, doc.name, "barcode_serial_number", doc.barcode)
    frappe.db.commit()
