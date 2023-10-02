from datetime import datetime
from psutil import *
from GPUtil import *
import os
def get_info():

    # Informações da CPU e memória RAM
    cpu_usage = cpu_percent(interval=1)  # Uso da CPU em percentagem
    ram = virtual_memory()  # Informações sobre a memória RAM

    # Informações da GPU (para GPUs NVIDIA)
    try:
        gpu = getGPUs()[0]
        gpu_name = gpu.name
        gpu_usage = gpu.load * 100  # Uso da GPU em percentagem
        gpu_memory_total = gpu.memoryTotal
        gpu_memory_used = gpu.memoryUsed
    except Exception as e:
        gpu_name = "N/A"
        gpu_usage = "N/A"
        gpu_memory_total = "N/A"
        gpu_memory_used = "N/A"

    system_info = f"""
CPU Usage: {cpu_usage}%
RAM Total: {round(ram.total / (1024 ** 3), 2)}GB
RAM Used: {round(ram.used / (1024 ** 3), 2)}GB
GPU Name: {gpu_name}
GPU Usage: {gpu_usage}%
GPU Memory Total: {gpu_memory_total}MB
GPU Memory Used: {gpu_memory_used}MB"""

    return system_info

def get_hour():
    return datetime.now().strftime("%H:%M:%S")

def list_files(path):
    try:
        arquivos = os.listdir(path)

        arquivos = [arquivo for arquivo in arquivos if os.path.isfile(os.path.join(path, arquivo))]

        file_list = ""
        for arquivo in arquivos:
            file_list += ("-> " + arquivo + "\n")
            

        return file_list
    except OSError as error:
        print(f"Erro ao listar arquivos: {error}")
        return []

def get_archive(archive):
    pass

def exit():
    pass
