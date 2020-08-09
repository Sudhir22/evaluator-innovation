from django.shortcuts import render
from google.cloud import datastore
from django.http import HttpResponse
from django.template import Context,loader
import random,copy
import os
# Create your views here.

def getProjects(request):
    '''
    Used if running locally 
    
    x = os.getcwd()
    #os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = x+'/gender-innovation-309b59e30541.json'
    
    '''
    client = datastore.Client('gender-innovation')
    query = client.query(kind='ProjectData')
    id_list = list()
    for x in list(query.fetch()):
        id_list.append(x.id)
    
    
    return render(request,"evaluatorService/projectList.html",{"id_list":id_list})
    
    

'''

#Testing code

if __name__ == "__main__":
    print(getProjects("test"))

'''