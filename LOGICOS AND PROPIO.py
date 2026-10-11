# ==========================================================
# Sistema de Control de Acceso y Seguridad para Celda Robótica
# Aplicación práctica de Operadores Lógicos en Python
# ==========================================================

def verificar_seguridad_sistema():
    print("--- EVALUACIÓN DE CONDICIONES DE SEGURIDAD ---")
    
    # Estado actual de sensores y dispositivos en la celda
    puerta_cerrada = True
    boton_emergencia_presionado = False
    modo_mantenimiento = False
    nivel_bateria_ok = True
    
    # 1. Operador AND: Para operar el robot, la puerta DEBE estar cerrada 
    # Y el botón de emergencia NO debe estar presionado.
    sistema_seguro = puerta_cerrada and (not boton_emergencia_presionado)
    print(f"¿Condiciones óptimas de operación (AND): {sistema_seguro}")
    
    # 2. Operador OR: Se activa una alarma si OCURRE una falla crítica 
    # (por ejemplo, si el botón de emergencia está presionado O la batería no está OK).
    alarma_activa = boton_emergencia_presionado or (not nivel_bateria_ok)
    print(f"¿Alarma general activada (OR): {alarma_activa}")
    
    # 3. Operador NOT: Invierte el estado del modo mantenimiento para saber si está en producción.
    produccion_normal = not modo_mantenimiento
    print(f"¿Modo producción normal (NOT): {produccion_normal}")
    print()
    
    print("--- TOMA DE DECISIONES CON IF ---")
    # Condición combinada compleja usando operadores lógicos y precedencia
    if sistema_seguro and produccion_normal and not alarma_activa:
        print("[ESTADO: ACTIVO] El sistema está listo para iniciar el ciclo de trabajo.")
    else:
        print("[ESTADO: BLOQUEADO] ¡Atención! Se requiere revisión de seguridad antes de arrancar.")

if __name__ == "__main__":
    verificar_seguridad_sistema()