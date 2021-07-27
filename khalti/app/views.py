from django.shortcuts import render
import requests
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
# Create your views here.
def index_page(request):
    price = 27000
    return render(request,"html/index.html",{'price':price})


@csrf_exempt
def khalti(request):
   data = request.POST
   product_id = data['product_identity']
   token = data['token']
   amount = data['amount']

   url = "https://khalti.com/api/v2/payment/verify/"
   payload = {
   "token": token,
   "amount": amount
   }
   headers = {
   "Authorization": "test_public_key_dc74e0fd57cb46cd93832aee0a390234"
   }
   
   response = requests.post(url, payload, headers = headers)
   
   response_data = json.loads(response.text)
   status_code = str(response.status_code)

   if status_code == '400':
      response = JsonResponse({'status':'false','message':response_data['detail']}, status=500)
      return response

   import pprint 
   pp = pprint.PrettyPrinter(indent=4)
   pp.pprint(response_data)
   
   return JsonResponse(f"Payment Success !! . {response_data['user']['idx']}",safe=False)