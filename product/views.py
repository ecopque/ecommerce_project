# FILE: /product/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.list import ListView #1:
from django.views import View #2:
from . import models
from django.views.generic.detail import DetailView #8:
from django.contrib import messages #11:
from django.http import HttpResponse #12:
from django.urls import reverse #13:

class ProductList(ListView): #3:
    # IMPORT⬇: /product/models.py
    model = models.Product #4:

    template_name = 'product/list.html' #5:
    context_object_name = 'products' #6:
    paginate_by = 3 #7:

class ProductDetail(DetailView): #9:
    model = models.Product
    template_name = 'product/detail.html'
    context_object_name = 'product'

    #IMPORT⬇: /product/urls.py
    slug_url_kwarg = 'slug' #10:

class AddToCart(View):
    def get(self, *args, **kwargs):
        http_referer = self.request.META.get('HTTP_REFERER', reverse('product:list')) #14: #15:
        variation_id = self.request.GET.get('vid') #16:

        if not variation_id: #17:
            messages.error(self.request, 'Product does not exist.') #18:
            return redirect(http_referer) #19:
        
        # IMPORT⬇: /product/models.py
        variation = get_object_or_404(models.Variation, id=variation_id) #20:
        if not self.request.session.get('cart'): #21:
            self.request.session['cart'] = {} #22:
            self.request.session.save() #23:
        
        cart = self.request.session['cart'] #24:

        if variation_id in cart:
            ...
        else:
            ...

        return HttpResponse(f'{variation.product} {variation.name}') #25:

class RemoveFromCart(View):
    ...

class Cart(View):
    ...

class Finish(View):
    ...
    

# ------------------------------------------------------------------
#11: O módulo messages é parte da biblioteca django.contrib, que fornece funcionalidades comuns e reutilizáveis. Ele permite que mensagens temporárias sejam armazenadas na sessão de um usuário para exibição posterior. Isso é útil para exibir notificações ao usuário, como mensagens de erro ou sucesso, após alguma operação. No código fornecido, messages é utilizado para informar ao usuário quando algo não está certo, como "Product does not exist.#12: O módulo HttpResponse vem de django.http e é usado para retornar uma resposta HTTP para o navegador do usuário. Ele permite enviar texto simples, HTML ou outros conteúdos diretamente como uma resposta para o cliente. No código fornecido, é usado para retornar informações sobre o produto e a variação selecionados.
#13: A função reverse de django.urls é usada para obter uma URL a partir do nome de uma rota nomeada, permitindo que o código seja mais flexível e menos dependente de URLs fixas. Ao usar reverse, o Django gera a URL com base no padrão de URL configurado no arquivo de URLs do projeto ou aplicativo. Isso é útil para redirecionamentos ou geração de links dinâmicos.
#14: Retorna a URL anterior à vigente;
#15: Aqui, está sendo obtido o cabeçalho HTTP_REFERER, que é o endereço da página anterior a partir da qual o usuário veio. Se esse valor não estiver disponível, usa-se o valor padrão fornecido por reverse('product:list'), que gera a URL para a lista de produtos. Isso permite redirecionar o usuário para uma página segura, mesmo que o referer original esteja ausente.
#16: Este trecho obtém o valor de vid a partir dos parâmetros da URL, usando o método GET para capturar dados passados pela URL. Se vid estiver presente, seu valor será atribuído a variation_id; caso contrário, o valor será None.
#17: Verifica se variation_id é None ou uma string vazia. Se for, isso significa que o identificador da variação não foi fornecido, indicando que não há uma variação de produto válida para ser adicionada ao carrinho.
#18: Essa linha usa o módulo messages para adicionar uma mensagem de erro à solicitação. O método error adiciona uma mensagem de erro específica, que pode ser exibida ao usuário posteriormente. Aqui, a mensagem informa ao usuário que o produto não existe.
#19: Essa linha redireciona o usuário de volta para a URL armazenada em http_referer. É uma forma de retornar o usuário à página anterior, geralmente usada quando algo não deu certo.
#20: Usa o método get_object_or_404 para buscar um objeto Variation com o id especificado. Caso o objeto não seja encontrado, ele retorna uma página de erro "404 Not Found". Isso garante que, se a variação não existir, o código não irá falhar silenciosamente.
#21: Verifica se não há uma chave cart na sessão do usuário. Se não existir, significa que o carrinho ainda não foi criado para essa sessão.
#22: Inicializa o carrinho como um dicionário vazio na sessão do usuário. Esse dicionário será usado para armazenar os itens que o usuário adiciona ao carrinho.
#23: Salva a sessão atual do usuário, garantindo que qualquer modificação feita nos dados da sessão (como adicionar o carrinho) seja preservada.
#24: Recupera o carrinho da sessão do usuário. Como o carrinho foi inicializado anteriormente (se ainda não existia), agora pode ser usado para adicionar ou modificar itens.
#25: Retorna uma resposta HTTP com uma string formatada contendo o nome do produto e o nome da variação. É uma forma de enviar uma resposta simples ao navegador, mostrando ao usuário o que foi adicionado.
# ------------------------------------------------------------------
#8: Essa classe é uma view genérica fornecida pelo Django que facilita a exibição de detalhes de um objeto específico. No código, DetailView é usada na classe ProductDetail para mostrar os detalhes de um produto.
#9: A classe ProductDetail herda de DetailView, o que significa que ela é usada para exibir os detalhes de um objeto específico, no caso, um produto. O Django usa essa classe para buscar o objeto no banco de dados, renderizar o template especificado e fornecer o contexto para o template.
#10: Esse atributo especifica o nome do parâmetro na URL que será usado para procurar o objeto. Aqui, o parâmetro 'slug' na URL será utilizado para buscar o produto correspondente no banco de dados. A configuração geralmente é feita no arquivo urls.py para mapear a URL a essa view.
# ------------------------------------------------------------------
#1: Importa a classe ListView de django.views.generic.list. ListView é uma class-based view que renderiza uma lista de objetos. Essa classe é usada para facilitar a exibição de listas no Django.
#2: Importa a classe base View de django.views. View é a classe mais básica para todas as class-based views no Django.
#3: Define a view ProductList, que herda de ListView. Isso permite a exibição de uma lista de produtos da base de dados no template. A classe ProductList serve para exibir uma lista de produtos através de um queryset, que será passado para o contexto do template.
#4: Define o modelo Product (da pasta /product/models.py) que será utilizado pela ProductList para carregar os dados a serem exibidos.
#5: Especifica o template 'product/list.html' para renderizar a lista de produtos. Lógica: Indica qual arquivo HTML será renderizado ao acessar essa view.
#6: Define o nome do contexto que será passado ao template. Nesse caso, a lista de produtos será acessível pelo nome products dentro do template. Lógica: Facilita a referência ao conjunto de produtos no template, permitindo, por exemplo, iterações no loop for.
#7: Configura a paginação para exibir 3 produtos por página. Lógica: Controla a quantidade de produtos mostrados em cada página da lista.

# https://linktr.ee/edsoncopque