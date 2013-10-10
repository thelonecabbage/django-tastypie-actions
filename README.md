tastypie-actions
================

Adds the ability to (easily) append actions to Tastypie resources, without messing around with regex and url paths. (clean, readable code) 

###WHY?
**CLEAN CODE!** The normal way to add actions to your resources is by overriding the prepend_urls method and adding custom regex urls to match to your view.  The problem with this is that it is time consuming and makes the code harder to read/maintain.  tastypie-actions implements a solution similar to most MVC frameworks, allowing method names to pass through to the URI. 

##example client:
* __actionurls(self)__ Must be added to the prepend_urls method, though it can be concatenated to other urls.  This allows for the injection of the action urls. **required**
* __name__ Optional parameter to set the public name (in the uri) of the action. default is the decorated method name
* __allowed__ A list of allowed http verbs (methods) for this action. default = ['get', 'post', 'put', 'patch', 'delete']
* **require_loggedin** Does this action require an active user session to access. **default=False**
* __static__ Does the action attatch to the /resource/{action} or the /resource/{id}/action.  default=False

Below urls would look something like this:
```
    /api/v1/user/login/
    /api/v1/user/register/
    /api/v1/user/forgotpassword/
    /api/v1/user/12345678/logout/
    /api/v1/user/12345678/changepassword/
```

 ```python

from tastypie-actions import actionurls, action

 class UserResource(ModelResource):
       
         class Meta:
            queryset = User.objects.all()
            resource_name = 'user'
            detail_uri_name = 'slug'
            object_class = User
            authentication = SessionAuthentication()
            authorization = DjangoAuthorization()
            
        def prepend_urls(self):
            return actionurls(self)

        @action(name='login', allowed=['post'], static=True)
        def user_login(self, request, **kwargs):
            pass
        
        @action(allowed=['get'], require_loggedin=True)
        def logout(self, request, **kwargs):
            pass

        @action(allowed=['post'], static=True)
        def register(self, request, **kwargs):
            pass

        @action(allowed=['post'], require_loggedin=True)
        def changepassword(self, request, **kargs):
            pass

        @action(allowed=['post'], static=True)
        def forgotpassword(self, request, **kwargs):
            pass

```