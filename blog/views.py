from django.shortcuts import render
import os.path

def post_list(request):
    temppath = os.path.join('blog', 'post_list.html')
    return render(request, temppath, {})