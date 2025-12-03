import json

caminhoCompleto = 'C:\\Users\\Dell\\Documents\\Estudo\\Cursos\\Udemy\\Python\\Secao_4\\Aulas\\'
arquivo = 'primeiroSalvarDados.json'
caminhoCompleto += arquivo


dados = {
    "Tipos de dados":{
        "boolean": [True, False],
        "Number": 1234,
        "String": "Texto",
        "Null": None, 
        "[]": "array",
        "{}": "objeto"
    },
    "Importante": "json, não precisa ter varios dados, apenas um valor também é funcional"
}

with open(caminhoCompleto, 'w', encoding='utf8') as arquivo:
    json.dump(
        dados, # o valor que deseja colocar
        arquivo, # o arquivo que abriu
        ensure_ascii=False, # irá formatar no estilo json
        indent=2, # irá identar um embaixo do outro
        )