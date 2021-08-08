from rest_framework.views import APIView
from rest_framework.response import Response
from django.http.response import HttpResponseRedirect
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from django.conf import settings

from .serializers import UrlShortenerSerializer
from .utils import get_actual_path


class ShortenerView(APIView):
    """
    API to short url
    """
    def post(self, request):
        data = request.data
        serializer = UrlShortenerSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            res_data = serializer.data
            res_data.update({"short_url": settings.DOMAIN + res_data["short_url"]})
            return Response(data=res_data)
        return Response(data= {"error_msg": "something went wrong"}, status=HTTP_400_BAD_REQUEST)


class ActualUrlView(APIView):
    """
    API to short url
    """
    def get(self, request, short_url):
        path = short_url
        _actual_url = get_actual_path(path)
        return HttpResponseRedirect(_actual_url)




