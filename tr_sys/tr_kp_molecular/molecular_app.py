from tr_ars.default_ars_app.ars_app import AppConfig as ARSAppConfig
from django.urls import path, include
from tr_ars.default_ars_app.api import *

class AppConfig(ARSAppConfig):
    name = 'tr_kp_molecular.molecular_app' # must be dot path for module
    actors = [('https://translator.broadinstitute.org/molepro_reasoner/query',
               'runquery', 'general')] # tuple of remote, name, channel
    app_path = 'kp-molecular'
    regex_path = '^' + app_path + '/'

### code below this line is required, but doesn't require updating in most cases

apipatterns = [path(r'', init_api_index(AppConfig.actors, AppConfig.app_path), name=AppConfig.app_path + '-api')]
for actor in AppConfig.actors:
    query_path = actor[1]
    query_name = AppConfig.app_path + '-' + query_path
    apipatterns.append(path(query_path, init_api_fn(actor), name=query_name))

urlpatterns = [
    path(r'api/', include(apipatterns)),
]

