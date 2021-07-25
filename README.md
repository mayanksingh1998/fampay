# fampay
THE APP YoutubeSearch runs on localhost 8000 port
API END POINT = /api/v1/videos/
Query params = 1. channel_title 2. Description, 3. title(video_title)


There are two crons which run in asynchronus ways which updates the data in DB and other one updates the latest API_KEY for google
cron expressions to be added in cron tab
*/1 * * * * /Users/mayanksingh/fampay/scripts/crons/video_data_seeding.sh
*/1 * * * * /Users/mayanksingh/fampay/scripts/crons/update_youtube_api_key.sh


Docker file is also Added

To run the Server
Python3 manage.py runserver




