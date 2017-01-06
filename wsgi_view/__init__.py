from importlib import import_module

from django.core.exceptions import ImproperlyConfigured
from django.http import HttpResponse
from django.utils import six
from django.utils.decorators import classonlymethod
from django.views import View


class WsgiView(View):
    application = None

    def __init__(self, **kwargs):
        super(WsgiView, self).__init__(**kwargs)
        self.init_application()

    def init_application(self):
        application = self.application
        if callable(application):
            return
        if isinstance(application, six.string_types):
            self.application = import_module(application)
            return
        raise ImproperlyConfigured(f'{application} is not a WSGI application')

    @classonlymethod
    def as_view(cls, **initkwargs):
        view = super(WsgiView, cls).as_view(**initkwargs)
        return view

    def dispatch(self, request, *args, **kwargs):
        application = self.application
        path = args[0] if len(args) > 0 else ''
        environ = self.get_environ(request, path)
        self.response = HttpResponse()
        result = application(environ, self.start_response)
        try:
            for data in result:
                if data:
                    self.response.write(data)
        finally:
            if hasattr(result, 'close'):
                result.close()
        return self.response

    def get_environ(self, request, path):
        environ = request.environ.copy()
        if not path.startswith('/'):
            path += '/'
        environ['SCRIPT_NAME'] += path
        environ['PATH_INFO'] = path
        return environ

    def start_response(self, status, headers, exc_info=None):
        if exc_info:
            raise exc_info[1].with_traceback(exc_info[2])
        self.response.status_code = int(status.split(' ', 1)[0])
        return self.response.write
