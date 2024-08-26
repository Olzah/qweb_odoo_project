# -*- coding: utf-8 -*-

from odoo import http


class QwebTutorials(http.Controller):
    @http.route('/qweb-tutorials', type='http', auth='public', website=True)
    def qweb_tutorials(self):
        return http.request.render("qweb_app.somePythonTemplate")
    