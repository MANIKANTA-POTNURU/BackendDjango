from django.http import JsonResponse, HttpResponseBadRequest, HttpResponse
from django.shortcuts import redirect, render
import os
from django.http import JsonResponse, HttpResponseBadRequest

def create_file(request):
    filename = request.POST.get('filename')
    content = request.POST.get('content')
    if not (filename and content):
        return HttpResponseBadRequest("Missing filename or content")

    # Create the 'media' directory if it doesn't exist
    media_dir = 'media'
    if not os.path.exists(media_dir):
        os.makedirs(media_dir)

    # Save file to the 'media' directory
    save_path = os.path.join(media_dir, filename)
    with open(save_path, 'w') as file:
        file.write(content)

    return JsonResponse({"message": "File created successfully"}, status=200)


def get_files(request):
    file_list = os.listdir('media')
    return JsonResponse({"files": file_list}, status=200)


def get_file(request, filename):
    file_path = os.path.join('media', filename)
    if not os.path.exists(file_path):
        return HttpResponseBadRequest("File not found")

    with open(file_path, 'r') as file:
        file_content = file.read()

    return HttpResponse(file_content, content_type='text/plain')

def upload_file(request):
    return render(request, 'upload_file.html')

