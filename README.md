<div align="center">
    <img src="https://github.com/JSOM-Grupo-PCC/PrePCC_JSOM_/assets/115905335/f215246a-a4a2-44cc-826e-ceda69ef84a5" alt="Logo JSOM" width="50%">
</div>
<hr>
<h1 align="center">Projeto de Conclusão de Curso (PCC) - JSOM<h1>
<h3 align="center">Sistema de Gerenciamento de Alunos de Academia</h3>
<br> 
  
## Diagrama de classe
![Diagrama de classe](https://github.com/user-attachments/assets/4ad2e91c-4063-4698-8061-0384af42e4b7)

<hr>
<br>

## Diagrama Caso de Uso
![Diagrama Caso de Uso](https://github.com/user-attachments/assets/d1ccb18e-6d6c-402e-9d1a-077b4f2fa3f1)

<hr>
<br>

## Diagrama Entidade de Relacionamentos
![Diagrama Entidade de Relacionamentos](https://github.com/user-attachments/assets/c0a6a001-c530-4494-b637-1b74916ab2d1)

## Configuração do Ambiente

1. **Pré-requisitos:**
   - Python 3.x
   - Django
   - Outras dependências (verifique o arquivo `requirements.txt`)

2. **Configuração do Ambiente Virtual:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows: .\venv\Scripts\activate

3. **Instalação das Dependências:**
    ````bash
   pip install -r requirements.txt
   
4. **Configuração do Banco de Dados:**
    ````bash
   python manage.py makemigrations
   python manage.py migrate
    
5. **Execute os arquivos iniciar_dados.py:**
    ````bash
   python iniciar_dados.py
    
6. **Execução do Servidor de Desenvolvimento:**
    ````bash
   python manage.py runserver

7. **Entre como Personal:**
    ````bash
   *username:* personal;
   *password:* personal123;
