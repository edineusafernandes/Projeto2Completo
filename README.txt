Introdução

Atividade do módulo de Django do Bootcamp Python oferecido pela XP através do IGTI.

 Este projeto tem como objetivo criar uma aplicação Django funcional, 
desde a configuração básica até o desenvolvimento de páginas dinâmicas 
utilizando o modelo MVP (Model View Presenter). 
Iniciamos verificando a versão do Python, criando e ativando um ambiente virtual, 
instalando o Django e gerando o arquivo de dependências. 
Criamos um projeto chamado projeto1 e configuramos o arquivo settings.py 
para gerenciar arquivos estáticos e templates. Adicionamos o app app1, 
configuramos rotas, views e um modelo User. Realizamos migrações, 
criamos um super usuário e registramos o modelo no admin. Por fim, 
desenvolvemos páginas HTML e formulários.

####################### Configuração básica #######################

Verificar a versão do python (python 3.x.x)

Criar um ambiente virtual (python -m venv ./env)

Ativar o ambiente virtual (source ./env/bin/activate)

Instalação do django (pip install django)

Verificar a versão do django (python -m django --version)

guardar as dependências (pip freeze > requeriments.txt)

#######################   #######################

Criar projeto django (django-admin startproject projeto1)

Configurações do settings.py - :
static: //resposta do chatGPT//
STATIC_URL = '/static/'

STATICFILES_DIRS = [os.path.join(BASE_DIR, 'staticfiles')]

TEMPLATES > DRIS add: 'templates'

Subir aplicação no servidor: entrar na pasta projeto1 (cd projeto1/)
python manage.py runserver
CTRL+CLICK para abrir no navegador

CTRL+C para derrubar o servidor local
.......................................................................
################ MVP - Model View presenter ################

Criação de aplicativo dentro do projeto djanfo -  não precisa Ativar

Comando para criar a pasta do app (python manage.py startapp app1)

projeto1 > urls.py > urlpartterns >     path('app1/', include('app1.urls')),

app1 > urls.py > from .views import index

urlpatterns = [
    path('', index, name='index'),
]

app1 > views.py > from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello world, Edineusa!")

Comando para subir a aplicação no servidor local: python manage.py runserver
CTRL+click em http://127.0.0.1:8000/
Digitar após a / app1
    *******************************************************

Model
class User (models.Model):
    nome = models.CharField('nome', max_length=30)
    telefone = models.IntegerField('telefone')
    email = models.CharField('email', max_length=30)

    def _str_(self):
        return f"Nome:  {self.nome}, Telefone: {self.telefone}, E-mail: {self.email}"

Settings > Registrar o app > 'app1

Migrações

Criar as migrações: python manage.py makemigrations

Aplicar as migrações (criação das tabelas no BD Sqlite) > python manage.py migrate

-------------------------------- SHELL------------------
cd projeto1/
Verificação de criaçã de tabelas: python manage.py shell
from app1.models import User > User.objexts.all() (lista os usuários criados) > (Criar usuário) User(nome="",telefone=00000,email="") > User.save() > User.id 
----------------------------------------------------------
Criar super usuário (python manage.py createsuperuser)
edineusa - edineusa08@gmail.com - Neusa1234

Registrar models no admin.py (app1)
from .models import User
admin.site.register(User)
>> Adicionar e remove usuários

******************************************************************
Ajuste no campo 'telefone' > models.py > BigIntegerField 
Executar as migrações para valiar a mudança:
Criar as migrações: python manage.py makemigrations
Aplicar as migrações (criação das tabelas no BD Sqlite) > python manage.py migrate

python manage.py runserver

.........................TEMPLATE..............................
Dentro do app1 > template > Criar: user > indes.html e criar.html
Modificar na pasta viws.py: from django.shortcuts import render > 
def index(request):
    return render(request, 'user/index.html')
def create(request):
    return render(request, 'user/criar.html')

app1 > url.py 
from .views import index, create

urlpatterns = [
    path('', index, name='index'),
        path('criar', create, name='criar'),
]

.........................FORMULARIOS..............................
Criar no app1 - form.py - criar formulario
Testar formulário

bootstrap(https://getbootstrap.com/)
jinja (https://jinja.palletsprojects.com/en/3.1.x/switching/#django)
Criar no app1/template - base.html - 
Criar pasta static

*O formulário não funciona.

.........................Rotas..............................
Criar páginas dinamicas
