from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import URL
from .serializers import URLSerializer

def index(request):
    return render(request, 'index.html')

class URLViewSet(viewsets.ModelViewSet):
    queryset = URL.objects.all()
    serializer_class = URLSerializer
    ordering_fields = ['short_url','long_url']
    filterset_fields = ['short_url','long_url']


    def create(self, request, *args, **kwargs):
        # Check if the long_url already exists in the database
        long_url = request.data.get('long_url')
        existing_url = URL.objects.filter(long_url=long_url).first()

        if existing_url:
            # If it exists, return the existing short_url
            serializer = self.get_serializer(existing_url)
            return Response(serializer.data, status=status.HTTP_200_OK)

        # If it doesn't exist, proceed to create a new one
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    @action(detail=True, methods=['get'], url_path='redirect')
    def redirect_to_long_url(self, request, pk=None):
        url_instance = get_object_or_404(URL, short_url=pk)
        return redirect(url_instance.long_url)
