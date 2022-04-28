import frappe
from erpnext.assets.doctype.asset.depreciation import post_depreciation_entries

def execute():
    recreate_assets()

def recreate_assets():
    assets_to_copy = cancel_assets()
    copy_assets(assets_to_copy)
    # delete_assets(canceled_assets)

def cancel_assets():
    submitted_assets = frappe.get_list('Asset', filters={'docstatus': 1})
    assets_to_copy = []
    for asset in submitted_assets:
        asset = frappe.get_doc('Asset', asset.name)
        asset.cancel()
        assets_to_copy.append({
            'name': asset.name,
            'location': asset.location
        })
    frappe.db.commit()
    return assets_to_copy

def copy_assets(assets):
    for asset in assets:
        if asset.get('name') and asset.get('location'):
            location = asset.get('location')
            asset = frappe.get_doc('Asset', asset.get('name'))
            new_asset = frappe.copy_doc(asset)
            
            new_asset.calculate_depreciation = 1
            new_asset.location = location
            ac = frappe.get_doc('Asset Category', asset.asset_category)
            new_asset.finance_books = []
            for fb in ac.finance_books:
                new_asset.append('finance_books', {
                    'finance_book': fb.finance_book,
                    'depreciation_method': fb.depreciation_method,
                    'total_number_of_depreciations': fb.total_number_of_depreciations,
                    'frequency_of_depreciation': fb.frequency_of_depreciation,
                    'depreciation_start_date': fb.depreciation_start_date,
                    'value_after_depreciation': fb.value_after_depreciation,
                })
            new_asset.save()
            new_asset.submit()
    frappe.db.commit()
    post_depreciation_entries()

def delete_assets(assets):
    for asset in assets:
        asset = frappe.get_doc('Asset', asset.name)
        if asset.docstatus == 2:
            asset.delete()
    frappe.db.commit()
