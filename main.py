import matplotlib
import streamlit as st
import pandas as pd 
import numpy as np

from scipy.io import wavfile
import scipy.io as sio
import graph
import proccess

#FFT
from scipy.fft import fft, fftfreq

import matplotlib.pyplot as plt

example = False
st.set_page_config(layout="wide")

with st.sidebar:
    uploaded_file = st.file_uploader("Escoga un archivo de AVM", 
        type=['wav'], accept_multiple_files=False,
        help="Solo se aceptan archivos provenientes del dispositivo AVM")
    
    with st.form("Set data"):
        
        example_form=st.checkbox('Usar Archivo Ejemplo',value=False)
        #values_form = st.slider("Select a range of values", a, b, (a, b))
        st.write("Datos paciente")
        NOMBRE_form = st.text_input("NOMBRE", value='N/N')
        RUT_form = st.text_input("RUT", value='N/N')
        EDAD_form = st.text_input("EDAD", value='0')
        st.write("Ingrese los parametros IBIF")
        Q1_form = float(st.text_input("Q1", value='1.0'))
        Q2_form = float(st.text_input("Q2", value='1.0'))
        Q3_form = float(st.text_input("Q3", value='1.0'))
        gain_form = float(st.text_input("Gain", value='1.0'))
    # Every form must have a submit button.
        submitted = st.form_submit_button("Procesar examen")
        if submitted:
            example = example_form
            NOMBRE = NOMBRE_form
            RUT = RUT_form
            EDAD = EDAD_form
            Q1=Q1_form
            Q2=Q2_form
            Q3=Q3_form
            gain=gain_form
            

if (uploaded_file is not None or example) and submitted:
    if example:
        [sr,data] = wavfile.read("testfile.wav")#uploaded_file)
    else:
        [sr,data] = wavfile.read(uploaded_file)
        
    st.title('EXAMEN AVM')

    col1, col2, col3 = st.columns(3)
    with col1:
        st.write(' Ficha personal')
        st.write(' Paciente:',NOMBRE)    
        st.write(' RUT: ',RUT)
        st.write(' Edad:',EDAD)
                

    with col2:
        st.write(' Parámetros IBIF')
        st.write(' Q1:',Q1)    
        st.write(' Q2: ',Q2)
        st.write(' Q3:',Q3)
        st.write(' GAIN:',gain)

    with col3:
        st.write(' Paciente:',NOMBRE)    
        st.write(' RUT: ',RUT)
        st.write(' Edad:',EDAD)

    fig = graph.graph_temp(data)
    st.pyplot(fig)
         
    gvv=proccess.get_gvv(data,Q1,Q2,Q3,gain)
    fig2=graph.graf_gvv(gvv)
    fig3=graph.graf_fft(data[:,1])
    st.pyplot(fig2)
    st.pyplot(fig3)


else:
    st.title("Seleccione un archivo para procesar")


