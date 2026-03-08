from .dados import sobre

def dados_globais(request):
    return {
        'contato': {
            'email': sobre['email'],
            'linkedin': sobre['linkedin'],
            'github': sobre['github'],
            'nome': sobre['nome'],
        }
    }