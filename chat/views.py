from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse
from .models import Room, Message


# Create your views here.
def home(request):
    return render(request, 'home.html')


def room(request, room):
    username = request.GET.get('username')  # henry
    room_details = Room.objects.get(name=room)
    return render(request, 'room.html', {

        'username': username,
        'room': room,
        'room_details': room_details,
    })


def checkview(request):
    room = request.POST['room_name']
    username = request.POST['username']

    if Room.objects.filter(name=room).exists():
        return redirect('/' + room + '/?username=' + username)
    else:
        new_room = Room.objects.create(name=room)
        new_room.save()
        return redirect('/' + room + '/?username=' + username)


def send(request):
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']

    new_msg = Message.objects.create(
        value=message, user=username, room=room_id
    )
    new_msg.save()
    # return HttpResponse('Messsage send SuccessFully')


def getMessge(request, room):
    room_detail = Room.objects.get(name=room)
    messge = Message.objects.filter(room=room_detail.id)
    return JsonResponse({
        "messages":list(messge.values())
    })

