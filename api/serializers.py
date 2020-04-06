from rest_framework import serializers

from api.models import Livro
from .models import Entry, Livro, Receita, Blog


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['name', 'tagline']


class EntrySerializer(serializers.ModelSerializer):
    blog = BlogSerializer()

    class Meta:
        model = Entry
        fields = ['blog']

    def create(self, validated_data):
        blog_data = validated_data.pop('blog', None)
        if blog_data:
            blog = Blog.objects.get_or_create(**blog_data)[0]
            validated_data['blog'] = blog

        return Entry.objects.create(**validated_data)

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('blog')
        instance.name = profile_data.name
        instance.tagline = profile_data.tagline
        instance.save()


class ReceitaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receita
        fields = ['name', 'description']


class LivroSerializer(serializers.ModelSerializer):
    receitas = ReceitaSerializer(many=True)

    class Meta:
        model = Livro
        fields = ['receitas']

    def create(self, validated_data):
        receitas = validated_data.pop('receitas')
        instance = Livro.objects.create(**validated_data)
        for receita in receitas:
            instance.receitas.append(receita)
        return instance
