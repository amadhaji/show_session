// Copyright (c) 2023, Fintechsys and contributors
// For license information, please see license.txt


frappe.provide('frappe._session_navbar');
frappe.provide('frappe.dom');


class SessionNavbar {
	constructor() {
		if (frappe.desk == null) {
			frappe.throw(__('Session Default can not be added outside Desk.'));
			return;
		}
		this.is_online = frappe.is_online ? frappe.is_online() : false;
		this.on_online = null;
		this.on_offline = null;
		this.refresh_interval = 60000;

		let me = this;
		$(window).on('online', function() {
			me.is_online = true;
			me.on_online && me.on_online.call(me);
			me.on_online = null;
		});
		$(window).on('offline', function() {
			me.is_online = false;
			me.on_offline && me.on_offline.call(me);
			me.on_offline = null;
		});

		this.settings = {};
		this.data = "";

		this.setup();
	}
	destroy() {
		this.clear_sync();
		if (this.$app) this.$app.remove();
		this.data = this._on_online = this._on_offline = this._syncing = null;
		this.$app = this.$body = null;
	}
	setup() {
		if (!this.is_online) {
			this.on_online = this.setup;
			return;
		}
		this.set_default_session();
		this.setup_display();
		this.sync_reload();
	}
	set_default_session() {
		let default_session = this.get_default_session();
		let show_dialog = this.get_show_dialog();

		if (localStorage._show_session_first_login) {
			localStorage.removeItem("_show_session_first_login");
			if (show_dialog == "after_login"){
				frappe.ui.toolbar.setup_session_defaults();
			}
			else if (show_dialog == "after_login_if_empty" && ! default_session){
				frappe.ui.toolbar.setup_session_defaults();
			}
		}
		if (! default_session && show_dialog == "after_refresh_if_empty"){
			frappe.ui.toolbar.setup_session_defaults();
		}
	}
	setup_display() {
		let doctype = this.get_default_session_doctype();
		let title = __(doctype);
		let session_label = __('Session Defaults');

		this.$app = $(`
			<li class="nav-item session-navbar-item" title="${title}">
				<a class="nav-link session-navbar-data text-muted"
					data-persist="true"
					href="#" onclick="return false;">
					<span class="session-navbar-text"></span>
				</a>
			</li>
			<li class="nav-item session-set_default-navbar-item" title="${session_label}">
				<a class="nav-link session-set_default-navbar"
					data-persist="true"
					href="#" onclick="return frappe.ui.toolbar.setup_session_defaults()">
					<span class="fa fa-pencil fa-lg fa-fw session-navbar-set_default"></span>
				</a>
			</li>
		`);
		$('header.navbar > .container > .navbar-collapse > ul.navbar-nav').prepend(this.$app);

		let me = this;
		this.$body = this.$app.find('.session-navbar-data.nav-link').hide().click(function(){
		  frappe.set_route('Form', doctype, me.data);
		});
		this.$body_text = this.$body.find('.session-navbar-text');
		this.$session_body = this.$app.find('.session-set_default-navbar-item');
	}
	sync_reload() {
		if (!this.is_online) return;
		this.clear_sync();
		var me = this;
		Promise.resolve()
			.then(function() { me.sync_data(); })
			.then(function() { me.setup_sync(); });
	}
	clear_sync() {
		if (this.sync_timer) {
			window.clearInterval(this.sync_timer);
			this.sync_timer = null;
		}
	}
	get_default_session() {
		let doctype = this.get_default_session_doctype();
		return frappe.defaults.get_user_default(doctype);
	}
	get_default_session_doctype() {
		return frappe.boot.show_session_in_navbar_doctype;
	}
	get_show_dialog() {
		return frappe.boot.show_session_dialog;
	}
	sync_data() {
		this._syncing = true;
		this.data = this.get_default_session();
		this.update_data();
		this._syncing = null;
	}
	setup_sync() {
		var me = this;
		this.sync_timer = window.setInterval(function() {
			me.sync_data();
		}, this.refresh_interval);
	}
	update_data() {
		if (this.data){
			this.$body_text.text(this.data);
			this.$body.show();
		}
		else{
			this.$body.hide();
		}
	}
}

frappe._session_navbar.init = function() {
	if (frappe._session_navbar._init) frappe._session_navbar._init.destory();
	if (frappe.desk == null) return;
	frappe._session_navbar._init = new SessionNavbar();
};

$(document).ready(function() {
	frappe._session_navbar.init();
});
