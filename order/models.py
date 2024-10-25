# FILE: /order/models.py

from django.db import models
from django.contrib.auth.models import User

#URL⬇: http://127.0.0.1:8000/admin/order/order/add/
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) #1:
    total = models.FloatField() #2:
    total_qtd = models.PositiveBigIntegerField() ##
    status = models.CharField(
        default='C',
        max_length=1,
        choices=(
            ('A', 'Approved'),
            ('C', 'Created'),
            ('R', 'Rejected'),
            ('P', 'Pending'),
            ('S', 'Sent'),
            ('F', 'Finalized'),
        )
    ) #3:

    def __str__(self):
        return f'Order number {self.pk}.' #4:

#URL⬇: http://127.0.0.1:8000/admin/order/orderitem/add/
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE) #5:
    product_name = models.CharField(max_length=255) #6:
    product_id = models.PositiveBigIntegerField()
    variation = models.CharField(max_length=255)
    variation_id = models.PositiveBigIntegerField()
    price = models.FloatField()
    price_promotional = models.FloatField(default=0)
    quantitative = models.PositiveIntegerField() #7:
    image = models.CharField(max_length=2000) #8:

    def __str__(self):
        return f'Order Item {self.order}.' #9:
    
    class Meta:
        verbose_name = 'Order item'
        verbose_name_plural = 'Order items'


# ------------------------------------------------------------------
#1: Esta linha define um campo user na classe Order, que é uma chave estrangeira (ForeignKey) para o modelo User (importado de django.contrib.auth.models). O argumento on_delete=models.CASCADE significa que, se o usuário associado for deletado, todas as ordens relacionadas a ele também serão excluídas.
#2: Esta linha cria um campo total para a ordem, que armazenará o valor total do pedido. Ele é do tipo FloatField, ou seja, armazenará números de ponto flutuante (decimais).
#3: Esta linha cria o campo status como um CharField com comprimento máximo de 1 caractere. O argumento choices define as opções disponíveis para o status do pedido, como 'A' (Approved), 'C' (Created), 'R' (Rejected), entre outros. O valor padrão (default='C') é 'Created', que indica que a ordem foi criada mas ainda não está finalizada.
#4: Este método especial define a representação string do objeto Order. Quando o objeto é convertido em string (por exemplo, ao ser exibido no admin), ele mostrará "Order number" seguido pelo ID primário (self.pk) do pedido.
#5: Este campo define uma relação de chave estrangeira com o modelo Order. Cada item de pedido (OrderItem) está relacionado a um pedido específico. O on_delete=models.CASCADE garante que, se o pedido for deletado, todos os itens associados também serão excluídos.
#6: Cria um campo product_name para armazenar o nome do produto em um item de pedido. O campo é do tipo CharField com um comprimento máximo de 255 caracteres.
#7: Define o campo quantity, que armazena a quantidade de um produto neste item de pedido. Ele é do tipo PositiveBigIntegerField, garantindo que apenas valores positivos sejam permitidos. Obs: Corrigido para PositiveIntegerField.
#8: Este campo image armazena o caminho ou URL de uma imagem associada ao produto no item de pedido. Ele é um CharField com um limite de 2000 caracteres.
#9: Define a representação em string de um objeto OrderItem. Ele exibe "Order Item" seguido pela ordem associada ao item (self.order).

# https://linktr.ee/edsoncopque