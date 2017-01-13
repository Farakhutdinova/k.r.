from pyramid.config import Configurator
from sqlalchemy import engine_from_config
from pyramid.static import static_view

from .security import groupfinder

from .models import (
    DBSession,
    Base,
)


def main(global_config, **settings):
    config = Configurator(settings=settings)
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine

    config = Configurator(settings=settings,
                          root_factory='sad.Models.Root')
    config.include('pyramid_jinja2')
    config.add_route('home', '/')
    config.add_static_view('static', 'sad:static', cache_max_age=3600)
    config.add_static_view('deform_static', 'deform:static/')
    config.scan('.views')
    return config.make_wsgi_app()
