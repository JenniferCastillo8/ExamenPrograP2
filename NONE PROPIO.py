# ==========================================================
# Sistema de Monitoreo de Sensores con Manejo de "None"
# Útil en Automatización para detectar fallas o lecturas nulas.
# ==========================================================

def leer_sensor(id_sensor):
    # Simulación de lectura de sensores
    lecturas_simuladas = {
        "TEMP_01": 25.5,
        "PRES_02": 101.3,
        "FLUX_03": None,  # Sensor desconectado o con falla (ausencia total de valor)
        "NIVEL_04": 0.0   # Sensor funcionando, el nivel es cero (es un valor válido, no None)
    }
    return lecturas_simuladas.get(id_sensor, None)

def procesar_sensores():
    sensores = ["TEMP_01", "PRES_02", "FLUX_03", "NIVEL_04", "HUMEDAD_99"]
    
    print("--- REPORTE DE ESTADO DE SENSORES ---")
    for sensor in sensores:
        valor = leer_sensor(sensor)
        
        # Identificar correctamente si el sensor devolvió None usando 'is None'
        if valor is None:
            print(f"[ALERTA] Sensor {sensor}: Sin conexión o error de lectura (Retornó None).")
        else:
            print(f"[OK] Sensor {sensor}: Lectura = {valor} (Tipo: {type(valor).__name__})")

if __name__ == "__main__":
    procesar_sensores()