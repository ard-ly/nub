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

def set_latest_cost_center_in_asset(doc, method):
    current_cost_center = ""
    cond = "1=1"

    for d in doc.assets:
        args = {"asset": d.asset, "company": doc.company}

        # latest entry corresponds to current document's cost_center when transaction date > previous dates
        # In case of cancellation it corresponds to previous latest document's cost_center
        latest_movement_entry = frappe.db.sql(
            """
            SELECT asm_item.cost_center
            FROM `tabAsset Movement Item` asm_item, `tabAsset Movement` asm
            WHERE
                asm_item.parent=asm.name and
                asm_item.asset=%(asset)s and
                asm.company=%(company)s and
                asm.docstatus=1 and {0}
            ORDER BY
                asm.transaction_date desc limit 1
            """.format(
                cond
            ),
            args,
        )
        if latest_movement_entry:
            current_cost_center = latest_movement_entry[0][0]
        
        if len(current_cost_center) <= 0: continue
        
        frappe.db.set_value("Asset", d.asset, "cost_center", current_cost_center)

        asset = frappe.get_doc('Asset', d.asset)
        # update cost center in journals
        for journal in asset.schedules:
            if journal.journal_entry:
                journal = frappe.get_doc('Journal Entry', journal.journal_entry)
                if journal.docstatus == 1:
                    for account in journal.accounts:
                        frappe.db.set_value("Journal Entry Account", account.name, "cost_center", current_cost_center)
