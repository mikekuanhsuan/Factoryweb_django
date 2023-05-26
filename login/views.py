
# Create your views here.



from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required


import logging

logger = logging.getLogger(__name__)

from django.http import JsonResponse

import json
from django.http import JsonResponse
import json
from django.http import JsonResponse


import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def my_view(request):
    if request.method == 'POST':
        try:
            json_data = json.loads(request.body)  # 解析请求体中的JSON数据
            account = json_data.get('Account')  # 获取JSON数据中的'account'字段
            password = json_data.get('Password')  # 获取JSON数据中的'password'字段
            print(account)
            # 进行数据验证和处理
            # 如果数据没有问题，可以返回一个包含'true'的JSON响应
            if account !="" and password !="":
                # 在这里进行你的数据处理逻辑
                request.session['Account'] = account
                return JsonResponse({'success': True})
            else:
                return JsonResponse({'success': False, 'error': 'Invalid data'})
        except json.JSONDecodeError:
            return JsonResponse({'success': False, 'error': 'Invalid JSON data'})




def login_list(request):
    return render(request, 'login/login_list.html')

def home(request):
    return render(request, 'home/index.html', {'title': 'Home Page'})