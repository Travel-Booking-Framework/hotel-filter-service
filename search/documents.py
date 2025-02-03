from elasticsearch_dsl import Document, Text, Integer, connections

connections.create_connection(hosts=['localhost:9200'])

class HotelDocument(Document):
    name = Text()
    location = Text()
    price = Integer()

    class Index:
        name = 'hotels'

    def save(self, **kwargs):
        return super().save(**kwargs)