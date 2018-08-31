from rest_framework import serializers

from .models import FlexUser, Flex


class GenerateCodeSerializer(serializers.Serializer):
    phone = serializers.CharField(max_length=12, min_length=12)


class GenerateTokenSerializer(serializers.Serializer):
    code = serializers.CharField(max_length=4, min_length=4)
    phone = serializers.CharField(max_length=12, min_length=12)


class FlexUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlexUser
        fields = [
            'first_name',
            'last_name',
            'username',
            'bio',
            'phone',
        ]


class FlexSerializer(serializers.ModelSerializer):
    owner = FlexUserSerializer(required=False)
    members_count = serializers.IntegerField(source='get_members_count', read_only=True)
    followed_count = serializers.SerializerMethodField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True, required=False)

    class Meta:
        model = Flex
        exclude = ['members']

    def get_followed_count(self, obj):
        """
        Count user's friends which already members in this flex.
        :param obj:
        :return: int:
        """

        user_followed = self.context.get('request').user.followed.all()
        flex_members = obj.members.all()
        return user_followed.intersection(flex_members).count()


