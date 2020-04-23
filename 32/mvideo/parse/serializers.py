from rest_framework.serializers import ModelSerializer
from parse.models import Comp


class CompSerializer(ModelSerializer):

    class Meta:
        model = Comp
        fields = ('name', 'price')