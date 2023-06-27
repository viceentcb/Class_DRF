# Django and DRF imports
from rest_framework import serializers

# proof class imports
from .models import Shirt, ColorType
from authentication.serializers import UserProfileSerializer


class ListShirtSerializer(serializers.ModelSerializer):

    color = serializers.ChoiceField(choices=ColorType.choices, source='get_color_display')
    user_id = UserProfileSerializer()
    is_favorite = serializers.SerializerMethodField()
    favorites = serializers.SerializerMethodField()

    class Meta:
        model = Shirt
        exclude = ["created_at", "updated_at", "deleted_at", "active"]

    def get_is_favorite(self, obj):
        return self.context["request"].user.is_favorite(obj)

    def get_favorites(self, obj):
        return obj.favorites()

class ListProfileShirtSerializer(serializers.ModelSerializer):
    user_id = UserProfileSerializer()

    color = serializers.ChoiceField(choices=ColorType.choices, source='get_color_display')

    class Meta:
        model = Shirt
        fields = "__all__"


class CreateShirtSerializer(serializers.ModelSerializer):

    class Meta:
        model = Shirt
        fields = "__all__"

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        color_key = representation['color']
        color_value = dict(ColorType.choices)[color_key]
        representation['color'] = color_value
        return representation


class UpdateShirtSerializer(serializers.ModelSerializer):

    color = serializers.ChoiceField(choices=ColorType.choices, source='get_color_display')

    class Meta:
        model = Shirt
        fields = "__all__"
        read_only_fields = ["id", "color", "phrase", "emoji"]
