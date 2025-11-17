FROM python:3.10

WORKDIR /src

# Dependencias mínimas para ComfyUI y nodos comunes
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Descarga los modelos exactos desde HuggingFace (reemplaza los nombres con los de tu workflow si fuera necesario)
RUN wget -O "4x_NMKD-Siax_200k.pth" "https://huggingface.co/JAJOED/UpcalePortrait/resolve/main/4x_NMKD-Siax_200k.pth"
RUN wget -O "FLUX.1-Turbo-Alpha 8steps .safetensors" "https://huggingface.co/JAJOED/UpcalePortrait/resolve/main/FLUX.1-Turbo-Alpha%208steps%20.safetensors"
RUN wget -O "Flux1-Dev-SRPO-v1-Q8_0.gguf" "https://huggingface.co/JAJOED/UpcalePortrait/resolve/main/Flux1-Dev-SRPO-v1-Q8_0.gguf"
RUN wget -O "GFPGANv1.4.pth" "https://huggingface.co/JAJOED/UpcalePortrait/resolve/main/GFPGANv1.4.pth"
RUN wget -O "ae.safetensors" "https://huggingface.co/JAJOED/UpcalePortrait/resolve/main/ae.safetensors"
RUN wget -O "clip_l.safetensors" "https://huggingface.co/JAJOED/UpcalePortrait/resolve/main/clip_l.safetensors"
RUN wget -O "flux1-dev-Q8_0.gguf" "https://huggingface.co/JAJOED/UpcalePortrait/resolve/main/flux1-dev-Q8_0.gguf"
RUN wget -O "seedvr2_ema_7b_fp16.safetensors" "https://huggingface.co/JAJOED/UpcalePortrait/resolve/main/seedvr2_ema_7b_fp16.safetensors"
RUN wget -O "t5xxl_fp8_e4m3fn.safetensors" "https://huggingface.co/JAJOED/UpcalePortrait/resolve/main/t5xxl_fp8_e4m3fn.safetensors"
# Si tienes otros archivos añade más líneas como las de arriba.

# Nodos personalizados (repos oficiales confirmados)
RUN git clone https://github.com/rgthree/rgthree-comfy custom_nodes/rgthree-comfy
RUN git clone https://github.com/ssitu/ComfyUI_UltimateSDUpscale custom_nodes/ComfyUI_UltimateSDUpscale
RUN git clone https://github.com/Jonseed/ComfyUI-Detail-Daemon custom_nodes/ComfyUI-Detail-Daemon
RUN git clone https://github.com/yolain/ComfyUI-Easy-Use custom_nodes/ComfyUI-Easy-Use
RUN git clone https://github.com/city96/ComfyUI-GGUF custom_nodes/ComfyUI-GGUF
RUN git clone https://github.com/chflame163/ComfyUI_LayerStyle custom_nodes/ComfyUI_LayerStyle
RUN git clone https://github.com/Gourieff/ComfyUI-ReActor custom_nodes/ComfyUI-ReActor || git clone https://github.com/lz98/comfyui-reactor-node custom_nodes/ComfyUI-ReActor
RUN git clone https://github.com/numz/ComfyUI-SeedVR2_VideoUpscaler custom_nodes/ComfyUI-SeedVR2_VideoUpscaler
RUN git clone https://github.com/ZhiHui6/zhihui_nodes_comfyui custom_nodes/zhihui_nodes_comfyui

COPY . .

ENV PORT 8080
EXPOSE 8080
