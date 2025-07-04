from rest_framework import serializers
from .models import Vacation, Like
from apps.core.models import Country


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['id', 'name']


class VacationSerializer(serializers.ModelSerializer):
    country_name = serializers.CharField(source='country.name', read_only=True)
    is_liked = serializers.SerializerMethodField()

    class Meta:
        model = Vacation
        fields = [
            'id', 'country', 'country_name', 'description',
            'start_date', 'end_date', 'price', 'image',
            'is_liked', 'created_at', 'updated_at'
        ]
        read_only_fields = ['created_at', 'updated_at']

    def get_is_liked(self, obj):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            return obj.is_liked_by(request.user)
        return False


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'
        read_only_fields = ('user',)
