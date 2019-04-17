from database import Database
from flask import Flask, jsonify, request
from flask_restful import reqparse, abort, Api, Resource
from vendor import custom_url_shortener
import random

app = Flask(__name__)
api = Api(app)

class UrlStatistics(Resource):
    def get(self):
        db = Database()
        str_sql_statistic = "Select new_url as 'short', original_url as 'original', total_clicks, timestamp from shortened_url order by timestamp"
        rs = db.execute(str_sql_statistic, None, False)
        return jsonify(url_details=rs)

class UrlShortener(Resource):
    def post(self):
        json_request = request.get_json()
        objUrlShortener = custom_url_shortener.CustomUrlShortener()
        str_short_url = objUrlShortener.doShortener(json_request['url'])['short']
        str_mm_cod = str_short_url.split('/')[3]
        db = Database()
        str_sql_insert = "insert into shortened_url(mm_cod, original_url, total_clicks, new_url) values ('%s','%s',%d,'%s')"
        list_args = (str_mm_cod, json_request['url'], random.randint(1,2000), str_short_url)
        db.execute(str_sql_insert, list_args, True)
        return jsonify(original=json_request['url'], short=str_short_url)

api.add_resource(UrlStatistics,'/get-details')
api.add_resource(UrlShortener, '/shorturl')

if __name__ == '__main__':
    app.run()
