import os
import time

from botcity.maestro import *
from watchdog.events import FileSystemEvent, FileSystemEventHandler
from watchdog.observers import Observer

from config import KEY, LOGIN, PATH, SERVER
from log import logger

WATCH_PATH = PATH

def create_task(file_name):
    logger.info("Processo de criar tarefa iniciando...")

    maestro = BotMaestroSDK.from_sys_args()
    maestro.login(
        server=SERVER, 
        login=LOGIN,
        key=KEY
    )

    params = {"nome_arquivo": file_name}
    task = maestro.create_task(
        activity_label="label_primeiro_bot",
        parameters=params,
        test=True
    )
    logger.info(f"Tarefa criada, id: {task.id}")


class WatcherHandler(FileSystemEventHandler):

    def on_created(self, event: FileSystemEvent):
        name = os.path.basename(event.src_path)
        logger.info(f"Novo arquivo recebido: {name}' criado em {time.ctime()}")
        logger.info("Verificação do tipo de aquivo .csv")
        if '.csv' in name:
            logger.info("Aquivo .csv")
            logger.info("Chama processo de criar tarefa")
            create_task(name)
        else:
            logger.warning("Aquivo não é do tipo esperado")


if __name__ == "__main__":
    logger.info("Iniciando a execução do script")
    event_handler = WatcherHandler()
    observer = Observer()
    observer.schedule(event_handler, WATCH_PATH, recursive=False)
    observer.start()
    print(f"Monitorando a pasta '{WATCH_PATH}'. Pressione Ctrl+C para sair.")
    try:
        while True:
            time.sleep(10)
            logger.info("Monitorando pasta...")
    except KeyboardInterrupt:
        observer.stop()
        logger.info("Encerrado")
    observer.join()
