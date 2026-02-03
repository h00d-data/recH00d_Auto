## 📊 Dashboard Power BI (Pronto para Integração)

O RecH00D foi modelado desde a origem para integração direta com **Power BI**, permitindo visualização executiva 
e técnica da superfície de ataque ao longo do tempo.

O banco MySQL já segue um modelo estrela-relacional, evitando qualquer transformação pesada no Power BI.

---

### 🔌 Conexão com MySQL

No Power BI Desktop:

1. **Obter Dados → Banco de Dados MySQL**
2. Servidor: `localhost`
3. Banco: `rech00d`
4. Autenticação: usuário `rech00d`

Tabelas principais para importação:
- `domain`
- `recon_run`
- `subdomain`
- `ip_address`
- `recon_result`

Modo recomendado:
- ✔ Import (para performance)
- ✔ Atualização agendada opcional

---

### 🔗 Relacionamentos (já prontos)

Configurar (ou validar) os relacionamentos:


Cardinalidade:
- Todos **One-to-Many**
- Direção de filtro: **Single**

---

### 📈 Dashboards Sugeridos (Prontos para Uso)

#### 1️⃣ Visão Geral da Superfície de Ataque
- Total de domínios monitorados
- Total de subdomínios descobertos
- Total de IPs únicos
- Última execução de recon

**Visuais**:
- Cards
- KPI
- Tabela resumida por domínio

---

#### 2️⃣ Subdomínios por Domínio
- Gráfico de barras:
  - Eixo: Domínio
  - Valor: Contagem de Subdomínios

Uso:
- Identificar domínios mais expostos

---

#### 3️⃣ Infraestrutura Compartilhada
- Gráfico de barras ou matriz:
  - IP → Quantidade de subdomínios
- Destaque para IPs com alta concentração

Uso:
- Detecção de hosting compartilhado
- Mapeamento de infraestrutura crítica

---

#### 4️⃣ Crescimento Histórico (Attack Surface Drift)
- Gráfico de linhas:
  - Eixo X: Data (`recon_run.executed_at`)
  - Eixo Y: Quantidade de subdomínios

Uso:
- Identificar expansão ou redução da superfície de ataque
- Comparar execuções ao longo do tempo

---

#### 5️⃣ Drill-down Técnico
- Tabela detalhada:
  - Domínio
  - Subdomínio
  - IP
  - Data da descoberta

Uso:
- Análise técnica
- Exportação para times ofensivos ou defensivos

---

### 🧮 Medidas DAX Sugeridas

```DAX
Total Subdomínios =
DISTINCTCOUNT(subdomain[id])

Total IPs =
DISTINCTCOUNT(ip_address[id])

Subdomínios por Domínio =
CALCULATE(
    DISTINCTCOUNT(subdomain[id]),
    ALLEXCEPT(domain, domain[name])
)


🔄 Atualização Automática

Opções:

- Atualização manual no Power BI Desktop
- Power BI Service com gateway local
- Integração via API REST do RecH00D (roadmap)
