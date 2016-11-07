from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import requests
import json
import threading
import os
import time


HEADERS = {
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'es-ES,es;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.76 Mobile Safari/537.36',
    'Accept': '*/*',
    #'Referer': 'http://localhost:63342/TimeLine/scrappers/latercera.html?_ijt=9ojhk8aq76m4oc53v31vbjoa9c',
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
}


def html_parser(url):
    try:
        html = urlopen(url)
        bsObj = BeautifulSoup(html, "html.parser")
        return bsObj
    except HTTPError as e:
        print(e)


class LTScrapper:

    def __init__(self):
        self.run()

    def run(self):
        workers = []
        for number in range(1000, 700000):
            worker = Reporter(number)
            workers.append(worker)
            worker.start()
            if number % 50 == 0:
                active_workers = threading.active_count()
                print("{} active workers".format(active_workers))
                time.sleep(1)
                while threading.active_count() >= 300:
                    pass
        for worker in workers:
            worker.join()


class Reporter(threading.Thread):

    def __init__(self, counter):
        threading.Thread.__init__(self)
        self.number = counter
        self.info = {}

    def run(self):
        response = self.get_response()
        if response:
            try:
                self.gather_info(response)
                self.save()
            except IndexError as e:
                print(e)
            except KeyError as e:
                print(e)
            print("Reporter {} finised".format(self.number))

    def get_response(self):
        link = "http://m1.data.copesa.cl/gcdata/manager?" \
          "action=GetContentById&id={}&siteCode=" \
          "latercera&limit=10&time=168&alt=json&callback=" \
          "__gwt_jsonp__.P0.onSuccess".format(self.number)
        try:
            r = requests.get(link, headers=HEADERS)
            r = r.text[27:-3]
            response = json.loads(r)
            if len(response["data"]) > 0:
                return response
            return False
        except:
            return False

    def gather_info(self, response):
        info = response["data"][0]
        self.info["title"] = info["title"]
        self.info["date"], self.info["time"] = self.normalize_date(info["associates"][0]["date"]["date"])
        self.info["intro"] = info["description"]
        self.info["text"] = info["associates"][0]["note"]
        self.info["link"] = info["url"]

    def normalize_date(self, date):
        date, time = date.split(" ")[0], date.split(" ")[1]
        date = date.split("/")
        date = "{0}-{1}-{2}".format(date[2], date[1], date[0])
        return date, time

    def save(self):
        file_path = "../sources/latercera/{}".format(self.number)
        with open(file_path, "w") as f:
            json.dump(self.info, f)

if __name__ == '__main__':
    LTScrapper()
