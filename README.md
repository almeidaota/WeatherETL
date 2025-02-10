# WeatherETL

WeatherETL é um projeto de ETL (Extract, Transform, Load) que coleta dados meteorológicos da API OpenWeather, processa e armazena as informações em um banco de dados MySQL.

## Funcionalidades
- Coleta de previsão horária do tempo
- Coleta de histórico de dados meteorológicos
- Processamento e transformação dos dados
- Armazenamento dos dados em um banco de dados MySQL

## Tecnologias Utilizadas
- **Python**
- **Pandas** (para manipulação de dados)
- **Requests** (para chamadas de API)
- **SQLAlchemy** (para conexão com banco de dados)
- **OpenWeather API** (para obter dados meteorológicos)
- **MySQL** (para armazenamento dos dados)

## Configuração e Uso

### 1. Clonar o Repositório
```bash
$ git clone https://github.com/almeidaota/WeatherETL.git
$ cd WeatherETL
```

### 2. Criar e Ativar um Ambiente Virtual (Opcional, mas Recomendado)
```bash
# No Windows
type nul > .env
python -m venv venv
venv\Scripts\activate

# No Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar Dependências
```bash
pip install -r requirements.txt
```

### 4. Configurar Variáveis de Ambiente
Crie um arquivo `.env` e adicione suas credenciais:
```ini
API_KEY=seu_token_da_api
DB_USER=seu_usuario
DB_PASSWORD=sua_senha
DB_HOST=seu_host
DB_NAME=weatherapi
```

### 5. Executar o Script
```bash
python main.py
```

## Estrutura do Projeto
```
WeatherETL/
│── queries.py              # Consultas SQL utilizadas
│── main.py                 # Script principal
│── requirements.txt        # Dependências do projeto
│── README.md               # Documentação
└── .env                    # Configuração das variáveis de ambiente (não incluído no repositório)
```

## Melhorias Futuras
- Implementar logging estruturado
- Adicionar suporte a outros bancos de dados
- Criar um dashboard para visualização dos dados

## Licença
Este projeto está licenciado sob a [MIT License](LICENSE).

## Autor
Desenvolvido por **Otávio Almeida**. Entre em contato via [GitHub](https://github.com/almeidaota).

