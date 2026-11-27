%% BLE Link Layer Using Stateflow
% This script creates a BLE link layer object bleLinkLayer and simulates 10
% seconds of mesh communications over an advertising bearer using Generic
% Access Profile (GAP). The link layer object relies on the standalone
% chart sf_bluetooth.sfx for control logic and on the link layer queue
% object bleQueue for storing data from the advertising bearer.

% Do not run unless if Communications Toolbox license exists
if ~license('test','communication_toolbox')
    error('This example requires Communications Toolbox.');
end

% Simulation parameters
simulationTime = 10000; % In milliseconds
stepTime = 1; % In milliseconds

% Create a link layer object with default configuration
llObj = bleLinkLayer();

% Create link layer state machine using standalone Stateflow chart
llStateMachine = sf_bluetooth('-animationDelay',0);

% Configure advertising and scan intervals, in multiples of 5 milliseconds
llStateMachine.AdvertisingInterval = 4; % 20 milliseconds
llStateMachine.ScanInterval = 10; % 50 milliseconds
llObj.LLStateMachine = llStateMachine;
llObj.init();

% The simulation consists of 10,000 time steps. Each time step represents
% an execution of the link layer object (which corresponds to 1 millisecond
% of simulation time) and typically consists of these steps:
%
% 1. If the link layer queue is not empty, read a data packet. The data in
% the queue represents the advertising data packets that the link layer
% obtains from the host layer.
%
% 2. Set the value of the chart data TxData and execute the standalone
% chart. In this step, the chart determines whether the device acts as an
% advertiser or scanner.
%
% 3. If the chart is in the Advertising.Transmit state, generate a BLE link
% layer advertising channel protocol data unit (PDU) using the data read
% from the link layer queue. The PDU represents a transmission by the PHY
% layer.

for i = 1:stepTime:simulationTime   

    llPDU = [];
    
% Every 1000 time steps, push data into the link layer queue before
% executing the link layer object. This data represents the advertising
% data packets that the link layer obtains from the host layer.
    
    if ~mod(i,1000)
        seq = randi([1 100], 1, 1);
        networkPDU = [104;25;0;0;seq;0;1;0;3;1;2;3;4;5;6];
        llObj.pushGAPData(networkPDU);
    end
    
% Every 2500 time steps, generate a BLE link layer advertising channel PDU
% that represents the advertising data packets received by the PHY layer.
% If the chart is in the Scanning state, the link layer object attempts to
% decode the PDU and, if the decoding is successful, passes the PDU to the
% host layer.
    
    if ~mod(i,2500)
        cfg = bleLLAdvertisingChannelPDUConfig;
        seq = 100 + randi([1 100], 1, 1);
        networkPDU = [104;25;0;0;seq;0;1;0;3;1;2;3;4;5;6];
        gapData = [16;42;networkPDU];
        cfg.PDUType = 'Advertising non connectable indication';
        cfg.AdvertisingData = gapData;
        llPDU = bleLLAdvertisingChannelPDU(cfg);
    end
    
% Execute link layer object.

    [channelIndex, txPDU] = llObj.run(llPDU);
end

% When the simulation is complete, print a summary that lists the number of
% data PDUs and bytes transmitted and received by the link layer.

fprintf('Number of PDUs transmitted from link layer: %d\n', llObj.TransmittedPDUs);
fprintf('Number of bytes transmitted from link layer: %d\n', llObj.BytesTransmitted);
fprintf('Number of PDUs received at link layer: %d\n', llObj.ReceivedPDUs);
fprintf('Number of bytes received at link layer: %d\n', llObj.BytesReceived);

% Delete chart object to clear animation
delete(llObj.LLStateMachine);
delete(llObj);