from ui import Ui, UiElement
import pandas as pd ### not in requirements file - need to add this
import matplotlib.pyplot as plt
import numpy as np

LGPS_list=['LPelTilt','LHipFlex','LKneeFlex','LAnkDors',
           'LPelObl','LHipAbd','LPelRot','LHipRot','LFootProg']
RGPS_list=['RPelTilt','RHipFlex','RKneeFlex','RAnkDors',
           'RPelObl','RHipAbd','RPelRot','RHipRot','RFootProg']

GPS_list=['LPelTilt','LHipFlex','LKneeFlex','LAnkDors',
           'LPelObl','LHipAbd','LPelRot','LHipRot','LFootProg',
           'RHipFlex','RKneeFlex','RAnkDors',
           'RHipAbd','RHipRot','RFootProg']


class State:
    patient = []
    control = [] 
    map_GPS = []
    ui=[]
        
def GPS(data):
    sq_sum=0
    for i in range(len(data)):
        sq_sum=sq_sum+ np.power((data[i]),2)
    return np.power(sq_sum/len(data),0.5)
    
def load_patient_file(path):
    # code to load data goes here
    pass

    
def load_control_file(path):
    # code to load data goes here
    pass

    
def calc_GPS():
    data=[]
    col=[]
    try:
        pass
        # your code to calculate GPS goes here.
        # for each angle in State.control.columns, and for 'L' and 'R' you need to calculate
        # rms of difference between each point for control subject and patient.
        # create a dataframe where columns are called side+ angle eg LHipFlex
        # the data for the dataframe will be the rms value for this parameter
        
        # add 3 more columns to the dataframe called LGPS, RGPS and GPS.
        # these are the rms values of the list of variables listed in LGPS_list above.
        
        # the code below sets the values of State.map_GPS and the text boxes
        
#        State.map_GPS=pd.DataFrame([data],columns=col)
    
#        State.ui.set_element(UiElement.OUT_GPS,"{:.2f}".format(State.map_GPS['GPS'][0]))
#        State.ui.set_element(UiElement.OUT_LGPS,"{:.2f}".format(State.map_GPS['LGPS'][0]))
#        State.ui.set_element(UiElement.OUT_RGPS,"{:.2f}".format(State.map_GPS['RGPS'][0]))
    except AttributeError:
        print('no data to perform calculation')

    
def show_graph(path):
    # path is the name of the angle from the drop down list
    fig,ax = plt.subplots()
    # your code to plot 3 line (patient left in red, patient right in green, control in blue)

    State.ui.plot(fig) # this will send the plot to the canvas
    
def radio_choice(choice):
    if choice == 1:
        print("you selected graph")
    if choice == 2:
        print("you selected GPS")
        try:
            pass
            # your code to plot bar chart of GPS_map goes here
            
            # this is how you actually plot it            
#            State.ui.plot(fig)
            
        except AttributeError:
            print('no data - can not show data')

if __name__ == '__main__':
    ui = Ui()
    State.ui=ui
    ui.add_select_callback(UiElement.SELECT_PATIENT, load_patient_file)
    ui.add_select_callback(UiElement.SELECT_CONTROL, load_control_file)
    ui.add_button_callback(UiElement.BUTTON_CALC, calc_GPS)
    
    ui.add_select_callback(UiElement.SELECT_GRAPH, show_graph)
    
    ui.add_radio_callback(UiElement.RADIO_PLOT, radio_choice)
    
    
    ui.mainloop()

