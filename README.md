# 🖼️ Reconhecimento Facial e Transformação de Imagens em Dados no Azure ML

Este projeto utiliza **Microsoft Azure Machine Learning (Azure ML)** e **Azure Cognitive Services - Face API** para reconhecimento facial e extração de dados a partir de imagens. O objetivo é processar imagens, identificar rostos e converter essas informações em dados estruturados.

---

## 📌 Recursos Criados no Azure

- **Grupo de Recursos**: `FacialRecognitionProjectRG`
- **Conta de Armazenamento**: `facialrecogstorage` (Para armazenar as imagens)
- **Azure Cognitive Services - Face API**: `facialRecognitionCognitive` (Para detectar rostos e características faciais)
- **Azure Machine Learning Workspace**: `facialRecogMLWorkspace` (Para processar os dados e treinar modelos)

---

## 🚀 Como Configurar e Rodar o Projeto

### 1️⃣ Criando os Recursos no Azure
1. **Faça login no Azure CLI**:
   ```sh
   az login

2. **Crie um grupo de recursos**
   az
   group create --name FacialRecognitionProjectRG --location "East US"

3. **Implante os serviços usando o JSON**
   az
   deployment group create --resource-group FacialRecognitionProjectRG --template-file facial_recognition_azure_project.json

4. **Verifique se os serviços foram criados**
   az
   resource list --resource-group FacialRecognitionProjectRG --output table



  **⚠️ Antes de rodar o script, lembre-se de substituir:**
  "SUA_CHAVE_AQUI" pela sua chave de API do Azure.
  "SUA_URL_DA_IMAGEM_AQUI" pelo caminho correto das suas imagens.

