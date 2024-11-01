# FILE: /product/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.list import ListView #1:
from django.views import View #2:
from . import models
from django.views.generic.detail import DetailView #8:
from django.contrib import messages #11:
from django.http import HttpResponse #12:
from django.urls import reverse #13:
from client_profile.models import Client_Profile
from django.db.models import Q


class ProductList(ListView): #3:
    # IMPORT⬇: /product/models.py
    model = models.Product #4:

    template_name = 'product/list.html' #5:
    context_object_name = 'products' #6:
    paginate_by = 3 #7:
    ordering = ['-id'] #58:

class Search(ProductList):
    def get_queryset(self, *args, **kwargs):
        
        # EXPORT⬆: /templates/partials/_nav.html
        term = self.request.GET.get('term') or self.request.session['term'] #59:
        qs = super().get_queryset(*args, **kwargs) #60:

        if not term:
            return qs
        
        self.request.session['term'] = term #61:

        # IMPORT⬇: /product/models.py
        qs = qs.filter( #62:
            Q(name__icontains=term) |
            Q(short_description__icontains=term) |
            Q(long_description__icontains=term)
        )
        
        self.request.session.save()
        return qs

class ProductDetail(DetailView): #9:
    model = models.Product
    template_name = 'product/detail.html'
    context_object_name = 'product'

    #IMPORT⬇: /product/urls.py
    slug_url_kwarg = 'slug' #10:

class AddToCart(View):
    def get(self, *args, **kwargs):
        # if self.request.session.get('cart'):
        #     del self.request.session['cart']
        #     self.request.session.save()

        http_referer = self.request.META.get('HTTP_REFERER', reverse('product:list')) #14: #15:
        variation_id = self.request.GET.get('vid') #16:

        if not variation_id: #17:
            messages.error(self.request, 'Product does not exist.') #18:
            return redirect(http_referer) #19:
        
        # IMPORT⬇: /product/models.py
        variation = get_object_or_404(models.Variation, id=variation_id) #20:
        variation_stock = variation.stock #26:
        product = variation.product #27:
        product_id = product.id #28:
        product_name = product.name
        variation_name = variation.name or ''
        unit_price = variation.price
        promotional_unit_price = variation.price_promotional
        quantitative = 1
        slug = product.slug
        image = product.image

        if image: #29:
            image = image.name #30:
        else:
            image = '' #31:

        if variation.stock < 1: #32:
            messages.error(self.request, 'Insufficient stock') #33:
            return redirect(http_referer) #34:

        if not self.request.session.get('cart'): #21:
            self.request.session['cart'] = {} #22:
            self.request.session.save() #23:
        
        cart = self.request.session['cart'] #24:

        if variation_id in cart:
            quantitative_cart = cart[variation_id]['quantitative'] #32:
            quantitative_cart += 1

            if variation_stock < quantitative_cart: #35: 
                messages.warning(self.request, f'Insufficient {quantitative_cart}x for {product_name} product. Add {variation_stock}x.') #36:
                quantitative_cart = variation_stock #37:

            cart[variation_id]['quantitative'] = quantitative_cart #38:
            cart[variation_id]['quantitative_price'] = unit_price * quantitative_cart #39:
            cart[variation_id]['promotional_quantitative_price'] = promotional_unit_price * quantitative_cart #40:

        else:
            cart[str(variation_id)] = {
                'product_id': product_id,
                'product_name': product_name,
                'variation_name': variation_name,
                'variation_id': variation_id,
                'unit_price': unit_price,
                'promotional_unit_price': promotional_unit_price,
                'quantitative_price': unit_price,
                'promotional_quantitative_price': promotional_unit_price,
                'quantitative': 1,
                'slug': slug,
                'image': image,
            } #44:
        self.request.session.save() #41:
        messages.success(self.request, f'Product {product_name} {variation_name} added to your cart {cart[variation_id]["quantitative"]}x.') #42:
        return redirect(http_referer)
        # return HttpResponse(f'{variation.product} {variation.name}') #25:

class RemoveFromCart(View):
    def get(self, *args, **kwargs):
       
        http_referer = self.request.META.get('HTTP_REFERER', reverse('product:list'))
        variation_id = self.request.GET.get('vid')

        if not variation_id:
            return redirect(http_referer)
        
        if not self.request.session.get('cart'):
            return redirect(http_referer)
        
        if variation_id not in self.request.session['cart']:
            return redirect(http_referer)
        
        cart = self.request.session['cart'][variation_id] #45:
        messages.success(self.request, f'{cart["product_name"]} {cart["variation_name"]} product removed from the system.') #46:

        del self.request.session['cart'][variation_id] #47:
        self.request.session.save()
        
        return redirect(http_referer)

class Cart(View):
    def get(self, *args, **kwargs):
        context = {'cart': self.request.session.get('cart', {})} #48:
        return render(self.request, 'product/cart.html', context) #43:

class PurchaseSummary(View):
    def get(self, *args, **kwargs):
        if not self.request.user.is_authenticated: #49:
            return redirect('client_profile:create')
        
        client_profile = Client_Profile.objects.filter(user=self.request.user).exists() #52: #54:
        if not client_profile: #55:
            messages.error(self.request, 'User without profile.')
            return redirect('client_profile:create')
        
        if not self.request.session.get('cart'): #53: #56: #57:
            messages.error(self.request, 'Empty cart.')
            return redirect('product:list')
        
        # AI:
        cart = self.request.session.get('cart', {})
        context = {'user': self.request.user, 'cart': cart}

        # context = {'user': self.request.user, 'cart': self.request.session['cart'],} #50:
        return render(self.request, 'product/purchasesummary.html', context) #51:
    


#59: Esta linha obtém o termo de busca (term) da URL (se fornecido) ou da sessão do usuário. Se não houver term na URL, o código tenta recuperar o último termo de busca armazenado na sessão. A sessão armazena o termo de busca para permitir que ele seja usado em uma consulta persistente, mesmo que o usuário navegue por outras páginas. Este termo é configurado a partir da entrada no formulário de busca no template _nav.html.
#60: Este código chama o método get_queryset da classe ProductList herdada. Essa chamada inicializa qs como o conjunto de produtos disponíveis antes do filtro de busca ser aplicado. Interação: A linha ajuda a manter a lógica básica de listagem de produtos, permitindo, em seguida, que o filtro de busca seja aplicado a qs apenas quando necessário.
#61: Armazena o termo de busca atual na sessão do usuário. Isso permite que o termo persista nas próximas requisições enquanto a sessão estiver ativa. Interação: Quando o usuário realiza uma busca no site, esse valor é salvo na sessão e pode ser recuperado posteriormente, o que possibilita o uso contínuo da busca e melhora a experiência do usuário.
#62: Esta linha aplica um filtro ao conjunto de dados qs para retornar apenas os produtos cujo name, short_description, ou long_description contenham o term da busca, independentemente de maiúsculas ou minúsculas. Interação: Utiliza o módulo Q do Django para criar uma busca complexa, que permite múltiplas condições OR, resultando em uma experiência de pesquisa mais completa para o usuário.
# ------------------------------------------------------------------
#58: Organiza a lista de produtos em ProductList em ordem decrescente de id, mostrando os produtos mais recentes primeiro na lista.
# ------------------------------------------------------------------
#52: Criamos esta variável pois ela identifica ou filtra o 'perfil' do usuário. É com ela que vamos fazer a verificação p/ saber se o usuário tem 'perfil' para então poder chegar no resuma da compra;
#53: Se dentro do resumo você excluir os itens do carrinho, quando zerar automaticamente vocẽ será redirecionado para 'list', ou seja, para a página inicial do e-commerce.
#54: Esta linha verifica se existe um perfil de cliente associado ao usuário autenticado que está fazendo a requisição. Utiliza o modelo Client_Profile importado do módulo client_profile.models, e o método filter é usado para buscar registros onde o campo user corresponde ao usuário atual (self.request.user). A função exists() retorna um valor booleano (True ou False) indicando se pelo menos um perfil correspondente foi encontrado.
#55: Esta linha verifica se o resultado da linha 52 foi False, ou seja, se não existe um perfil de cliente associado ao usuário autenticado. Caso o perfil não exista, a execução seguirá para o bloco dentro do if.
#56: Esta linha verifica se o carrinho de compras na sessão do usuário está vazio ou não existe. O método get é utilizado para tentar recuperar o dicionário do carrinho, retornando None caso ele não exista. Se o carrinho estiver vazio, o fluxo de execução seguirá para o bloco dentro do if.
#57: Aqui, self.request.session.get('cart') tenta obter o valor associado à chave 'cart' na sessão do usuário. Se a chave 'cart' não existir ou estiver vazia (ou seja, o retorno será None ou uma estrutura vazia), a expressão será avaliada como False. if not self.request.session.get('cart'): será verdadeiro (True) quando não houver um carrinho na sessão do usuário, ou seja, quando a chave 'cart' não existir ou for considerada vazia.
# ------------------------------------------------------------------
#49: Verifica se o usuário está autenticado. Isso é feito para garantir que somente usuários logados possam prosseguir para o resumo da compra. Caso contrário, ele será redirecionado para a página de criação de perfil do cliente (client_profile:create). Esse redirecionamento é importante para validar a identidade do usuário antes de continuar com a compra.
#50: Esta porra não funcionou!
#51: Renderiza a página de resumo da compra com o template purchasesummary.html e o contexto que contém informações do usuário e o carrinho. Essa linha se comunica com o módulo de templates do Django, especificamente com o template mencionado.
# ------------------------------------------------------------------
#45: Obtém os detalhes do item do carrinho associado ao variation_id fornecido.
#46: Exibe uma mensagem de sucesso ao usuário, informando que o produto foi removido.
#47: Remove o item do carrinho da sessão do usuário.
#48: Prepara o contexto para renderizar a página do carrinho, passando o carrinho atual (ou um dicionário vazio, caso não exista) para o template.
# ------------------------------------------------------------------
#26: A variável variation_stock é definida para armazenar o valor do estoque disponível da variação do produto. Isso é importante para verificar a quantidade disponível antes de adicionar ao carrinho.
#27: Aqui, a variável product armazena o produto associado à variação. Isso permite o acesso a informações do produto, como nome e imagem.
#28: A variável product_id armazena o identificador único do produto. Essa informação pode ser usada para operações como rastreamento ou exibição do produto no carrinho.
#29: Verifica se o produto tem uma imagem associada. O campo image pode ser nulo ou vazio, então é necessário verificar se ele existe antes de utilizá-lo.
#30: Se a imagem existir, define a variável image com o nome do arquivo da imagem. Isso é útil para exibir a imagem do produto.
#31: Caso o produto não tenha uma imagem associada, a variável image será definida como uma string vazia, garantindo que não ocorra erro ao tentar acessá-la.
#32: Verifica se o estoque da variação é menor que 1. Se for, significa que não há estoque suficiente para adicionar ao carrinho.
#33: Envia uma mensagem de erro ao usuário indicando que o estoque é insuficiente.
#34: Redireciona o usuário para a página anterior (http_referer), caso o estoque seja insuficiente.
#35: Verifica se a quantidade desejada no carrinho ultrapassa o estoque disponível.
#36: Envia uma mensagem de aviso ao usuário sobre a quantidade insuficiente no estoque para o produto selecionado.
#37: Ajusta a quantidade no carrinho para o máximo disponível em estoque.
#38: Atualiza o carrinho com a quantidade ajustada.
#39: Atualiza o preço total para a quantidade de produtos no carrinho.
#40: Atualiza o preço promocional total para a quantidade de produtos no carrinho, se aplicável.
#41: Salva as mudanças na sessão para persistir as atualizações no carrinho.
#42: Envia uma mensagem de sucesso ao usuário indicando que o produto foi adicionado ao carrinho com a quantidade especificada.
#43: Renderiza a página HTML do carrinho, localizada no arquivo cart.html.
#44: Este bloco de código no arquivo views.py adiciona um novo item ao carrinho de compras na sessão do usuário. Se a variação do produto (identificada pelo variation_id) ainda não estiver no carrinho, ele cria uma nova entrada no dicionário do carrinho.
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