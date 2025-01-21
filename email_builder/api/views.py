from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.decorators import api_view
from .models import EmailTemplate
from .serializers import EmailTemplateSerializer

class GetEmailLayout(APIView):
    def get(self, request):
        with open('layout.html', 'r') as f:
            html_content = f.read()
        return HttpResponse(html_content, content_type='text/html')

class UploadImage(APIView):
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request):
        file = request.FILES['file']
        file_path = f'media/images/{file.name}'
        with open(file_path, 'wb') as f:
            for chunk in file.chunks():
                f.write(chunk)
        return Response({'url': f'/media/images/{file.name}'})

class UploadEmailConfig(APIView):
    def post(self, request):
        serializer = EmailTemplateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Template saved successfully!'})
        return Response(serializer.errors)

class RenderAndDownloadTemplate(APIView):
    def get(self, request):
        template = EmailTemplate.objects.first()  # Fetch the latest template
        with open('layout.html', 'r') as f:
            layout = f.read()

        rendered_html = layout.replace('{{title}}', template.title).replace(
            '{{content}}', template.content).replace(
            '{{image}}', f'<img src="{template.image.url}" />'
        )
        response = HttpResponse(rendered_html, content_type='text/html')
        response['Content-Disposition'] = 'attachment; filename="email_template.html"'
        return response
