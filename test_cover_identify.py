import requests


def test():
    headers = {"Accept": "application/json",
               "device_type": "m3", "device_id": "11691500272904",
               "device_sign": "",
               "User-Agent": "okhttp/3.12.0", "Connection": "keep-alive",
               "Host": "119.23.148.25:9900",
               "Accept-Encoding": "gzip"
               }
    url = "http://119.23.148.25:9900/paipai/coverIdentify"
    files = {'file': ("cover-crop.jpeg", open("cover-crop.jpeg", "rb"), "image/jpeg", {})}
    res = requests.request("POST", url, data=None, files=files, headers=headers)
    print("status code " + str(res.status_code))
    print("response " + res.text)
    print("******************************")


if __name__ == '__main__':
    for i in range(20):
        test()
