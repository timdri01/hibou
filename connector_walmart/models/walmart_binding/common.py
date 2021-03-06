# -*- coding: utf-8 -*-
# © 2017,2018 Hibou Corp.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, models, fields
from odoo.addons.queue_job.job import job, related_action


class WalmartBinding(models.AbstractModel):
    """ Abstract Model for the Bindings.

    All of the models used as bindings between Walmart and Odoo
    (``walmart.sale.order``) should ``_inherit`` from it.
    """
    _name = 'walmart.binding'
    _inherit = 'external.binding'
    _description = 'Walmart Binding (abstract)'

    backend_id = fields.Many2one(
        comodel_name='walmart.backend',
        string='Walmart Backend',
        required=True,
        ondelete='restrict',
    )
    external_id = fields.Char(string='ID in Walmart')

    _sql_constraints = [
        ('walmart_uniq', 'unique(backend_id, external_id)', 'A binding already exists for this Walmart ID.'),
    ]

    @job(default_channel='root.walmart')
    @related_action(action='related_action_walmart_link')
    @api.model
    def import_batch(self, backend, filters=None):
        """ Prepare the import of records modified on Walmart """
        if filters is None:
            filters = {}
        with backend.work_on(self._name) as work:
            importer = work.component(usage='batch.importer')
            return importer.run(filters=filters)

    @job(default_channel='root.walmart')
    @related_action(action='related_action_walmart_link')
    @api.model
    def import_record(self, backend, external_id, force=False):
        """ Import a Walmart record """
        with backend.work_on(self._name) as work:
            importer = work.component(usage='record.importer')
            return importer.run(external_id, force=force)

    # @job(default_channel='root.walmart')
    # @related_action(action='related_action_unwrap_binding')
    # @api.multi
    # def export_record(self, fields=None):
    #     """ Export a record on Walmart """
    #     self.ensure_one()
    #     with self.backend_id.work_on(self._name) as work:
    #         exporter = work.component(usage='record.exporter')
    #         return exporter.run(self, fields)
    #
    # @job(default_channel='root.walmart')
    # @related_action(action='related_action_walmart_link')
    # def export_delete_record(self, backend, external_id):
    #     """ Delete a record on Walmart """
    #     with backend.work_on(self._name) as work:
    #         deleter = work.component(usage='record.exporter.deleter')
    #         return deleter.run(external_id)
