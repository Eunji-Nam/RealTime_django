from django.shortcuts import render
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from shop.models import Shop, Review
from shop.serializers import ShopSerializer, ReviewSerializer


class ShopViewSet(ModelViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer

    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]
        return [IsAuthenticated()]

    # def get_queryset(self):
    #     qs= super().get_queryset()
    #
    #     query=self.request.query_params.get("query","")
    #     if query:
    #         qs=qs.filter(champion__icontains=query)
    #
    #     return qs


class ReviewViewSet(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]
        return [IsAuthenticated()]