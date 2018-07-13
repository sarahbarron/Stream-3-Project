from django.contrib.auth.models import User

# to authenticate a user using their email address & password
class EmailAuth:
    
    #method to get an instance of a User using the email & verify the password
    def authenticate(self, username=None, password=None):
        
        try:
            # get an instance of the user
            user = User.objects.get(email=username)
            
            # if the user & password match return the user
            if user.check_password(password):
                return user
            
            # otherwise don't return anything
            return None
        
        # exception if the user does not exist return nothing
        except User.DoesNotExist:
            return None
    
    # method used by the Django authentication to get a user instance
    def get_user(self, user_id):
        
        try: 
            #get an instance of the User with the user id
            user = User.objects.get(pk=user_id)
            
            # if the user is active return the user 
            if user.is_active:
                return user
            
            # otherwise return nothing
            return None
        
        #exception if the user doesn't exist return nothing
        except User.DoesNotExist:
            return None
    