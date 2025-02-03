from .documents import HotelDocument

class HotelRepository:
    @staticmethod
    def search_hotels(query):
        return HotelDocument.search().query("multi_match", query=query, fields=['name', 'location']).execute()