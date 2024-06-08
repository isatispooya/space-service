from rest_framework import serializers
from .models import Menu

class MenuSerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField()

    class Meta:
        model = Menu
        fields = ['id', 'title', 'url', 'icon', 'children']

    def get_children(self, obj):
        children = obj.children.all()
        if children:
            return MenuSerializer(children, many=True).data
        return None
