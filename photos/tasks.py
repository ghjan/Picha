import logging
from celery.task.schedules import crontab
from celery.decorators import periodic_task
from celery.utils.log import get_task_logger

from photos.utils import save_latest_flickr_image

# logger = get_task_logger(__name__)
logger = logging.getLogger('django.task')

@periodic_task(
    run_every=(crontab(minute='*/60')),
    name="task_save_latest_flickr_image",
    ignore_result=True
)
def task_save_latest_flickr_image():
    """
    Saves latest image from Flickr
    """
    # print("tasks.task_save_latest_flickr_image begin111")
    save_latest_flickr_image()
    # print("tasks.task_save_latest_flickr_image end -----")
    logger.info("Saved image from Flickr")
