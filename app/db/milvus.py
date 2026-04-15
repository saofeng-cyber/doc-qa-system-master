from pymilvus import MilvusClient

def create_milvus_uri():
    client = MilvusClient(uri="http://localhost:19530", user="saofeng", password="saofeng666", token="root:Milvus")
    # 2. Create a user
    # client.create_user(user_name="saofeng", password="saofeng666")
    # client.create_database(db_name="my_database")
    return client