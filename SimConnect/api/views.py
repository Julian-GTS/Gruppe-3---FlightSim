from io import BytesIO
import json
from django.conf import settings
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect
from . import api_response, urls
from upload_jason.models import JsonData
import base64
from PIL import Image, ImageDraw, ImageFont

from . import flight_data, flight_data_helper

def redirect_latest(request):
    return redirect("api-root")

def root(request):
    response = api_response.APIResponse(True, ["Welcome to the API!", "Endpoint list: /api/v1/tree"])
    return JsonResponse(response.to_json())

def tree(request):
    response = api_response.APIResponse(True, [pattern.name for pattern in urls.urlpatterns])
    return JsonResponse(response.to_json())

def jsondata(request):
    list = JsonData.objects.values_list()
    response = api_response.APIResponse(True, [json.loads(entry[1]) for entry in list])
    return JsonResponse(response.to_json())

def serve_image(request):
    # Assuming you have the base64 encoded image stored in a variable called 'image_data'
    with (settings.BASE_DIR / "static" / "bg.jpg").open("rb") as image_file:
        image_data = base64.b64encode(image_file.read()).decode('utf-8')

    # Decode the base64 image data
    decoded_image = base64.b64decode(image_data)

    # Open the image using PIL
    image = Image.open(BytesIO(decoded_image))

    # Get the text from the request.GET parameters
    text = request.GET.get('text')

    # Create a new image with the same size as the original image
    new_image = Image.new(image.mode, image.size)

    # Draw the original image onto the new image
    new_image.paste(image, (0, 0))

    # Create a draw object
    draw = ImageDraw.Draw(new_image)

    # Set the font and size
    font = ImageFont.truetype("segoeui.ttf", image.width/text.__len__())

    # Set the text color
    text_color = (0, 0, 0)

    # Set the text position
    text_position = (image.width*0.2, image.height*0.5)

    # Draw the text onto the image
    draw.text(text_position, text, font=font, fill=text_color)

    # Create a response object
    response = HttpResponse(content_type="image/png")

    # Save the modified image to a byte stream
    modified_image_stream = BytesIO()
    new_image.save(modified_image_stream, format='PNG')

    # Set the content of the response to the modified image
    response.write(modified_image_stream.getvalue())

    return response

def flight_data(request):
    flight_data_obj = flight_data_helper.generate_flight_data()
    file_path = settings.BASE_DIR / "flight_data.json"
    flight_data_helper.write_flight_data_to_file(flight_data_obj, file_path)
    response = api_response.APIResponse(True, flight_data_obj.to_json())
    return JsonResponse(response.to_json())