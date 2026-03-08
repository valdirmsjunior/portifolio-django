# Django Portfolio Training 🚀

Este projeto é um laboratório de treinamento focado em dominar os fundamentos do **Django 6.0** e **Python 3.14**. O objetivo foi construir uma estrutura de portfólio profissional e escalável, utilizando as melhores práticas de organização de templates e lógica de exibição.

## 🛠️ Tech Stack

- **Python 3.14.0** (Gerenciado via pyenv)
- **Django 6.0** (Framework Web)
- **Tailwind CSS** (via Play CDN para prototipagem rápida)
- **Git** (Controle de versão)

## 🏗️ Diferenciais Técnicos deste Projeto

Diferente de projetos iniciantes, este treinamento focou em recursos avançados do motor de templates do Django:

- **Arquitetura Modular:** Separação entre as configurações centrais (`core/`) e a lógica da aplicação (`portfolio/`).
- **Template Inheritance:** Uso de um `base.html` global para manter o código DRY (Don't Repeat Yourself).
- **Custom Template Tags:** Criação de tag `active_link` para gerenciar o estado ativo do menu via servidor.
- **Custom Filters:** Filtro `tech_badge_style` para estilização dinâmica de badges baseada em dados.
- **Context Processors:** Injeção global de dados de contato em todos os templates do site.
- **Mock Database:** Centralização de dados em um arquivo Python (`dados.py`) para simular o banco de dados antes da implementação dos Models.

## 🚀 Como Executar

1. Clone o repositório.
2. Crie e ative o ambiente virtual:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```
3. Instale as dependências:
