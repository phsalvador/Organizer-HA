import datetime

# Define a data em que começaste (Ano, Mês, Dia)
DATA_INICIO = datetime.date(2026, 4, 8) 
hoje = datetime.date.today()
dias_sem_bagunca = (hoje - DATA_INICIO).days

readme_content = f"""
# 🛡️ Painel de Disciplina: Operação Sem Bagunça

![Status](https://img.shields.io/badge/Status-Ativo-brightgreen)
![Dias](https://img.shields.io/badge/Dias%20Sem%20Bagunça-{dias_sem_bagunca}-blue?style=for-the-badge)

## 📊 Contador Atual: {dias_sem_bagunca} dias

*“A organização é o caminho para a clareza mental.”*

---
**Regras do Desafio:**
- Armário Organizado.
- Mesa de trabalho limpa.
- Todos equipamentos identificados.
"""

with open("README.md", "w", encoding="utf-8") as f:

    f.write(readme_content)

