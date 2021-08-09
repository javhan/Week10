
from django.shortcuts import render
## For sending JSON Responses
from django.http import JsonResponse
## To serialize objects into json strings
from django.core.serializers import serialize
## To turn json strings into dictionaries
import json
## The Dog Model
from .models import Dog, Cat
## View class
from django.views import View
## GetBody
from .helpers import GetBody

# class for "/turtle" routes
class PetView(View):
    ## Route to get all Turtles
    def get(self, request, pet):
        ## get all the Turtles
        all = Dog.objects.all()
        ## Turn the object into a json string
        serialized = serialize("json", all)
        ## Turn the json string into a dictionary
        finalData = json.loads(serialized)
        ## Send json response, turn safe off to avoid errors
        return JsonResponse(finalData, safe=False)

    ## Route to create a turtle
    def post (self, request, pet):
        ## get data from the body
        body = GetBody(request)
        print(body)
        ## create new turtle
        dog = Dog.objects.create(name=body["name"], age=body["age"])
        ## turn the new turtle into json string then a dictionary
        finalData = json.loads(serialize("json", [dog])) #turtle in array to be serializable
        ## Send json response
        return JsonResponse(finalData, safe=False)

# class for "/turtle/<id>" routes
class PetViewID(View):
    ## Function to show 1 Turtle
    def get (self, request, pet, id):
        ## get the turtle
        if pet.lower() == "dog": 
            turtle = Dog.objects.get(id=id)
        elif pet.lower() == "cat":
            turtle = Cat.objects.get(id=id)
        ## serilize then turn into dictionary
        finalData = json.loads(serialize("json", [turtle]))
        ## send json response
        return JsonResponse(finalData, safe=False)

    ## Function for updating turtle
    def put (self, request, pet, id):
        ## get the body
        body = GetBody(request)
        ##update turtle
        ## ** is like JS spread operator
        Dog.objects.filter(id=id).update(**body)
        ## query for turtle
        turtle = Dog.objects.get(id=id)
        ## serialize and make dict
        finalData = json.loads(serialize("json", [turtle]))
        ## return json data
        return JsonResponse(finalData, safe=False)

    def delete (self, request, pet, id):
        ## query the turtle
        turtle = Dog.objects.get(id=id)
        ## delete the turtle
        turtle.delete()
        ## serilize and dict updated turtle
        finalData = json.loads(serialize("json", [turtle]))
        ##send json response
        return JsonResponse(finalData, safe=False)
