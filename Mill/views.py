from datetime import datetime, timedelta
from django.shortcuts import render
from .models import GMillingMachine , GMillingMachineMapping


from django import template

from django.http import JsonResponse
from django.db import connection
from datetime import datetime, timedelta

# 在 Mill.views 模組中
def mill_chart_list(request):
    f = request.POST.get('f')
    m = request.POST.get('m')
    check = request.POST.get('check')
    day = request.POST.get('day')

    # 執行資料庫查詢和處理

    # 範例回傳資料
    data = [
        ["2023-05-12 08:00:00", 10.5],
        ["2023-05-12 09:00:00", 15.2],
        ["2023-05-12 10:00:00", 12.8],
        # 其他資料項目...
    ]
    print(data)
    return JsonResponse(data, safe=False)



def mill_report(request, day=None, millId=None, factoryId=None):
    millid = GMillingMachine.objects.filter(factoryid=factoryId).values('mill_id').distinct()

    millId_list = [m['mill_id'] for m in millid]

    context = {'millId': millId_list}

    menu = millId if millId is not None else "#1#2"
    m11 = ""
    m22 = ""

    if menu == '#1':
        m11, m22 = '#1', ''
    elif menu == '#2':
        m11, m22 = '', '#2'
    elif menu == '#1#2':
        m11, m22 = '#1', '#2'
    elif menu == '#2#3':
        m11, m22 = '#2', '#3'
    elif menu == '#3#4':
        m11, m22 = '#3', '#4'
    elif menu == '#5#6':
        m11, m22 = '#5', '#6'
    elif menu == '#7#8':
        m11, m22 = '#7', '#8'
        
    context['m11'] = m11
    context['m22'] = m22

    if day is None and millId is None:
        factory = factoryId
        menu = "#1#2"
        millId = "#1#2"
        now = datetime.now()
        day_str = now.strftime('%Y-%m-%d')
        nowDate = datetime.strptime(day_str + " 08:00:00", '%Y-%m-%d %H:%M:%S')
        yesDate = datetime.strptime(day_str + " 07:00:00", '%Y-%m-%d %H:%M:%S').date() + timedelta(days=1)
        data = GMillingMachine.objects.filter(factoryid=factoryId, datatime__gte=nowDate, datatime__lte=yesDate, mill_id=millId)

        context['factory'] = factory
        context['menu'] = menu
        context['day'] = day_str
        context['data'] = data
    else:
        factory = factoryId
        day_str = day
        menu = millId
        nowDate = datetime.strptime(day_str + " 08:00:00", '%Y-%m-%d %H:%M:%S')
        yesDate = datetime.strptime(day_str + " 08:00:00", '%Y-%m-%d %H:%M:%S') + timedelta(days=1)
        data = GMillingMachine.objects.filter(factoryid=factoryId, datatime__gte=nowDate, datatime__lt=yesDate, mill_id=millId)
        

        # print(factoryId)
        # print(nowDate)
        # print(yesDate)
        # print(millId)

        print(factory)
        print("SDfsfsf")
        print("SDfsfsf")
        print("SDfsfsf")
        print("SDfsfsf")
        print("SDfsfsf")
        
        context['factory'] = factory
        context['day'] = day_str
        context['menu'] = menu
    
        context['data'] = data
        # print("sdfdsf")
        # print(data)
        # for obj in data:
        #     # 存取每個GMillingMachine物件的屬性
        #     print(obj.factoryid)
        #     print(obj.datatime)
        #     print(obj.mill_id)
        #     print(obj.dtime)
        #     print(obj.motor_current_a)
            

    return render(request, 'Mill/Mill_Report.html', context)
