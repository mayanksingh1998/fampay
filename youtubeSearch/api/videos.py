from django.http import JsonResponse
from rest_framework.exceptions import PermissionDenied, APIException, ValidationError
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from youtubeSearch.service import VideoService
from youtubeSearch.constants import VIDEO_CONSTANT, PAGINATOR
import utils


class Videos(APIView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.replay_json_response = True
        self.video_service = VideoService()

    def validate_and_get_request_params(self, request):
        query_params = request.query_params.copy()
        video_title = query_params.get(VIDEO_CONSTANT.TITLE, VIDEO_CONSTANT.DEFAULT_TITLE)
        channel_title = query_params.get(VIDEO_CONSTANT.CHANNEL_TITLE, VIDEO_CONSTANT.DEFAULT_CHANNEL_TITLE)
        description = query_params.get(VIDEO_CONSTANT.DESCRIPTION, VIDEO_CONSTANT.DEFAULT_DESCRIPTION)

        page = query_params.get(PAGINATOR.PAGE, PAGINATOR.DEFAULT_PAGE)
        page_size = query_params.get(PAGINATOR.PAGE_SIZE, PAGINATOR.CONTENT_DEFAULT_PAGE_SIZE)
        page, page_size = utils.paginator.Paginator.get_validated_params(page, page_size)
        query_params_dict = {PAGINATOR.PAGE: page,
                             PAGINATOR.PAGE_SIZE: page_size, }
        if video_title:
            query_params_dict.update({VIDEO_CONSTANT.TITLE: video_title})
        if channel_title:
            query_params_dict.update({VIDEO_CONSTANT.CHANNEL_TITLE: channel_title})
        if description:
            query_params_dict.update({VIDEO_CONSTANT.DESCRIPTION: description})
        return query_params_dict

    def get(self, request):
        query_params = self.validate_and_get_request_params(request)
        videos, page_info = self.video_service.get_videos(**query_params)
        return JsonResponse({VIDEO_CONSTANT.VIDEOS: videos, PAGINATOR.PAGE_INFO: page_info })
