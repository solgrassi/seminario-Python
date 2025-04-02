from datetime import datetime
import random
import string

def generar_codigo (user):
    """
    Genera un codigo, teniendo en cuenta un nombre recibido,
    la fecha, y una serie de caracteres random.
    Parametros:
    nombre de usuario (Str)
    Retorno:
    codigo (Str) todo en mayuscula
    """
    fec = datetime.now().strftime("%Y-%m-%d")
    codigo = user.upper() +"-" + fec.replace('-', '') + "-"
    dig_faltante= (30 - len(codigo))
    caracteres = string.ascii_letters + string.digits
    aleatorio = ''.join(random.choices(caracteres, k=dig_faltante))
    
    return codigo + aleatorio.upper()

