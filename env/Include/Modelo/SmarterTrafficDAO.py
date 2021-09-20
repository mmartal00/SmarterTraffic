from flask import json
import Include.conexion as cnx
from Include.Modelo.SmarterTrafficVO import SmarterTrafficVO

class SmarterTrafficDAO:
    def __init__(self):
        self.__tabla = "SmarterTraffic"
    
    def selectall(self):
        try:
            conn=cnx.mysql.connect()
            cursor=conn.cursor()
            cursor.execute('select * from '+self.__tabla+' order by IdUsuario desc')
            data = cursor.fetchall()
            listaVO=[]
            for fila in data:
                vo=SmarterTrafficVO(fila[0], fila[1], fila[2], fila[3], fila[4])
                listaVO.append(vo)
                return listaVO
        except Exception as e:
            return json.dumps({'error':str(e)})
        finally:
            cursor.close()
            conn.close()