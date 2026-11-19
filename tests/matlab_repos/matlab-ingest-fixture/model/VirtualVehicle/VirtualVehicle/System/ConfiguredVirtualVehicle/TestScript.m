mdl = 'ConfiguredHevMmVirtualVehicle';
open_system(mdl);

%%

%Test 1 
in(1) = Simulink.SimulationInput(mdl); 
in(1) = setParamforManeuverAndDriver('ConfiguredHevMmVirtualVehicle','Drive Cycle', 'FTP75', 'Longitudinal Driver',1, in(1), 'ConfiguredVirtualVehicle',1);
simout = sim(in, 'ShowSimulationManager', 'on');
save('simout.mat','simout');
