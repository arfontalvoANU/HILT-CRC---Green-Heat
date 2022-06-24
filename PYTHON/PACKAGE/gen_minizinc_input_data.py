# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 10:28:44 2022 @author: Ahmad Mojiri
Modified on 18 Jun 2022 by Ye Wang for Green Heat models
"""
from projdirs import optdir
import numpy as np
import platform


class GenDZN:
    
    def __init__(self, model_name, simparams, casedir=None):
        
        if model_name=='pv_wind_battery_heat':
            textinput=self.data_pv_wind_battery_heat(**simparams)
        elif model_name=='pv_wind_TES_heat':
            textinput=self.data_pv_wind_TES_heat(**simparams)
        elif model_name=='pv_battery_heat':
            textinput=self.data_pv_battery_heat(**simparams)            
        elif model_name=='CST_TES_heat':
            textinput=self.data_CST_TES_heat(**simparams)  
                   
        

        if casedir==None:
            self.dzn_fn=optdir +"%s_data.dzn"%model_name
        else:
            self.dzn_fn=casedir+"/%s_data.dzn"%model_name
        

        with open(self.dzn_fn, "w") as text_file:
            text_file.write(textinput)



    def data_pv_wind_battery_heat(self, DT, RM, t_storage, BAT_ETA_in, BAT_ETA_out, P_heater, ETA_heater, 
                      C_PV, C_Wind, C_BAT_energy, C_BAT_power, C_heater,
                      PV_ref_capa, PV_ref_out, Wind_ref_capa, Wind_ref_out, L, r_pv=None):

        textinput="""
N = %i;

DT = %.2f;      %% time difference between sample points (s)

RM = %.1f;  %% renewable multiple
t_storage = %.1f;   %% storage hour (h)

BAT_ETA_in = %.2f;   %%charging efficiency of electrochemical battery
BAT_ETA_out = %.2f;  %%discharging efficiency of electrochemical battery 

P_heater = %.1f;    %% design power of the heater (kW)
ETA_heater = %.4f;  %% efficiency of the heater

C_PV = %.4f;    %% unit cost of PV (USD/kW)
C_Wind =  %.4f;    %% unit cost of Wind farm (USD/kW)
C_BAT_energy = %.6f;   %% unit cost of electrochemical battery energy (USD/kWh)
C_BAT_power = %.6f;   %% unit cost of electrochemical battery power (USD/kW)
C_heater = %.6f;   %% unit cost of heater (USD/kW)

pv_ref_capa = %.4f;       %%the capacity of the reference PV plant (kW)

%% Power output time series from reference PV plant (kW)
pv_ref_out = %s;                                  
 
wind_ref_capa = %.4f;  %% the capacity of the refernce wind plant (kW)

%% power output time series from the reference wind plant (kW)
wind_ref_out = %s;  

%% load timeseries                          
L = %s;                              
"""%(len(L), DT, RM, t_storage, BAT_ETA_in, BAT_ETA_out,
        P_heater, ETA_heater,
        C_PV, C_Wind, C_BAT_energy, C_BAT_power, C_heater,
        PV_ref_capa, str(PV_ref_out), Wind_ref_capa,
        str(Wind_ref_out), str(L)) 

        if r_pv!=None:
            textinput+='\nr_pv=%s;'%r_pv
        
        return textinput

   

    def data_pv_battery_heat(self, DT, RM, t_storage, BAT_ETA_in, BAT_ETA_out, P_heater, ETA_heater, 
                      C_PV, C_BAT_energy, C_BAT_power, C_heater,
                      PV_ref_capa, PV_ref_out, L):


        textinput="""
N = %i;

DT = %.2f;      %% time difference between sample points (h)

RM = %.1f;  %% renewable multiple
t_storage = %.1f;   %% storage hour (h)

BAT_ETA_in = %.2f;   %%charging efficiency of electrochemical battery
BAT_ETA_out = %.2f;  %%discharging efficiency of electrochemical battery 

P_heater = %.1f;    %% design power of the heater (kW)
ETA_heater = %.4f;  %% efficiency of the heater

C_PV = %.4f;    %% unit cost of PV (USD/kW)
C_BAT_energy = %.6f;   %% unit cost of electrochemical battery energy (USD/kWh)
C_BAT_power = %.6f;   %% unit cost of electrochemical battery power (USD/kW)
C_heater = %.6f;   %% unit cost of heater (USD/kW)

pv_ref_capa = %.4f;       %%the capacity of the reference PV plant (kW)

%% Power output time series from reference PV plant (kW)
pv_ref_out = %s;                                  
 
%% load timeseries                          
L = %s;                              
"""%(len(L), DT, RM, t_storage, BAT_ETA_in, BAT_ETA_out,
        P_heater, ETA_heater,
        C_PV, C_BAT_energy, C_BAT_power, C_heater,
        PV_ref_capa, str(PV_ref_out), str(L)) 


        return textinput

  

    def data_pv_wind_TES_heat(self, DT, RM, t_storage, eta_TES_in, eta_TES_out, P_heater, eta_heater, 
                      c_PV, c_Wind, c_TES, c_heater,
                      PV_ref_capa, PV_ref_out, Wind_ref_capa, Wind_ref_out, L, r_pv=None):

        textinput="""
N = %i;

DT = %.2f;      %% time difference between sample points (s)

RM = %.1f;  %% renewable multiple
t_storage = %.1f;   %% storage hour (h)

eta_TES_in = %.2f;   %%charging efficiency of electrochemical battery
eta_TES_out = %.2f;  %%discharging efficiency of electrochemical battery 

P_heater = %.1f;    %% design power of the heater (kW)
eta_heater = %.4f;  %% efficiency of the heater

c_PV = %.4f;    %% unit cost of PV (USD/kW)
c_Wind =  %.4f;    %% unit cost of Wind farm (USD/kW)
c_TES = %.6f;   %% unit cost of TES (USD/kWh)
c_heater = %.6f;   %% unit cost of heater (USD/kW)

pv_ref_capa = %.4f;       %%the capacity of the reference PV plant (kW)

%% Power output time series from reference PV plant (kW)
pv_ref_out = %s;                                  
 
wind_ref_capa = %.4f;  %% the capacity of the refernce wind plant (kW)

%% power output time series from the reference wind plant (kW)
wind_ref_out = %s;  

%% load timeseries                          
L = %s;                              
"""%(len(L), DT, RM, t_storage, eta_TES_in, eta_TES_out,
        P_heater, eta_heater,
        c_PV, c_Wind, c_TES, c_heater,
        PV_ref_capa, str(PV_ref_out), Wind_ref_capa,
        str(Wind_ref_out), str(L)) 

        if r_pv!=None:
            textinput+='\nr_pv=%s;'%r_pv
        
        return textinput 


    def data_CST_TES_heat(self, DT, t_storage, eta_TES_in, eta_TES_out, P_recv_out, L):

        textinput="""
N = %i;
DT = %.2f;      %% time difference between sample points (s)
t_storage = %.1f;   %% storage hour (h)
eta_TES_in = %.2f;   %%charging efficiency of electrochemical battery
eta_TES_out = %.2f;  %%discharging efficiency of electrochemical battery 

%% Power output time series from the receiver (kW)
P_recv_out = %s;                                  

%% load timeseries                          
L = %s;                              
"""%(len(L), DT, t_storage, eta_TES_in, eta_TES_out,
        str(P_recv_out), str(L)) 


        return textinput 