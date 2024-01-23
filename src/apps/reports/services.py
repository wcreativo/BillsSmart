from django.db.models import Q

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

    @classmethod
    def bulk_create_clients(cls, data):
        try:
            bulk_instances = []
            for client in data:
                bulk_instances.append(Client(**client))
            Client.objects.bulk_create(bulk_instances)
            return True
        except Exception as e:
            print(f"Error: {e}")
            return False

    @classmethod
    def check_duplicate_data(cls, data):
        unique_values = set()

        list_without_duplicates = []

        for dictionary in data:
            document_value = dictionary.get("document")
            email = dictionary.get("email")

            if document_value not in unique_values or email not in unique_values:
                unique_values.add(document_value)
                unique_values.add(email)
                list_without_duplicates.append(dictionary)

        return list_without_duplicates

    @classmethod
    def check_client_on_db(cls, data):
        for i, dictionary in enumerate(data):
            document = dictionary.get("document")
            email = dictionary.get("email")
            client = Client.objects.filter(Q(document=document) | Q(email=email))
            if client:
                data.remove(i)
        return data
