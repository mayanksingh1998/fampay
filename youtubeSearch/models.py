from django.db import models
app_name = 'tests'


class Video(models.Model):
    youtube_video_id = models.CharField(max_length=100,null=True,db_index=True, unique=True)
    title = models.CharField(max_length=250, null=True, blank=True, db_index=True)
    high_thumbnail = models.CharField(max_length=250, null=True, blank=True)
    description = models.CharField(max_length=250, null=True, blank=True)
    published_at = models.DateTimeField()
    default_thumbnail = models.CharField(max_length=250, null=True, blank=True)
    medium_thumbnail = models.CharField(max_length=250, null=True, blank=True)
    channel_id = models.CharField(max_length=100, null=True, db_index=True)
    channel_title = models.CharField(max_length=100, null=True, db_index=True)

    class Meta:
        unique_together = ["title", "youtube_video_id"]

    def to_json(self):
        return dict(
            youtube_video_id=self.youtube_video_id,
            title=self.title,
            description=self.description,
            high_thumbnail=self.high_thumbnail,
            default_thumbnail=self.default_thumbnail,
            medium_thumbnail=self.medium_thumbnail,
            channel_id=self.channel_id,
            channel_title=self.channel_title
        )

class YoutubeApiKey(models.Model):
    api_key = models.CharField(max_length=250)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

