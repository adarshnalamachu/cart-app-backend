from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer

@api_view(['GET'])
def product_list(request):
    # products = Product.objects.all()
    # serializer = ProductSerializer(products, many=True)
    # return Response(serializer.data)
    qs = Product.objects.all()
    try:
        min_p = request.query_params.get('min_price')
        max_p = request.query_params.get('max_price')
        if min_p is not None:
            qs = qs.filter(price__gte=float(min_p))
        if max_p is not None:
            qs = qs.filter(price__lte=float(max_p))
    except (ValueError, TypeError):
        # ignore invalid params and return unfiltered results (or return bad request)
        pass

    serializer = ProductSerializer(qs, many=True)
    return Response(serializer.data)


