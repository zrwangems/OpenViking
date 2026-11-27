/* This is the header function included with Simulink to allow the Simulink
    model to call the SOC estimation C code*/

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
extern double estimateSOC(double V, double I, double T);

/*helper functions*/
extern double batteryResistance(double T);
extern double voltage_EMF(double V, double I, double r_int);
extern double calculateSOC(double V, double T);

