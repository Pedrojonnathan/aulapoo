from aulapoo.svc.banco.banco_lista import BancoLista
from aulapoo.svc.conta.criar_conta import CriarConta


class CriarBanco:
    if __name__ == '__main__':
        BancoLista.cadastrar(CriarConta)
        print(BancoLista.procurar_conta())
        BancoLista.creditar(CriarConta,10)
        BancoLista.creditar(CriarConta, 10)
        print(BancoLista.saldo())

