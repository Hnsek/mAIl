# mAIl - Classificação e Resposta Automática de Emails

## 📝 Descrição do Projeto

O **mAIl** é uma aplicação web que utiliza **Inteligência Artificial** para **classificar emails** em categorias **Produtivo** e **Improdutivo** e **sugerir respostas automáticas** de acordo com a categoria.  

A solução foi desenvolvida como parte de um **case prático da AutoU**, simulando um cenário real de alto volume de emails no setor financeiro, com o objetivo de automatizar tarefas manuais e liberar tempo da equipe para atividades estratégicas.

---

## 🎯 Funcionalidades

1. **Classificação de Emails**
   - Produtivo: Emails que exigem ação ou resposta (ex.: solicitações de suporte, dúvidas sobre o sistema).
   - Improdutivo: Emails que não exigem ação imediata (ex.: felicitações, agradecimentos).

2. **Geração de Respostas Automáticas**
   - Sugestões de respostas relevantes baseadas na categoria do email.

3. **Interface Web Intuitiva**
   - Upload de arquivos `.txt` ou `.pdf` contendo emails.
   - Inserção direta de texto de emails.
   - Exibição clara da categoria e da resposta sugerida.

4. **Integração com AI**
   - Uso de API de AI para classificação e geração de respostas.

5. **Deploy na Nuvem**
   - Aplicação acessível online sem necessidade de instalação local.

---

## 🛠 Tecnologias Utilizadas

- **Frontend:** HTML, CSS, JavaScript
- **Backend:** Python 3.x, Django
- **Inteligência Artificial:** Gemini
- **Hospedagem:** Render 
- **Gerenciamento de Dependências:** `requirements.txt`

## ⚡ Como Executar Localmente

### Pré-requisitos

- Python 3.9+ instalado
- Pip ou Poetry
- Conta/API Key da Google AI Studio(https://aistudio.google.com/apikey)

### Passos

1. Clonar o repositório:

```bash
git clone https://github.com/Hnsek/mAIl.git
cd mAIl
```

2. Instalar dependências:

```bash
pip install -r requirements.txt
```

3. Configurar variáveis de ambiente

```bash
export OPENAI_API_KEY="sua_chave_aqui"
```

3. Configurar variáveis de ambiente

```bash
python3 manage.py runserver
```

4. Acessar aplicação no navegador

http://localhost:5000

## Acessar via docker

1. Fazer build da imagem

```bash
   docker build -t m-ai-l . 
```

2. Executar container

```bash
   docker run -p 8000:8000 m-ai-l 
```

🖥 Demonstração

Vídeo: Link do vídeo demonstrativo
Aplicação Online: https://mail-pboo.onrender.com/analyser/form

⚠️ Observações

Esta aplicação é um protótipo para demonstração do case prático da AutoU.
Certifique-se de ter API Keys válidas caso utilize serviços de AI externos.

Desenvolvido por: Henrique Sousa
Contato: henrique2001sousa@gmail.com
Linkedin: www.linkedin.com/in/henriquesousaleandro

