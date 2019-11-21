from odoo import fields, models, api, _
from lxml import etree

import logging
_logger = logging.getLogger(__name__)


class BaseModelExtend(models.AbstractModel):
    _inherit = 'base'

    @api.model
    def _fields_view_get(self, view_id=None, view_type='form', toolbar=False, submenu=False):
        # Override BaseModel _fields_view_get to return generated default_view if view_id == 'get_default_form_view'
        if view_id == 'get_default_form_view':
            view_type = 'form'
            arch_etree = getattr(self, '_get_default_%s_view' % view_type)()
            return {
                'model': self._name,
                'field_parent': False,
                'arch': etree.tostring(arch_etree, encoding='unicode'),
                'type': view_type,
                'name': 'default',
            }
        else:
            return super(BaseModelExtend, self)._fields_view_get(view_id, view_type, toolbar, submenu)
