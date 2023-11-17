import re

# Ação para caso 1


def action_a():
    return "Para atualizar as informações de pagamento você deve entrar na dashboard de cliente, acessar a aba 'Pagamentos' e por fim selecionar qual tipo de pagamento você deseja atualizar"


# Ação para caso 2
def action_b():
    return "Para acompanhar o seu pedido você deve entrar na dashboard de cliente, acessar a aba 'Pedidos' e por fim selecionar qual pedido você deseja acompanhar"


# Regex para cada situação
intent_dict = {
    r"/\b(atualizar(?= meu cartao))\s?|\b(mudar(?= a forma de pagamento))\s?|\b(atualizar(?= minhas informações de pagamento))\s?|\b(M[ée]todo(?= de pagamento desatualizado))\s?/gmi": "payment",
    r"/\b(status(?= do meu pedido))\s?|\b(rastrear(?= meu pedido))\s?|\b(onde(?= est[áa] meu pedido))\s?|\b(status(?= de entrega))\s?/gmi": "status",
}

# Dicionário para mapear cada ação para cada regex
action_dict = {
    "payment": action_a,
    "status": action_b
}

# Função para pedir o input do usuário


def wait_input():
    while True:
        command = input("Digite o seu comando: ")
        for key, value in intent_dict.items():
            pattern = re.compile(key)
            groups = pattern.findall(command)
            if groups:
                print(f"{action_dict[value]()}", end=" ")
        print()


if __name__ == '__main__':
    wait_input()
