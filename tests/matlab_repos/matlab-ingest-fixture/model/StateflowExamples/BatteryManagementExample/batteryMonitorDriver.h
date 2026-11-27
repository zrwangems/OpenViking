/* This is the header file we would include with the model generated code
 * so that the the model code can automatically communicate with our 
 * "Battery Monitor" hardware to get sensor readings from the battery 
 * "The Sensor Reading with Fault Detection" Stateflow Chart calls these 
 * functions*/

/*
 * Function:  readVoltage
 * --------------------
 *  requests a battery voltage reading from the battery monitor.
 *  If request times out then returns error code: -99999
 *
 *  returns: the battery voltage in mV
 */
extern int readVoltage(void);

/*
 * Function:  readCurrent 
 * --------------------
 *  requests a temperature reading from the battery monitor.
 *  If request times out then returns error code: -99999
 *
 *  returns: the battery temperature in mA
 */
extern int readCurrent(void);

/*
 * Function:  readTemperature 
 * --------------------
 *  requests a battery temperature reading from the battery monitor.
 *  If request times out then returns error code: -99999
 *
 *  returns: the battery temperature in degC*1000
 */
extern int readTemperature(void);