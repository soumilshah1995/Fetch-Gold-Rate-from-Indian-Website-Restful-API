#!/usr/bin/env python

__Author__ = 'Soumil Nitin Shah '
__Version__ = '0.0.1'
__Email__ = "shahsoumil519@gmail.com"


try:

    from flask import Flask, request
    from flask_restful import Resource, Api
    from flask_restful import reqparse
    from flasgger import Swagger
    from flasgger.utils import swag_from
    from flask_restful_swagger import swagger
    import json
    from bs4 import  BeautifulSoup
    import requests
    print("All Modules Loaded .......")
except Exception as e:
    print("Some Modlues are Missings {}".format(e))


app = Flask(__name__)
api = Api(app)
parser = reqparse.RequestParser()
parser.add_argument('name', type = str)
api = swagger.docs(Api(app), apiVersion='1', api_spec_url="/doc")


data = ["soumil"]

class Goldrate(object):

    def __init__(self):

        self.__headers = {
            'Accept-Encoding': 'gzip, deflate, sdch',
            'Accept-Language': 'en-US,en;q=0.8',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Referer': 'http://www.wikipedia.org/',
            'Connection': 'keep-alive',
        }
        self.url = " https://www.paisabazaar.com/gold-rate/"

    @property
    def get(self):
        """

        :return: String value for Gold Rates
        """

        r = requests.get(url=self.url, headers=self.__headers)
        soup = BeautifulSoup(r.text, 'html.parser')

        data = soup.findAll(class_='g-6-s goldRate__price goldRatePriceHighLite')
        tem = []
        for x in data:
            val = x.text[3:]
            tem.append(val)

            break
        return tem[0]


class Data(Resource):

    @swagger.model
    @swagger.operation(notes='some really good notes')
    def get(self):
        obj = Goldrate()
        data = obj.get
        payload = {'Response':200,'Data':data}
        payload = json.dumps(payload)
        print(payload)
        return payload

api.add_resource(Data, '/goldrate')

if __name__ == '__main__':
    app.run(debug=True)
