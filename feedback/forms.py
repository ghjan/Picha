from django import forms
from feedback.tasks import send_feedback_email_task, mail_admins
from django.core.mail import EmailMessage
from django.template import Context
from django.template.loader import render_to_string

class FeedbackForm(forms.Form):
    email = forms.EmailField(label="Email Address")
    message = forms.CharField(
        label="Message", widget=forms.Textarea(attrs={'rows': 5}))
    honeypot = forms.CharField(widget=forms.HiddenInput(), required=False)

    def send_email(self):
        # try to trick spammers by checking whether the honeypot field is
        # filled in; not super complicated/effective but it works
        if self.cleaned_data['honeypot']:
            return False
        email = self.cleaned_data['email']
        message = self.cleaned_data['message']
        c = Context({'email': email, 'message': message})
        email_subject = render_to_string(
            'feedback/email/feedback_email_subject.txt', c).replace('\n', '')
        email_body = render_to_string('feedback/email/feedback_email_body.txt', c)

        # subject = "feedback mail"
        # send_feedback_email_task.delay(
        #     self.cleaned_data['email'], self.cleaned_data['message'])
        mail_admins.delay(email_subject, email_body, fail_silently=True,
                         connection=None)
