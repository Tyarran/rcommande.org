from deform import Form
from pyramid.response import Response
from pyramid.view import view_config
from pyramid.i18n import TranslationString as _

from rcommande.contact.forms import ContactSchema
from rcommande.contact.tasks import send_email


class ContactView(object):
    """ Contact view """

    def __init__(self, request):
        self.request = request
        self.form = Form(ContactSchema(), buttons=(_('submit'),), method='POST')


    @view_config(route_name='contact', renderer='contact_form.jinja2')
    def render(self):
        if self.request.method == 'POST':
            try:
                values = self.form.validate(self.request.POST.items())
                send_email.delay(values['email'], values['content'], values['name'], values['last_name'])
                return {'form': 'Email send!'}
            except:
                pass
        return {'form': self.form.render()}
