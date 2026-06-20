import streamlit as st

# Configuración de la interfaz
st.set_page_config(page_title="Mi Gym App", page_icon="🏋️", layout="centered")

st.markdown("""
    <style>
    .big-font { font-size:22px !important; font-weight: bold; color: #2e86c1; }
    .key-point { color: #f63366; font-weight: bold; }
    .equipo-tag { background-color: #f2f3f4; padding: 4px 8px; border-radius: 4px; font-size: 14px; color: #34495e; border: 1px solid #bdc3c7;}
    </style>
    """, unsafe_allow_html=True)

st.title("🏋️‍♂️ Asistente de Entrenamiento por Músculo")
st.write("Selecciona el músculo específico que deseas trabajar y descubre cómo entrenarlo con máquinas o peso libre.")

# Base de datos enfocada en MÚSCULOS ESPECÍFICOS y TIPO DE EQUIPO
data_musculos = {
    "Pectoral Mayor (Pecho Medio/Bajo)": [
        {
            "ejercicio": "Press de Pecho en Máquina",
            "equipo": "Máquina",
            "descripcion": "Siéntate con la espalda recta y empuja las asas hacia adelante. Excelente para aislar el pecho sin preocuparte por el equilibrio.",
            "puntos_clave": ["Mantén los hombros atrás.", "Controla el peso al regresar."],
            "img_url": "pecho_maquina.png"
        },
        {
            "ejercicio": "Press Plano con Mancuernas",
            "equipo": "Mancuernas",
            "descripcion": "Acuéstate en un banco plano. Baja las mancuernas a los lados del pecho y empuja hacia arriba formando un triángulo imaginario.",
            "puntos_clave": ["Mayor rango de movimiento que la barra.", "Mantén los pies firmes en el suelo."],
            "img_url": "pecho_mancuernas.png"
        },
        {
            "ejercicio": "Aperturas (Pec Deck)",
            "equipo": "Máquina",
            "descripcion": "Siéntate y junta los brazos frente a tu pecho. Ideal para la parte final de la contracción del pectoral.",
            "puntos_clave": ["Mantén una ligera flexión de codos constante."],
            "img_url": "pec_deck.png"
        }
    ],
    "Pectoral Superior (Fibras Claviculares)": [
        {
            "ejercicio": "Press Inclinado con Mancuernas",
            "equipo": "Mancuernas",
            "descripcion": "En un banco a 30-45 grados, empuja las mancuernas hacia arriba. Enfoca el trabajo en la parte alta del pecho.",
            "puntos_clave": ["No inclines el banco más de 45 grados para no involucrar demasiado el hombro."],
            "img_url": "pecho_inclinado_mancuernas.png"
        }
    ],
    "Dorsal Ancho (Espalda)": [
        {
            "ejercicio": "Jalón al Pecho",
            "equipo": "Máquina",
            "descripcion": "Tira de la barra superior hacia tus clavículas juntando las escápulas.",
            "puntos_clave": ["Saca el pecho al tirar.", "No te balancees hacia atrás."],
            "img_url": "jalon_pecho.png"
        },
        {
            "ejercicio": "Remo a una mano con Mancuerna",
            "equipo": "Mancuernas",
            "descripcion": "Apoya una rodilla y mano en un banco. Tira de la mancuerna hacia tu cadera con la otra mano.",
            "puntos_clave": ["Mantén la espalda paralela al suelo.", "El codo debe ir hacia el techo y atrás."],
            "img_url": "remo_mancuerna.png"
        }
    ],
    "Deltoides (Hombros completos)": [
        {
            "ejercicio": "Press Militar Guiado",
            "equipo": "Máquina",
            "descripcion": "Empuja el peso por encima de tu cabeza. Trabaja principalmente el deltoides anterior (frontal).",
            "puntos_clave": ["No bloquees los codos al final del movimiento."],
            "img_url": "press_hombro_maquina.png"
        },
        {
            "ejercicio": "Elevaciones Laterales",
            "equipo": "Mancuernas",
            "descripcion": "De pie, levanta las mancuernas hacia los lados hasta la altura de los hombros. Aísla el deltoides lateral para dar amplitud al hombro.",
            "puntos_clave": ["Imagina que estás vertiendo agua de una jarra al llegar arriba."],
            "img_url": "laterales_mancuerna.png"
        }
    ],
    "Cuádriceps (Parte frontal de la pierna)": [
        {
            "ejercicio": "Prensa de Piernas",
            "equipo": "Máquina",
            "descripcion": "Empuja la plataforma con las piernas. Excelente para mover mucho peso de forma segura.",
            "puntos_clave": ["Pies en la parte baja/media de la plataforma enfocan más el cuádriceps."],
            "img_url": "prensa_piernas.png"
        },
        {
            "ejercicio": "Sentadilla Copa (Goblet Squat)",
            "equipo": "Pesas Rusas (Kettlebells)",
            "descripcion": "Sostén una pesa rusa o mancuerna pegada a tu pecho y haz una sentadilla profunda.",
            "puntos_clave": ["Mantén el torso lo más vertical posible.", "Abre las rodillas al bajar."],
            "img_url": "goblet_squat.png"
        },
        {
            "ejercicio": "Zancadas (Lunges)",
            "equipo": "Mancuernas",
            "descripcion": "Con una mancuerna en cada mano, da un paso adelante y baja la cadera hasta que ambas rodillas formen 90 grados.",
            "puntos_clave": ["Mantén el pecho arriba.", "La rodilla delantera no debe colapsar hacia adentro."],
            "img_url": "lunges.png"
        }
    ],
    "Isquiotibiales y Glúteos (Parte posterior)": [
        {
            "ejercicio": "Curl de Piernas Tumbado/Sentado",
            "equipo": "Máquina",
            "descripcion": "Flexiona las rodillas llevando el peso hacia tus glúteos. Aísla completamente los isquiotibiales.",
            "puntos_clave": ["Mantén la cadera pegada a la almohadilla."],
            "img_url": "curl_isquios.png"
        },
        {
            "ejercicio": "Kettlebell Swing (Balanceo)",
            "equipo": "Pesas Rusas (Kettlebells)",
            "descripcion": "Balancea la pesa rusa desde entre tus piernas hasta la altura del pecho usando la fuerza de tu cadera y glúteos.",
            "puntos_clave": ["Es un movimiento de bisagra de cadera, no una sentadilla.", "Contrae los glúteos fuerte al subir."],
            "img_url": "kettlebell_swing.png"
        },
        {
            "ejercicio": "Peso Muerto Rumano",
            "equipo": "Mancuernas",
            "descripcion": "Con las piernas ligeramente flexionadas, baja las mancuernas por el frente de tus piernas empujando la cadera hacia atrás.",
            "puntos_clave": ["Siente el estiramiento en la parte posterior de la pierna.", "Mantén la espalda completamente recta."],
            "img_url": "peso_muerto_rumano.png"
        }
    ],
    "Bíceps y Tríceps (Brazos)": [
        {
            "ejercicio": "Curl Alterno",
            "equipo": "Mancuernas",
            "descripcion": "Flexiona un brazo a la vez rotando la muñeca hacia afuera al subir (supinación).",
            "puntos_clave": ["Mantén los codos pegados a las costillas."],
            "img_url": "curl_biceps.png"
        },
        {
            "ejercicio": "Extensión de Tríceps en Polea",
            "equipo": "Máquina",
            "descripcion": "Empuja la cuerda o barra hacia abajo extendiendo completamente los brazos.",
            "puntos_clave": ["Solo se mueven los antebrazos, los codos quedan fijos."],
            "img_url": "triceps_polea.png"
        },
        {
            "ejercicio": "Extensión Copa a dos manos",
            "equipo": "Mancuernas",
            "descripcion": "Sostén una mancuerna por encima de tu cabeza y bájala por detrás de la nuca flexionando los codos.",
            "puntos_clave": ["Apunta los codos hacia el techo.", "Excelente para la cabeza larga del tríceps."],
            "img_url": "copa_triceps.png"
        }
    ]
}

# --- INTERFAZ DE BÚSQUEDA ---
st.divider()

# 1. Seleccionar el músculo
lista_musculos = list(data_musculos.keys())
musculo_seleccionado = st.selectbox("🔍 1. ¿Qué músculo principal vas a entrenar?", ["Selecciona un músculo..."] + lista_musculos)

if musculo_seleccionado != "Selecciona un músculo...":
    
    # 2. Filtrar por equipo disponible (Opcional)
    st.write("⚙️ 2. ¿Qué equipo tienes disponible?")
    filtro_equipo = st.radio(
        "Filtro de equipo:",
        ["Ver Todos", "Máquina", "Mancuernas", "Pesas Rusas (Kettlebells)"],
        horizontal=True,
        label_visibility="collapsed"
    )
    
    st.divider()
    st.markdown(f'<p class="big-font">Ejercicios para: {musculo_seleccionado}</p>', unsafe_allow_html=True)
    
    ejercicios_del_musculo = data_musculos[musculo_seleccionado]
    ejercicios_mostrados = 0
    
    for ejercicio in ejercicios_del_musculo:
        # Aplicar el filtro
        if filtro_equipo == "Ver Todos" or ejercicio["equipo"] == filtro_equipo:
            ejercicios_mostrados += 1
            
            with st.container():
                st.markdown(f"### 📍 {ejercicio['ejercicio']}")
                st.markdown(f"<span class='equipo-tag'>🛠️ Equipo requerido: {ejercicio['equipo']}</span>", unsafe_allow_html=True)
                st.write("") # Espacio
                
                # Imagen (Recuerda poner el nombre de tus imágenes reales en el diccionario)
                # st.image(ejercicio["img_url"], use_column_width=True) 
                
                st.info(f"**Técnica:** {ejercicio['descripcion']}")
                
                st.markdown("**🛑 Puntos Clave:**")
                for punto in ejercicio['puntos_clave']:
                    st.markdown(f"- <span class='key-point'>{punto}</span>", unsafe_allow_html=True)
                
                st.divider()
                
    if ejercicios_mostrados == 0:
        st.warning(f"No hay ejercicios registrados para {musculo_seleccionado} usando {filtro_equipo}. Prueba cambiando el filtro de equipo.")
