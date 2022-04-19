import matplotlib
import streamlit as st
import pandas as pd 
import numpy as np

from scipy.io import wavfile
import scipy.io as sio

#FFT
from scipy.fft import fft, fftfreq

import matplotlib.pyplot as plt

st.set_page_config(layout="wide")

with st.sidebar:
    uploaded_file = st.file_uploader("Escoga un archivo de AVM", 
        type=['wav'], accept_multiple_files=False,
        help="Solo se aceptan archivos provenientes del dispositivo AVM")
    
    with st.form("Set parameters"):
        
        #values_form = st.slider("Select a range of values", a, b, (a, b))
        st.write("Datos paciente")
        NOMBRE_form = st.text_input("NOMBRE", value='N/N')
        RUT_form = st.text_input("RUT", value='N/N')
        EDAD_form = st.text_input("EDAD", value='0')
        
    # Every form must have a submit button.
        submitted = st.form_submit_button("Procesar examen")
        if submitted:
            NOMBRE = NOMBRE_form
            RUT = RUT_form
            EDAD = EDAD_form
            

if uploaded_file is not None and submitted:
    [sr,stereo_data] = wavfile.read(uploaded_file)
    st.write(stereo_data)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.write(' Paciente:',NOMBRE)    
        st.write(' RUT: ',RUT)
        st.write(' Edad:',EDAD)

    with col2:
        st.write(' Paciente:',NOMBRE)    
        st.write(' RUT: ',RUT)
        st.write(' Edad:',EDAD)

    with col3:
        st.write(' Paciente:',NOMBRE)    
        st.write(' RUT: ',RUT)
        st.write(' Edad:',EDAD)

else:
    st.write("Seleccione un archivo para procesar")


