from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
from rest_framework import serializers


class SnippetSerializers(serializers.Serializer):
    # 定义序列化器，用于模型数据校验
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=True, allow_blank=True, max_length=100)
    code = serializers.CharField(style={'base_template': 'textarea.html'})
    linenos = serializers.BooleanField(required=False)
    language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
    style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')

    def create(self, validated_data):
        """
        根据提供的验证过的数据创建并返回新的实例
        :param validated_data:
        :return:
        """
        return Snippet.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        根据提供的验证过的数据更新并返回已经存在的实例
        :param instance:
        :param validated_data:
        :return:
        """
        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.linenos = validated_data.get('linenos', instance.linenos)
        instance.language = validated_data.get('language', instance.language)
        instance.style = validated_data.get('style', instance.style)
        instance.save()
        return instance