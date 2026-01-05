import streamlit as st
import json
import ast
from operacoes import Operacoes

st.set_page_config(page_title="RPC", layout="centered")

@st.cache_resource
def get_op():
    try:
        with open("settings.json") as f:
            settings = json.load(f)
            return Operacoes(**settings)
    except Exception:
        return None

op = get_op()

if 'display' not in st.session_state:
    st.session_state.display = ""

def update_display(char):
    if st.session_state.display == "Erro":
        st.session_state.display = ""
    st.session_state.display += str(char)

def clear_display():
    st.session_state.display = ""

def calculate():
    expr = st.session_state.display
    if not expr:
        return

    try:
        if "+" in expr:
            p = expr.split("+")
            res = op.soma(int(p[0]), int(p[1]), 0) 
        elif "-" in expr:
            p = expr.split("-")
            res = op.subtracao(int(p[0]), int(p[1]))
        elif "*" in expr:
            p = expr.split("*")
            res = op.multiplicacao(int(p[0]), int(p[1]))
        elif "/" in expr:
            p = expr.split("/")
            res = op.divisao(float(p[0]), float(p[1]))
        elif "!" in expr:
            val = expr.replace("!", "")
            res = op.fatorial(int(val))
        else:
            res = expr # Se não houver operador, mantém o número
            
        st.session_state.display = str(res)
    except Exception as e:
        st.error(f"Erro na operação RPC: {e}")
        st.session_state.display = "Erro"


st.title("Teste RPC")
tab1, tab2, tab3, tab4 = st.tabs(["Calculadora", "Primos", "Notícias UOL", "Resolver com IA"])

# Aba da calculadora
with tab1:
    
    st.markdown(f"""
        <div style="background-color: #f0f2f6; padding: 20px; border-radius: 10px; border: 2px solid #eaeaeb; margin-bottom: 20px; text-align: right;">
            <span style="font-family: 'Courier New', monospace; font-size: 30px; color: #000;">
                {st.session_state.display if st.session_state.display != "" else "0"}
            </span>
        </div>
    """, unsafe_allow_html=True)

    c1, c2, c3, c4 = st.columns(4)
    c1.button("7", on_click=update_display, args=("7",), use_container_width=True)
    c2.button("8", on_click=update_display, args=("8",), use_container_width=True)
    c3.button("9", on_click=update_display, args=("9",), use_container_width=True)
    c4.button("➗", on_click=update_display, args=("/",), use_container_width=True)

    c1, c2, c3, c4 = st.columns(4)
    c1.button("4", on_click=update_display, args=("4",), use_container_width=True)
    c2.button("5", on_click=update_display, args=("5",), use_container_width=True)
    c3.button("6", on_click=update_display, args=("6",), use_container_width=True)
    c4.button("✖️", on_click=update_display, args=("*",), use_container_width=True)

    c1, c2, c3, c4 = st.columns(4)
    c1.button("1", on_click=update_display, args=("1",), use_container_width=True)
    c2.button("2", on_click=update_display, args=("2",), use_container_width=True)
    c3.button("3", on_click=update_display, args=("3",), use_container_width=True)
    c4.button("➖", on_click=update_display, args=("-",), use_container_width=True)

    c1, c2, c3, c4 = st.columns(4)
    c1.button("C", on_click=clear_display, use_container_width=True, type="primary")
    c2.button("0", on_click=update_display, args=("0",), use_container_width=True)
    c3.button("!", on_click=update_display, args=("!",), use_container_width=True)
    c4.button("➕", on_click=update_display, args=("+",), use_container_width=True)

    st.button("🟰", on_click=calculate, use_container_width=True, type="secondary")

# Aba números primos
with tab2:

    st.header("Verificar Números Primos")
    txt_input = st.text_area("Insira números separados por espaço ou vírgula:", "10, 11, 13, 20")

    if st.button("Verificar", type="primary"):
        
        raw = txt_input.replace(",", " ")
        numeros = [int(x) for x in raw.split() if x.strip().isdigit()]

        if numeros:
            
            with st.spinner("Carregando..."):
                result = op.primes(*numeros)
            
            lista = ast.literal_eval(result)

            for index in range(0, len(lista)):
                if lista[index]:
                    st.success(f"✅ {numeros[index]} é primo")
                else:
                    st.error(f"❌ {numeros[index]} não é primo")

        else:
            st.warning("Insira números válidos.")


# Aba de notícias dea UOL
with tab3:

    st.header("Últimas Notícias UOL")

    if st.button("Buscar Notícias"):
        with st.spinner("Carregando..."):
            try:
                result = op.uolNews()
                news = ast.literal_eval(result)

                for n in news:
                    st.info(n)

            except Exception:
                st.error("Erro ao buscar notícias")


# Aba do chat com ia
with tab4:

    st.header("Math Solver com IA")
    prompt = st.chat_input("Pergunte um problema matemático")
    
    if prompt:

        with st.chat_message("user"):
            st.write(prompt)
            
        with st.chat_message("assistant"):
            with st.spinner("Pensando..."):

                result = op.mathSolverAi(prompt)

                try:
                    response = json.loads(result)

                    if response["is_math_problem"] == True:
                        st.write(f"Resultado: {response['result']}")
                    else:
                        st.warning("Não é uma operação matemática possível de se resolver numericamente!")
                
                except Exception:
                    st.error(f"Ocorreu um erro interno no servidor.")