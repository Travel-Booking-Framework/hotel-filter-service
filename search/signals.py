from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Hotel
from elasticsearch_dsl import connections, Document, Text

connections.create_connection()

class HotelDocument(Document):
    name = Text()
    address = Text()
    rating = Text()

    class Index:
        name = 'hotels'

@receiver(post_save, sender=Hotel)
def save_hotel(sender, instance, **kwargs):
    hotel = HotelDocument(meta={'id': instance.id}, name=instance.name, address=instance.address, rating=instance.rating)
    hotel.save()

@receiver(post_delete, sender=Hotel)
def delete_hotel(sender, instance, **kwargs):
    hotel = HotelDocument(meta={'id': instance.id})
    hotel.delete()
