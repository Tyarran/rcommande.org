from pyramid.config import Configurator


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    includeme(config)
    return config.make_wsgi_app()

def includeme(config):
    config.include('pyramid_jinja2')
    config.include('pyramid_celery')
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.scan()
