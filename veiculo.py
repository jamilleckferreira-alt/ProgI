class Veiculo:
    def __init__(self,placa, ano):
        self.placa = placa
        self.ano = ano

class Moto(Veiculo):
    def __init__(self, placa, ano):
        super(). __init__(placa, ano)

class  Caminhao(Veiculo):
     def __init__(self, placa, ano, peso_em_kg):
        super(). __init__(placa, ano)
        self.peso_em_kg = peso_em_kg

v1 = Veiculo("736tey43", 2025)
v2 = Moto("67137FT2", 2026)
v3 = Caminhao("7834TSAG23", 2023, 5)
print (f"Veículo: {v1.placa}, {v1.ano}")
print(f"Moto: {v2.placa}, {v2.ano}")
print(f"Caminhão: {v3.placa}, {v3.ano}, {v3.peso_em_kg}")