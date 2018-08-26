from rest_framework import serializers

from .models import FlexUser, Flex


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


