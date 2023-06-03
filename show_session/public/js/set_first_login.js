// Copyright (c) 2023, Fintechsys and contributors
// For license information, please see license.txt


frappe.provide('frappe.session.user');


$(document).ready(function() {
	if (frappe.session.user == "Guest"){
		localStorage._show_session_first_login = true;
	}
});
