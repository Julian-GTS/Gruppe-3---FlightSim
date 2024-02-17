from django.shortcuts import render
from .models import JsonData

def index(request):
    if request.method == 'POST':
        json_file = request.FILES['json_file']
        data = json_file.read().decode('utf-8')
        JsonData.objects.create(data=data).save()
        return render(request, 'success.html')
    return render(request, "upload.html")

# def save_json_to_database(request):
#     if request.method == 'POST':
#         try:
#             json_file = request.FILES['json_file']
#             data = json_file.read().decode('utf-8')  # Lese die JSON-Daten aus der Datei
#             parsed_data = json.loads(data)  # Parst die JSON-Daten

#             # Speichere die geparsten Daten in der Datenbank
#             JsonData.objects.create(data=parsed_data)

#             return JsonResponse({'message': 'JSON-Daten erfolgreich gespeichert.'}, status=200)
#         except Exception as e:
#             return JsonResponse({'error': str(e)}, status=400)

#     return JsonResponse({'message': 'Bitte eine JSON-Datei hochladen.'}, status=200)