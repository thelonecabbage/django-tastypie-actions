from __future__ import absolute_import

from django.conf.urls import url
from tastypie.exceptions import Unauthorized
from tastypie.utils import trailing_slash


def actionurls(self):
    urls = []
    for name, method in self.__class__.__dict__.iteritems():
        if hasattr(method, "is_auto_action"):

            actionName = name if not hasattr(method, "auto_action_name") \
                else method.auto_action_name

            if hasattr(method, "auto_action_url"):
                urls.append(
                    url(method.auto_action_url,
                        self.wrap_view(name),
                        name="api_action_%s" % actionName)
                )
            else:
                if not method.auto_action_static:
                    urls.append(
                        url(r"^(?P<resource_name>%s)/(?P<%s>[A-Za-z0-9]+)/%s%s$" % (
                            self._meta.resource_name,
                            self._meta.detail_uri_name,
                            actionName,
                            trailing_slash()),
                            self.wrap_view(name),
                            name="api_action_static_%s" % actionName)
                    )
                else:
                    urls.append(
                        url(r"^(?P<resource_name>%s)/%s%s$" % (
                            self._meta.resource_name,
                            actionName,
                            trailing_slash()),
                            self.wrap_view(name),
                            name="api_action_%s" % actionName)
                    )
    return urls


def action(name=None,
           allowed=['get', 'post', 'put', 'patch', 'delete'],
           require_loggedin=False,
           static=False,
           url=None):
    def wrap(method):
        def wrapped_f(self, request, *args, **kwargs):

            self.method_check(request, allowed=allowed)

            if require_loggedin is True:
                if not (request.user and request.user.is_authenticated()):
                    raise Unauthorized(
                        "User must be logged in to perform this opperation")

            res = method(self, request, *args, **kwargs)
            return res

        wrapped_f.is_auto_action = True
        wrapped_f.auto_action_static = static

        if not name is None:
            wrapped_f.auto_action_name = name

        if not url is None:
            wrapped_f.auto_action_url = url

        return wrapped_f
    return wrap
