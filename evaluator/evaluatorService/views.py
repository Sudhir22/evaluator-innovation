from django.shortcuts import render
from google.cloud import datastore
import os
# Create your views here.

def getProjects():
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/home/sudhir/Desktop/InnovationFieldExperiment/Evaluator/gender-innovation-309b59e30541.json'
    client = datastore.Client('gender-innovation')
    query = client.query(kind='ProjectData')
    id_list = list()
    for x in list(query.fetch()):
        id_list.append(x.id)
    
    return id_list


'''
Testing code

if __name__ == "__main__":
    print(getProjects())
    
'''        