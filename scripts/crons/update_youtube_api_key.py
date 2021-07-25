import logging
import os
import sys

from rest_framework.exceptions import APIException

os.environ['DJANGO_SETTINGS_MODULE'] = 'youtubeSearch.settings'

ROOT_FOLDER = os.path.realpath(os.path.dirname(__file__))
ROOT_FOLDER = ROOT_FOLDER[:ROOT_FOLDER.rindex('crons')]
ROOT_FOLDER = ROOT_FOLDER[:ROOT_FOLDER.rindex('scripts')]

if ROOT_FOLDER not in sys.path:
    sys.path.insert(1, ROOT_FOLDER + '/')

import django

django.setup()
from youtubeSearch.service.youtube_video_service import YoutubeVideoService
import  logging
log = logging.getLogger('fampay')
try:
    api_key = YoutubeVideoService.get_new_youtube_api_key()
    YoutubeVideoService.update_youtube_api_key(api_key)
except APIException as e:
    log.info(str(e))
