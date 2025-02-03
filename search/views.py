from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import HotelSearchSerializer
from .repository import HotelRepository
from .commands import SearchHotelsCommand
import pybreaker

circuit_breaker = pybreaker.CircuitBreaker(fail_max=5, reset_timeout=60)

class HotelSearchView(APIView):
    def get(self, request):
        serializer = HotelSearchSerializer(data=request.query_params)

        if serializer.is_valid():
            query = serializer.validated_data["query"]
            command = SearchHotelsCommand(HotelRepository())

            try:
                results = circuit_breaker.call(command.execute, query)
                return Response(results, status=status.HTTP_200_OK)
            except pybreaker.CircuitBreakerError:
                return Response({"error": "Service unavailable"}, status=status.HTTP_503_SERVICE_UNAVAILABLE)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
