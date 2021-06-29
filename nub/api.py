# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version
import frappe
import json
from PyPDF2 import PdfFileWriter
from frappe.utils.print_format import read_multi_pdf
from frappe.utils.print_format import download_pdf



def check_asset_barcode(doc, method):
    # if doc.barcode_serial_number and doc.barcode_serial_number != '':
    #     doc.db_set('is_available', 1)
    doc.barcode_serial_number = doc.barcode
    frappe.db.set_value(doc.doctype, doc.name,
                        "barcode_serial_number", doc.barcode)
    frappe.db.commit()


@frappe.whitelist()
def download_multi_pdf(docnames):
    docnames = json.loads(docnames)
    print_list = []
    new_doc = frappe.new_doc("Asset Printer")
    print_settings = frappe.get_doc('Print Settings', 'Print Settings')
    allow_print_for_draft = print_settings.allow_print_for_draft
    allow_print_for_cancelled = print_settings.allow_print_for_cancelled
    for doc in docnames:
        if frappe.db.exists("Asset", doc):
            asset = frappe.get_doc("Asset", doc)
            if asset.docstatus == 0 and allow_print_for_draft == 1 and asset.barcode:
                new_doc.append('asset_printer_table', {
                    'asset_name':asset.asset_name,
                    'barcode':asset.barcode
                })
            if asset.docstatus == 1 and asset.barcode:
                new_doc.append('asset_printer_table',{
                    'asset_name':asset.asset_name,
                    'barcode':asset.barcode
                })
            if asset.docstatus == 2 and allow_print_for_cancelled == 1 and asset.barcode:
                new_doc.append('asset_printer_table',{
                    'asset_name':asset.asset_name,
                    'barcode':asset.barcode
                })

    new_doc.save()
    frappe.db.commit()
    return {'name': new_doc.name}