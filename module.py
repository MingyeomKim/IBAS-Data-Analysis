import requests
import pprint
import json

class YoutubeCrawler:

    def __init__(self):
        self.key = "AIzaSyDfGrIi4N4kB0nHWe4W6uq2fAya0xvXOoQ"
        self.url = "https://www.googleapis.com/youtube/v3/"

    def get_popular_video(self, count=10):
        params = {
            "key": self.key,
            "part": ["snippet", "statistics"],
            "chart": "mostPopular",
            "regionCode": "KR",
            "maxResults": count
        }
        response = requests.get(self.url + "videos", params=params)
        videos_data = response.json()["items"]

        videos_list = []

        for i, item in enumerate(videos_data, start=1):
            temp_dict = {}

            temp_dict["rank"] = i
            temp_dict["id"] = item["id"]
            temp_dict["title"] = item["snippet"]["title"]
            temp_dict["channelTitle"] = item["snippet"]["channelTitle"]
            temp_dict["viewCount"] = item["statistics"]["viewCount"]

            videos_list.append(temp_dict)
        return videos_list

    def get_video_comments(self, id, count=100):
        params = {
            "key": self.key,
            "part": "snippet",
            "videoId": id,
            "maxResults": count,
            "order": "time",
            "textFormat": "plainText"
        }

        response = requests.get(self.url + "commentThreads", params=params)
        comments_data = response.json()["items"]

        comments_list = []
        for item in comments_data:
            comments_list.append(item["snippet"]["topLevelComment"]["snippet"]["textDisplay"].replace("\n", ". ").strip())

        return comments_list

    def get_popular_video_data(self, count=10, comment_count=100):
        video_data = self.get_popular_video()

        for i in range(len(video_data)):
            video_data[i]["comments"] = self.get_video_comments(video_data[i]["id"], comment_count)
        return video_data
