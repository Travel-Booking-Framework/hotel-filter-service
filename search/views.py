from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .commands import SearchHotelsCommand
from .repositories import HotelRepository

class HotelSearchView(APIView):
    def get(self, request):
        query = request.query_params.get('q', '')
        command = SearchHotelsCommand(HotelRepository())
        results = command.execute(query)
        return Response(results, status=status.HTTP_200_OK)