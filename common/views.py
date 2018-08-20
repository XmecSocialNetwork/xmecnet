"""
common.views
~~~~~~~~~~~~

This module implements the various endpoints for http requests.

:author: Siva R, Jeswin Cyriac
"""

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail

from .models import User
from .decorators import is_logged_in

import random
import datetime
import json


# To be removed.
@csrf_exempt
def register(request):
    """ 
    User registration endpoint.
    
    :http methods allowed: [POST]

    :params: email (string), name (string), password (string), dobday (string), 
    dobmonth (string), dobyear (string), branch (string), roll_no(string).

    :return: success, error codes on failure.
    :rtype: :json:
    """
    
    if request.method == "POST":
        try:
            data = json.loads(request.body.decode("utf-8"))
            
            if not User.objects.filter(email=data['email']).exists():
                try:
                    user = User.create(email=data['email'],
                                       name=data['name'],
                                       password=data['password'],
                                       dobday=data['dobday'],
                                       dobmonth=data['dobmonth'],
                                       dobyear=data['dobyear'],
                                       branch=data['branch'],
                                       roll_no = data.get('roll_no', None)
                    )

                    return JsonResponse({'status': "success"})

                except Exception as e:
                    return JsonResponse({'status': 'Invalid data'},
                                        status=400)

            else:
                return JsonResponse({'status': 'User already registered'},
                                        status=400)
            
        except Exception as e:
            return JsonResponse({'status': 'Something unexpected happened'},
                                status=500)
    else:
        return JsonResponse({'status': 'Invalid request'}, status=405)


@csrf_exempt
def login(request):
    """ 
    Endpoint for user authentication.

    :http methods allowed: ['POST']

    :params: email (string), password (string)

    :return: success, error codes on failure.
    :rtype: :json:
    """
    
    if request.method == "POST":
        try:
            data = json.loads(request.body.decode("utf-8"))
            
            if User.objects.filter(email=data['email']).exists():
                try:
                    user = User.login(data['email'], data['password'])

                    if user:
                        request.session['logged_in'] = True
                        return JsonResponse({'status': "success"})

                    else:
                        return JsonResponse({'status': 'Invalid password'}, status=403)

                except Exception as e:
                    return JsonResponse({'status': 'Error during login'}, status=400)

            else:
                return JsonResponse({'status': 'User not registered'}, status=400)

        except Exception as e:
            return JsonResponse({'status': 'Something unexpected happened'}, status=500)
    else:
        return JsonResponse({'status': 'Invalid request'}, status=403)



@csrf_exempt
@is_logged_in
def logout(request):
    """ 
    Logs out the user.
    
    :http methods allowed: ['POST']

    :params: None

    :return: success, Error codes on failure.
    :rtype: :json:
    """
    
    try:
        request.session.flush()
        return JsonResponse({"status":"success"})

    except Exception as e:
        return JsonResponse({'status': 'Failed'}, status=500)


"""
@csrf_exempt
def otp(request):
    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        request.session["otp"]=random.randint(1001,9999)
        send_mail(
        'OTP from Xmec Network',
        'Hello Mecian,We are glad to see you back.Enter this Verification code '+str(request.session["otp"])+'in the app to continue ',
        'jeswincyriac.k@gmail.com',
        [data["email"]],
        fail_silently=False,
        )
        print("reached here")
        return JsonResponse({'status': "Success"})
    except Exception as e:
        # To be changed during production
        print(e)
        return JsonResponse({'status': 'Failed'}, status=500)

@csrf_exempt
@is_logged_in
def search(request):
    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)

        return JsonResponse({"status":"successfull"})
    except Exception as e:
        # To be changed during production
        print(e)
        return JsonResponse({'status': 'Failed'}, status=500)


@csrf_exempt
def trying(request):
    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)

        print(request.session['logged_in'])
        return JsonResponse({'tryingreceived ': True})
    except Exception as e:
        # To be changed during production
        print(e)
        return JsonResponse({'Error': 'Something unexpected happened'}, status=500)

@csrf_exempt
def trying2(request):
    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)

        print(request.session['hai'])
        return JsonResponse({'tryingreceived ': True})
    except Exception as e:
        # To be changed during production
        print(e)
        return JsonResponse({'Error': 'Something unexpected happened'}, status=500)
"""
