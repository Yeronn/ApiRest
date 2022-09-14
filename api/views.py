from ast import Delete
import json
from telnetlib import GA
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from .models import Game
import json
# Create your views here.


class GameView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


    def get(self, request, id = 0):
        if (id > 0):
            games = list(Game.objects.filter(id = id).values())
            if len(games) > 0:
                game = games[0]
                datos = {'message' : "Success", 'game' : game}
            else:
                datos = {'message' : "Game not found"}
            return JsonResponse(datos)
        else:
            games = list(Game.objects.values()) #games listados atraves del ORM

            if  len(games) > 0:
                datos = {'message' : "Success", 'games' : games}
            else:
                datos = {'message' : "Games not found"}

            return JsonResponse(datos)


    def post(self, request):
        #print(request.body)
        jd = json.loads(request.body)
        #print(jd)
        Game.objects.create(name = jd['name'], gender = jd['gender'], website = jd['website']) #insertar en la base de datos
        datos = {'message' : "Success"}
        return JsonResponse(datos)


    def put(self, request, id):
        jd = json.loads(request.body)
        games = list(Game.objects.filter(id = id).values())
        if len(games) > 0:
            game = Game.objects.get(id = id)
            game.name = jd['name']
            game.gender = jd['gender']
            game.website = jd['website']
            game.save()
            datos = {'message' : "Success"}
            return JsonResponse(datos)
        else:
            datos = {'message' : "Games not found"}


    def delete(self, request, id):
        games = list(Game.objects.filter(id = id).values())
        if len(games) > 0:
            Game.objects.filter(id = id).delete()
            datos = {'message' : "Success"}
        else:
            datos = {'message' : "Games not found"}
        return JsonResponse(datos)