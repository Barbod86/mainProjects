from django.urls import path
from .views import PlanList, PlanCreate, PlanEdit, PlanDelete, CustomLogin, Register
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', CustomLogin.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', Register.as_view(), name='register'),

    path('', PlanList.as_view(), name='plan_list'),
    path('create_plan/', PlanCreate.as_view(), name='plan_create'),
    path('edit_plan/<int:pk>/', PlanEdit.as_view(), name='plan_edit'),
    path('delete_plan/<int:pk>/', PlanDelete.as_view(), name='plan_delete'),
]
