import streamlit as st

# Base de datos simulada con los ejercicios, máquinas e imágenes (URLs)
# Nota: Reemplaza las URLs con enlaces reales a imágenes o GIFs de tu preferencia.
rutinas = {
    "Pecho": [
        {
            "maquina": "Máquina de Press de Pecho (Chest Press)",
            "descripcion_movimiento": "Siéntate con la espalda recta. Empuja las asas hacia adelante hasta casi extender los brazos por completo, luego regresa lentamente controlando el peso.",
            "img_musculo": "https://via.placeholder.com/400x200.png?text=Músculo:+Pectoral+Mayor",
            "img_movimiento": "https://via.placeholder.com/400x200.png?text=Movimiento:+Press+de+Pecho"
        },
        {
            "maquina": "Máquina de Aperturas (Pec Deck)",
            "descripcion_movimiento": "Coloca los antebrazos en las almohadillas. Junta los brazos frente a tu pecho contrayendo el músculo, y luego abre lentamente.",
            "img_musculo": "https://via.placeholder.com/400x200.png?text=Músculo:+Pectorales+y+Deltoides",
            "img_movimiento": "https://via.placeholder.com/400x200.png?text=Movimiento:+Pec+Deck"
        }
    ],
    "Espalda": [
        {
            "maquina": "Jalón al Pecho (Lat Pulldown)",
            "descripcion_movimiento": "Agarra la barra más allá de la anchura de los hombros. Tira de la barra hacia la parte superior de tu pecho juntando las escápulas.",
            "img_musculo": "https://via.placeholder.com/400x200.png?text=Músculo:+Dorsal+Ancho",
            "img_movimiento": "https://via.placeholder.com/400x200.png?text=Movimiento:+Jalón+al+Pecho"
        }
    ],
    "Piernas": [
        {
            "maquina": "Prensa de Piernas (Leg Press)",
            "descripcion_movimiento": "Coloca los pies en la plataforma a la anchura de los hombros. Empuja la plataforma hasta extender las piernas (sin bloquear las rodillas) y baja lentamente.",
            "img_musculo": "https://via.placeholder.com/400x200.png?text=Músculo:+Cuádriceps+y+Glúteos",
            "img_movimiento": "https://via.placeholder.com/400x200.png?text=Movimiento:+Prensa+de+Piernas"
        },
        {
            "maquina": "Máquina de Extensión de Piernas",
            "descripcion_movimiento": "Siéntate y coloca los empeines bajo el rodillo. Levanta el peso extendiendo las rodillas y baja controladamente.",
            "img_musculo": "https://via.placeholder.com/400x200.png?text=Músculo:+Cuádriceps",
            "img_movimiento": "https://via.placeholder.com/400x200.png?text=Movimiento:+Extensión"
        }
    ]
}

# Configuración de la interfaz de la aplicación
st.set_page_config(page_title="Entrenador de Gimnasio", layout="centered")

st.title("🏋️‍♂️ Asistente de Entrenamiento en Gimnasio")
st.write("Selecciona el grupo muscular que deseas trabajar hoy para ver las máquinas recomendadas, los músculos implicados y la ejecución del movimiento.")

# Selector de grupo muscular
grupos_musculares = list(rutinas.keys())
seleccion = st.selectbox("¿Qué grupo muscular quieres entrenar?", ["Selecciona una opción..."] + grupos_musculares)

# Lógica para mostrar la información
if seleccion != "Selecciona una opción...":
    st.header(f"Rutina para: {seleccion}")
    st.divider()
    
    ejercicios = rutinas[seleccion]
    
    for ejercicio in ejercicios:
        st.subheader(f"✅ Máquina: {ejercicio['maquina']}")
        
        # Crear dos columnas para mostrar las imágenes lado a lado
        col1, col2 = st.columns(2)
        
        with col1:
            st.write("**Músculo Objetivo**")
            st.image(ejercicio["img_musculo"], use_container_width=True)
            
        with col2:
            st.write("**Ejecución del Movimiento**")
            # Lo ideal para el movimiento es usar URLs terminadas en .gif
            st.image(ejercicio["img_movimiento"], use_container_width=True)
            
        st.info(f"**Cómo hacerlo:** {ejercicio['descripcion_movimiento']}")
        st.divider()