
class PSU:
    def __init__(
        self,
        id: int, folio: str, fecha: str, hora: str, cr_plaza: str, 
        pregunta_meta: str, plaza: str, tienda: str, encuesta: str, 
        pregunta: str, respuesta: str, driver: str, seccion: str, 
        region: str, zona: str, concepto: str, 
        hallazgo_pregunta: str = None, numeracion: int = None
        ):
        self.id = id  # int
        self.folio = folio  # int
        self.fecha = fecha  # datetime
        self.hora = hora  # string
        self.cr_plaza = cr_plaza  # string
        self.pregunta_meta = pregunta_meta  # string
        self.plaza = plaza  # string
        self.tienda = tienda  # string
        self.encuesta = encuesta  # string
        self.pregunta = pregunta  # string
        self.respuesta = respuesta  # string
        self.hallazgo_pregunta = hallazgo_pregunta  # string or None
        self.numeracion = numeracion  # int or None
        self.driver = driver  # string
        self.seccion = seccion  # string
        self.region = region  # string
        self.zona = zona  # string
        self.concepto = concepto  # string

    def display_info(self):
        return f"PSU Entry {self.folio}: {self.pregunta} - {self.respuesta}"