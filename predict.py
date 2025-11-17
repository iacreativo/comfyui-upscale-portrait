from cog import BasePredictor, Input, Path
from PIL import Image
import requests
import os
import subprocess

class Predictor(BasePredictor):
    def setup(self):
        # Si necesitas validar modelos/pesos antes de correr, hazlo aquí.
        print("Predictor inicializado.")

    def predict(
        self,
        image: Path = Input(description="Imagen a procesar (jpg/png)", default=None),
        image_url: str = Input(description="URL de imagen (opcional)", default=""),
    ) -> Path:
        try:
            # 1. Recibe imagen y la guarda como input.jpg
            if image:
                img = Image.open(str(image))
            elif image_url:
                resp = requests.get(image_url, stream=True)
                resp.raise_for_status()
                img = Image.open(resp.raw)
            else:
                raise ValueError("Debes enviar 'image' o 'image_url'")
            input_path = "/src/input.jpg"
            img.save(input_path)
            print(f"Imagen guardada como {input_path}")

            # 2. Ejecuta tu workflow. Ajusta el comando si necesitas flags diferentes.
            # Asume que ComfyUI/main.py está en el repo, y workflow_api.json es tu workflow
            result = subprocess.run([
                "python", "main.py",
                "--workflow", "workflow_api.json",
                "--input", input_path
            ], capture_output=True, text=True)
            print("STDOUT:", result.stdout)
            print("STDERR:", result.stderr)

            # 3. Devuelve el archivo resultante. Ajusta nombre/ruta si tu workflow produce otro nombre.
            output_path = "/src/output.jpg"
            if os.path.exists(output_path):
                print(f"Resultado listo: {output_path}")
                return Path(output_path)
            else:
                print("No se encontró la imagen procesada, devolviendo error.")
                err_path = "/src/error.txt"
                with open(err_path, "w") as f:
                    f.write(result.stderr)
                return Path(err_path)
        except Exception as e:
            print("Error en la función predict:", e)
            err_path = "/src/error.txt"
            with open(err_path, "w") as f:
                f.write(str(e))
            return Path(err_path)
