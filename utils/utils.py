# FILE: /utils/utils.py

def format_pricevrs(value): #1:
    return f'₿ {value:.2f}'.replace('.', ',') #2:

def cart_total_qtd(cart): #3:
    return sum([i['quantitative'] for i in cart.values()]) #3:


#3: Função que calcula o total de itens no carrinho, somando a quantidade (quantitative) de cada produto.
# ------------------------------------------------------------------
#1: Declara a função que formata o valor recebido. Lógica: Esta função converte um número para o formato de preço em Bitcoin, substituindo o ponto decimal por uma vírgula.
#2: Retorna o valor formatado como uma string de Bitcoin, com duas casas decimais, e substitui o ponto decimal por uma vírgula. Lógica: A formatação é feita para seguir o estilo comum em alguns países (ex.: Brasil), onde a vírgula é usada como separador decimal.

# https://linktr.ee/edsoncopque