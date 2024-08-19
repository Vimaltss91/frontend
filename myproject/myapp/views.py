# Existing imports
from rest_framework import generics
from myapp.models import NamespaceStatus
from myapp.serializers import NamespaceStatusSerializer
import os

# New imports
from django.http import JsonResponse
import subprocess
from django.views.decorators.csrf import csrf_exempt
import json

class NamespaceStatusListView(generics.ListAPIView):
    queryset = NamespaceStatus.objects.all()
    serializer_class = NamespaceStatusSerializer

@csrf_exempt  # Disable CSRF for the API endpoint
def delete_namespace(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            namespace = data.get('namespace')

            if namespace:
                # Run the bash script to delete the namespace
                script_path = os.path.join(os.path.dirname(__file__), 'delete.sh')
                try:
                    subprocess.run([script_path, namespace], check=True) 
                    #subprocess.run(['./delete.sh', namespace], check=True)
                    return JsonResponse({'message': f'Namespace {namespace} deleted successfully!'})
                except subprocess.CalledProcessError as e:
                    return JsonResponse({'message': f'Error deleting namespace {namespace}: {str(e)}'}, status=500)
            else:
                return JsonResponse({'message': 'No namespace provided'}, status=400)

        except json.JSONDecodeError:
            return JsonResponse({'message': 'Invalid JSON input'}, status=400)
    else:
        return JsonResponse({'message': 'Only POST requests are allowed'}, status=405)
