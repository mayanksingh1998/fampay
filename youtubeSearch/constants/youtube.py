class Youtube(object):
    YOUTUBE_API_KEY = 'AIzaSyD7yWOqKYXssgsLhOiUWtm5XUxuqHS22wM'
    YOUTUBE_SEARCH_END_POINT = 'https://www.googleapis.com/youtube/v3/search?part=snippet&key={' \
                               'api_key}&type=video&q=iphone&maxResults=10'
    SNIPPET = 'snippet'
    THUMBNAILS = 'thumbnails'
    MEDIUM = 'medium'
    HIGH = 'high'
    DEFAULT = 'default'

    DESCRIPTION = 'description'
    CHANNEL_TITLE = 'channelTitle'
    CHANNEL_ID = 'channelId'
    VIDEO_ID = 'videoId'
    URL = 'url'
    ID = 'id'
    PUBLISHED_AT = 'publishedAt'
    TITLE = 'title'

YOUTUBE_CONSTANTS = Youtube()
