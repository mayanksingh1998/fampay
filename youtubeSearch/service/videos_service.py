from youtubeSearch.models import Video
from youtubeSearch.constants import VIDEO_CONSTANT, PAGINATOR
import utils
import logging

log = logging.getLogger('fampay')


class VideoService(object):

    @classmethod
    def get_filters(cls, **kwargs):
        filters = {}
        video_title = kwargs.get(VIDEO_CONSTANT.TITLE, VIDEO_CONSTANT.DEFAULT_TITLE)
        channel_title = kwargs.get(VIDEO_CONSTANT.CHANNEL_TITLE, VIDEO_CONSTANT.DEFAULT_CHANNEL_TITLE)
        description = kwargs.get(VIDEO_CONSTANT.DESCRIPTION, VIDEO_CONSTANT.DEFAULT_DESCRIPTION)
        if video_title:
            filters.update({'title__icontains': video_title})
        if channel_title:
            filters.update({'channel_title__icontains': channel_title})
        if description:
            filters.update({'description__icontains': description})
        return filters

    @classmethod
    def get_videos(cls, **kwargs):
        filters = cls.get_filters(**kwargs)
        log.info(filters)
        page = kwargs.get(PAGINATOR.PAGE)
        page_size = kwargs.get(PAGINATOR.PAGE_SIZE)
        videos = Video.objects.filter(**filters).order_by('-published_at')
        paginated_video_objs = utils.paginator.Paginator.paginate_queryset(videos, page=page, page_size=page_size)
        page_info = utils.paginator.Paginator.get_page_info(page, page_size, videos.count())

        paginated_response = []
        for video_objs in paginated_video_objs:
            paginated_response.append(video_objs.to_json())

        return paginated_response, page_info
