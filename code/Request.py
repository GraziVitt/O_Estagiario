import random


class Request:

    def __init__(self):

        # Todos os itens possíveis
        self.available_items = [
            "cafe",
            "caneta",
            "documentos",
            "copo",
            "grampeador",
            "pasta"
        ]

        # Itens que ainda precisam ser pedidos
        self.remaining_items = self.available_items.copy()

        # Pedido atual
        self.current_request = None

        # Quantidade de pedidos concluídos
        self.completed = 0

        # Escolhe o primeiro pedido
        self.next_request()

    def next_request(self):
        """
        Escolhe um novo pedido aleatório.
        Cada item será pedido apenas uma vez por partida.
        """

        if len(self.remaining_items) == 0:
            self.current_request = None
            return

        self.current_request = random.choice(self.remaining_items)
        self.remaining_items.remove(self.current_request)

    def check_delivery(self, item_name):
        """
        Verifica se o item entregue é o correto.
        """

        if item_name == self.current_request:

            self.completed += 1

            self.next_request()

            return True

        return False

    def game_finished(self):
        """
        Retorna True quando todos os pedidos foram concluídos.
        """

        return self.completed >= 6