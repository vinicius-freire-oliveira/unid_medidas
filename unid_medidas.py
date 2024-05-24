# Função para realizar a conversão entre unidades de medida
def converter_unidades(valor, unidade_origem, unidade_destino):
    conversoes = {
        ('m', 'cm'): valor * 100,
        ('cm', 'm'): valor / 100,
        ('m', 'km'): valor / 1000,
        ('km', 'm'): valor * 1000,
        ('cm', 'km'): valor / 100000,
        ('km', 'cm'): valor * 100000,
        ('m', 'mm'): valor * 1000,
        ('mm', 'm'): valor / 1000,
        ('cm', 'mm'): valor * 10,
        ('mm', 'cm'): valor / 10,
        ('km', 'mm'): valor * 1000000,
        ('mm', 'km'): valor / 1000000
    }
    return conversoes.get((unidade_origem, unidade_destino), "Conversão não suportada.")

# Solicitar ao usuário a unidade de origem e destino e o valor a ser convertido
unidade_origem = input("Informe a unidade de origem (mm, cm, m, km): ").lower()
unidade_destino = input("Informe a unidade de destino (mm, cm, m, km): ").lower()
valor = float(input(f"Informe o valor em {unidade_origem} que deseja converter: "))

# Realizar a conversão
resultado = converter_unidades(valor, unidade_origem, unidade_destino)

# Exibir o resultado
print(f"{valor} {unidade_origem} é igual a {resultado} {unidade_destino}.")
