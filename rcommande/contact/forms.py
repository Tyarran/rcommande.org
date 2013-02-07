import colander

from deform.widget import TextAreaWidget
from pyramid.i18n import TranslationStringFactory

_ = TranslationStringFactory('pyramid')


class ContactSchema(colander.MappingSchema):
    name = colander.SchemaNode(colander.String(), title=_('name'))
    last_name = colander.SchemaNode(colander.String(), title=_('Last_name'))
    email = colander.SchemaNode(colander.String(), title=_('Email'), validator=colander.Email())
    content = colander.SchemaNode(colander.String(), widget=TextAreaWidget(), title=_('Content'))
