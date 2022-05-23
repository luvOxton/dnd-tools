from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.generic import TemplateView, ListView

# SurgeTables Dep
import pandas as pd
import random

# Create your views here.


def surgeTableView(request):
    # return HttpResponse('Hello World') # testing
    userInput = request.GET.get('indexInput')
    results = {
        'success':False,
        'input': '',
    }

    if userInput != None:
        results['data'] = getValue(userInput)
        results['success'] = True
        results['input'] = userInput

    return render(request, 'surgeTable.html', results)


def printFull(indexSurge, df):
    Effect = df.iloc[indexSurge]['Effect']
    Intensity = str(df.iloc[indexSurge]['Intensity'])

    print('Rolled: ' + str(indexSurge + 1))
    print('Effect: ' + Effect)
    print('Intensity: ' + Intensity)

    return ({
        'rolled': str(indexSurge + 1),
        'effect': Effect,
        'intensity': Intensity,
    })


def getValue(userInput):
    df = pd.read_excel('wild_magic.xlsx')
    userIn = userInput
    intensityLevel = ['mid', 'weak', 'extreme'] # As far as I know, this is all the possible intensity levels. You can probably update just the list, and it'll still work.

    usedDataframe = df 
    indexSurge = 0

    if userIn.isnumeric() and int(userIn) in range(0, len(df)): # Checks if the input is numeric and between 0 - 414.
        indexSurge = int(userIn) - 1
    elif userIn.lower() in intensityLevel: # Checks if the input is in the intensityLevel List.
        usedDataframe = df[df.Intensity == userIn]
        indexSurge = random.randint(0, len(usedDataframe))
    else: # Any other input which would have been recognized as invalid, will instead return a random.
        indexSurge = random.randint(0, len(df))

    return printFull(indexSurge, usedDataframe)
