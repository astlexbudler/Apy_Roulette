from django.shortcuts import render
from . import models
import datetime
from django.db.models import Q

def user_index(request):

    # 사용자 IP 가져오기
    user_ip = request.META.get('REMOTE_ADDR')
    if user_ip == '' or user_ip == None:
        user_ip = '127.0.0.1'

    # IP를 이용해서 방문자 정보 저장
    today_ip_has_visit = models.VISIT.objects.filter(
        Q(ip=user_ip) &
        Q(visit_date__gte=datetime.datetime.now().replace(hour=0, minute=0, second=0)) &
        Q(visit_date__lte=datetime.datetime.now().replace(hour=23, minute=59, second=59))
    ).exists()
    if not today_ip_has_visit: # 오늘 방문한 적이 없다면
        models.VISIT.objects.create(ip=user_ip)

    # 방문자수 가져오기
    visit_count = models.VISIT.objects.filter(
        Q(visit_date__gte=datetime.datetime.now().replace(hour=0, minute=0, second=0)) &
        Q(visit_date__lte=datetime.datetime.now().replace(hour=23, minute=59, second=59))
    ).count()

    return render(request, 'index.html', {
        'visit_count': visit_count
    })