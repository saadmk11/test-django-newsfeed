from celery.decorators import task

from newsfeed.models import Newsletter
from newsfeed.utils.send_newsletters import send_email_newsletter


@task(name="send_email_newsletter_task")
def send_email_newsletter_task(newsletters_ids=None, respect_schedule=True):
    newsletters = None

    if newsletters_ids:
        newsletters = Newsletter.objects.filter(
            id__in=newsletters_ids
        )
    send_email_newsletter(
        newsletters=newsletters,
        respect_schedule=respect_schedule
    )
