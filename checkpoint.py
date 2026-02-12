import pickle
import time
import os

# Nombre del archivo donde guardaremos el "checkpoint"
ARCHIVO_CHECKPOINT = "estado_guardado.pkl"

def guardar_estado(estado):
    """
    Usa pickle.dump para guardar el diccionario 'estado' en un archivo binario.
    Esto es el 'Checkpoint'.
    """
    with open(ARCHIVO_CHECKPOINT, "wb") as f:
        pickle.dump(estado, f)
    print(f"   [Checkpoint] Estado guardado: {estado}")

def cargar_estado():
    """
    Intenta leer el archivo de checkpoint.
    Si existe, usa pickle.load para restaurar las variables.
    Si no existe, devuelve un estado inicial (desde cero).
    """
    if os.path.exists(ARCHIVO_CHECKPOINT):
        print(">>> ¡Archivo de checkpoint encontrado! Restaurando sistema...")
        with open(ARCHIVO_CHECKPOINT, "rb") as f:
            return pickle.load(f)
    else:
        print(">>> Iniciando programa desde CERO.")
        return {"contador": 0, "lista_tareas": []}

def main():
    # 1. Al iniciar, intentamos recuperar el pasado
    estado_actual = cargar_estado()
    
    contador = estado_actual["contador"]
    total_iteraciones = 20

    print(f"--- Iniciando procesamiento desde el paso {contador} ---")

    try:
        # Simulamos un proceso largo (un bucle)
        while contador < total_iteraciones:
            contador += 1
            
            # Simulamos trabajo pesado
            print(f"Procesando tarea #{contador}...")
            time.sleep(2) # Espera 2 segundos
            
            # Actualizamos el estado en memoria
            estado_actual["contador"] = contador
            
            # 2. CHECKPOINTING: Guardamos el estado en disco
            guardar_estado(estado_actual)

        print("--- ¡Proceso terminado exitosamente! ---")
        
        # Opcional: Borrar el checkpoint al terminar para que la próxima vez inicie de 0
        if os.path.exists(ARCHIVO_CHECKPOINT):
            os.remove(ARCHIVO_CHECKPOINT)

    except KeyboardInterrupt:
        print("\n\n!!! ALERTA: El programa se detuvo abruptamente (Simulación de fallo).")
        print(f"!!! El último estado guardado fue: {contador}")

if __name__ == "__main__":
    main()