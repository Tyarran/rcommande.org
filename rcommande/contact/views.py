#-*- coding: UTF8 -*-
import transaction
import logging

from deform import Form
from pyramid.view import view_config
from pyramid.i18n import TranslationString as _
from js.bootstrap import bootstrap
from colanderalchemy import SQLAlchemyMapping
from deform.exception import ValidationFailure

from rcommande.contact.forms import ContactSchema
from rcommande.contact.tasks import send_email
from rcommande.contact.models import Contact
from rcommande.models import DBSession

log = logging.getLogger(__name__)


class View(object):
    """ Base view """
    title = ''

    def get_context(self):
        return {'title': self.title}

    def render(self):
        bootstrap.need()
        return self.get_context()


class ContactView(View):
    """ Contact view """
    title = 'Formulaire de contact'

    def __init__(self, request):
        self.request = request
        self.form = Form(ContactSchema(), buttons=(_('submit'),), method='POST')

    @view_config(route_name='contact', renderer='contact_form.jinja2')
    def render(self):
        context = super(ContactView, self).render()
        if self.request.method == 'POST':
            try:
                values = self.form.validate(self.request.POST.items())
                send_email.delay(values['email'], values['content'], values['name'], values['last_name'])
                contact = Contact(values['name'], values['last_name'], values['email'],
                    values['content'])
                with transaction.manager:
                    DBSession.add(contact)
                context['message'] = 'Email sent'
                context['message_type'] = 'info'
                log.info('%s from %s %s' % (context['message'], values['name'], values['last_name']))
                return context
            except Exception as ex:
                if not issubclass(ValidationFailure, ex.__class__):
                    log.error(ex.message)
        context['form'] = self.form.render()
        return context
