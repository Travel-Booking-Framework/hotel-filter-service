from rest_framework import serializers

class HotelSerializer(serializers.Serializer):
    id = serializers.CharField()
    name = serializers.CharField()
    location = serializers.CharField()
    rating = serializers.FloatField()
    price_per_night = serializers.DecimalField(max_digits=10, decimal_places=2)
    amenities = serializers.ListField(child=serializers.CharField())

    def to_representation(self, instance):
        """Convert Elasticsearch result into a standardized format."""
        source = instance["_source"]
        return {
            "id": instance["_id"],
            "name": source.get("name"),
            "location": source.get("location"),
            "rating": source.get("rating"),
            "price_per_night": source.get("price_per_night"),
            "amenities": source.get("amenities", []),
        }
