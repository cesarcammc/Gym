import streamlit as st

# Configuración avanzada de la interfaz
st.set_page_config(page_title="Mi Gym App", page_icon="🏋️", layout="centered")

# Estilo personalizado
st.markdown("""
    <style>
    .big-font { font-size:22px !important; font-weight: bold; color: #2e86c1; }
    .key-point { color: #f63366; font-weight: bold; }
    .zona-tag { background-color: #e8f4f8; padding: 4px 8px; border-radius: 4px; font-size: 14px; color: #117a65; }
    </style>
    """, unsafe_allow_html=True)

st.title("🏋️‍♂️ Asistente de Entrenamiento Inteligente")
st.write("Explora las máquinas, equipos y zonas disponibles en el gimnasio.")

# Base de datos adaptada a tu gimnasio real
data_rutinas = {
    "Pecho (Musculación)": [
        {
            "maquina": "Banco de Press Plano",
            "zona": "Zona de Pesas y Musculación",
            "musculo_activado": "Pectoral Mayor",
            "musculos_secundarios": "Tríceps, Deltoides Anterior",
            "descripcion_detallada": "Acuéstate en el banco. Usa la barra olímpica o mancuernas. Baja el peso de forma controlada hasta el nivel del pecho y empuja hacia arriba.",
            "puntos_clave": ["Mantén los pies firmes en el suelo.", "No rebotes la barra en el pecho."],
            "img_anatomia": "https://drive.google.com/uc?export=1hsqqQVWGnsYKeRDcrKx8x4-MohSmhBmE"
        },
        {
            "maquina": "Banco de Press Inclinado",
            "zona": "Zona de Pesas y Musculación",
            "musculo_activado": "Pectoral Superior (Fibras Claviculares)",
            "musculos_secundarios": "Deltoides Frontal, Tríceps",
            "descripcion_detallada": "Acuéstate en el banco inclinado. Baja la barra o mancuernas hacia la parte superior del pecho y empuja.",
            "puntos_clave": ["Ajusta el banco a unos 30-45 grados.", "Controla la bajada para no forzar los hombros."],
            "img_anatomia": "https://i.imgur.com/pecho_inclinado.png"
        },
        {
            "maquina": "Estación de Poleas Cruzadas (Crossover)",
            "zona": "Zona de Pesas y Musculación",
            "musculo_activado": "Pectoral Mayor (Aislamiento)",
            "musculos_secundarios": "Core (Estabilización)",
            "descripcion_detallada": "Coloca las poleas en la posición alta. Da un paso adelante, inclina ligeramente el torso y junta las asas frente a ti con los codos ligeramente flexionados.",
            "puntos_clave": ["El movimiento debe ser como dar un abrazo, no empujar.", "Aprieta el pecho al juntar las manos."],
            "img_anatomia": "https://i.imgur.com/poleas_pecho.png"
        },
        {
            "maquina": "Máquina Pec Dec",
            "zona": "Zona de Pesas y Musculación",
            "musculo_activado": "Pectoral Mayor y Menor",
            "musculos_secundarios": "Deltoides Anterior",
            "descripcion_detallada": "Siéntate, coloca los brazos en las almohadillas o agarra las asas. Junta los brazos frente al pecho y regresa controladamente.",
            "puntos_clave": ["No dejes que el peso tire tus brazos bruscamente hacia atrás."],
            "img_anatomia": "https://i.imgur.com/pec_dec.png"
        }
    ],
    "Piernas (Musculación)": [
        {
            "maquina": "Jaula para Sentadillas (Squat Rack)",
            "zona": "Zona de Pesas y Musculación",
            "musculo_activado": "Cuádriceps, Glúteos",
            "musculos_secundarios": "Isquiotibiales, Core, Espalda Baja",
            "descripcion_detallada": "Coloca la barra olímpica sobre tus trapecios. Flexiona rodillas y cadera como si fueras a sentarte, manteniendo la espalda recta.",
            "puntos_clave": ["Las rodillas deben apuntar en la misma dirección que las puntas de los pies.", "Usa los seguros de la jaula para mayor seguridad."],
            "img_anatomia": "https://i.imgur.com/sentadilla.png"
        },
        {
            "maquina": "Prensa de Piernas Guiada",
            "zona": "Zona de Pesas y Musculación",
            "musculo_activado": "Cuádriceps, Glúteo Mayor",
            "musculos_secundarios": "Isquiotibiales",
            "descripcion_detallada": "Empuja la plataforma con los pies separados a la anchura de los hombros. Baja lentamente hasta que tus rodillas formen 90 grados.",
            "puntos_clave": ["Nunca bloquees (hiperextiendas) las rodillas al empujar.", "Mantén la zona lumbar pegada al respaldo."],
            "img_anatomia": "https://i.imgur.com/prensa.png"
        },
        {
            "maquina": "Máquina de Extensión de Piernas",
            "zona": "Zona de Pesas y Musculación",
            "musculo_activado": "Cuádriceps (Aislamiento)",
            "musculos_secundarios": "Ninguno",
            "descripcion_detallada": "Siéntate y coloca el empeine bajo el rodillo. Extiende las piernas por completo y baja el peso de forma controlada.",
            "puntos_clave": ["Alinea tus rodillas con el eje de rotación de la máquina."],
            "img_anatomia": "https://i.imgur.com/extension.png"
        },
        {
            "maquina": "Máquina de Curl de Piernas",
            "zona": "Zona de Pesas y Musculación",
            "musculo_activado": "Isquiotibiales (Parte posterior del muslo)",
            "musculos_secundarios": "Gemelos",
            "descripcion_detallada": "Acuéstate boca abajo o siéntate (según la máquina). Flexiona las rodillas llevando los talones hacia los glúteos.",
            "puntos_clave": ["No levantes la cadera al flexionar las rodillas."],
            "img_anatomia": "https://i.imgur.com/curl_pierna.png"
        }
    ],
    "Cardiovascular": [
        {
            "maquina": "Banda Caminadora (Cinta)",
            "zona": "Zona Cardiovascular",
            "musculo_activado": "Sistema Cardiovascular",
            "musculos_secundarios": "Cuádriceps, Gemelos",
            "descripcion_detallada": "Ideal para calentamiento o resistencia. Ajusta la velocidad e inclinación. Corre o camina manteniendo una postura erguida.",
            "puntos_clave": ["Usa el clip de seguridad.", "Evita sostenerte de los pasamanos para quemar más calorías."],
            "img_anatomia": "https://i.imgur.com/cinta.png"
        },
        {
            "maquina": "Máquina Elíptica",
            "zona": "Zona Cardiovascular",
            "musculo_activado": "Cardio (Bajo Impacto)",
            "musculos_secundarios": "Piernas completas, Hombros, Brazos",
            "descripcion_detallada": "Movimiento fluido sin impacto articular. Empuja y tira de los manubrios mientras pedaleas.",
            "puntos_clave": ["Mantén los talones apoyados la mayor parte del recorrido."],
            "img_anatomia": "https://i.imgur.com/eliptica.png"
        },
        {
            "maquina": "Bicicleta Estática",
            "zona": "Zona Cardiovascular",
            "musculo_activado": "Cardio",
            "musculos_secundarios": "Cuádriceps, Gemelos",
            "descripcion_detallada": "Ajusta la altura del sillín para que tu pierna quede ligeramente flexionada en el punto más bajo del pedal.",
            "puntos_clave": ["Mantén la espalda recta y no apoyes todo tu peso en el manubrio."],
            "img_anatomia": "https://i.imgur.com/bici_estatica.png"
        }
    ],
    "Funcional y Peso Libre": [
        {
            "maquina": "Pesas Rusas (Kettlebells)",
            "zona": "Zona Funcional",
            "musculo_activado": "Cuerpo Completo (Core, Glúteos, Espalda)",
            "musculos_secundarios": "Hombros, Brazos",
            "descripcion_detallada": "Ideales para balanceos (Swings), sentadillas copa (Goblet Squats) o levantamientos turcos.",
            "puntos_clave": ["En los swings, la fuerza viene de la cadera (glúteos), no de los brazos."],
            "img_anatomia": "https://i.imgur.com/kettlebell.png"
        },
        {
            "maquina": "Cajón Pliométrico",
            "zona": "Zona Funcional",
            "musculo_activado": "Potencia de Piernas",
            "musculos_secundarios": "Cardio",
            "descripcion_detallada": "Úsalo para saltos de cajón (Box Jumps) o steps ups. Amortigua la caída al saltar flexionando las rodillas.",
            "puntos_clave": ["Salta hacia el centro del cajón y baja caminando, no saltando hacia atrás."],
            "img_anatomia": "https://i.imgur.com/cajon.png"
        },
        {
            "maquina": "Bandas de Resistencia",
            "zona": "Zona Funcional",
            "musculo_activado": "Músculos Estabilizadores",
            "musculos_secundarios": "Rehabilitación",
            "descripcion_detallada": "Perfectas para calentamiento articular, trabajo de movilidad o añadir tensión a ejercicios de peso corporal.",
            "puntos_clave": ["Controla siempre la banda, no dejes que ella te 'jale' bruscamente en el retorno."],
            "img_anatomia": "https://i.imgur.com/bandas.png"
        }
    ],
    "Clases Grupales": [
        {
            "maquina": "Bicicleta Indoor (Spinning)",
            "zona": "Zona de Clases",
            "musculo_activado": "Cardio Alta Intensidad (HIIT)",
            "musculos_secundarios": "Cuádriceps, Core",
            "descripcion_detallada": "Diseñadas para clases guiadas. Permiten un pedaleo de pie y simulaciones de montaña con alta resistencia.",
            "puntos_clave": ["Asegura bien los pies en los pedales y ajusta el manubrio para no tensar la espalda baja."],
            "img_anatomia": "https://i.imgur.com/spinning.png"
        },
        {
            "maquina": "Clases de Yoga / Pilates / Rumba",
            "zona": "Zona de Clases",
            "musculo_activado": "Flexibilidad, Core y Ritmo",
            "musculos_secundarios": "Estabilidad Mental y Física",
            "descripcion_detallada": "Uso de colchonetas y steps. Enfocado en la conexión mente-músculo, quema calórica divertida y salud articular.",
            "puntos_clave": ["Sigue las indicaciones del instructor y escucha a tu cuerpo para evitar sobreestiramientos."],
            "img_anatomia": "https://i.imgur.com/clases.png"
        }
    ]
}

# Preparar un diccionario plano para la búsqueda por máquinas
todas_las_maquinas = {}
for categoria, lista_maquinas in data_rutinas.items():
    for maquina in lista_maquinas:
        todas_las_maquinas[maquina["maquina"]] = maquina
        todas_las_maquinas[maquina["maquina"]]["categoria_perteneciente"] = categoria

# --- INTERFAZ DE BÚSQUEDA ---
st.divider()
tipo_busqueda = st.radio(
    "Selecciona tu método de búsqueda:",
    ["🔍 Buscar por Categoría / Grupo Muscular", "⚙️ Buscar por Equipo / Máquina"],
    horizontal=True
)
st.divider()

# Función para mostrar la tarjeta de información
def mostrar_detalle_maquina(ejercicio):
    with st.container():
        st.markdown(f"### 📍 {ejercicio['maquina']}")
        st.markdown(f"<span class='zona-tag'>🗺️ Ubicación: {ejercicio['zona']}</span>", unsafe_allow_html=True)
        st.write("") # Espaciador
        
        # Imagen
        st.image(ejercicio["img_anatomia"], use_container_width=True, caption=f"Enfoque: {ejercicio['musculo_activado']}")
        
        # Detalles de los músculos
        st.markdown(f"**Principal:** <span class='key-point'>{ejercicio['musculo_activado']}</span>", unsafe_allow_html=True)
        if ejercicio['musculos_secundarios'] != "Ninguno":
            st.write(f"**Secundarios:** {ejercicio['musculos_secundarios']}")
        
        # Instrucciones
        st.info(f"**Cómo usarlo:** {ejercicio['descripcion_detallada']}")
        
        # Puntos clave
        st.markdown("**🛑 Puntos Clave de Seguridad:**")
        for punto in ejercicio['puntos_clave']:
            st.markdown(f"- {punto}")
        st.divider()


# LÓGICA: BÚSQUEDA POR CATEGORÍA
if tipo_busqueda == "🔍 Buscar por Categoría / Grupo Muscular":
    categorias = list(data_rutinas.keys())
    seleccion_cat = st.selectbox("Elige la categoría o grupo muscular:", ["Selecciona una opción..."] + categorias)
    
    if seleccion_cat != "Selecciona una opción...":
        st.markdown(f'<p class="big-font">Equipos disponibles para: {seleccion_cat}</p>', unsafe_allow_html=True)
        ejercicios = data_rutinas[seleccion_cat]
        
        for ejercicio in ejercicios:
            mostrar_detalle_maquina(ejercicio)


# LÓGICA: BÚSQUEDA POR MÁQUINA
elif tipo_busqueda == "⚙️ Buscar por Equipo / Máquina":
    nombres_equipos = list(todas_las_maquinas.keys())
    nombres_equipos.sort() 
    
    seleccion_equipo = st.selectbox("Busca la máquina o equipo que vas a usar:", ["Selecciona una opción..."] + nombres_equipos)
    
    if seleccion_equipo != "Selecciona una opción...":
        equipo_elegido = todas_las_maquinas[seleccion_equipo]
        st.markdown(f'<p class="big-font">Detalles del Equipo</p>', unsafe_allow_html=True)
        
        mostrar_detalle_maquina(equipo_elegido)
