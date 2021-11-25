import requests
import json
import secret

#하나의 비디오 정보를 불러오자!

#1. 인증정보 key

#2. 전달 주소
# https://www.googleapis.com/youtube/v3/videos
# django에서 secret KEY 파일을 가져오는 방법

url = "https://www.googleapis.com/youtube/v3/videos"
params = { # get요청 시 전달할 parameter
    #key, value로 구성
    "key": secret.secretKey,
    "id": "scy4bOferow",
    "part": ["snippet", "statistics"],
} #dictionary

# GET Method
response = requests.get(url, params=params)

print(response, type(response))
# 200이 나오면 정상 출력된 것임
data = response.json()
print(data, type(data)) #dictonary형태로 출력

#json 라이브러리 함수를 사용해 보기 좋게 출력
print(json.dumps(data, indent=4, ensure_ascii=False))

#제목만 출력하는 방식
print(data["items"][0]["snippet"]["title"])

#통계  중 시청 수와 좋아요 수를 출력
print("시청 수 : " , data["items"][0]["statistics"]["viewCount"])
print("좋아요 수 : " , data["items"][0]["statistics"]["likeCount"])

#한국에서 인기를 끄는 10개으ㅣ 동영상 (이름, 순위. 채널명, 조회수, 좋아요 수 )
url = "https://www.googleapis.com/youtube/v3/videos"
params = {
    "key": secret.secretKey,
    "part": ["snippet", "statistics"],
    "char": "mostPopular",
    "maxResults": 10,
    "regionCode": "KR",
}
response = requests.get(url, params=params)
print(json.dumps(response.json(), indent=4, ensure_ascii=False))