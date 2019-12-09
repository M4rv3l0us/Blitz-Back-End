from flask import Flask
from flask_restful import Api
from controller.Authenticate import Authenticate
from controller.Webhook import WebHook
from controller.Hello import HelloWorld
from controller.SyncData import SyncData
from controller.PullData import PullData
from controller.SortByPrice import PriceSort
from controller.SortByQT import QTSort
from controller.PushGETMarket import PushGetMarket
# from controller.GetToken import GetToken
application = Flask(__name__)
api = Api(application)

api.add_resource(HelloWorld, '/')
api.add_resource(Authenticate, '/auth')
api.add_resource(WebHook, '/webhook')
api.add_resource(SyncData, '/sync')
api.add_resource(PullData, '/pull')
api.add_resource(PriceSort, '/psort')
api.add_resource(QTSort, '/qsort')
api.add_resource(PushGetMarket, '/pushgetmarket')
# api.add_resource(GetToken, '/token')

if __name__ == '__main__':
    application.run(debug=True)
