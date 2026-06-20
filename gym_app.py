import streamlit as st

# Configuración avanzada de la interfaz
st.set_page_config(page_title="Entrenador Pro", page_icon="💪", layout="centered")

# Estilo personalizado para textos
st.markdown("""
    <style>
    .big-font { font-size:24px !important; font-weight: bold; }
    .key-point { color: #f63366; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

st.title("🏋️‍♂️ Asistente de Entrenamiento ProGym")
st.write("Encuentra tu rutina o consulta una máquina específica.")

# Base de datos actualizada (Sin movimientos, con Cardio)
data_rutinas = {
    "Pecho (Pectorales)": [
        {
            "maquina": "Máquina de Press de Pecho (Chest Press)",
            "musculo_activado": "Pectoral Mayor",
            "musculos_secundarios": "Tríceps, Deltoides Anterior",
            "descripcion_detallada": "Siéntate y ajusta el asiento para que las asas estén a la altura de tu pecho medio. Empuja las asas de forma controlada hasta casi extender los brazos. Regresa lentamente controlando el peso.",
            "puntos_clave": ["Mantén los hombros retraídos contra el respaldo.", "No impulses con el torso.", "Exhala al empujar."],
            "img_anatomia": "https://i.imgur.com/tu_enlace_anatomia_pecho.png"
        },
        {
            "maquina": "Máquina Pec Deck (Aperturas)",
            "musculo_activado": "Pectoral Mayor",
            "musculos_secundarios": "Deltoides Anterior",
            "descripcion_detallada": "Junta los brazos frente a tu cuerpo contrayendo el pecho intensamente. Regresa lentamente hasta el punto de estiramiento inicial sin rebotar.",
            "puntos_clave": ["Mantén una ligera flexión en los codos.", "Controla la fase negativa."],
            "img_anatomia": "https://i.imgur.com/tu_enlace_anatomia_pecdeck.png"
        }
    ],
    "Espalda (Dorsales/Trapecios)": [
        {
            "maquina": "Máquina de Jalón al Pecho (Lat Pulldown)",
            "musculo_activado": "Dorsal Ancho (Latissimus Dorsi)",
            "musculos_secundarios": "Bíceps, Trapecio Inferior",
            "descripcion_detallada": "Agarra la barra más allá del ancho de los hombros. Tira de la barra hacia la parte superior del pecho apretando los dorsales.",
            "puntos_clave": ["Inicia el movimiento con las escápulas.", "No uses balanceo.", "Exhala al tirar."],
            "img_anatomia": "https://i.imgur.com/tu_enlace_anatomia_espalda.png"
        }
    ],
    "Piernas (Cuádriceps)": [
        {
            "maquina": "Prensa de Piernas (Leg Press)",
            "musculo_activado": "Cuádriceps, Glúteo Mayor",
            "musculos_secundarios": "Gemelos, Isquiotibiales",
            "descripcion_detallada": "Coloca los pies en la plataforma a la anchura de los hombros. Empuja la plataforma hasta extender las piernas. Baja lentamente.",
            "puntos_clave": ["Mantén la espalda baja pegada al asiento.", "No juntes las rodillas al empujar.", "No bloquees las rodillas al extender."],
            "img_anatomia": "https://i.imgur.com/tu_enlace_anatomia_prensa.png"
        }
    ],
    "Cardio": [
        {
            "maquina": "Cinta de Correr (Treadmill)",
            "musculo_activado": "Sistema Cardiovascular",
            "musculos_secundarios": "Cuádriceps, Gemelos, Core",
            "descripcion_detallada": "Ajusta la velocidad y la inclinación según tu nivel. Mantén una postura erguida, evita mirar hacia abajo y balancea los brazos naturalmente al ritmo de tu zancada.",
            "puntos_clave": ["Empieza con un calentamiento suave.", "No te agarres de las barandas si no es estrictamente necesario.", "Mantén el abdomen firme."],
            "img_anatomia": "https://i.imgur.com/tu_enlace_anatomia_cinta.png"
        },
        {
            "maquina": "Máquina Elíptica",
            "musculo_activado": "Sistema Cardiovascular (Cuerpo Completo)",
            "musculos_secundarios": "Glúteos, Isquiotibiales, Hombros",
            "descripcion_detallada": "Súbete a los pedales y agarra los manubrios móviles. Empuja y jala con los brazos mientras pedaleas con las piernas en un movimiento fluido, manteniendo la espalda recta.",
            "puntos_clave": ["Mantén los talones pegados a los pedales la mayor parte del tiempo.", "Usa tanto los brazos como las piernas.", "Mantén una resistencia que te rete sin perder la fluidez."],
            "img_anatomia": "https://i.imgur.com/tu_enlace_anatomia_eliptica.png"
        }
    ]
}

# Preparar un diccionario plano para la búsqueda por máquinas
todas_las_maquinas = {}
for grupo_muscular, lista_maquinas in data_rutinas.items():
    for maquina in lista_maquinas:
        # Guardamos la máquina y le añadimos a qué grupo pertenece
        todas_las_maquinas[maquina["maquina"]] = maquina
        todas_las_maquinas[maquina["maquina"]]["grupo_perteneciente"] = grupo_muscular

# --- INTERFAZ DE BÚSQUEDA ---
st.divider()
tipo_busqueda = st.radio(
    "Selecciona tu método de búsqueda:",
    ["🔍 Buscar por Grupo Muscular", "⚙️ Buscar por Máquina"],
    horizontal=True
)
st.divider()

# Función para mostrar la tarjeta de información de una máquina
def mostrar_detalle_maquina(ejercicio):
    with st.container():
        st.subheader(f"📍 {ejercicio['maquina']}")
        
        # Mostrar la imagen centrada
        st.image(ejercicio["img_anatomia"], use_container_width=True, caption=f"Enfoque: {ejercicio['musculo_activado']}")
        
        # Detalles de los músculos
        st.markdown(f"**Principal:** <span class='key-point'>{ejercicio['musculo_activado']}</span>", unsafe_allow_html=True)
        st.write(f"**Secundarios:** {ejercicio['musculos_secundarios']}")
        
        # Instrucciones
        st.info(f"**Cómo ejecutarlo:** {ejercicio['descripcion_detallada']}")
        
        # Puntos clave
        st.markdown("**🛑 Puntos Clave:**")
        for punto in ejercicio['puntos_clave']:
            st.markdown(f"- {punto}")
        st.divider()


# LÓGICA: BÚSQUEDA POR GRUPO MUSCULAR
if tipo_busqueda == "🔍 Buscar por Grupo Muscular":
    grupos = list(data_rutinas.keys())
    seleccion_grupo = st.selectbox("Elige el grupo muscular o tipo de entrenamiento:", ["Selecciona una opción..."] + grupos)
    
    if seleccion_grupo != "Selecciona una opción...":
        st.markdown(f'<p class="big-font">Rutina para: {seleccion_grupo}</p>', unsafe_allow_html=True)
        ejercicios = data_rutinas[seleccion_grupo]
        
        for ejercicio in ejercicios:
            mostrar_detalle_maquina(ejercicio)


# LÓGICA: BÚSQUEDA POR MÁQUINA
elif tipo_busqueda == "⚙️ Buscar por Máquina":
    nombres_maquinas = list(todas_las_maquinas.keys())
    # Ordenar alfabéticamente para que sea más fácil buscar
    nombres_maquinas.sort() 
    
    seleccion_maquina = st.selectbox("Escribe o selecciona la máquina que tienes frente a ti:", ["Selecciona una opción..."] + nombres_maquinas)
    
    if seleccion_maquina != "Selecciona una opción...":
        maquina_elegida = todas_las_maquinas[seleccion_maquina]
        st.markdown(f'<p class="big-font">Detalles de la máquina</p>', unsafe_allow_html=True)
        st.caption(f"Esta máquina pertenece a la categoría: {maquina_elegida['grupo_perteneciente']}")
        
        mostrar_detalle_maquina(maquina_elegida)
