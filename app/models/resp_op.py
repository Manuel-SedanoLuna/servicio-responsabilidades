class AMEF_GPT:
    def __init__(
        self, 
        id: int, seccion: str, responsabilidad_operativa: str, problematica: str, efecto_de_falla: str, 
        severidad: int, ocurrencia: int, deteccion: int, riesgo_potencial: int, acciones_preventivas: str = None
        ):
        self.id = id
        self.seccion = seccion
        self.responsabilidad_operativa = responsabilidad_operativa
        self.problematica = problematica
        self.efecto_de_falla = efecto_de_falla
        self.severidad = severidad
        self.ocurrencia = ocurrencia
        self.deteccion = deteccion
        self.riesgo_potencial = riesgo_potencial
        self.acciones_preventivas = acciones_preventivas

    def display_risk(self):
        return f"AMEF Risk {self.id}: {self.problematica} (RP: {self.riesgo_potencial})"