import asyncio

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


async def bulk_create_clients(data):
    try:
        bulk_instances = []
        for client in data:
            bulk_instances.append(Client(**client))
        await asyncio.to_thread(Client.objects.bulk_create, bulk_instances)
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False


unique_values = set()


async def is_duplicate_data(client):
    await asyncio.sleep(1)

    document = client["document"]
    email = client["email"]
    if document not in unique_values:
        unique_values.add(document)
        unique_values.add(email)
        return client
    return None


async def is_client_on_db(client):
    await asyncio.sleep(1)
    document = client.get("document")
    email = client.get("email")
    client = Client.objects.filter(Q(document=document) | Q(email=email))
    if client:
        return None
    return client


async def check_clients(client):
    client = await is_duplicate_data(client)
    if client:
        client = await is_client_on_db(client)
        return client
    else:
        return None


async def check_data_bulk_create(data):
    data = await asyncio.gather(*(check_clients(client) for client in data))
    clients_data = [client for client in data if client is not None]
    bulk_result = await bulk_create_clients(clients_data)
    return bulk_result
