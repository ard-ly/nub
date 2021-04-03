# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version
import frappe

def check_asset_barcode(doc, method):
    if doc.asset_barcode and doc.asset_barcode != '':
        doc.db_set('is_available', 1)
        frappe.db.commit()