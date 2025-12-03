"""
pip é um instalador de pacotes, ele baixa bibliotecas do pypi
link pypi:
https://pypi.org

Instalar pip
python.exe -m pip install --upgrade pip

Verificar o que está instalado no pip no ambiente
pip freeze

Verificar as versoes da biblioteca disponiveis
pip index versions [nomeBiblioteca]

instalar biblioteca
pip install [nomeBiblioteca]

desinstalar biblioteca 
pip uninstall [nomeBiblioteca]

instalando versão especifica
pip install [nomeBiblioteca]==[versão]

criando um requirements
pip freeze > requirements.txt

instalando requirements novamente 
pip install -r .\requirements.txt
"""