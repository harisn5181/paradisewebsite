
from django.urls import path

from paradiseapp import views
app_name='paradiseapp'

urlpatterns = [

    path('',views.index,name="index"),
    path('chatbot/<int:chatbot_id>/',views.detail,name='detail'),
    path('add/',views.addchatbot,name='addchatbot'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/', views.delete, name='delete')
]
