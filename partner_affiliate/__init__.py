# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from . import models

from openupgradelib import openupgrade


def module_migration(cr):
    res_partner_affiliate = "res_partner_affiliate"
    partner_affiliate = "partner_affiliate"
    if openupgrade.is_module_installed(cr, res_partner_affiliate):
        openupgrade.update_module_names(
            cr,
            [
                (res_partner_affiliate, partner_affiliate),
            ],
            merge_modules=True,
        )
