# FILE: /project/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static #1:

urlpatterns = [
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #2:

if settings.DEBUG: #3:
    import debug_toolbar #4:
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)), #5:
    ] + urlpatterns


# ------------------------------------------------------------------
#1: Importa a função static de django.conf.urls. Ela é usada para servir arquivos de mídia em um ambiente de desenvolvimento.
#2: Configura o Django para servir arquivos de mídia durante o desenvolvimento. O argumento settings.MEDIA_URL define a URL para acessar os arquivos, e settings.MEDIA_ROOT aponta para o diretório físico onde eles são armazenados. Isso só deve ser usado em desenvolvimento, pois o Django não serve arquivos de mídia em produção.
#3: Verifica se o modo de depuração (DEBUG) está ativado. Se estiver, a lógica abaixo será executada, permitindo a ativação de ferramentas como o Django Debug Toolbar.
#4: Importa o pacote debug_toolbar, necessário para que a barra de ferramentas de depuração seja incluída nas URLs e exibida no navegador.
#5: Adiciona uma rota (__debug__/) para o Django Debug Toolbar. Quando o modo de depuração está ativado, essa rota permite acessar as ferramentas de depuração diretamente no navegador.

# https://linktr.ee/edsoncopque