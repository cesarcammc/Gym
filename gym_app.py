import streamlit as st

# Configuración avanzada de la interfaz
st.set_page_config(page_title="Entrenador Pro", page_icon="💪", layout="wide")

# Estilo personalizado para textos
st.markdown("""
    <style>
    .big-font { font-size:24px !important; font-weight: bold; }
    .medium-font { font-size:18px !important; }
    .key-point { color: #f63366; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

st.title("🏋️‍♂️ Asistente de Entrenamiento ProGym")
st.write("Selecciona un grupo muscular para ver detalles profundos de las máquinas recomendadas.")

# Base de datos expandida y detallada
data_rutinas = {
    "Pecho (Pectorales)": [
        {
            "maquina": "Máquina de Press de Pecho (Chest Press)",
            "musculo_activado": "Pectoral Mayor (énfasis medio/inferior)",
            "musculos_secundarios": "Tríceps, Deltoides Anterior",
            "descripcion_detallada": "Siéntate y ajusta la altura del asiento para que las asas estén a la altura de tu pecho medio. Empuja las asas de forma controlada hasta casi extender los brazos, pero sin bloquear los codos. Regresa lentamente controlando el peso hasta sentir un estiramiento controlado.",
            "puntos_clave": ["Mantén los hombros retraídos contra el respaldo.", "No impulses con el torso.", "Exhala al empujar, inhala al regresar."],
            "img_anatomia": "https://i.imgur.com/tu_enlace_anatomia.png", # REEMPLAZAR CON URL REAL
            "img_movimiento": "https://i.imgur.com/tu_enlace_movimiento.gif" # REEMPLAZAR CON URL REAL
        },
        {
            "maquina": "Máquina Pec Deck (Aperturas)",
            "musculo_activado": "Pectoral Mayor (énfasis en el estiramiento y contracción medial)",
            "musculos_secundarios": "Deltoides Anterior",
            "descripcion_detallada": "Ajusta el asiento para que tus brazos queden paralelos al suelo cuando agarres las asas. Junta los brazos frente a tu cuerpo contrayendo el pecho intensamente. Regresa lentamente hasta el punto de estiramiento inicial sin rebotar.",
            "puntos_clave": ["Mantén una ligera flexión en los codos.", "No permitas que el peso te 'estire' bruscamente.", "Controla la fase negativa."],
            "img_anatomia": "https://i.imgur.com/tu_enlace_anatomia_2.png",
            "img_movimiento": "https://i.imgur.com/tu_enlace_movimiento_2.gif"
        }
    ],
    "Espalda (Dorsales/Trapecios)": [
        {
            "maquina": "Máquina de Jalón al Pecho (Lat Pulldown)",
            "musculo_activado": "Dorsal Ancho (Latissimus Dorsi)",
            "musculos_secundarios": "Bíceps, Braquial, Trapecio Inferior",
            "descripcion_detallada": "Ajusta el rodillo para sujetar tus muslos. Agarra la barra más allá del ancho de los hombros. Tira de la barra hacia la parte superior del pecho (clavículas) apretando los dorsales, no solo los brazos. Inclina el torso ligeramente hacia atrás.",
            "puntos_clave": ["Inicia el movimiento con las escápulas, no con los bíceps.", "No uses 'momentum' o balanceo.", "Exhala al tirar."],
            "img_anatomia": "https://i.imgur.com/tu_enlace_anatomia_3.png",
            "img_movimiento": "https://i.imgur.com/tu_enlace_movimiento_3.gif"
        },
        {
            "maquina": "Máquina de Remo Sentado (Seated Row)",
            "musculo_activado": "Dorsal Ancho, Trapecio Medio, Romboides",
            "musculos_secundarios": "Bíceps, Braquial",
            "descripcion_detallada": "Coloca los pies en los soportes y mantén una ligera flexión de rodillas. Agarra el manubrio y mantén la espalda recta. Tira del manubrio hacia tu ombligo apretando las escápulas hacia atrás. Extiende los brazos completamente en el regreso.",
            "puntos_clave": ["Mantén el pecho erguido y los hombros hacia atrás.", "No encorves la espalda baja.", "Controla el retorno del peso."],
            "img_anatomia": "https://i.imgur.com/tu_enlace_anatomia_4.png",
            "img_movimiento": "https://i.imgur.com/tu_enlace_movimiento_4.gif"
        }
    ],
    "Hombros (Deltoides)": [
        {
            "maquina": "Máquina de Press Militar (Shoulder Press)",
            "musculo_activado": "Deltoides Anterior (frontal), Deltoides Lateral",
            "musculos_secundarios": "Tríceps, Trapecio Superior",
            "descripcion_detallada": "Ajusta el asiento. Agarra las asas con las palmas hacia adelante. Empuja el peso hacia arriba sobre tu cabeza hasta casi extender los brazos. Baja lentamente hasta que las asas estén a la altura de las orejas.",
            "puntos_clave": ["Mantén la espalda baja pegada al respaldo.", "No bloquees los codos arriba.", "No permitas que los codos se abran excesivamente hacia atrás."],
            "img_anatomia": "https://i.imgur.com/tu_enlace_anatomia_5.png",
            "img_movimiento": "https://i.imgur.com/tu_enlace_movimiento_5.gif"
        }
    ],
    "Brazos (Bíceps)": [
        {
            "maquina": "Máquina de Curl de Bíceps (Cable/Polea)",
            "musculo_activado": "Bíceps Braquial",
            "musculos_secundarios": "Braquiorradial",
            "descripcion_detallada": "Usa una barra recta o E-Z enganchada a una polea baja. Agarra la barra con las palmas hacia arriba. Flexiona los brazos llevando la barra hacia los hombros. Aprieta el bíceps arriba y baja controladamente sin mover los codos.",
            "puntos_clave": ["Mantén los codos pegados al cuerpo.", "No muevas el torso.", "Rango de movimiento completo."],
            "img_anatomia": "https://i.imgur.com/tu_enlace_anatomia_6.png",
            "img_movimiento": "https://i.imgur.com/tu_enlace_movimiento_6.gif"
        }
    ],
    "Piernas (Cuádriceps)": [
        {
            "maquina": "Prensa de Piernas (Leg Press)",
            "musculo_activado": "Cuádriceps, Glúteo Mayor, Isquiotibiales (secundario)",
            "musculos_secundarios": "Gemelos",
            "descripcion_detallada": "Coloca los pies en la plataforma a la anchura de los hombros. Empuja la plataforma hasta extender las piernas (sin bloquear las rodillas). Baja lentamente controlando el peso hasta que tus rodillas formen un ángulo cercano a 90 grados.",
            "puntos_clave": ["Mantén la espalda baja y glúteos pegados al asiento.", "No juntes las rodillas al empujar.", "Exhala al empujar."],
            "img_anatomia": "https://i.imgur.com/tu_enlace_anatomia_7.png",
            "img_movimiento": "https://i.imgur.com/tu_enlace_movimiento_7.gif"
        },
        {
            "maquina": "Máquina de Extensión de Piernas (Leg Extension)",
            "musculo_activado": "Cuádriceps (énfasis aislado)",
            "musculos_secundarios": "Ninguno (ejercicio de aislamiento)",
            "descripcion_detallada": "Ajusta la máquina para que el rodillo esté sobre tus empeines y el pivote de la máquina alineado con tus rodillas. Levanta el peso extendiendo completamente las piernas. Aprieta arriba y baja controladamente.",
            "puntos_clave": ["Mantén el torso recto y usa los agarres laterales.", "No impulses con la cadera.", "No hiperextiendas las rodillas."],
            "img_anatomia": "https://i.imgur.com/tu_enlace_anatomia_8.png",
            "img_movimiento": "https://i.imgur.com/tu_enlace_movimiento_8.gif"
        }
    ]
}

# Selector de grupo muscular
grupos_musculares = list(data_rutinas.keys())
seleccion = st.selectbox("¿Qué grupo muscular quieres entrenar hoy?", ["Selecciona una opción..."] + grupos_musculares)

# Lógica para mostrar la información detallada
if seleccion != "Selecciona una opción...":
    st.divider()
    st.markdown(f'<p class="big-font">Rutina Profesional para: {seleccion}</p>', unsafe_allow_html=True)
    
    ejercicios = data_rutinas[seleccion]
    
    for ejercicio in ejercicios:
        with st.expander(f"📖 DETALLES: {ejercicio['maquina']}", expanded=True):
            
            # Crear dos columnas para mostrar las imágenes lado a lado
            col_anat, col_mov = st.columns(2)
            
            with col_anat:
                st.write("**📍 Anatomía del Músculo Objetivo**")
                st.image(ejercicio["img_anatomia"], use_container_width=True, caption=f"Activación: {ejercicio['musculo_activado']}")
                
            with col_mov:
                st.write("**🎥 Ejecución del Movimiento**")
                st.image(ejercicio["img_movimiento"], use_container_width=True, caption="Movimiento controlado")
                
            # Sección de información textual rica
            st.divider()
            st.markdown(f"**Músculo Principal:** <span class='key-point'>{ejercicio['musculo_activado']}</span>", unsafe_allow_html=True)
            st.write(f"**Músculos Secundarios:** {ejercicio['musculos_secundarios']}")
            
            st.info(f"**Cómo ejecutarlo:** {ejercicio['descripcion_detallada']}")
            
            st.markdown("**🛑 Puntos Clave de la Técnica:**")
            for punto in ejercicio['puntos_clave']:
                st.markdown(f"- {punto}")
