# Observe
Pensando em processos automatizados, uma das formas de gatilho para disparar novas tarefas é através de uma pasta compartilhada.

Esse script monitora uma pasta especifica, aguardando por eventos de criação de documentos do tipo `.csv`, quando criados disparam uma nova tarefa do Orquestrador BotCity através do SDK.


## Pré requisitos
- Python 3.9^
- Conta na BotCity
- Automação para consumo do arquivo pronta na plataforma


## Como utilizar
Você pode executar o script localmente, faça algumas configurações necessárias:

`config_example.py` (altere o nome do arquivo para `config.py`)
``` python
SERVER="https://developers.botcity.dev"
LOGIN="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
KEY="xxxxxxxxxxxxxxxxxxxxxxx"
PATH=r"C:\Users\xxx\xxx\xxx\arquivos"
```

- SERVER: seu servidor BotCity, para community mantenha o exemplo.
- LOGIN e SERVER: são as credenciais do seu workspace na BotCity.
- PATH: caminho da pasta a ser monitorada,
---
`monitor.py` (linha 25):
``` python
task = maestro.create_task(
    activity_label="DadosBotCandidatos",
    parameters=params,
    test=True
)
```

- activity_label: Nome da automação que está no Orquestrador BotCity.
---
Criar e ativar ambiente virtual:


   - MacOS/Linux:

     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

   - Windows:

     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```
---
Instalar dependencias:

```bash
pip install -r requirements.txt
```
---
Execute diretamente o script de monitoramento:

```bash
python monitor.py
```
