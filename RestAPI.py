from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_sqlalchemy import SQLAlchemy
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
db = SQLAlchemy(app)

SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
swaggerui_blueprint = get_swaggerui_blueprint(SWAGGER_URL, API_URL, config={'app_name': "Weather API"})
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

class WeatherResource(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('date', type=str)
        parser.add_argument('station_id', type=str)
        args = parser.parse_args()

        query = WeatherData.query
        if args['date']:
            query = query.filter(WeatherData.date == args['date'])
        if args['station_id']:
            query = query.filter(WeatherData.station_id == args['station_id'])
        result = query.paginate().items
        return [record.as_dict() for record in result]

class WeatherStatsResource(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('year', type=int)
        parser.add_argument('station_id', type=str)
        args = parser.parse_args()

        query = WeatherStats.query
        if args['year']:
            query = query.filter(WeatherStats.year == args['year'])
        if args['station_id']:
            query = query.filter(WeatherStats.station_id == args['station_id'])
        result = query.paginate().items
        return [record.as_dict() for record in result]

api.add_resource(WeatherResource, '/api/weather')
api.add_resource(WeatherStatsResource, '/api/weather/stats')

if __name__ == '__main__':
    app.run(debug=True)
