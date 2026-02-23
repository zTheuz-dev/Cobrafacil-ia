# 1. Instalar Ollama
# (acesse ollama.com para baixar e instalar)

# 2. Baixar um modelo leve
ollama pull llama3.2:3b-instruct-q4_K_M
# 3. Testar se funciona
ollama run lama3.2:3b-instruct-q4_K_M "Olá!"

# 4. Instalar dependências do projeto
pip install streamlit pandas requests

# 5. Garantir que Ollama está rodando
ollama serve

# 6. Rodar o app
streamlit run ./src/app.py
