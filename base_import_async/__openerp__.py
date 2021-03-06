# -*- coding: utf-8 -*-
###############################################################################
#
#   Module for Odoo
#   Copyright (C) 2014 ACSONE SA/NV (http://acsone.eu).
#   Copyright (C) 2013 Akretion (http://www.akretion.com).
#   @author Stéphane Bidoul <stephane.bidoul@acsone.eu>
#   @author Sébastien BEAU <sebastien.beau@akretion.com>
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU Affero General Public License as
#   published by the Free Software Foundation, either version 3 of the
#   License, or (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU Affero General Public License for more details.
#
#   You should have received a copy of the GNU Affero General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################
{
    'name': 'Asynchronous Import',
    'version': '1.0',
    'author': 'Akretion, ACSONE SA/NV, Odoo Community Association (OCA)',
    'license': 'AGPL-3',
    'category': 'Generic Modules',
    'depends': [
        'base_import',
        'connector',
    ],
    'data': [
        'views/base_import_async.xml',
    ],
    'qweb': [
        'static/src/xml/import.xml',
    ],
    'installable': True,
    'application': False,
}
