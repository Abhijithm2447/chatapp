from django.shortcuts import render
from django.views.generic import View
from recognitionapp.mixins import HttpResponseMixin
import json

from recognitionapp.predict_object import predict_object

# ___________________________ Object Recognition ____________________________
""" 
url: rec_object/
input: {
    'image' : <base64 encypted image>
}
"""
# ___________________________________________________________________________
class RecognizeObject(HttpResponseMixin, View):
    def get(self, request, *args, **kwargs):
        predict_object()
        json_data = json.dumps({'msg':'This is from get method'})
        return self.render_to_http_response(json_data)
    def post(self, request, *args, **kwargs):
        json_data = json.dumps({'msg':'This is from post method'})
        return self.render_to_http_response(json_data)

