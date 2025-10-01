from .models import ConfiguracaoPlataforma

def config_processor(request):
    config = ConfiguracaoPlataforma.objects.first()
    return {'config': config}