# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version
import frappe
import json
from PyPDF2 import PdfFileWriter
from frappe.utils.print_format import read_multi_pdf
from frappe.utils.print_format import download_pdf


@frappe.whitelist()
def download_multi_pdf(docnames):
    docnames = json.loads(docnames)
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


@frappe.whitelist()
def set_asset_cost_center(doc, method):
    for asset in doc.assets:
        if asset.cost_center:
            if frappe.db.exists("Asset", asset.asset):
                asset_doc = frappe.get_doc("Asset", asset.asset)
                if asset.cost_center != asset_doc.cost_center:
                    asset_doc.db_set("cost_center", asset.cost_center)
                    for row in asset_doc.schedules:
                        if row.journal_entry:
                            jv = frappe.get_doc('Journal Entry', row.journal_entry)
                            for account in jv.accounts:
                                account.db_set('cost_center', asset.cost_center)
                    frappe.db.commit()

@frappe.whitelist()
def reset_asset_cost_center(doc, method):
    for asset in doc.assets:
        if asset.cost_center:
            if frappe.db.exists("Asset", asset.asset):
                prev_cost_center = frappe.db.set_value("Asset", asset.asset, "cost_center", asset.source_cost_center)
                frappe.db.commit()
