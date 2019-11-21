odoo.define('web_view_record_fields.debug_manager_included', function (require) {
"use strict";

    var core = require("web.core");
    var DebugManager = require('web.DebugManager');

    var QWeb = core.qweb;
    var _t = core._t;

    DebugManager.include({
        get_all_fields_data: function () {
            var model = this._action.res_model,
                self = this;
            var selectedIDs = this._controller.getSelectedIds();
            if (!selectedIDs.length) {
                console.warn(_t("No selected ids available"));
                return;
            }
            this.do_action({
                name: _t('Manage Attachments'),
                type: 'ir.actions.act_window',
                res_model: model,
                res_id: selectedIDs[0],
                views: [['get_default_form_view', 'form']],
                target: 'current',
                view_mode: 'form',
                view_type: 'form',
            });
        },

    });
});
