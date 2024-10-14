from rest_framework import APIView
from rest_framework.response import Response
from .models import Product, Variant
from .serializers import ProductSerializer

class BulkInsert(APIView):
    
    def post(self, request):
        products_data = request.data
        #get data from request
        
        #create productinstances from requested data
        products = [Product(name=data['name'], image=data['image']) for data in products_data]
        created_products = Product.objects.bulk_create(products) #to insert many products at once
       
       #create and combine variants for every product
        variants = [] 
        for idx, product_data in enumerate(products_data):
            for variant_data in product_data['variants']:
               variant = Variant(
                   product = created_products[idx],
                   variant_name =variant_data['variant_name'],
                   sku = variant_data['sku'],
                   price = variant_data['price'],
                   details = variant_data['details']
               )
               variants.append(variant)
               
        Variant.objects.bulk_create(variants)
    
        return Response({'message': 'Products and all variants added.'})