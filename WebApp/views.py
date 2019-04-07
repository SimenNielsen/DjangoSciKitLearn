from django.shortcuts import render
from .rock_paper_scissors import RPS
from .tic_tac_toe import TTT
from django.http import JsonResponse
from django.http import HttpResponse
import json

# Create your views here.

def index(request):
    return render(request, 'index.html')

def ML_RPS(request):
    if request.method == 'GET':
        return render(request, 'ml_rps.html')
    else:
        game = RPS()
        if request.POST.get('action') == 'play':
            human_choice = request.POST.get('human_c')
            turn_order = request.POST.get('turn_order') #0=computer,1=player,2=both
            prediction = game.play_RPS(turn_order,int(human_choice))
            data = game.get_RPS_data()
            #return HttpResponse(json.dumps(response), content_type='application/json')
            return HttpResponse(json.dumps(
                {
                    'prediction':int(prediction), 
                    'result':game.process_game([int(prediction), int(human_choice)]),
                    'data':data.tolist(),
                }), content_type='application/json')
        elif request.POST.get('action') == 'reset':
            dataset = game.generate_first(2)
            game.save_RPS_data(dataset)
            data = game.get_RPS_data()
            return HttpResponse(json.dumps(
                {
                    'data':data.tolist(),
                }), content_type='application/json')
        elif request.POST.get('action') == 'train':
            dataset = game.generate_first(500)
            game.save_RPS_data(dataset)
            data = game.get_RPS_data()
            return HttpResponse(json.dumps(
                {
                    'data':data.tolist(),
                }), content_type='application/json')
        else:
            return None

def ML_TTT(request):
    if request.method == 'GET':
        return render(request, 'ml_ttt.html')
    else:
        ttt = TTT()
        if request.POST.get('action') == 'play':
            history = request.POST.get('history')
            
            prediction = play_RPS(turn_order,int(human_choice))
            data = get_RPS_data()
            #return HttpResponse(json.dumps(response), content_type='application/json')
            return HttpResponse(json.dumps(
                {
                    'prediction':int(prediction), 
                    'result':process_game([int(prediction), int(human_choice)]),
                    'data':data.tolist(),
                }), content_type='application/json')
        elif request.POST.get('action') == 'reset':
            dataset = generate_first(2)
            save_RPS_data(dataset)
            data = get_RPS_data()
            return HttpResponse(json.dumps(
                {
                    'data':data.tolist(),
                }), content_type='application/json')
        elif request.POST.get('action') == 'train':
            ttt.train(100000)
            return HttpResponse(json.dumps(
                {
                    'data':'data.tolist()',
                }), content_type='application/json')
        else:
            return None