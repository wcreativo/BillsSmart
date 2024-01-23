from apps.clients.models import Client


class ClientService:
    @classmethod
    def total_bills_by_client(cls):
        clients = Client.objects.all()
        if clients:
            data = []
            for client in clients:
                client_data = {
                    "document": client.document,
                    "full_name": f"{client.first_name} {client.last_name}",
                    "total_bills": client.bills.count(),
                }
                data.append(client_data)
            return data
        return None
