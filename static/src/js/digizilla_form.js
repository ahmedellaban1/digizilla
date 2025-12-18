/** @odoo-module **/

import { FormController } from "@web/views/form/form_controller";
import { patch } from "@web/core/utils/patch";

patch(FormController.prototype, {
    setup() {
        super.setup(...arguments);
        if (this.props.resModel === 'digizilla.digizilla') {
            // Hide the create button for Digizilla model
            if (this.props.activeActions) {
                this.props.activeActions.create = false;
            }
        }
    },
});