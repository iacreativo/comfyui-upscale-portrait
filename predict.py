from typing import Any
import json

class Predictor:
    def __init__(self):
        with open("workflow_api.json", "r") as f:
            self.workflow = json.load(f)

    def predict(self, **inputs) -> Any:
        return {"workflow": self.workflow}
