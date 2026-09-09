from datetime import date

class Cliente:
    def __init__(self,nome, data_nascimento, cpf):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf

class Pedido:
    def __init__(self,data_pedido, percentual_desconto, valor_final, cliente, pratos):
        self.data_pedido = data_pedido 
        self.percentual_desconto = percentual_desconto
        self.valor_final = valor_final
        self.cliente = cliente 
        self.pratos = pratos

    def __str__(self):
        pratos_str = ""

        for prato in self.pratos:
            pratos_str += (
                f"\n  Nome: {prato.nome}"
                f"\n  Ingredientes: {', '.join(prato.ingredientes)}"
                f"\n  Modo de preparo: {prato.modo_preparo}"
                f"\n  Preço: R$ {prato.preco:.2f}\n"
            )

        return (
            f"=== PEDIDO ===\n"
            f"Data do pedido: {self.data_pedido}\n"
            f"Cliente: {self.cliente.nome}\n"
            f"Data de nascimento: {self.cliente.data_nascimento}\n"
            f"CPF: {self.cliente.cpf}\n"
            f"Desconto: {self.percentual_desconto}%\n"
            f"Valor final: R$ {self.valor_final:.2f}\n"
            f"Pratos:{pratos_str}"
        )
class Prato:
    def __init__(self, nome, ingredientes, modo_preparo, preco):
        self.nome = nome
        self.ingredientes = ingredientes
        self.modo_preparo = modo_preparo
        self.preco = preco

c1= Cliente("Sofia", date(2009,11,5), "15216886729")
p1= Pedido(date(2026,6,17), 20.0, 123.4, c1, [Prato("macarrão à bolonhesa", ["macarrão", "molho de tomate", "carne moída"], "Fazer o macarrão e adicionar o molho e a carne", 123.4)])
print(p1)