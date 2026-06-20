import streamlit as st

# Configuración de la interfaz
st.set_page_config(page_title="Mi Gym App", page_icon="🏋️", layout="centered")

st.markdown("""
    <style>
    .big-font { font-size:22px !important; font-weight: bold; color: #2e86c1; }
    .key-point { color: #f63366; font-weight: bold; }
    .equipo-tag { background-color: #f2f3f4; padding: 4px 8px; border-radius: 4px; font-size: 14px; color: #34495e; border: 1px solid #bdc3c7;}
    /* Estilo para que los botones parezcan zonas del cuerpo */
    div.stButton > button { height: 60px; font-weight: bold; border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

st.title("🧍 Mapa Anatómico de Entrenamiento")
st.write("Toca la zona del cuerpo que deseas entrenar hoy:")

# --- MEMORIA DE LA APP (Session State) ---
# Esto guarda el músculo que seleccionaste al tocar un botón
if 'musculo_seleccionado' not in st.session_state:
    st.session_state.musculo_seleccionado = None

def seleccionar_musculo(musculo):
    st.session_state.musculo_seleccionado = musculo

# --- DIBUJAR EL CUERPO CON BOTONES ---
st.divider()

# Nivel 1: Hombros (Arriba al centro)
col_h_izq, col_h_cen, col_h_der = st.columns([1, 2, 1])
with col_h_cen:
    if st.button("💪 Hombros (Deltoides)", use_container_width=True): 
        seleccionar_musculo("Deltoides (Hombros completos)")

# Nivel 2: Pecho y Espalda (Centro)
col_pecho, col_espalda = st.columns(2)
with col_pecho:
    if st.button("🛡️ Pecho Medio/Bajo", use_container_width=True): 
        seleccionar_musculo("Pectoral Mayor (Pecho Medio/Bajo)")
    if st.button("🫁 Pecho Superior", use_container_width=True): 
        seleccionar_musculo("Pectoral Superior (Fibras Claviculares)")
with col_espalda:
    if st.button("🦇 Espalda (Dorsales)", use_container_width=True): 
        seleccionar_musculo("Dorsal Ancho (Espalda)")
    # Espacio vacío para equilibrar el diseño
    st.write("") 

# Nivel 3: Brazos (A los lados del centro)
col_brazo_izq, col_centro, col_brazo_der = st.columns([2, 1, 2])
with col_brazo_izq:
    if st.button("🦾 Bíceps / Tríceps", use_container_width=True): 
        seleccionar_musculo("Bíceps y Tríceps (Brazos)")
with col_brazo_der:
    if st.button("🦾 Bíceps / Tríceps ", use_container_width=True): 
        seleccionar_musculo("Bíceps y Tríceps (Brazos)")

# Nivel 4: Piernas (Abajo)
col_pierna_frente, col_pierna_atras = st.columns(2)
with col_pierna_frente:
    if st.button("🦵 Cuádriceps (Frente)", use_container_width=True): 
        seleccionar_musculo("Cuádriceps (Parte frontal de la pierna)")
with col_pierna_atras:
    if st.button("🍑 Glúteos e Isquios (Atrás)", use_container_width=True): 
        seleccionar_musculo("Isquiotibiales y Glúteos (Parte posterior)")

st.divider()

# --- BASE DE DATOS DE EJERCICIOS ---
data_musculos = {
    "Pectoral Mayor (Pecho Medio/Bajo)": [
        {"ejercicio": "Press de Pecho en Máquina", "equipo": "Máquina", "descripcion": "Siéntate con la espalda recta y empuja las asas hacia adelante.", "puntos_clave": ["Mantén los hombros atrás."], "img_url": "pecho_maquina.png"},
        {"ejercicio": "Press Plano con Mancuernas", "equipo": "Mancuernas", "descripcion": "Acuéstate en un banco plano y empuja las mancuernas.", "puntos_clave": ["Mantén los pies firmes en el suelo."], "img_url": "pecho_mancuernas.png"}
    ],
    "Pectoral Superior (Fibras Claviculares)": [
        {"ejercicio": "Press Inclinado con Mancuernas", "equipo": "Mancuernas", "descripcion": "En un banco a 30-45 grados, empuja hacia arriba.", "puntos_clave": ["No inclines más de 45 grados."], "img_url": "inclinado.png"}
    ],
    "Dorsal Ancho (Espalda)": [
        {"ejercicio": "Jalón al Pecho", "equipo": "Máquina", "descripcion": "Tira de la barra superior hacia tus clavículas.", "puntos_clave": ["Saca el pecho al tirar."], "img_url": "jalon.png"},
        {"ejercicio": "Remo con Mancuerna", "equipo": "Mancuernas", "descripcion": "Apoya una rodilla y mano en un banco. Tira de la mancuerna hacia tu cadera.", "puntos_clave": ["Espalda paralela al suelo."], "img_url": "remo.png"}
    ],
    "Deltoides (Hombros completos)": [
        {"ejercicio": "Press Militar Guiado", "equipo": "Máquina", "descripcion": "Empuja el peso por encima de tu cabeza.", "puntos_clave": ["No bloquees los codos."], "img_url": "militar.png"},
        {"ejercicio": "Elevaciones Laterales", "equipo": "Mancuernas", "descripcion": "Levanta las mancuernas hacia los lados.", "puntos_clave": ["Imagina verter agua de una jarra arriba."], "img_url": "laterales.png"}
    ],
    "Cuádriceps (Parte frontal de la pierna)": [
        {"ejercicio": "Prensa de Piernas", "equipo": "Máquina", "descripcion": "Empuja la plataforma con las piernas.", "puntos_clave": ["No bloquees las rodillas."], "img_url": "prensa.png"},
        {"ejercicio": "Sentadilla Copa", "equipo": "Pesas Rusas", "descripcion": "Sostén la pesa en el pecho y haz una sentadilla profunda.", "puntos_clave": ["Torso vertical."], "img_url": "copa.png"}
    ],
    "Isquiotibiales y Glúteos (Parte posterior)": [
        {"ejercicio": "Curl de Piernas", "equipo": "Máquina", "descripcion": "Flexiona las rodillas llevando el peso hacia glúteos.", "puntos_clave": ["Cadera pegada al asiento."], "img_url": "curl.png"},
        {"ejercicio": "Kettlebell Swing", "equipo": "Pesas Rusas", "descripcion": "Balancea la pesa desde entre tus piernas usando la cadera.", "puntos_clave": ["Bisagra de cadera, no sentadilla."], "img_url": "swing.png"}
    ],
    "Bíceps y Tríceps (Brazos)": [
        {"ejercicio": "Curl Alterno", "equipo": "Mancuernas", "descripcion": "Flexiona un brazo a la vez.", "puntos_clave": ["Codos pegados a costillas."], "img_url": "curl_bi.png"},
        {"ejercicio": "Extensión de Tríceps", "equipo": "Máquina", "descripcion": "Empuja la cuerda hacia abajo.", "puntos_clave": ["Solo se mueven antebrazos."], "img_url": "triceps.png"}
    ]
}

# --- MOSTRAR RESULTADOS ---
# Si se ha tocado algún botón del cuerpo, mostramos las opciones
if st.session_state.musculo_seleccionado is not None:
    
    st.write("⚙️ **Filtro rápido de equipo:**")
    filtro_equipo = st.radio(
        "Filtro:",
        ["Ver Todos", "Máquina", "Mancuernas", "Pesas Rusas"],
        horizontal=True,
        label_visibility="collapsed"
    )
    
    st.markdown(f'<p class="big-font">Rutina para: {st.session_state.musculo_seleccionado}</p>', unsafe_allow_html=True)
    
    ejercicios_del_musculo = data_musculos[st.session_state.musculo_seleccionado]
    ejercicios_mostrados = 0
    
    for ejercicio in ejercicios_del_musculo:
        if filtro_equipo == "Ver Todos" or ejercicio["equipo"] == filtro_equipo:
            ejercicios_mostrados += 1
            
            with st.container():
                st.markdown(f"### 📍 {ejercicio['ejercicio']}")
                st.markdown(f"<span class='equipo-tag'>🛠️ Equipo: {ejercicio['equipo']}</span>", unsafe_allow_html=True)
                st.write("")
                
                # st.image(ejercicio["img_url"], use_column_width=True) 
                
                st.info(f"**Técnica:** {ejercicio['descripcion']}")
                
                st.markdown("**🛑 Puntos Clave:**")
                for punto in ejercicio['puntos_clave']:
                    st.markdown(f"- <span class='key-point'>{punto}</span>", unsafe_allow_html=True)
                
                st.divider()
                
    if ejercicios_mostrados == 0:
        st.warning(f"No hay ejercicios para {st.session_state.musculo_seleccionado} con {filtro_equipo}.")
