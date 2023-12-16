class PedidoItem:
    def __init__(self, item, quantidade):
        self.item = item
        self.quantidade = quantidade

class Pedido:
    def __init__(self):
        self.itens = []
        self.cliente = {}

    def adicionar_item(self, item, quantidade):
        pedido_item = PedidoItem(item, quantidade)
        self.itens.append(pedido_item)

    def calcular_total(self):
        total = 0.0
        for pedido_item in self.itens:
            item = pedido_item.item
            quantidade = pedido_item.quantidade
            total += item['preco'] * quantidade
        return total

    def mostrar_pedido(self):
        print("\nPedido:")
        for pedido_item in self.itens:
            item = pedido_item.item
            quantidade = pedido_item.quantidade
            print(f"{quantidade}x {item['nome']} - R${item['preco']:.2f} cada")

class Menu:
    def __init__(self):
        self.cardapio = []
        self.pedido = Pedido()

    def adicionar_pizza(self, nome, tamanho, ingredientes, preco):
        pizza = {'nome': nome, 'tamanho': tamanho,  'ingredientes': ingredientes, 'preco': preco}
        self.cardapio.append(pizza)

    def mostrar_cardapio(self):
        print("Cardápio:")
        for item in self.cardapio:
            if 'ingredientes' in item:  # Verifica se é uma pizza
                print(f"{item['nome']} ({item['tamanho']}): {', '.join(item['ingredientes'])} - R${item['preco']:.2f}")
            elif 'preco' in item:  # Verifica se 'preco' está presente, indicando que é uma bebida
                print(f"{item['nome']} ({item['tamanho']}): Bebida - R${item['preco']:.2f}")
        else:
            print(f"{item['nome']} ({item['tamanho']}): Item inválido")

    def adicionar_bebida(self, nome, tamanho, preco):
        bebida = {'nome': nome, 'tamanho': tamanho, 'preco': preco}
        self.cardapio.append(bebida)

    def mostrar_bebidas(self):
        print("Cardápio de Bebidas:")
        for item in self.cardapio:
            if 'ingredientes' in item:  # Verifica se é uma pizza
                continue
            print(f"{item['nome']} ({item['tamanho']}): R${item['preco']:.2f}")

    def fazer_pedido(self, item, quantidade=1):
        try:
            pedido_item = {'item': item, 'quantidade': quantidade}
            self.pedido.adicionar_item(item, quantidade)
        except Exception as e:
            print(f"Erro ao adicionar item ao pedido: {e}")

    def receber_dados_cliente(self):
        try:
            nome = input("Digite seu nome: ")
            telefone = input("Digite seu telefone: ")
            endereco = input("Digite seu endereço: ")
            self.pedido.cliente = {'nome': nome, 'telefone': telefone, 'endereco': endereco}
        except Exception as e:
            print(f"Erro ao receber dados do cliente: {e}")

    def concluir_pedido(self):
        try:
            if self.pedido.itens:
                print("\nPedido final:")
                self.pedido.mostrar_pedido()
                print("\nDados do Cliente:")
                for chave, valor in self.pedido.cliente.items():
                    print(f"{chave}: {valor}")
                total_pedido = self.pedido.calcular_total()
                print(f"\nTotal do Pedido: R${total_pedido:.2f}")
            else:
                print("Pedido vazio. Nada a concluir.")
        except Exception as e:
            print(f"Erro ao concluir o pedido: {e}")
        finally:
            print("Processo concluído.")

    def adicionar_item_interativo(self):
        try:
            self.mostrar_cardapio()
            tipo_item = input("Digite o nome do item que deseja adicionar ao pedido: ")

            for item in self.cardapio:
                if item['nome'].lower() == tipo_item.lower():
                    quantidade = int(input(f"Digite a quantidade de '{item['nome']}': "))
                    self.fazer_pedido(item, quantidade)
                    print(f"{quantidade}x '{item['nome']}' adicionado ao pedido.")
                    break
            else:
                print(f"Item '{tipo_item}' não encontrado no cardápio.")
        except Exception as e:
            print(f"Erro ao adicionar item de forma interativa: {e}")

# Exibir Cardápio
menu = Menu()

# Adicionar Pizzas
menu.adicionar_pizza("Margherita", "Grande", ["molho de tomate", "mussarela", "manjericão"], 30.0)
menu.adicionar_pizza("Calabresa", "Grande", ["molho de tomate", "calabresa", "cebola", "azeitonas"], 35.0)
menu.adicionar_pizza("Frango com catupiri", "Grande", ["molho de tomate", "frango temperado", "catupiri", "azeitonas"], 45.0)
menu.adicionar_pizza("Mussarela", "Grande", ["molho de tomate", "mussarela", "azeitonas"], 32.0)
menu.adicionar_pizza("Peperoni", "Grande", ["molho de tomate", "mussarela", "peperoni", "azeitonas"], 38.0)

# pizzas pequenas

menu.adicionar_pizza("Portuguesa", "pequena", ["molho de tomate", "presunto", "ovo", "cebola", "mussarela", "azeitonas"], 25.0)
menu.adicionar_pizza("Quatro Queijos", "Pequena", ["molho de tomate", "mussarela", "provoloni", "gorgonzola", "catupiry"], 28.0)
menu.adicionar_pizza("Bali", "Pequena", ["molho de tomate", "mussarela", "cebola", "parmesão", "azeitonas"], 28.0)
menu.adicionar_pizza("Atum", "Pequena", ["molho de tomate", "atum", "cebola", "azeitonas"], 29.0)

# Adicionar Bebidas

menu.adicionar_bebida("coca cola", "grande", 12.0)
menu.adicionar_bebida("Fanta", "grande", 13.0)
menu.adicionar_bebida("Guarana", "pequena", 5.0)
menu.adicionar_bebida("Skol", "pequena", 5.0)

# Mostrar Cardápio
menu.mostrar_cardapio()
menu.mostrar_bebidas()

# Receber dados do cliente

menu.receber_dados_cliente()

# Fazer Pedidos

menu.fazer_pedido(menu.cardapio[0], quantidade=2)  # Exemplo de pedido de duas Margheritas
menu.fazer_pedido(menu.cardapio[5], quantidade=1)  # Exemplo de pedido de uma Fanta

# Mostrar Pedido, Dados do Cliente e Calcular o Total do pedido

menu.pedido.mostrar_pedido()
print("\nDados do Cliente:")
for chave, valor in menu.pedido.cliente.items():
    print(f"{chave}: {valor}")
total_pedido = menu.pedido.calcular_total()
print(f"\nTotal do Pedido: R${total_pedido:.2f}")     



# Projeto cardápio de pizzaria

# Este projeto realizado em linguagem de programacão python, é um sistema simples de pedidos para uma pizzaria, 
# destacando a interatividade com o usuário. 
# O sistema permite que os clientes visualizem o cardápio, 
# escolham pizzas e bebidas, adicionem os itens ao pedido, fornecendo informacões pessoais e concluem o pedido. 
# O projeto é estruturado em três classes principais(class: PedidoItem, Pedido,e Menu)e 
# cada class tem suas funcões específicas.
# Para lidar com as excecões, foi incluido o bloco 'try...except' em operacões de adicão de itens ao pedido, 
# recebimento de dados do cliente e conclusão do pedido.
# No caso de excecão, uma mensage de erro é exibida na saída padrão