from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('add_request/',views.add_request,name='add_request'),
    path('browse_requests/',views.browse_requests,name='browse_requests'),
    path('browse_requests/<int:transferRequest_id>/',views.request_detail,name="request_detail"),
]
