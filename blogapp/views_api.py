from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User

from django.contrib.auth import authenticate,login


class LoginView(APIView):
    def post(self,request):
        response={}
        response['status'] = 500
        response['message'] = 'Something went wrong'
        
        try:
            data=request.data

            if data.get('username') is None:
                response['message'] = 'Username not found'

                raise Exception('Username not found')
 
            if data.get('password') is None:
                response['message'] = 'Password not found'

                raise Exception('Password not found')  

            check_user=User.objects.filter(username=data.get('username')).first()

            if check_user is None:
                response['message'] = 'Invalid Username'
                raise Exception('Invalid Username')

            user_obj = authenticate(username=data.get('username'),password=data.get('password'))

            if user_obj:
                login(request,user_obj)
                response['message']='Welcome'
                response['status'] = 200
            else:
                response['message']="Invalid password"
                raise Exception('Invalid Password')


        except Exception as e:
            print(e)          

        return Response(response)   
LoginView=LoginView.as_view()


class RegisterView(APIView):
    def post(self,request):
        response={}
        response['status'] = 500
        response['message'] = 'Something went wrong'
        
        try:
            data=request.data

            if data.get('username') is None:
                response['message'] = 'Username not found'

                raise Exception('Username not found')
 
            if data.get('password') is None:
                response['message'] = 'Password not found'

                raise Exception('Password not found')  

            check_user=User.objects.filter(username=data.get('username')).first()

            if check_user:
                response['message'] = 'Username already Taken'
                raise Exception('Username already taken')

            user_obj=User.objects.create(username=data.get('username'))
            user_obj.set_password(data.get('password'))
            user_obj.save()
            response['message']='User created'
            response['status']=200

            


        except Exception as e:
            print(e)          

        return Response(response)   
RegisterView=RegisterView.as_view()