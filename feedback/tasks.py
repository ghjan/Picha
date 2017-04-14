from celery.decorators import task
from celery.utils.log import get_task_logger

from feedback.emails import send_feedback_email

logger = get_task_logger(__name__)


@task(name="send_feedback_email_task")
def send_feedback_email_task(email, message):
    """sends an email when feedback form is filled successfully"""
    logger.info("Sent feedback email")
    return send_feedback_email(email, message)

from django.core import mail

@task(name="mail_admins")
def mail_admins(subject, message, fail_silently=False, connection=None,
                html_message=None):
    '''
    '''
    mail.mail_admins(subject, message, fail_silently, connection, html_message)
