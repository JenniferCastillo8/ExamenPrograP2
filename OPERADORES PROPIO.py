# ==========================================================
# Calculadora de Presupuesto y Materiales para Proyecto de Automatización
# Aplicación práctica de Operadores Aritméticos en Python
# ==========================================================

def calcular_proyecto():
    print("--- COTIZACIÓN DE COMPONENTES PARA ROBÓTICA ---")
    
    costo_plc = 2500.0
    costo_sensor = 350.0
    costo_motor = 1200.0
    
    cant_plc = 2
    cant_sensor = 6
    cant_motor = 4
    
    # Cálculo del subtotal por componente usando multiplicación (*)
    sub_plc = costo_plc * cant_plc
    sub_sensor = costo_sensor * cant_sensor
    sub_motor = costo_motor * cant_motor
    
    # Suma total parcial (+)
    subtotal_general = sub_plc + sub_sensor + sub_motor
    
    # 3. Aplicación de impuestos con precedencia y paréntesis
    iva = subtotal_general * 0.16
    total_con_iva = subtotal_general + iva
    
    print(f"Subtotal componentes: ${subtotal_general:,.2f}")
    print(f"IVA (16%):           ${iva:,.2f}")
    print(f"Total a pagar:       ${total_con_iva:,.2f}")
    print()
    
    print("--- DISTRIBUCIÓN EN KITS DE TRABAJO ---")
    # 4. División entera (//) y Módulo (%) para empaquetado de sensores en kits
    total_sensores = cant_sensor
    kits_armables = total_sensores // 4  # Cada kit requiere 4 sensores
    sensores_sobrantes = total_sensores % 4  # Residuo
    
    print(f"Sensores totales disponibles: {total_sensores}")
    print(f"Kits completos que se pueden armar: {kits_armables}")
    print(f"Sensores restantes sin kit:         {sensores_sobrantes}")
    print()
    
    print("--- ESTIMACIÓN DE COMBINACIONES / EXPONENCIALES ---")
    # 5. Potencia (**) para cálculo de combinaciones de entradas/salidas o canales
    canales_base = 2
    expansion_niveles = 3
    total_combinaciones = canales_base ** expansion_niveles
    print(f"Canales base ({canales_base}) con {expansion_niveles} niveles de expansión = {total_combinaciones} combinaciones posibles.")

if __name__ == "__main__":
    calcular_proyecto()