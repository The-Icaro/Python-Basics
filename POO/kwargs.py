# Kwargs são utilizados para receber dados.py para vários atributos
# Utilizados também em Funções Sozinhas ou em composições de Classes
# Não precisam ser chamadas de **kwargs -> só uma convenção
# Identificam-se por dois ** -> pode ser **kwargs ou **x


def calcularPreco(valor, **dados):  # Função para calcular preço, tendo **dados.py recebendo diversos dados.py
    taxa = dados.get('taxa')  # taxa recebendo um dos valores de **dados.py
    desconto = dados.get('desconto')  # desconto recebendo um dos valores de **dados.py

    if taxa:  # Se for atribuido um valor para **dados.py em taxa=
        valor += valor * (taxa / 100)

    if desconto:  # Se for atribuido um valor para **dados.py em desconto=
        valor -= valor * (desconto / 100)

    return valor  # Retorna valor


produto1 = calcularPreco(100)  # **dados.py recebendo nenhum valor
print(produto1)
produto2 = calcularPreco(100, desconto=25)  # **dados.py recebendo um valor para o atributo desconto=
print(produto2)
produto3 = calcularPreco(100, taxa=15)  # **dados.py recebendo um valor para o atributo taxa=
print(produto3)
produto4 = calcularPreco(100, desconto=20, taxa=7)  # dados.py recebendo dois valores, para os atributos desconto e taxa
print(produto4)
