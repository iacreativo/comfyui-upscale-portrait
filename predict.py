from cog import BasePredictor, Input, Path
from PIL import Image
import requests
import os
import json

class Predictor(BasePredictor):
    def setup(self):
        # Validación de presencia de modelos
        required_models = [
            "4x_NMKD-Siax_200k.pth",
            "FLUX.1-Turbo-Alpha 8steps .safetensors",
            "Flux1-Dev-SRPO-v1-Q8_0.gguf",
            "GFPGANv1.4.pth",
            "ae.safetensors",
            "clip_l.safetensors",
            "flux1-dev-Q8_0.gguf",
            "seedvr2_ema_7b_fp16.safetensors",
            "t5xxl_fp8_e4m3fn.safetensors"
        ]
        missing = [m for m in required_models if not os.path.exists(m)]
        if missing:
            raise RuntimeError(f"Faltan modelos esenciales: {missing}")

        # Workflow, si lo necesitas cargar global
        try:
            with open("workflow_api.json") as f:
                self.workflow = json.load(f)
        except Exception as e:
            self.workflow = None
            print("Error cargando workflow_api.json:", e)

    def predict(
        self,
        image: Path = Input(description="Imagen local para procesar", default=None),
        image_url: str = Input(description="URL de imagen (si no se carga archivo)", default=""),
    ) -> Path:
        try:
            if image is not None:
                img = Image.open(str(image))
            elif image_url:
                resp = requests.get(image_url, stream=True)
                resp.raise_for_status()
                img = Image.open(resp.raw)
            else:
                raise ValueError("Debes enviar image o image_url")

            img = img.convert("RGB")
            output_path = "output.jpg"
            img.save(output_path)
            # Aquí aplicarías el workflow real con tus modelos
            # output_path debe devolver la imagen procesada final
            return Path(output_path)
        except Exception as e:
            # Crea un archivo txt con el error y lo retorna como señal
            err_path = "error.txt"
            with open(err_path, "w") as f:
                f.write(str(e))
            return Path(err_path)
