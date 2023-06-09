from . import __version__ as app_version

app_name = "show_session"
app_title = "Show Session"
app_publisher = "almad.alaaa@proton.me"
app_description = "Show Default Session in navbar"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "almad.alaaa@proton.me"
app_license = "Apache License Version 2.0"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/show_session/css/show_session.css"
app_include_js = f"/assets/{app_name}/js/desk_navbar.js"

# include js, css files in header of web template
# web_include_css = "/assets/show_session/css/show_session.css"
web_include_js = f"/assets/{app_name}/js/set_first_login.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "show_session/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

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

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "show_session.install.before_install"
# after_install = "show_session.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "show_session.uninstall.before_uninstall"
# after_uninstall = "show_session.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "show_session.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
	"Session Default Settings": {
		"validate": f"{app_name}.utils.validate_one_in_navbar",
	}
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"show_session.tasks.all"
#	],
#	"daily": [
#		"show_session.tasks.daily"
#	],
#	"hourly": [
#		"show_session.tasks.hourly"
#	],
#	"weekly": [
#		"show_session.tasks.weekly"
#	]
#	"monthly": [
#		"show_session.tasks.monthly"
#	]
# }

# Testing
# -------

# before_tests = "show_session.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "show_session.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "show_session.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Request Events
# ----------------
# before_request = ["show_session.utils.before_request"]
# after_request = ["show_session.utils.after_request"]

# Job Events
# ----------
# before_job = ["show_session.utils.before_job"]
# after_job = ["show_session.utils.after_job"]

# User Data Protection
# --------------------

user_data_fields = [
	{
		"doctype": "{doctype_1}",
		"filter_by": "{filter_by}",
		"redact_fields": ["{field_1}", "{field_2}"],
		"partial": 1,
	},
	{
		"doctype": "{doctype_2}",
		"filter_by": "{filter_by}",
		"partial": 1,
	},
	{
		"doctype": "{doctype_3}",
		"strict": False,
	},
	{
		"doctype": "{doctype_4}"
	}
]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"show_session.auth.validate"
# ]

fixtures = [{
		"dt": "Custom Field",
		"filters": [{
			"name": ["in", [
				"Session Default-show_dialog",
				"Session Default-show_in_navbar",
			]],
		}],
	},
]


boot_session = f"{app_name}.utils.boot_session"
