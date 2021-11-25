from module import YoutubeCrawler
import pprint

import csv

if __name__ == '__main__':
    pp = pprint.PrettyPrinter(indent=4)
    crawler = YoutubeCrawler()
    video_data = crawler.get_popular_video_data()

    with open("data_set.csv", "w+", encoding="utf-8-sig", newline="")as file:
        csv_writer = csv.writer(file)
        for data in video_data:
            csv_writer.writerow([data["rank"],data["id"],data["title"],data["channelTitle"],data["viewCount"]])

            with open("./comment/" + data["id"] + ".csv" , "w+", encoding="utf-8-sig") as comment_file:
                csv_comment_writer = csv.writer(comment_file)

                for comment in data["comments"]:
                    csv_comment_writer.writerow([comment])

    with open("data_set.csv", 'r', encoding="utf-8-sig") as file:
        csv_reader = csv.reader(file)
        print(csv_reader)

        for data in csv_reader:
            print(data)
