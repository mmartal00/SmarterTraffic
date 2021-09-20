class SmarterTrafficVO:

    def __init__(self, id, usuario, password, nombre, tipo_usuario):
        self.__id = id
        self.__idusuario = usuario
        self.__password = password
        self.__nombre = nombre
        self.__tipo_usuario = tipo_usuario

    #METODOS
    def setId(self, n):
        self.__id = n

    def getId(self):
        return self.__id

    def setIdUsuario(self, n):
        self.__idusuario = n

    def getIdUsuario(self):
        return self.__idusuario
    
    def setPassword(self, n):
        self.__password = n

    def getPassword(self):
        return self.__password

    def setNombre(self, n):
        self.__monto = n

    def getNombre(self):
        return self.__nombre

    def setTipoUsuario(self, n):
        self.__monto = n

    def getTipoUsuario(self):
        return self.__tipo_usuario