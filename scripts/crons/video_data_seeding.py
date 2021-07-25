import logging
import os
import sys

os.environ['DJANGO_SETTINGS_MODULE'] = 'fampay.settings'

ROOT_FOLDER = os.path.realpath(os.path.dirname(__file__))
ROOT_FOLDER = ROOT_FOLDER[:ROOT_FOLDER.rindex('crons')]
ROOT_FOLDER = ROOT_FOLDER[:ROOT_FOLDER.rindex('scripts')]

if ROOT_FOLDER not in sys.path:
    sys.path.insert(1, ROOT_FOLDER + '/')

import django

django.setup()
import logging

log = logging.getLogger('fampay')
from youtubeSearch.service.youtube_video_service import YoutubeVideoService

try:
    video = YoutubeVideoService.seed_video_data()
except Exception as e:
    log.info(str(e))
