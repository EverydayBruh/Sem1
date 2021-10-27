from django.http import JsonResponse
from .models import Category
from .serializers import CategorySerializer

def api_category(request):
    if request.method == 'GET':
        category = Category.objects.all()
        serializer = CategorySerializer(category, many=True)
        return JsonResponse(serializer.data, safe=False)
