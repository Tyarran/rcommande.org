import logging
import smtplib

from email.mime.text import MIMEText

from celery.task import task

logger = logging.getLogger(__name__)

@task
def send_email(email, content, name, last_name):
    to = "commande.romain@gmail.com"
    gmail_user = 'commande.romain'
    gmail_pwd = '***********'
    smtpserver = smtplib.SMTP("smtp.gmail.com",587)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo
    smtpserver.login(gmail_user, gmail_pwd)
    header = u'To:%s\nFrom:%s\nSubject:Message va rcommande.org' % (to, email)
    email_content = '%s %s \n' % (name, last_name)
    email_content += content
    _msg = header + '\n' + email_content
    msg  = MIMEText(_msg, _subtype='plain', _charset='utf-8').as_string()
    smtpserver.sendmail(gmail_user, to, msg)
    smtpserver.close()
    logger.info('Email correctly send')
    #return 42
