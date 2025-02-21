import requests
import json
import os

# Configuração da API
FACE_API_URL = "https://facialRecognitionCognitive.cognitiveservices.azure.com/face/v1.0/detect"
SUBSCRIPTION_KEY = "SUA_CHAVE_AQUI"  # Substitua pela sua chave do Azure
HEADERS = {
    "Ocp-Apim-Subscription-Key": SUBSCRIPTION_KEY,
    "Content-Type": "application/json"
}

# Diretórios de entrada e saída
INPUT_DIR = "inputs"
OUTPUT_DIR = "output"

# Criar diretório de saída se não existir
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Processar cada imagem na pasta 'inputs'
for image_name in os.listdir(INPUT_DIR):
    image_path = os.path.join(INPUT_DIR, image_name)
    
    # Verifica se é um arquivo de imagem válido
    if not image_name.lower().endswith(('.png', '.jpg', '.jpeg')):
        continue

    # Converte a imagem em uma URL pública ou carrega como bytes (caso API suporte)
    image_url = {"url": f"SUA_URL_DA_IMAGEM_AQUI/{image_name}"}
    
    # Parâmetros para a API
    params = {
        "returnFaceId": "true",
        "returnFaceAttributes": "age,gender,emotion,smile"
    }

    # Fazendo a requisição para a API
    response = requests.post(FACE_API_URL, headers=HEADERS, json=image_url, params=params)

    if response.status_code == 200:
        result = response.json()
        
        # Salvar resultado no arquivo de saída
        output_file = os.path.join(OUTPUT_DIR, f"{image_name}_result.json")
        with open(output_file, "w") as f:
            json.dump(result, f, indent=4)
        
        print(f"✅ Processado: {image_name}, resultado salvo em {output_file}")
    else:
        print(f"❌ Erro ao processar {image_name}: {response.text}")
