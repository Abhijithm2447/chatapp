from django.shortcuts import render
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
# utils
from recognitionapp.utils import is_json
from recognitionapp.mixins import HttpResponseMixin

import json
import base64
from PIL import Image
from io import BytesIO
import PIL
import numpy as np
import cv2
import pdb

# custom
from recognitionapp.predict_object import predict_object


# ___________________________ Object Recognition ____________________________
""" 
url: rec_object/
input: {
    'image' : <base64 encypted image>
}
"""
# ___________________________________________________________________________
@method_decorator(csrf_exempt, name='dispatch')
class RecognizeObject(HttpResponseMixin, View):
    def get(self, request, *args, **kwargs):
        # predict_object()
        json_data = json.dumps({'msg':'This is from get method'})
        return self.render_to_http_response(json_data)
    def post(self, request, *args, **kwargs):
        result = {}
        error = []
        
        data = request.body
        main_flag = False
        if is_json(data):
            data = json.loads(data)
            main_flag = True
        else:
            main_flag = True
            data = request.POST
        if main_flag:
            if 'image' in data:            
                image_bs64 = data['image']
                try:
                    enc = base64.b64decode(image_bs64)
                    # pdb.set_trace()
                    image_pil = Image.open(BytesIO(base64.b64decode(enc)))                     
                    # image_np = np.array(image_pil, dtype=np.uint8)
                    # if image_np.shape[2] == 4:
                    #     #convert the image from RGBA2RGB
                        
                    #     image = cv2.cvtColor(image_np, cv2.COLOR_RGBA2RGB)
                    # # convert to PIL image format
                    # image = cv2.cvtColor(image_np, cv2.COLOR_RGB2BGR)
                    
                    p_status = True               
                except:
                    p_status = False                    
                    error.append("Invalid image or base64 encryption error")                                 
            else:
                status = 406
                p_status = False
            if p_status:
                detected_classes = predict_object(image_pil)
                result["detected_classes"] = detected_classes
        json_data = json.dumps({'result':result, "error" : error})
        return self.render_to_http_response(json_data)

