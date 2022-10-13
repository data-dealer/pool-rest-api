from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework import status

from .serializers import PoolSerializer
from .models import Pool


@api_view(['GET', 'POST'])
def PoolEndPoint(request, **kwargs):

    if request.method == 'GET':
        queryset = Pool.objects.all()
        serializer = PoolSerializer(queryset, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        pool_obj, created= Pool.objects.get_or_create(
            poolId=request.data["poolId"],
        )
        pool_obj.poolValues += request.data["poolValues"]
        pool_obj.save(update_fields=["poolValues"])
        status_code = status.HTTP_201_CREATED if created else status.HTTP_200_OK

        return Response(status=status_code)


def quantile(arr:list, q:float):
    """
    Parameters
    ----------
    arr : Input array.
    q : Quantile in range(1, 100) 
    ----------
    Test
    have the same result with numpy.quantile
    """
    arr = sorted(arr)
    index = (len(arr)-1) * q/100
    floor = int(index//1)
    ceil = int(-(-index//1))
    return arr[floor] * (ceil-index) + arr[ceil] * (index - floor)

@api_view(['POST'])
def PoolQuantileEndPoint(request, **kwargs):
    
    if request.method == 'POST':
        pool_obj = Pool.objects.get(
            poolId=request.data["poolId"],
        )
        res_data = {
            "totalElement": len(pool_obj.poolValues),
            "quantile": quantile(pool_obj.poolValues, float(request.data["percentile"]))
        }
        
        
        return JsonResponse(res_data, status=status.HTTP_200_OK)