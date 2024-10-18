# FILE: /utils/utils.py

def format_pricevrs(value): #1:
    return f'₿ {value:.2f}'.replace('.', ',') #2:

def cart_total_qtd(cart): #3:
    return sum([i['quantitative'] for i in cart.values()]) #3:

def cart_totals_products(cart): #4:
    total = 0
    for i in cart.values():
        if i.get('promotional_quantitative_price'):
            total += i.get('promotional_quantitative_price')
        else:
            total += i.get('quantitative_price')
    return total

    # return sum(
    #     [
    #         i.get('promotional_quantitative_price')
    #         if i.get('promotional_quantitative_price')
    #         else i.get('quantitative_price')
    #         for i
    #         in cart.values()
    #     ]
    # )


#4: Esta função calcula o total de preços de todos os produtos no carrinho. Para cada item no carrinho (cart), verifica se existe um preço promocional (promotional_quantitative_price). Se existir, ele é somado ao total. Caso contrário, o preço regular (quantitative_price) é somado. Por fim, retorna o total acumulado. Dependência: O carrinho (cart) é um dicionário cujos valores são itens do carrinho, presumivelmente representando os produtos e seus detalhes.
# ------------------------------------------------------------------
#3: Função que calcula o total de itens no carrinho, somando a quantidade (quantitative) de cada produto.
# ------------------------------------------------------------------
#1: Declara a função que formata o valor recebido. Lógica: Esta função converte um número para o formato de preço em Bitcoin, substituindo o ponto decimal por uma vírgula.
#2: Retorna o valor formatado como uma string de Bitcoin, com duas casas decimais, e substitui o ponto decimal por uma vírgula. Lógica: A formatação é feita para seguir o estilo comum em alguns países (ex.: Brasil), onde a vírgula é usada como separador decimal.

# https://linktr.ee/edsoncopque