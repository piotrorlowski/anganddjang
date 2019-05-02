from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import ToDoList
from .serializers import ToDoListSerializer

@csrf_exempt
def todolist_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        to_do_lists = ToDoList.objects.all()
        serializer = ToDoListSerializer(to_do_lists, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ToDoListSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def todolist_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        to_do_list = ToDoList.objects.get(pk=pk)
    except ToDoList.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ToDoListSerializer(to_do_list)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ToDoListSerializer(to_do_list, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        to_do_list.delete()
        return HttpResponse(status=204)