from rest_framework.generics import ListAPIView

from parse.models import Comp
from parse.serializers import CompSerializer


class ParseView(ListAPIView):
    queryset = Comp.objects.all()
    serializer_class = CompSerializer
