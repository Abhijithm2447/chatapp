from django.shortcuts import render
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from chatapp.mixins import HttpResponseMixin
from chatapp.utils import is_json
from chatapp import db_handler

import json
import pdb
#________________________________________________________________________________
"""
Create Dataset - for intent classification
url: insert_data/
input
{
    "data" : <string data>,
    "intent" : <string intent>
}
"""
#________________________________________________________________________________
@method_decorator(csrf_exempt, name='dispatch')
class CreateDataset(View, HttpResponseMixin):
    def get(self, request, *args, **kwargs):
        json_data = json.dumps({'message':'This is from get method'})
        return self.render_to_http_response(json_data)
    def post(self, request, *args, **kwargs):
        result = {}
        error = []
        status = 200
        data = request.body
        if is_json(data):
            # pdb.set_trace()
            data = json.loads(data)
            input_data = data["data"]
            input_intent = data["intent"]
            context = {
                "query" : input_data,
                "intent" : input_intent
            }
            result, error = db_handler.insert_query(context)      
            # if len(error) > 0:
            #     status = 400
        else:
            print("This is not valid json")
        json_data = json.dumps({"result" : result, "error" : error})
        return self.render_to_http_response(json_data, status = status)  
#________________________________________________________________________________

#________________________________________________________________________________
"""
Retrieve all intents 
url: all_intent/
input
{
}
"""
#________________________________________________________________________________
@method_decorator(csrf_exempt, name='dispatch')
class RetrieveAllIntents(View, HttpResponseMixin):
    def get(self, request, *args, **kwargs):
        json_data = json.dumps({'message':'This is from get method'})
        return self.render_to_http_response(json_data)
    def post(self, request, *args, **kwargs):
        result = {}
        error = []
        status = 200
        data = request.body
        if is_json(data):
            # pdb.set_trace()
            data = json.loads(data)            
            context = {                
            }
            result, error = db_handler.retrieve_all_intent(context)      
            if len(error) > 0:
                status = 400
        else:
            print("This is not valid json")
        json_data = json.dumps({"result" : result, "error" : error})
        return self.render_to_http_response(json_data, status = status)  
#________________________________________________________________________________
