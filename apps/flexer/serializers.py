from rest_framework import serializers

from .models import FlexUser, Flex


class GenerateCodeSerializer(serializers.Serializer):
    phone = serializers.CharField(max_length=12, min_length=12)


class GenerateTokenSerializer(serializers.Serializer):
    code = serializers.CharField(max_length=4, min_length=4)
    phone = serializers.CharField(max_length=12, min_length=12)


class FlexUserSerializer(serializers.ModelSerializer):
    phone = serializers.CharField(read_only=True)

    class Meta:
        model = FlexUser
        fields = [
            'first_name',
            'last_name',
            'username',
            'bio',
            'phone',
            'photo'
        ]


class FlexListSerializer(serializers.ModelSerializer):
    owner = FlexUserSerializer(required=False, read_only=True)
    members_count = serializers.IntegerField(source='get_members_count', read_only=True)
    friends_count = serializers.SerializerMethodField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True, required=False)

    class Meta:
        model = Flex
        exclude = ['members']

    def get_friends_count(self, obj):
        """
        Count user's friends which already members in this flex.
        :param obj:
        :return: int:
        """

        friends = self.context.get('request').user.friends.all()
        flex_members = obj.members.all()
        return friends.intersection(flex_members).count()


class FlexDetailSerializer(serializers.ModelSerializer):
    owner = FlexUserSerializer(required=False, read_only=True)
    members_count = serializers.IntegerField(source='get_members_count', read_only=True)
    friends_count = serializers.SerializerMethodField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True, required=False)

    class Meta:
        model = Flex
        fields = '__all__'

    def get_friends_count(self, obj):
        """
        Count user's friends which already members in this flex.
        :param obj:
        :return: int:
        """

        friends = self.context.get('request').user.friends.all()
        flex_members = obj.members.all()
        return friends.intersection(flex_members).count()

