# RecH00D 🕶️

O RecH00D Auto é uma plataforma automatizada de reconhecimento de domínios e subdomínios, 
projetada para Red Team, Bug Bounty, Pentest e Análise de Superfície de Ataque, com foco em histórico, BI, stealth e escalabilidade.

Não é um script.  
É um pipeline completo de coleta, persistência, análise e visualização de dados**.

---

## 🚀 Features Principais

- 🔍 Descoberta de subdomínios (assetfinder, subfinder, amass, findomain)
- 🌐 Resolução DNS com coleta de IP
- 🗂️ Suporte **multi-domínio**
- 🕰️ **Histórico temporal** de execuções (attack surface drift)
- 🗄️ Persistência em **MySQL relacional**
- 📊 Exportação pronta para **Power BI / BI Tools**
- 📄 Relatório HTML automático
- 🔐 Criptografia de dados sensíveis
- 🕶️ **Modo Stealth (nível APT)**
- 🌐 API REST para consulta
- 🐳 Docker ready

🛠️ Requisitos

Sistema

- Kali Linux (recomendado)
- Docker (opcional)
- MySQL 8+
- Ferramentas
- assetfinder
- subfinder
- amass
- findomain
- Python
- Python 3.9+
- flask
- cryptography
- mysql-connector-python

⚙️ Instalação:

Banco de Dados
mysql -u root -p < db/schema.sql

CREATE USER 'rech00d'@'localhost' IDENTIFIED BY 'rech00d';
GRANT ALL PRIVILEGES ON rech00d.* TO 'rech00d'@'localhost';
FLUSH PRIVILEGES;

⚙️ Execução:

chmod +x recon.sh
./recon.sh dominio.com outrodominio.com

⚙️ Docker:

docker build -t rech00d .
docker run --rm rech00d dominio.com

🕶️ Modo Stealth (APT-style)

* Configurado em stealth.conf:

- Delay randômico entre execuções
- Ordem aleatória de ferramentas
- Baixa verbosidade
- Execução menos detectável
- Preparado para DoH e output criptografado
- Ativado automaticamente via configuração.


---

## 📁 Estrutura do Projeto

```text
RecH00D/
├── recon.sh               # Pipeline principal de recon
├── stealth.conf           # Configuração do modo stealth
├── Dockerfile
├── requirements.txt
├── README.md
│
├── output/
│   ├── raw/               # Saída bruta das ferramentas
│   ├── resolved/          # Subdomínios resolvidos (CSV)
│   ├── data/              # Dados estruturados
│   └── reports/           # Relatórios gerados
│
├── db/
│   ├── schema.sql         # Modelo relacional MySQL
│   └── ingest_mysql.py   # Ingestão automática dos dados
│
├── api/
│   └── app.py             # API REST
│
├── crypto/
│   └── crypto_utils.py    # Criptografia
│
├── bi/
│   └── powerbi_model.md   # Modelo de dados para BI
│
└── reports/
    └── report.py          # Gerador de relatório HTML
