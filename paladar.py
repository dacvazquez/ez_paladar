import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Calculadora de Ventas",
    layout="centered"
)

st.title("Calculadora de Ventas")

# -----------------------------
# Estado inicial
# -----------------------------
if "productos" not in st.session_state:
    st.session_state.productos = [
        {"nombre": "Producto 1", "precio": 0.0, "cantidad": 0}
    ]

# -----------------------------
# Funciones
# -----------------------------
def agregar_producto():
    n = len(st.session_state.productos) + 1
    st.session_state.productos.append(
        {"nombre": f"Producto {n}", "precio": 0.0, "cantidad": 0}
    )

def aumentar_cantidad(idx):
    st.session_state.productos[idx]["cantidad"] += 1

def disminuir_cantidad(idx):
    if st.session_state.productos[idx]["cantidad"] > 0:
        st.session_state.productos[idx]["cantidad"] -= 1

def eliminar_producto(idx):
    st.session_state.productos.pop(idx)

# -----------------------------
# Renderizado
# -----------------------------
total_general = 0.0

for idx, producto in enumerate(st.session_state.productos):
    with st.container(border=True):
        col1, col2, col3, col4 = st.columns([3, 2, 3, 1])

        with col1:
            producto["nombre"] = st.text_input(
                "Producto",
                value=producto["nombre"],
                key=f"nombre_{idx}"
            )

        with col2:
            producto["precio"] = st.number_input(
                "Precio",
                min_value=0.0,
                step=0.01,
                value=producto["precio"],
                key=f"precio_{idx}"
            )

        with col3:
            st.write("Cantidad")
            c1, c2, c3 = st.columns([1, 2, 1])

            with c1:
                st.button(
                    "➖",
                    key=f"menos_{idx}",
                    on_click=disminuir_cantidad,
                    args=(idx,),
                    help="Disminuir cantidad"
                )

            with c2:
                st.markdown(
                    f"<h3 style='text-align:center'>{producto['cantidad']}</h3>",
                    unsafe_allow_html=True
                )

            with c3:
                st.button(
                    "➕",
                    key=f"mas_{idx}",
                    on_click=aumentar_cantidad,
                    args=(idx,),
                    help="Aumentar cantidad"
                )

        with col4:
            st.write(" ")
            st.button(
                "🗑️",
                key=f"eliminar_{idx}",
                on_click=eliminar_producto,
                args=(idx,),
                help="Eliminar producto"
            )

        subtotal = producto["precio"] * producto["cantidad"]
        total_general += subtotal

        st.caption(f"Subtotal: ${subtotal:,.2f}")

# -----------------------------
# Acciones generales
# -----------------------------
st.divider()

col_a, col_b = st.columns(2)

with col_a:
    st.button("➕ Agregar producto", on_click=agregar_producto)

with col_b:
    if st.session_state.productos:
        df = pd.DataFrame(st.session_state.productos)
        df["subtotal"] = df["precio"] * df["cantidad"]

        st.download_button(
            label="💾 Guardar resultados (CSV)",
            data=df.to_csv(index=False),
            file_name="ventas.csv",
            mime="text/csv"
        )

# -----------------------------
# Total
# -----------------------------
st.divider()
st.subheader("Total General")
st.markdown(f"## ${total_general:,.2f}")
