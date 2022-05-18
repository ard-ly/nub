import frappe

def boot_session(bootinfo):
    ignore_fraction = frappe.get_system_settings('overwrite_currency_fraction') or 0
    bootinfo.update({
        'ignore_fraction': ignore_fraction
    })