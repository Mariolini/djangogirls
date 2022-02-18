from django.shortcuts import redirect, render
import os.path

from .models import BpEntry
from django.utils import timezone

def bloodpressure_main(request):
    temppath = os.path.join('bloodpressure', 'bloodpressure_main.html')
    return render(request, temppath, {})
