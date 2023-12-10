from django.template import RequestContext

def process_random(request):
    return RequestContext(request).push({"randomName": "[Context Processed]Yooh bro, we made it"})