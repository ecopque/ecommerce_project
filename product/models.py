# FILE: /product/models.py

from django.db import models
from PIL import Image #1:
import os
from django.conf import settings #2:
from django.utils.text import slugify #24:
from utils import utils

class Product(models.Model): #3:
    name = models.CharField(max_length=255)
    short_description = models.TextField(max_length=255)
    long_description = models.TextField()
    image = models.ImageField(upload_to='product_images/%Y/%m', blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, null=True) #25:
    marketing_price = models.FloatField()
    price_promotional_marketing = models.FloatField(default=0)
    type = models.CharField(default='V', max_length=1, choices=(
        ('V', 'Variation'),
        ('S', 'Simple'),
        ),
    )

    def get_formatted_price(self): #26:
        return f'${self.marketing_price:.2f}'.replace('.', ',') #27:
        # return utils.format_pricevrs(self.marketing_price) #32:
    get_formatted_price.short_description = 'Preço BR' #28:
    
    def get_formatted_price2(self): #33:
        return f'${self.price_promotional_marketing:.2f}'.replace('.', ',') #34:
    get_formatted_price2.short_description = 'Preço BR' #35:

    @staticmethod #4:
    def resize_image(img, new_width=800): #4:
        img_full_path = os.path.join(settings.MEDIA_ROOT, img.name) #5:
        print(img_full_path)
        
        img_pil = Image.open(img_full_path) #6:
        original_width, original_height = img_pil.size #7:
        print(original_width, original_height)

        if original_width <= new_width:
            print('Original width smaller than new width.')
            img_pil.close() #8:
            return
        
        new_height = round((new_width * original_height) / original_width) #9:
        new_img = img_pil.resize((new_width, new_height), Image.LANCZOS) #10:
        new_img.save(img_full_path, optimize=True, quality=50) #11:
        print('Image has been resized.')

    def save(self, *args, **kwargs): #12:
        if not self.slug: #29:
            slug2 = f'{slugify(self.name)}' #30:
            self.slug = slug2 #31:
        super().save(*args, **kwargs) #13:

        max_image_size = 800
        if self.image: #14:
            self.resize_image(self.image, max_image_size) #15:

    def __str__(self):
        return self.name #16:

class Variation(models.Model): #17:
    class Meta:
        verbose_name = 'Variation'
        verbose_name_plural = 'Variations'

    product = models.ForeignKey(Product, on_delete=models.CASCADE) #18:
    name = models.CharField(max_length=50, blank=True, null=True) #19:
    price = models.FloatField() #20:
    price_promotional = models.FloatField(default=0) #21:
    stock = models.PositiveIntegerField(default=1) #22:

    def __str__(self):
        return self.name or self.product.name #23:
    
    
# ------------------------------------------------------------------
#32: Só um exemplo de como poderíamos utilizar o novo recurso que criei de 'utils';
#33: Função do modelo Product que retorna o preço promocional formatado. Lógica: Usa formatação para exibir o preço promocional em um formato específico, substituindo o ponto decimal por vírgula.
#34: Retorna o preço promocional formatado como string com 2 casas decimais, substituindo o ponto por vírgula.
#35: Define uma descrição curta para a função get_formatted_price2 no admin do Django. Lógica: Serve para identificar a função de maneira amigável na interface de administração do Django.
# ------------------------------------------------------------------
#24: A função slugify converte um texto em um slug, que é uma versão simplificada e segura de uma string para ser usada em URLs. Normalmente, remove caracteres especiais e substitui espaços por hífens, além de transformar todas as letras em minúsculas.
#25: O campo slug define um slug único para o produto. Um slug é usado para criar URLs amigáveis ao usuário e otimizadas para SEO. Este campo pode ser preenchido automaticamente, mas é opcional (blank=True, null=True).
#26: Este método formata o preço (marketing_price) para o formato brasileiro de moeda (R$), substituindo o ponto decimal por uma vírgula, o que é uma prática comum no Brasil.
#27: Aqui, o preço é formatado para duas casas decimais com a string f'R${self.marketing_price:.2f}' e o ponto decimal é substituído por uma vírgula usando o método replace.
#28: Esta linha define um nome substituto.
#29: No método save, verifica se o campo slug está vazio (None ou ''). Se estiver, significa que o produto não tem um slug ainda, e ele será gerado na próxima linha.
#30: Aqui, a função slugify transforma o nome do produto (self.name) em um slug e atribui o resultado à variável slug2.
#31: A variável slug2, que contém o slug gerado na linha anterior, é atribuída ao campo slug do produto.
# ------------------------------------------------------------------
#1: Este código importa a biblioteca PIL (Python Imaging Library), especificamente o módulo Image. Este módulo é utilizado para manipulação de imagens, como abrir, redimensionar e salvar imagens. Ele será utilizado na função resize_image para redimensionar a imagem do produto.
#2: Importa o módulo settings de Django, que contém todas as configurações do projeto. Será usado para acessar o caminho das mídias (imagens) através da variável MEDIA_ROOT, localizada no arquivo settings.py.
#3: Define a classe Product, que herda de models.Model. Isso cria um modelo de banco de dados que representa os produtos na aplicação. Cada instância dessa classe será um produto.
#4: O decorador @staticmethod define um método estático, que pode ser chamado diretamente pela classe Product sem precisar de uma instância. O método resize_image recebe uma imagem e a redimensiona para um valor máximo de largura (padrão de 800 pixels). É uma lógica útil para garantir que imagens não fiquem muito grandes.
#5: Combina o caminho das mídias (MEDIA_ROOT, definido no settings.py) com o nome da imagem (img.name) para gerar o caminho completo da imagem no sistema de arquivos. Isso é necessário para carregar a imagem para o processamento.
#6: Abre a imagem localizada no caminho completo usando a função open da biblioteca PIL. O objeto retornado, img_pil, é uma instância de imagem manipulável.
#7: Obtém a largura e altura originais da imagem usando a propriedade size da imagem PIL. Essa informação é necessária para calcular o novo tamanho proporcional ao redimensionar.
#8: Fecha o arquivo da imagem aberta. É uma boa prática fechar arquivos abertos para liberar os recursos do sistema.
#9:  Calcula a nova altura da imagem mantendo a proporção entre largura e altura. Isso é feito com base na largura original e altura original, garantindo que a imagem não seja distorcida.
#10: Redimensiona a imagem usando o método resize do PIL, com a nova largura e altura calculadas. O argumento Image.LANCZOS é um algoritmo de alta qualidade para redimensionamento de imagem, garantindo uma boa qualidade ao redimensionar.
#11: Salva a imagem redimensionada no mesmo caminho original (img_full_path), otimizando o tamanho do arquivo (optimize=True) e ajustando a qualidade da imagem para 50%, o que reduz o tamanho do arquivo sem perder muita qualidade.
#12: Sobrescreve o método save da classe models.Model. Este método é responsável por salvar o objeto no banco de dados, e aqui ele é modificado para incluir o redimensionamento da imagem após o salvamento.
#13: Chama o método save original da superclasse (models.Model), garantindo que o comportamento padrão de salvar o produto no banco de dados seja mantido.
#14: Verifica se o produto tem uma imagem associada. Se existir uma imagem, o método resize_image será chamado para redimensioná-la.
#15: Chama o método estático resize_image e passa a imagem do produto e o valor máximo de largura (800 pixels) para redimensionar a imagem.
#16: Define o método __str__ da classe Product, retornando o nome do produto quando a instância da classe for representada como uma string.
#17: Define a classe Variation, que herda de models.Model. Esse modelo representa variações de um produto (como tamanho ou cor) e está relacionado ao modelo Product.
#18: Cria um relacionamento entre a variação e o produto, usando uma chave estrangeira (ForeignKey). O argumento on_delete=models.CASCADE garante que, se o produto for deletado, todas as variações associadas também serão deletadas.
#19: Define o campo name da variação, que é um campo de texto com no máximo 50 caracteres. O blank=True, null=True indica que este campo é opcional.
#20: Define o campo price da variação, que é um campo de ponto flutuante (decimal) para armazenar o preço da variação.
#21: Define o campo promotional_price como um preço promocional da variação, com valor padrão de 0.
#22: Define o campo stock, que armazena a quantidade de variações em estoque. Ele é um número inteiro positivo, com valor padrão de 1.
#23: No método __str__ da classe Variation, retorna o nome da variação (se existir) ou o nome do produto ao qual a variação pertence.

# https://linktr.ee/edsoncopque