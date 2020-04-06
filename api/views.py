from rest_framework import viewsets
from .models import Entry,Livro,Receita
from .serializers import EntrySerializer,LivroSerializer


# Create your views here.
class EntryViewSet(viewsets.ModelViewSet):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer


class LivroViewSet(viewsets.ModelViewSet):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer