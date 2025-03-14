import calendar

def imprimir_calendario_2025():
    # Crear un calendario en formato de texto para el año 2025
    calendario_2025 = calendar.TextCalendar()
    
    # Imprimir el calendario completo
    print(calendar.calendar(2025))

# Llamar a la función para imprimir el calendario
imprimir_calendario_2025()

def imprimir_dias_festivos():
    # Lista de días festivos en 2025 para Colombia
    dias_festivos = {
        "Enero": ["1 - Año Nuevo", "6 - Reyes Magos"],
        "Febrero": ["16 - Día de la Candelaria"],
        "Marzo": ["24 - Día de San José"],
        "Abril": ["6 - Viernes Santo", "7 - Sábado Santo", "20 - Domingo de Pascua"],
        "Mayo": ["1 - Día del Trabajador", "19 - Ascensión de la Virgen"],
        "Junio": ["16 - Corpus Christi", "23 - Sagrado Corazón"],
        "Julio": ["20 - Día de la Independencia", "21 - Batalla de Boyacá"],
        "Agosto": ["7 - Batalla de Boyacá", "15 - La Asunción de la Virgen"],
        "Septiembre": [],
        "Octubre": ["12 - Día de la Raza"],
        "Noviembre": ["1 - Día de Todos los Santos", "11 - Independencia de Cartagena", "17 - Día de la Virgen del Rosario"],
        "Diciembre": ["8 - Día de la Inmaculada Concepción", "25 - Navidad"]
    }
    
    print("Días festivos en Colombia en 2025:")
    for mes, dias in dias_festivos.items():
        print(f"{mes}:")
        if dias:
            for dia in dias:
                print(f"  {dia}")
        else:
            print("  No hay días festivos")

# Llamar a las funciones para imprimir el calendario y los días festivos
imprimir_calendario_2025()
imprimir_dias_festivos()
