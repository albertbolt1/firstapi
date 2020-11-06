from django.shortcuts import render

# Create your views here.
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from api.models import Pizza
from api.serializers import PizzaSerializer
from rest_framework.decorators import api_view



@api_view(['GET','POST','DELETE'])
def pizza_list(request):
	if(request.method=='GET'):
		pizza_list=Pizza.objects.all()

		pizza_name=request.query_params.get('name', None)
		if pizza_name is not None:
			pizza_list = pizza_list.filter(title__icontains=pizza_name)

		pizza_serializer=PizzaSerializer(pizza_list, many=True)
		return JsonResponse(pizza_serializer.data, safe=False)

	elif(request.method=='POST'):
		pizza_list=JSONParser().parse(request)
		pizza_serializer=PizzaSerializer(data=pizza_list)
		if(pizza_serializer.is_valid()):
			pizza_serializer.save()
			return JsonResponse(pizza_serializer.data, status=status.HTTP_201_CREATED)
		return JsonResponse(pizza_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	elif(request.method=='DELETE'):
		count=Pizza.objects.all().delete()
		return JsonResponse({'message': '{} pizzas were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)



@api_view(['GET','PUT','DELETE'])
def pizza_detail(request,pk):

	try:
		pizza_list=Pizza.objects.get(pk=pk)
	except:
		return JsonResponse({'message': 'The pizza does not exist'}, status=status.HTTP_404_NOT_FOUND)

	if(request.method=="GET"):
		pizza_serializer=PizzaSerializer(pizza_list)
		return JsonResponse(pizza_serializer.data)

	elif(request.method=="PUT"):
		pizza_list_data=JSONParser().parse(request)
		pizza_serializer=PizzaSerializer(pizza_list,data=pizza_list_data)
		if(pizza_serializer.is_valid()):
			pizza_serializer.save()
			return JsonResponse(pizza_serializer.data, status=status.HTTP_201_CREATED)
		return JsonResponse(pizza_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	elif(request.method=='DELETE'):
		count=Pizza.objects.get(pk=pk).delete()
		return JsonResponse({'message': 'pizza was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)



@api_view(['GET'])
def pizza_list_veg_nonveg(request):
    pizza_list=Pizza.objects.filter(veg_nonveg=True)
        
    if request.method == 'GET': 
        pizza_serializer = PizzaSerializer(pizza_list, many=True)
        return JsonResponse(pizza_serializer.data, safe=False)
    





