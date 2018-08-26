import uuid


def generate_auth_token():
    return str(uuid.uuid4()).replace('-', '')

