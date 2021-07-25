from youtubeSearch.constants import YOUTUBE_CONSTANTS, ERROR_MESSAGES
from youtubeSearch.models import YoutubeApiKey, Video
from rest_framework.exceptions import APIException
import requests
from core import caches
import logging

log = logging.getLogger('fampay')


class YoutubeVideoService(object):

    @classmethod
    def get_latest_api_key(cls):
        api_key = caches.get(caches.CACHE.LATEST_API_KEY).decode("utf-8")
        if not api_key:
            api_key = ''
            try:
                api_key_obj = YoutubeApiKey.objects.latest('created_at')
                api_key = api_key_obj.api_key
                caches.set(caches.CACHE.LATEST_API_KEY, api_key, duration=caches.ONE_MONTH)
                return api_key

            except Exception as e:
                return api_key
        return api_key

    @classmethod
    def get_api_end_point(cls):
        end_point = YOUTUBE_CONSTANTS.YOUTUBE_SEARCH_END_POINT
        key = cls.get_latest_api_key()
        url = end_point.format(api_key=key)
        return url

    @classmethod
    def get_videos(cls):
        api_endpoint = cls.get_api_end_point()
        log.info(api_endpoint)
        try:
            response_data = requests.get(url=api_endpoint, timeout=5)
            return response_data
        except Exception as e:
            log.info(e)
            raise e

    @classmethod
    def update_youtube_api_key(cls, api_key=None):
        if not api_key:
            return APIException()
        try:
            api_key = YoutubeApiKey(api_key=api_key)
            api_key.save()
            caches.delete(caches.CACHE.LATEST_API_KEY)
        except:
            raise Exception(ERROR_MESSAGES.UNABLE_TO_ADD_API_KEY)

    @classmethod
    def get_new_youtube_api_key(cls):
        #to be implemented
        return "xyz"

    @classmethod
    def seed_video_data(cls):
        videos_json = cls.get_videos().json()
        video_objs = cls.get_video_object_from_json(videos_json=videos_json['items'])
        try:
            Video.objects.bulk_create(video_objs)
            return True
        except Exception as e:
            print("error while adding data ", str(e))
            return False

    @classmethod
    def get_video_object_from_json(cls, videos_json):
        video_django_objs = []
        for video in videos_json:
            video_id = video[YOUTUBE_CONSTANTS.ID][YOUTUBE_CONSTANTS.VIDEO_ID]
            high_thumbnail = video[YOUTUBE_CONSTANTS.SNIPPET][YOUTUBE_CONSTANTS.THUMBNAILS][YOUTUBE_CONSTANTS.HIGH][YOUTUBE_CONSTANTS.URL]
            medium_thumbnail = video[YOUTUBE_CONSTANTS.SNIPPET][YOUTUBE_CONSTANTS.THUMBNAILS][YOUTUBE_CONSTANTS.MEDIUM][YOUTUBE_CONSTANTS.URL]
            default_thumbnail = video[YOUTUBE_CONSTANTS.SNIPPET][YOUTUBE_CONSTANTS.THUMBNAILS][YOUTUBE_CONSTANTS.DEFAULT][YOUTUBE_CONSTANTS.URL]
            channel_id = video[YOUTUBE_CONSTANTS.SNIPPET][YOUTUBE_CONSTANTS.CHANNEL_ID]
            published_at = video[YOUTUBE_CONSTANTS.SNIPPET][YOUTUBE_CONSTANTS.PUBLISHED_AT]
            title = video[YOUTUBE_CONSTANTS.SNIPPET][YOUTUBE_CONSTANTS.TITLE]
            description = video[YOUTUBE_CONSTANTS.SNIPPET][YOUTUBE_CONSTANTS.DESCRIPTION]
            channel_title = video[YOUTUBE_CONSTANTS.SNIPPET][YOUTUBE_CONSTANTS.CHANNEL_TITLE]
            video_obj = Video(youtube_video_id=video_id, high_thumbnail=high_thumbnail,
                              medium_thumbnail=medium_thumbnail, default_thumbnail=default_thumbnail,
                              channel_id=channel_id, channel_title=channel_title, title=title, description=description,
                              published_at=published_at)
            video_django_objs.append(video_obj)
        return video_django_objs
