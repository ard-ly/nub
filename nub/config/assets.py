from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": _("Reports"),
			"icon": "fa fa-table",
			"items": [
				{
					"type": "report",
					"name": "NUB Asset",
					"label": "Al-Nuran Bank Asset",
					"doctype": "Asset",
					"is_query_report": True,
					"dependencies": ["Asset"],
				},
				{
					"type": "doctype",
					"name": "Assets Submission Report",
					"onboard": 1,
				}
			]
		}
	]
