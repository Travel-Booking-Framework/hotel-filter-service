from rest_framework import serializers

class HotelSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    location = serializers.CharField()
    price = serializers.FloatField()

    def validate_price(self, value):
        """Ensure the price is not negative."""
        if value < 0:
            raise serializers.ValidationError("Price must be a positive number.")
        return value