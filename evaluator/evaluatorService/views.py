from django.shortcuts import render
from google.cloud import datastore
import os
# Create your views here.

def getProjects():
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/home/sudhir/Downloads/creator-innovation-8998992cc013.json'
    client = datastore.Client('creator-innovation')
    query = client.query(kind='ProjectData')
    id_list = list()
    for x in list(query.fetch()):
        id_list.append(x.id)
    
    return id_list
        