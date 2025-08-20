# 📦 Sistema de Gestão de Estoque  

Este é um projeto completo desenvolvido em **Django**, que implementa um **Sistema de Gestão de Estoque**.  
O sistema foi pensado desde o levantamento de requisitos até a entrega da aplicação final, seguindo boas práticas de desenvolvimento de software e arquitetura em Django.  

---

## 📖 Visão Geral  

O objetivo principal do projeto é facilitar a **gestão de produtos em estoque**, permitindo:  
- Registro de **entradas e saídas** de produtos;  
- Controle do **valor total do estoque**;  
- Acompanhamento de **vendas e lucros**;  
- Exibição de métricas em **gráficos dinâmicos em JavaScript**, como vendas diárias, categorias de produtos e valor em estoque.  

---

## 🚀 Tecnologias Utilizadas  

- **Backend:** Django, Django REST Framework  
- **Frontend:** HTML, CSS, Bootstrap  
- **Gráficos:** JavaScript (Chart.js)  
- **Banco de Dados:** SQLite  
- **Controle de Versão:** Git + GitHub  

---

## 🔑 Funcionalidades  

- **API REST própria:** desenvolvida para possibilitar consumo de dados e integração com outros sistemas.  
- **Autenticação de usuários:** com controle de acesso e alteração dinâmica dos templates conforme o perfil do usuário.  
- **Arquitetura organizada:** separação de URLs por apps, seguindo boas práticas de projeto Django.  
- **Código padronizado:** em conformidade com as diretrizes da **PEP8**, garantindo legibilidade e manutenção futura.  
- **Interface responsiva:** construída com HTML, CSS e Bootstrap, proporcionando usabilidade e design limpo.  

---

## 📊 Recursos de Análise  

O sistema apresenta gráficos interativos para:  
- Vendas diárias (quantidade e valor).  
- Lucros obtidos.  
- Valor total do estoque.  
- Quantidade de produtos por marca e categoria.  

---

## 📦 Instalação e Uso

```bash
# 1. Clone este repositório
git clone https://github.com/nkf-kiefer/Sistema_de_Gerenciamento_de_Estoque-SGE.git

# 2. Acesse o diretório do projeto
cd nome-repositorio

# 3. Crie um ambiente virtual
python -m venv venv

# 4. Ative o ambiente virtual
# Linux/Mac
source venv/bin/activate
# Windows
venv\Scripts\activate

# 5. Instale as dependências
pip install -r requirements.txt

# 6. Execute as migrações
python manage.py migrate

# (Opcional) 7. Crie um superusuário para acessar o Django Admin
python manage.py createsuperuser

# 8. Inicie o servidor
python manage.py runserver

# 9. Acesse no navegador
http://localhost:8000

