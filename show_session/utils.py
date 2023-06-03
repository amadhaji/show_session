
import frappe
from frappe import _


def validate_one_in_navbar(doc, method=None):
	exist = list(filter(lambda i: i.get("show_in_navbar"), doc.session_defaults))
	if len(exist) > 1:
		frappe.throw(_("Only one session default is allowed to be shown in navbar"))


def boot_session(boot_info):
	doc = frappe.get_single("Session Default Settings")
	show_in_navbar = [
		{"doctype": i.get("ref_doctype"), "show_dialog": i.get("show_dialog")}
		for i in filter(lambda i: i.get("show_in_navbar"), doc.session_defaults)
	]

	if show_in_navbar:
		boot_info.show_session_in_navbar_doctype = show_in_navbar[0]["doctype"]
		boot_info.show_session_dialog = frappe.scrub(show_in_navbar[0]["show_dialog"])

	return boot_info
