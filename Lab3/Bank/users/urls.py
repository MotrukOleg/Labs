from django.urls import path
from . import views
from .views import UserList, UserDetail, UserDelete

urlpatterns = [
    path('userreg/', views.userreg, name='userreg'),  # сторінка реєстрації
    path('insertuser/', views.insertuser, name='insertuser'),  # обробка додавання користувача
    path('user_profile/', views.user_profile, name='user_profile'),  # сторінка профілю користувача
    path('user_extract/', views.userextract, name='userextract'),  # сторінка виписки
    path('userlog/', views.userlog, name='userlog'),  # сторінка входу
    path('loginuser/', views.loginuser, name='loginuser'),  # обробка входу
    # Інші ваші маршрути
    path('transfer_funds/<int:sender_id>/', views.transfer_funds, name='transfer_funds'),
    path('delete_account/', views.delete_current_user, name='delete_account'),

    path('users/', UserList.as_view(), name='user_list'),
    path('<int:pk>/', UserDetail.as_view(), name='user_detail'),
    path('delete/<int:pk>/', UserDelete.as_view(), name='user_delete'),
]
