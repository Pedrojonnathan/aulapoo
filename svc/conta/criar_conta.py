from aulapoo.svc.conta.conta import Conta
from aulapoo.svc.conta.conta_imposto import ContaImposto

class CriarConta:
    if __name__ == '__main__':
        conta = Conta('21.342-7')
        conta_imposto = ContaImposto('21.342-7')

        conta.creditar(500.87)
        conta.debitar(45.00)
        print(conta.get_saldo())

