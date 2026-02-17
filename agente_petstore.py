import requests
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate

llm = ChatOllama(model="llama3", temperature=0)

template = """
Você é um Engenheiro de QA. Converta o requisito abaixo em um script de teste 
funcional em Python usando a biblioteca 'requests' para a Petstore API.

REQUISITO: {instrucao}

DADOS DA API:
- Base URL: https://petstore.swagger.io/v2
- Endpoint: POST /pet (JSON: id, name, status)

Retorne APENAS o código Python.
"""

prompt = ChatPromptTemplate.from_template(template)
chain = prompt | llm

def rodar_agente():
    requisito = input("Digite o requisito para o teste funcional: ")
    print(f"Agente IA processando: {requisito}")
    
    
    try:
        resposta = chain.invoke({"instrucao": requisito})
        print("\n--- SCRIPT GERADO LOCALMENTE ---")
        print(resposta.content)
        
    except Exception as e:
        print(f"Erro: Certifique-se de que o Ollama está aberto! \n{e}")

if __name__ == "__main__":
    rodar_agente()