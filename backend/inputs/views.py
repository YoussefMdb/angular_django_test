from django.http import HttpRequest, HttpResponse
from .models import Label, Document
from .serializer import LabelSerializer, DocumentSerializer
from rest_framework import generics

# labels by id - get, update, delete
class LabelDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Label.objects.all()
    serializer_class = LabelSerializer

# get labels
class LabelList(generics.ListCreateAPIView):
    queryset = Label.objects.all()
    serializer_class = LabelSerializer

# documents by id - get, update, delete
class DocumentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer

# get documents
class DocumentList(generics.ListCreateAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer

# hello world
def helloWorld(HttpRequest):
    return HttpResponse("Hello World!")