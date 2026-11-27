/* This is the C source file called by the "Battery State Estimator" chart
    It includes an algorithm which estimates Battery State of Charge (SOC)
    from measurements of battery voltage temperature and current */

#include "estimateSOC.h"
#include <math.h>

/*
 * Function:  estimateSOC 
 * --------------------
 * A simple stateless estimate of battery state of charge based on 
 * parameter fit eqations.  
 *
 *  V: battery voltage in Volts
 *  I: battery current in Amps
 *  T: battery tempetayure in degC
 *
 *  returns: a stateless estimate of battery SOC
 */
double estimateSOC(double V, double I, double T)
{
    double SOC;
    double r_int;
    double V_emf;
    
    r_int = batteryResistance(T); /*internal resistance calculation*/
    
    V_emf = voltage_EMF(V,I,r_int); /*open circuit voltage calculation*/
    
    SOC = calculateSOC(V_emf,T);
    
    return SOC;
}

/*Helper function to calculate change in battery resistance due to 
 * temperature*/
double batteryResistance(double T){
    double r; /* battery resistance [ohms]*/
    double r_nom = 0.1; /*nominal battery resistance [ohms]*/
    double T_nom = 25; /*nominal battery temperature [degC]*/
    double LR = -0.004; /*constant [ohms/degC]*/
    
    r = r_nom *(1+LR*(T-T_nom)); //[ohms] temperature affect on resistance
    
    return r;
}

/*Helper function to calculate open circuit battery voltage*/
double voltage_EMF(double V, double I, double r_int) {
    double V_r = I * r_int; /*volage drop from internal resistance [volts]*/
    double V_emf = V - V_r; /*open circuit voltage of battery [volts]*/
    return V_emf;
}

/*Helper function to estimate SOC*/
double calculateSOC(double V, double T) {
    double SOC; /*SOC estimate*/
    double V0T; //volts
    double Vnom = 300; //[volts]
    double Tnom = 25; //[degC]
    double beta = 0.722; // constant
    double LV = 0.004; //[volts/degC]
    
    V0T = Vnom*(1+LV*(T-Tnom)); //[volts] temperature affect on nominaml voltage
    SOC = (V - beta*V)/(V0T - beta*V); // SOC at voltage and temp
    
    return SOC;
    
}


    