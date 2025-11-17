import json

class Predictor:
    def __init__(self):
        # Carga tu workflow aquí
        with open("workflow_api.json", "r") as f:
            self.workflow = json.load(f)

    def predict(self, **inputs):
        # Aquí deberías poner la lógica para ejecutar tu workflow
        # Por ahora, solo devuelve el workflow cargado
        return {"workflow": self.workflow}
