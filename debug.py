import requests
import json

headers = {
    "Referer": "https://www.xuexi.cn/",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/138.0.0.0 Safari/537.36",
}


def get_video_links():
    try:
        # 解决视频不能正常学习的问题
        video_json = requests.get(
            "https://www.xuexi.cn/lgdata/4426aa87b0b64ac671c96379a3a8bd26/db086044562a57b441c24f2af1c8e101.json",
            headers=headers,
        ).content.decode("utf8")
        video = json.loads(video_json)["DataSet"]
        json_urls = []
        for i in video:
            json_urls.append("https://www.xuexi.cn/lgdata/" + i.split("!")[1])

        all_video_object = []
        for url in json_urls:
            choose_json_str = requests.get(url, headers=headers).content.decode("utf8")
            all_video_object.extend(json.loads(choose_json_str))
        new_list = sorted(
            all_video_object, key=lambda x: x.get("publishTime", "0"), reverse=False
        )
        return [news["url"] for news in new_list]
    except:
        print("=" * 60)
        print("get_video_links获取失败")
        print("=" * 60)
        raise


get_video_links()
