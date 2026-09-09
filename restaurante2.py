from datetime import date

class Cliente:
    def __init__(self,nome, data_nascimento, cpf):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf

class Pedido:
    def __init__(self,data_pedido, percentual_desconto, cliente, itens, valor_total):
        self.data_pedido = data_pedido 
        self.percentual_desconto = percentual_desconto
        self.cliente = cliente 
        self.itens = itens
        self.valor_total = valor_total

    def __str__(self):
        itens_str = ""

        for item in self.itens:
            itens_str += (
                f"\n- Prato: {item.prato.nome}"
                f"\n  Ingredientes: {', '.join(item.prato.ingredientes)}"
                f"\n  Modo de preparo: {item.prato.modo_preparo}"
                f"\n  Valor unitário: R$ {item.valor_prato:.2f}"
                f"\n  Quantidade: {item.quantidade}"
                f"\n  Subtotal: R$ {item.valor_prato * item.quantidade:.2f}\n"
            )

        return (
            f"=== PEDIDO ===\n"
            f"Data do pedido: {self.data_pedido}\n"
            f"Cliente: {self.cliente.nome}\n"
            f"Data de nascimento: {self.cliente.data_nascimento}\n"
            f"CPF: {self.cliente.cpf}\n"
            f"Desconto: {self.percentual_desconto}%\n"
            f"Valor total: R$ {self.valor_total:.2f}\n"
            f"Itens:{itens_str}"
        )
    
class ItemDoPedido:
    def __init__(self, prato, valor_prato, quantidade):
        self.prato = prato
        self.valor_prato = valor_prato
        self.quantidade = quantidade

class Prato:
    def __init__(self, nome, ingredientes, modo_preparo, preco):
        self.nome = nome
        self.ingredientes = ingredientes
        self.modo_preparo = modo_preparo
        self.preco = preco

c1 = Cliente("Sofia", date(2009,11,5), "15216886729")

p1 = Pedido(
    date(2026,6,17),
    20.0,
    c1,
    [
        ItemDoPedido(
            Prato(
                "macarrão à bolonhesa",
                ["macarrão", "molho de tomate", "carne moída"],
                "Fazer o macarrão e adicionar o molho e a carne",
                123.4
            ),
            34.5,  # valor_prato
            1      # quantidade
        )
    ],
    34.5  # valor_total
)

print(p1)