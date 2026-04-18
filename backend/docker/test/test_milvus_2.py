from pymilvus import MilvusClient, MilvusException


def test_connect_to_milvus():
    """
    连接到 Milvus 服务。
    使用配置中的 URI，如果没有配置，则使用默认值。
    """
    try:
        uri = "http://47.103.8.209:19014"
        token = ""
        db_name =""
        client = MilvusClient(
            uri=uri,
            token=token,
            db_name=db_name
        )
        # 可以添加一个简单的测试来确保连接成功
        client.list_collections()
        # logger.info(f"Successfully connected to Milvus at {uri}")
        print("连接")
        return True
    except MilvusException as e:
        # logger.error(f"Failed to connect to Milvus: {e}")
        print("失败")
        return False

if __name__ == '__main__':
    connect_to_milvus()