

from django.urls import path
from . import views as v


urlpatterns = [

    # 메인 페이지
    path('', v.user_index, name='user_index'),

]