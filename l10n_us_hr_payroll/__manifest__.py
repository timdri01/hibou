# Part of Hibou Suite Professional. See LICENSE_PROFESSIONAL file for full copyright and licensing details.

{
    'name': 'United States of America - Payroll',
    'author': 'Hibou Corp. <hello@hibou.io>',
    'version': '15.0.2021.0.0',
    'category': 'Payroll Localization',
    'depends': [
        'hr_payroll_hibou',
    ],
    'description': """
United States of America - Payroll Rules.
=========================================

    """,

    'data': [
        'security/ir.model.access.csv',
        'data/base.xml',
        'data/integration_rules.xml',
        'data/federal/fed_940_futa_parameters.xml',
        'data/federal/fed_940_futa_rules.xml',
        'data/federal/fed_941_fica_parameters.xml',
        'data/federal/fed_941_fica_rules.xml',
        'data/federal/fed_941_fit_parameters.xml',
        'data/federal/fed_941_fit_rules.xml',
        'data/state/ak_alaska.xml',
        'data/state/al_alabama.xml',
        'data/state/ar_arkansas.xml',
        'data/state/az_arizona.xml',
        'data/state/ca_california.xml',
        'data/state/co_colorado.xml',
        'data/state/ct_connecticut.xml',
        'data/state/de_delaware.xml',
        'data/state/fl_florida.xml',
        'data/state/ga_georgia.xml',
        'data/state/hi_hawaii.xml',
        'data/state/ia_iowa.xml',
        'data/state/id_idaho.xml',
        'data/state/il_illinois.xml',
        'data/state/in_indiana.xml',
        'data/state/ks_kansas.xml',
        'data/state/ky_kentucky.xml',
        'data/state/la_louisiana.xml',
        'data/state/me_maine.xml',
        'data/state/mi_michigan.xml',
        'data/state/mn_minnesota.xml',
        'data/state/mo_missouri.xml',
        'data/state/ms_mississippi.xml',
        'data/state/mt_montana.xml',
        'data/state/nc_northcarolina.xml',
        'data/state/nd_north_dakota.xml',
        'data/state/ne_nebraska.xml',
        'data/state/nh_new_hampshire.xml',
        'data/state/nj_newjersey.xml',
        'data/state/nm_new_mexico.xml',
        'data/state/nv_nevada.xml',
        'data/state/ny_new_york.xml',
        'data/state/oh_ohio.xml',
        'data/state/ok_oklahoma.xml',
        'data/state/pa_pennsylvania.xml',
        'data/state/ri_rhode_island.xml',
        'data/state/sc_south_carolina.xml',
        'data/state/sd_south_dakota.xml',
        'data/state/tn_tennessee.xml',
        'data/state/tx_texas.xml',
        'data/state/ut_utah.xml',
        'data/state/vt_vermont.xml',
        'data/state/va_virginia.xml',
        'data/state/wa_washington.xml',
        'data/state/wi_wisconsin.xml',
        'data/state/wv_west_virginia.xml',
        'data/state/wy_wyoming.xml',
        'views/hr_contract_views.xml',
        'views/us_payroll_config_views.xml',
    ],
    'demo': [
    ],
    'auto_install': False,
    'post_init_hook': '_post_install_hook',
    'license': 'OPL-1',
}
