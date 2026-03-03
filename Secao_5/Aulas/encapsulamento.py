"""
Encapsulamento (modificadores de acesso: public, protected e private)
python NAO TEM modificadores de acesso
mas podemos seguir as seguintes convenções
    (sem underline) = public
        pode ser usado em qualquer lugar
_   (um underline) = protected
        não DEVE ser usado fora da classe ou suas subclasse
__  (dois underlines) = private
        'name mangling' (desfiguração de nomes) em Python
        só DEVE ser usado na classe em que foi declarado
"""

class Foo:
    def __init__(self):
        self.public = 'Isso é publico'
        self._protected = 'isso é protegido'
        self.__private = 'Isso é privado'
