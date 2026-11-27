classdef bleLinkLayer < handle
%bleLinkLayer Create an object for BLE link layer (LL) functionality
%supporting mesh communication over advertising bearer using Generic Access
%Profile (GAP).
%
%   MESHLL = bleLinkLayer creates a BLE LL object supporting mesh
%   communication over advertising bearer. This object supports Broadcaster
%   (switches between standby and advertising states) and Observer
%   (switches between standby and scanning states) roles. This object uses
%   LL state machine implemented as a standalone Stateflow chart.
%
%   MESHLL = bleLinkLayer(Name, Value) creates a BLE LL object with the
%   specified property Name set to the specified Value. You can specify
%   additional name-value pair arguments in any order as (Name1, Value1,
%   ..., NameN, ValueN).

%   Copyright 2020 The MathWorks, Inc.

properties
    %LLStateMachine Link layer state machine
    %   Specify LLStateMachine as standalone state flow chart. This
    %   property models BLE LL state machine. The default value is a state
    %   chart of type 'sf_bluetooth' with all properties set to their
    %   default values.
    LLStateMachine
end
    
properties (Access = private)
    %pQueue Queue for storing PDUs from upper layers
    pQueue
    
    %pGAPDataRx Received GAP data block while scanning
    pGAPDataRx = zeros(1, 0)
    
    %pGAPDataTx GAP data block to be transmitted while advertising
    pGAPDataTx = zeros(1, 0)
end
    
properties (SetAccess = private)
    %TransmittedPDUs Number of PDUs transmitted
    TransmittedPDUs = 0
    
    %BytesTransmitted Number of bytes transmitted
    BytesTransmitted = 0
    
    %ReceivedPDUs Number of PDUs received
    ReceivedPDUs = 0
    
    %BytesReceived Number of bytes received
    BytesReceived = 0
    
    %CRCFailedPDUs Number of PDUs received with CRC failures
    CRCFailedPDUs = 0
end
    
methods
    % Constructor
    function obj = bleLinkLayer(varargin)
        % Name-value pairs
        for idx = 1:2:nargin
            obj.(varargin{idx}) = varargin{idx+1};
        end
        maxQueueSize = 50; % Maximum size of link layer queue is 50
        maxPDUSize = 33; % Maximum payload size at link layer is 33
        obj.pQueue = bleQueue(maxQueueSize, maxPDUSize);
    end
    
    function set.LLStateMachine(obj, value)
        validateattributes(value, {'sf_bluetooth'}, {'scalar'}, ...
            mfilename, 'LLStateMachine');
        obj.LLStateMachine = value;
    end
    
    function flag = pushGAPData(obj, gapData)
        %pushGAPData Push GAP data block into link layer queue
        %
        %   FLAG = pushGAPData(OBJ, GAPDATA)
        %
        %   FLAG indicates status of enqueue whether success or failure.
        %
        %   GAPDATA is a column vector of decimal octets.
        
        % Validate GAP data block
        validateattributes(gapData, {'numeric'}, {'column', 'integer', ...
            'nonnegative', '<=', 255}, mfilename, 'gapData');
        % Push GAP data block into queue
        flag = obj.pQueue.enqueue(gapData);
    end
    
    function init(obj)
        %init Initialize link layer intervals
        
        % Scan interval in milliseconds
        obj.LLStateMachine.ScanInterval = obj.LLStateMachine.ScanInterval * 5;
        % Advertising interval (with added random delay) in milliseconds
        obj.LLStateMachine.AdvertisingInterval = obj.LLStateMachine.AdvertisingInterval * 5 + ...
            randi([1 10]);
    end
    
    function [channelIndex, output] = run(obj, input)
        %run Runs link layer state machine
        %
        %   This function performs the following operations: 1. Maintain
        %   link layer state machine supporting Broadcaster and
        %      Observer roles
        %   2. Transmit and decode advertising packets
        %
        %   [CHANNELINDEX, OUTPUT] = run(OBJ, INPUT) performs link layer
        %   actions.
        %
        %   OUTPUT is the link layer protocol data unit (PDU) appended with
        %   cyclic redundancy check (CRC) in binary format.
        %
        %   CHANNELINDEX is an integer indication channel on which the
        %   advertising packet is to be transmitted.
        %
        %   INPUT is the link layer protocol data unit (PDU) appended with
        %   cyclic redundancy check (CRC) in binary format.
        
        % Initialize
        output = zeros(1, 0);
        channelIndex = -1;
        
        % Fetch data from the queue for transmission
        if ~isEmpty(obj.pQueue) && isempty(obj.pGAPDataTx)
            [~, obj.pGAPDataTx] = dequeue(obj.pQueue);
        end
        
        % If data available for transmission set TxData flag as true
        if ~isempty(obj.pGAPDataTx)
            obj.LLStateMachine.TxData = true;
        else
            obj.LLStateMachine.TxData = false;
        end
        
        % Run LL state machine
        step(obj.LLStateMachine);
        
        % Tx
        if obj.LLStateMachine.TxOn
            % Get the channel index for transmitting the PDU
            channelIndex = obj.LLStateMachine.ChannelIndex;
            
            % Configure link layer non-connectable and non-scannable
            % advertising indication
            llCfg = bleLLAdvertisingChannelPDUConfig;
            llCfg.PDUType = 'Advertising non connectable indication';
            llCfg.AdvertisingData = obj.pGAPDataTx;
            
            % Generate an advertising channel PDU
            output = bleLLAdvertisingChannelPDU(llCfg);
            
            % Update the number of PDU transmissed
            obj.TransmittedPDUs = obj.TransmittedPDUs + 1;
            obj.BytesTransmitted = obj.BytesTransmitted + numel(output)/8;
        end
        
        % Rx
        if obj.LLStateMachine.RxOn
            % Process the input PDU
            if ~isempty(input)
                % Decode link layer PDU
                [status, llCfg] = bleLLAdvertisingChannelPDUDecode(input);
                % Received non-connectable non-scannable advertising
                % indication
                if strcmp(status, 'Success')
                    if strcmp(llCfg.PDUType, 'Advertising non connectable indication')
                        obj.pGAPDataRx = llCfg.AdvertisingData;
                    end
                    % Update number of PDUs received
                    obj.ReceivedPDUs = obj.ReceivedPDUs + 1;
                    obj.BytesReceived = obj.BytesReceived + numel(input)/8;
                else
                    % Received LL PDU with invalid CRC
                    if strcmp(status, 'CRCFailed')
                        obj.CRCFailedPDUs = obj.CRCFailedPDUs + 1;
                    end
                    obj.pGAPDataRx = zeros(1, 0);
                end
            end
        end
        
        % Reset GAP data
        if obj.LLStateMachine.TxData == false
            obj.pGAPDataTx = [];
        end
    end
end
end
