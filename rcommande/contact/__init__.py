from pyramid.config import Configurator
from sqlalchemy import engine_from_config
from rcommande.models import DBSession, Base


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    includeme(config)
    return config.make_wsgi_app()


def includeme(config):
    settings = config.registry.settings
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine

    config.include('pyramid_jinja2')
    config.include('pyramid_celery')
    config.include('pyramid_fanstatic')
    config.include('deform_bootstrap')
    config.add_route('contact', '/')
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.scan()
