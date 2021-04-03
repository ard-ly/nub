# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "nub"
app_title = "Nub"
app_publisher = "Anvil Team"
app_description = "Al-Nuran Bank Customization"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "support@anvilerp.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/nub/css/nub.css"
# app_include_js = "/assets/nub/js/nub.js"

# include js, css files in header of web template
# web_include_css = "/assets/nub/css/nub.css"
# web_include_js = "/assets/nub/js/nub.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "nub.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "nub.install.before_install"
# after_install = "nub.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "nub.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

doc_events = {
	"Asset": {
		"on_update_after_submit": "nub.api.check_asset_barcode",
		"on_update": "nub.api.check_asset_barcode"
	}
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"nub.tasks.all"
# 	],
# 	"daily": [
# 		"nub.tasks.daily"
# 	],
# 	"hourly": [
# 		"nub.tasks.hourly"
# 	],
# 	"weekly": [
# 		"nub.tasks.weekly"
# 	]
# 	"monthly": [
# 		"nub.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "nub.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "nub.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "nub.task.get_dashboard_data"
# }

fixtures = [
    {
        "dt": "Custom Field",
        "filters": [
            [
                "name",
                "in",
                [
                    "Asset-is_available",
                    "Asset-asset_barcode",
                ]
            ]
        ]
    }
]