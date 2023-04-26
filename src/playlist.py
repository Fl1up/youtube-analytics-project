import os, isodate, datetime
from src.channel import Channel
from googleapiclient.discovery import build


class PlayList(Channel):

    def __init__(self, playlist_id):
        self.api_key: str = os.getenv('YT_API_KEY')
        self.youtube = build('youtube', 'v3', developerKey=self.api_key)
        self.playlist_videos = self.youtube.playlistItems().list(playlistId=playlist_id, part='contentDetails', maxResults=50,).execute()
        self.video_ids: list[str] = [video['contentDetails']['videoId'] for video in self.playlist_videos['items']]
        self.video_response = self.youtube.videos().list(part='contentDetails,statistics',  id=','.join(self.video_ids)).execute()

        self.title = "Редакция. АнтиТревел"
        self.url = f"https://www.youtube.com/playlist?list={playlist_id}"


    @property
    def total_duration(self):
        a = []
        for video in self.video_response['items']:
            iso_8601_duration = video['contentDetails']['duration']
            duration = isodate.parse_duration(iso_8601_duration)
            a.append(duration)
        result = sum(a, datetime.timedelta())
        return result

    def show_best_video(self):
        max_likes = 0
        for video in self.video_response["items"]:
            print(self.video_response)
            print(self.playlist_videos)
            if int(video['statistics']['likeCount']) > max_likes:
                max_likes = int(video['statistics']['likeCount'])
                best_video: str = video["id"]
        return f"https://youtu.be/{best_video}"
