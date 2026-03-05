# ITW - iPhone to Windows File Transfer
# Copyright (C) 2026 Thiago Grossi Pacheco
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

from fastapi import FastAPI, UploadFile
from fastapi import HTTPException
from fastapi.staticfiles import StaticFiles
from pathlib import Path
import uvicorn 
import socket
import psutil
import pyqrcode
import os

"""
Servidor FastAPI para upload de arquivos via rede local.
- Detecta IP da interface Wi-Fi
- Gera QR Code para acesso rápido
- Salva arquivos em chunks para evitar alto consumo de memória
"""

app = FastAPI()

BASE_DIR = os.path.dirname(os.path.abspath(__file__)) #localiza em qual pasta o script está
UPLOAD_DIR = os.path.join(BASE_DIR, "uploads") #Diretorio de download (/uploads) dos arquivos 
os.makedirs(UPLOAD_DIR, exist_ok=True)

interface = psutil.net_if_addrs() #Listagem de endereços

if 'Wi-Fi' in interface: #Localização do ipv4 do WIFI do computador
    for i in interface['Wi-Fi']:
         if i.family == socket.AF_INET:
              ip = i.address
if not ip: #Tratamento caso não haja um endereço de WIFI
     ip = socket.gethostbyname(socket.gethostname()) #Localização do ipv4 principal do computador 

def generate_qrcode(): #Função de geração de qrcode
    URL = (f"http://{ip}:8000").strip() #URL para gerar o QrCode
    qr = pyqrcode.create(URL) #Criação do QrCode
    print(qr.terminal(quiet_zone=1)) #Imprimir o QrCode no terminal

@app.post("/file/upload")
async def uploadfile(file: UploadFile):
        
        chunk_size = 1024 * 1024 #Chunk maximo de transferencia 
        
        filename = Path(file.filename).name #Remove possíveis diretórios enviados no nome do arquivo
        SAVE_FILE_PATH = os.path.join(UPLOAD_DIR, filename)
        try:
            with open(SAVE_FILE_PATH, "wb") as f:
                while True:
                    
                    chunk = await file.read(chunk_size)

                    if not chunk:
                        await file.close()
                        break

                    f.write(chunk)

            return {"filename": filename, "status": "Arquivo transferido com sucesso!"} #Retornar uma mensagem de que deu certo

        except Exception: #Tratamento de erro em caso de falha no envio dos arquivos
            raise HTTPException(status_code=500, detail="Erro ao transferir o arquivo") #Retornar uma mensagem de erro
        

app.mount("/", StaticFiles(directory="static", html=True), name="static") #Diretorio da interface estatica            

if __name__ == "__main__":
    generate_qrcode() #Chamada para gerar o QRCODE
    uvicorn.run(app, host="0.0.0.0", port=8000) #Configuração host e porta (0.0.0.0 todos da rede tem acesso)

#🕷