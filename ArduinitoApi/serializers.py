from rest_framework import serializers
from Arduinitos import models

class DynamicFieldsModelSerializer(serializers.HyperlinkedModelSerializer):
    def __init__(self, *args, **kwargs):

        fields = kwargs.pop('fields', None)

        super(DynamicFieldsModelSerializer, self).__init__(*args, **kwargs)

        if fields:
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields.keys())
            for field_name in existing - allowed:
                self.fields.pop(field_name)

class TemperaturaSerializer(DynamicFieldsModelSerializer):

    class Meta:
        model = models.Temperatura
        fields = ('id_temp', 'valor', 'unidad', 'estado')
        extra_kwargs = {
            'url': {'view_name': 'temperatura-detail', 'lookup_field': 'url'},
        }

class AguaSerializer(DynamicFieldsModelSerializer):

    class Meta:
        model = models.Agua
        fields = ('id_agua', 'valor', 'unidad', 'estado')
        extra_kwargs = {
            'url': {'view_name': 'agua-detail', 'lookup_field': 'url'},
        }

class LuzSerializer(DynamicFieldsModelSerializer):

    class Meta:
        model = models.Luz
        fields = ('id_Luz', 'valor', 'unidad', 'estado')
        extra_kwargs = {
            'url': {'view_name': 'luz-detail', 'lookup_field': 'url'},
        }

class InformacionSerializer(DynamicFieldsModelSerializer):
    temperatura = TemperaturaSerializer()
    agua = AguaSerializer()
    luz = LuzSerializer()

    class Meta:
        model = models.Informacion
        fields = ('id_info', 'fecha', 'hora', 'temperatura', 'agua', 'luz')
        extra_kwargs = {
            'url': {'view_name': 'informacion-detail', 'lookup_field': 'url'},
        }
