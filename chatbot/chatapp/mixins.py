from django.http import HttpResponse
class HttpResponseMixin(object):
    def render_to_http_response(self, json_data, status=200):
        #1000 lines of code
        return HttpResponse(json_data, content_type='application/json', status = status)
