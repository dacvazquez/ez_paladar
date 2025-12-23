import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Calculadora de Ventas",
    layout="wide"
)

# -----------------------------
# CSS OPTIMIZADO PARA MÓVIL
# -----------------------------
st.markdown("""
<style>
/* Texto general */
html, body, [class*="css"]  {
    font-size: 18px;
}

/* Inputs */
input {
    height: 3rem !important;
    font-size: 1.1rem !important;
}

/* Botones */
button {
    height: 3.2rem !important;
    font-size: 1.2rem !important;
}

/* Botones de cantidad */
.qty-btn {
    width: 100%;
    font-size: 1.6rem !important;
}

/* Cantidad */
.qty-display {
    text-align: center;
    font-size: 2rem;
    font-weight: bold;
}

/* Subtotal */
.subtotal {
    font-size: 1.1rem;
    font-weight: 500;
}

/* Botón eliminar */
.delete-btn button {
    background-color: #ff4b4b;
    color: white;
}
</style>
""", unsafe_allow_html=True)

st.title("Calculadora de Ventas")

# -----------------------------
# Estado
# -----------------------------
if "productos" not in st.session_state:
    st.session_state.productos = [
        {"nombre": "Producto 1", "precio": 0, "cantidad": 0}
    ]

# -----------------------------
# Funciones
# -----------------------------
def agregar_producto():
    st.session_state.productos.append(
        {"nombre": f"Producto {len(st.session_state.productos)+1}", "precio": 0.0, "cantidad": 0}
    )

def aumentar(idx):
    st.session_state.productos[idx]["cantidad"] += 1

def disminuir(idx):
    if st.session_state.productos[idx]["cantidad"] > 0:
        st.session_state.productos[idx]["cantidad"] -= 1

def eliminar(idx):
    st.session_state.productos.pop(idx)

# -----------------------------
# Render
# -----------------------------
total = 0.0

for i, p in enumerate(st.session_state.productos):
    with st.container(border=True):
        p["nombre"] = st.text_input(
            "Producto",
            value=p["nombre"],
            key=f"nombre_{i}"
        )

        p["precio"] = st.number_input(
            "Precio",
            min_value=0.0,
            step=1.0,
            value=p["precio"],
            key=f"precio_{i}"
        )

        col_menos, col_qty, col_mas, col_del = st.columns([1, 2, 1, 1])

        with col_menos:
            st.button("➖", key=f"menos_{i}", on_click=disminuir, args=(i,), use_container_width=True)

        with col_qty:
            st.markdown(
                f"<div class='qty-display'>{p['cantidad']}</div>",
                unsafe_allow_html=True
            )

        with col_mas:
            st.button("➕", key=f"mas_{i}", on_click=aumentar, args=(i,), use_container_width=True)

        with col_del:
            st.button("🗑️", key=f"del_{i}", on_click=eliminar, args=(i,), use_container_width=True)

        subtotal = p["precio"] * p["cantidad"]
        total += subtotal

        st.markdown(
            f"<div class='subtotal'>Subtotal: ${subtotal:,.2f}</div>",
            unsafe_allow_html=True
        )

# -----------------------------
# Acciones finales
# -----------------------------
st.divider()

st.button("➕ Agregar producto", on_click=agregar_producto, use_container_width=True)

if st.session_state.productos:
    df = pd.DataFrame(st.session_state.productos)
    df["subtotal"] = df["precio"] * df["cantidad"]

    st.download_button(
        "💾 Guardar ventas (CSV)",
        data=df.to_csv(index=False),
        file_name="ventas.csv",
        mime="text/csv",
        use_container_width=True
    )

# -----------------------------
# Total
# -----------------------------
st.divider()
st.subheader("Total a cobrar")
st.markdown(f"## 💰 ${total:,.2f}")
