from django.http import JsonResponse

def is_logged_in(view_func):
    """ 
    Decorator to verify access to protected endpoints.

    :param view_func: The function to be decorated

    :return: Decorated function.
    """

    def new_view_func(request):
        """ 
        Checks whether the user is logged in.

        :param request: The incoming request to be intercepted.

        :return: view_func on success, not logged in on failure.
        """
            
        if request.session.get('logged_in',False):
            return view_func(request)
        else:
            return JsonResponse({'status' : 'User not logged in'})

    return new_view_func
