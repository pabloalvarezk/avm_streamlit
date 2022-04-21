import SIBIF_output_Journal_Z_Scores as SIBIF
import scipy.io as sio

def get_gvv(data,Q1,Q2,Q3,gain):    
    ######### abrir archivo .wav ############
    dataACC = data[:, 1]
    ######## Parametros Q ############
    mat_contents = sio.loadmat("Weibel_IF_IBIF_GUI.mat")
    indexPos = 8
    indexLen = 5
    Hsub1 = mat_contents["Hsub1_cell"][indexLen - 1, indexPos - 1][0]
    Zsub2 = mat_contents["Zsub2_cell"][indexLen - 1, indexPos - 1][0]
    fWeibel = mat_contents["fWeibel"][0]
    ########### IBIF ###########
    gvv_acc = SIBIF.SIBIF_output_Journal_Z_Scores(
        Q1, Q2, Q3, gain, dataACC / 32767, fWeibel, Hsub1, Zsub2
    )
    gvv_acc2 = gvv_acc[0:-1]

    return gvv_acc2