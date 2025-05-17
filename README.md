# 📊 API do Google Sheets com Python

Este projeto permite **ler e escrever dados** em planilhas do Google Sheets utilizando a API oficial do Google e Python. Foi refatorado para ter uma estrutura modular, profissional e com suporte a argumentos via linha de comando.

---

## 🧱 Tecnologias

- Python 3.10+
- Google Sheets API
- Google Auth (OAuth 2.0)
- `argparse` para entrada por linha de comando

---

## 📁 Estrutura do Projeto

Api-do-Google-Sheets/
├── auth.py # Autenticação com Google OAuth
├── main.py # Arquivo principal (executável via terminal)
├── requirements.txt # Dependências
├── sheet_service.py # Funções de leitura e escrita
├── utils.py # Parâmetros e dados de exemplo
└── README.md # Documentação



---

## ⚙️ Instalação

1. **Clone o repositório**:

```bash
git clone https://github.com/BennyLopesWeb/Api-do-Google-Sheets.git
cd Api-do-Google-Sheets

1. Crie e ative o ambiente virtual:
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

3. Instale as dependências:
pip install -r requirements.txt

🔑 Configuração
1. Acesse o Console de APIs do Google.

2. Crie um projeto e ative a Google Sheets API.

3. Crie credenciais OAuth 2.0 (tipo: Desktop).

4. Baixe o arquivo credentials.json e coloque na raiz do projeto.

▶️ Como Usar
✅ Leitura da planilha:
bash
python main.py --mode read --range "Página1!A1:C10"

✅ Escrita na planilha:
bash
python main.py --mode write --range "Página1!A1:C10"

Os dados de exemplo a serem escritos estão definidos em utils.py.

📌 Personalização
Planilha: Edite o ID da planilha no utils.py:

bash
SPREADSHEET_ID = "seu_id_aqui"

✅ Exemplo de Dados Escritos
SAMPLE_DATA = [
    ['Nome', 'Email', 'Idade'],
    ['Maria', 'maria@email.com', 30],
    ['João', 'joao@email.com', 28]
]

🧼 Melhorias Futuras
Adicionar suporte a múltiplas abas e múltiplas planilhas.

Interface Web para envio de dados.

Upload de dados via CSV.

👨‍💻 Autor
Desenvolvido por Benny Lopes 🚀

📄 Licença
Este projeto está licenciado sob a licença MIT.



