from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout as auth_logout
from .models import User, Person, Extract
from datetime import datetime
from django.db import connection
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializers import UserSerializer

def userreg(request):
    return render(request, 'myapp/userreg.html', {})

def insertuser(request):
    vuid = request.POST['tuid']
    vuname = request.POST['tuname']
    vuemail = request.POST['tuemail']
    vucontact = request.POST['tucontact']
    vudoc = request.POST['tudoc']
    vupass = request.POST['tupass']
    vums = request.POST['tums']
    terms = '1'
    per = Person(ID=vuid, Phone_Number=vucontact, Documents=vudoc, Email=vuemail)
    per.save()
    us = User(
        ID=vuid,
        Terms_Of_Use=terms,
        Hashed_Password=vupass,
        Mother_Surname=vums,
        Money_Left=1000.0,
        User_Created=datetime.now()
    )
    us.save()
    request.session['user_id'] = us.ID  # Зберегти ID у сесії
    request.session['balance'] = float(us.Money_Left)
    return redirect('user_profile')  # виконує перенаправлення на user_profile

def user_profile(request):
    us = request.user  # Отримання поточного користувача
    return render(request, 'myapp/user_profile.html', {'us': us})




def userextract(request):
    user_id = request.session.get('user_id')  # Отримуємо ID користувача з сесії
    if not user_id:
        return redirect('userlog')  # Якщо ID не знайдено, перенаправляємо на сторінку входу

    with connection.cursor() as cursor:
        cursor.callproc('TakeExtract', [user_id])

        total_summary = cursor.fetchall()

        cursor.nextset()
        columns = [col[0] for col in cursor.description]
        operation_details = [
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ]

    return render(request, "myapp/user_extract.html", {
        'total_summary': total_summary,
        'operation_details': operation_details
    })



def transfer_funds(request, sender_id):
    if request.method == 'POST':
        receiver_id = int(request.POST['receiver_id'])
        transfer_amount = float(request.POST['transfer_amount'])
        choice = bool(int(request.POST['choice']))  # 1 or 0 for True/False

        try:
            with connection.cursor() as cursor:
                cursor.callproc('transfer_funds', [sender_id, receiver_id, transfer_amount, choice])
            with connection.cursor() as cursor:
                cursor.execute("SELECT Money_Left FROM user WHERE ID = %s", [sender_id])
                balance = cursor.fetchone()
                if balance:
                    request.session['balance'] = float(balance[0])  # Convert to float before saving

            messages.success(request, 'Transfer completed successfully!')
            return redirect('user_profile')
        except Exception as e:
            messages.error(request, f'Error during transfer: {str(e)}')
            return redirect('user_profile')

    return render(request, 'myapp/transfer_funds.html')


def userlog(request):
    return render(request, 'myapp/userlog.html')


def loginuser(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        password = request.POST.get('password')
        try:
            user = User.objects.get(ID=user_id)
            if user.Hashed_Password == password:
                request.session['user_id'] = user.ID
                request.session['balance'] = float(user.Money_Left)
                return redirect('user_profile')
            else:
                messages.error(request, 'Неправильний ID або пароль')
        except User.DoesNotExist:
            messages.error(request, 'Користувача з таким ID не існує')

    return redirect('userlog')

def delete_current_user(request):
    user_id = request.session.get('user_id')

    if user_id:
        try:

            user = User.objects.get(ID=user_id)
            user.delete()
            messages.success(request, 'Ваш акаунт успішно видалено.')

            del request.session['user_id']
        except User.DoesNotExist:
            messages.error(request, 'Користувача з таким ID не існує.')
    else:
        messages.error(request, 'Ви не увійшли в систему.')

    return redirect('userreg')

# yourapp/views.py

# Отримати список користувачів
class UserList(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

# Отримати одного користувача
class UserDetail(APIView):
    def get(self, request, pk):
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = UserSerializer(user)
        return Response(serializer.data)

# Видалити користувача
class UserDelete(APIView):
    def delete(self, request, pk):
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
