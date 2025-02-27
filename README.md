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

### 4. Atualizar as variáveis no código
Atualize as variáveis no código
```ini
API KEY
USER 
DB PASSWORD
DB HOST
DB NAME
```

### 4. Executar o Script
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
```

## Melhorias Futuras
- Comparação da previsão de chuva com os dados reais
- Implementar logging estruturado
- Envio de email em caso de erro
- Soltar informações de comparação numa API
- Adicionar suporte a outros bancos de dados
- Criar um dashboard para visualização dos dados


## Autor
Desenvolvido por **Otávio Almeida**. Entre em contato via [GitHub](https://github.com/almeidaota).

