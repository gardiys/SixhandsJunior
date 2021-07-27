from rest_framework import status, viewsets, mixins, generics, decorators, views,\
    permissions as rest_permissions
from rest_framework.response import Response

from django_filters import rest_framework as filters

from . import models, serializers, permissions
from .paginators import CustomPagination
from .filters import BookFilter



@decorators.api_view(["GET", "POST"])
def get_books(request):
    # Через сериализатор
    # books = models.Book.objects.all() # select всех полей
    # ser = serializers.BookSerializer(books, many=True)
    # return Response(ser.data, status=status.HTTP_200_OK)
    # Через выборку
    if request.method == "GET":
        books = models.Book.objects.values("id", "name", 'pages')
        return Response(books)
    elif request.method == "POST":
        return Response(status.HTTP_201_CREATED)


class BookAPIView(views.APIView):

    def get(self, request):
        books = models.Book.objects.values('id', 'name')
        return Response(books)

    def post(self, request):
        return Response(status=status.HTTP_201_CREATED)


class BookGenericAPIView(generics.ListCreateAPIView):
    queryset = models.Book.objects.all()
    serializer_class = serializers.BookSerializer


class BookGenericDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Book.objects.all()
    serializer_class = serializers.BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = models.Book.objects.all()
    serializer_class = serializers.BookSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = BookFilter
    pagination_class = CustomPagination
    permission_classes = [rest_permissions.IsAuthenticated, permissions.IsManager]

    @decorators.action(methods=['GET'], detail=False)
    def statistics(self, request, *args, **kwargs):
        return Response(self.get_queryset().count())
