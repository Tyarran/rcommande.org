from rcommande.models import Base
from sqlalchemy import Column, Integer, Unicode, UnicodeText


class Contact(Base):
    __tablename__ = 'contact_contact'

    id = Column(Integer, primary_key=True)
    name = Column(Unicode(255), nullable=False)
    last_name = Column(Unicode(255), nullable=False)
    email = Column(Unicode(255), nullable=False)
    content = Column(UnicodeText, nullable=False)

    def __init__(self, name, last_name, email, content):
        self.name = name
        self.last_name = last_name
        self.email = email
        self.content = content

    def __unicode__(self):
        return '%s - %s:  %s' % (self.name, self.last_name, self.content[0: 10])

    __str__ = __unicode__
