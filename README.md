# 🧮 Calculadora Distribuída RPC

Projeto acadêmico desenvolvido para a disciplina de Sistemas Distribuídos

O sistema oferece, além das operações matemáticas básicas, recursos como verificação de números primos, integração com inteligência artificial e busca de notícias em tempo real. Para demonstrar o funcionamento, foi desenvolvida uma interface gráfica utilizando Streamlit.



<img width="70%" alt="print_rpc" src="https://github.com/user-attachments/assets/0b756d5e-ed3c-4f0d-bcde-d1f94f6cb860"/>



## 📚 Sobre o Projeto

Este projeto implementa uma calculadora distribuída que explora conceitos fundamentais de sistemas distribuídos. Embora seja funcionalmente uma calculadora, sua arquitetura foi desenvolvida propositalmente de forma complexa para demonstrar conceitos como:

- **RPC (Remote Procedure Call)** - Chamadas de procedimento remoto
- **Sockets TCP e UDP** - Comunicação entre processos
- **Cache distribuído** - Em múltiplas camadas (cliente e servidor)
- **Concorrência e Paralelismo** - Threading e multiprocessing
- **Thread Safety** - Operações thread-safe
- **Servidor de Nomes** - Descoberta de serviços e load balancing
- **Escalabilidade** - Múltiplos servidores distribuídos

Além das operações matemáticas básicas, o sistema inclui funcionalidades extras como:
- **Web Scraping** - Busca de notícias da UOL
- **Integração com IA** - Resolução de problemas com Google Gemini

## 🏗️ Arquitetura

### Servidores (Backend)

O sistema possui **5 servidores Python**:

1. **Name Server**
   - Usa protocolo **UDP** para resposta rápida
   - Realiza load balancing entre os servidores RPC

2. **Servidores RPC** - 4 servidores de processamento
   - Usam protocolo **TCP** para operações confiáveis
   - Implementam **cache local** persistente
   - Processam operações matemáticas distribuídas

### Cliente (Frontend)

Interface gráfica desenvolvida com **Streamlit** que permite:
- Calculadora interativa com operações básicas
- Verificação de números primos (com processamento paralelo)
- Consulta de notícias da UOL em tempo real
- Resolução de problemas matemáticos com IA

O cliente implementa **cache local com TTL** (Time To Live) para otimizar requisições repetidas.

## 📦 Instalação

### 1. Clone o repositório
```bash
git clone https://github.com/codevinni/RPC.git
cd RPC
```

### 2. Crie e ative o ambiente virtual
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

### 3. Instale as dependências
```bash
pip install -r requirements.txt
```

### 4. Configure a chave da API Gemini (opcional, para funcionalidade IA)
Crie um arquivo `.env` na pasta `servers/`:
```env
GEMINI_KEY=sua_chave_api_aqui
```

## ▶️ Como Rodar

### Opção 1: Iniciar automaticamente (Recomendado)

```bash
cd servers
python start_servers.py
```

Este script inicia automaticamente todos os 5 servidores.

### Opção 2: Iniciar manualmente

Abra **5 terminais diferentes** e execute:

```bash
# Terminal 1 - Name Server
cd servers
python name_server.py

# Terminal 2 - Server 1
cd servers
python server1.py

# Terminal 3 - Server 2
cd servers
python server2.py

# Terminal 4 - Server 3
cd servers
python server3.py

# Terminal 5 - Server 4
cd servers
python server4.py
```

### Iniciar a Interface (Cliente)

#### Opção 1: App Desktop (PyQt6)
Execute como um aplicativo nativo independente:
```bash
cd client
python desktop_app.py
```
> ⚠️ **Atenção:** Esta opção **não funciona no WSL** (Windows Subsystem for Linux) pois depende de bibliotecas gráficas do Windows/Qt. Se estiver no WSL, use a Opção 2.

#### Opção 2: Interface Web (Streamlit)
Execute no navegador padrão:
```bash
cd client
streamlit run app.py --server.port 9898
```
A aplicação abrirá automaticamente em `http://localhost:9898`

## 🎯 Funcionalidades

- ✅ Operações matemáticas básicas (soma, subtração, multiplicação, divisão, fatorial)
- ✅ Verificação de números primos com processamento paralelo
- ✅ Web scraping de notícias da UOL
- ✅ Resolução de problemas matemáticos com IA (Google Gemini)
- ✅ Cache em múltiplas camadas para otimização de performance
- ✅ Balanceamento de carga entre servidores

## 🛠️ Tecnologias

- **Python** - Linguagem principal
- **Sockets** (TCP/UDP) - Comunicação distribuída
- **Streamlit** - Interface web
- **Threading & Multiprocessing** - Concorrência
- **Google Gemini API** - Inteligência artificial
- **lxml & Requests** - Web scraping
