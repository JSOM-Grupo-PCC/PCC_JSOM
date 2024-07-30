<div align="center">
    <img src="https://github.com/JSOM-Grupo-PCC/PrePCC_JSOM_/assets/115905335/f215246a-a4a2-44cc-826e-ceda69ef84a5" alt="Logo JSOM" width="50%">
</div>
<hr>
<h1 align="center">Projeto de Conclusão de Curso (PCC) - JSOM<h1>
<h3 align="center">Sistema de Gerenciamento de Alunos de Academia</h3>
<br> 
  
## Diagrama de classe
![Diagrama de classe](https://github.com/JSOM-Grupo-PCC/PCC_JSOM/assets/115905335/bb7f0da8-2d8e-4270-adc7-94f7ee66e79d)


<!--## Diagrama Caso de Uso
![Caso de Uso](https://github.com/JSOM-Grupo-PCC/PrePCC_JSOM_/assets/115905335/50206489-0ab5-4f2a-b6a5-8d9334d95e3d)


## Diagrama Entidade de Relacionamentos 
![Entidade de Relacionamentos](https://github.com/JSOM-Grupo-PCC/PrePCC_JSOM_/assets/115905335/db2f5622-ccba-4ad3-ae5f-b3a58fa8722c) -->

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
5. **Execute os arquivos inicializa_dados.py e inicializar_alunos.py:**
    ````bash
   python inicializa_dados.py
   python inicializar_alunos.py.py
6. **Execução do Servidor de Desenvolvimento:**
    ````bash
   python manage.py runserver
