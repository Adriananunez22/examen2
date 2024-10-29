from classGetRecord import resultado_label
class ShowRecord:

    def __init__(self):
        self.__textoRegistro = None

    def mostrar_datos(self, registro):

        self.__textoRegistro = registro

        resultado_label.config(text=self.__textoRegistro)