classdef bleQueue < handle
%bleQueue Queuing of packets in a Bluetooth node
%
%   QUEUE = bleQueue(MAXPACKETS, MAXPACKETSIZE) creates a queue
%   to buffer MAXPACKETS packets with each packet having size in the range
%   [1, MAXPACKETSIZE].
%
%   MAXPACKETS indicates the number of packets that can be queued,
%   specified as a scalar positive integer.
%
%   MAXPACKETSIZE is the maximum size of a packet in the queue, specified
%   as a scalar positive integer.
%
%   bleQueue methods:
%
%   enqueue  - Insert data into queue
%   dequeue  - Remove data from queue
%   isEmpty  - Check whether queue is empty or not
%   isFull   - Check whether queue is full or not
%   hasValue - Check whether specified value is present in queue or not

%   Copyright 2019-2020 The MathWorks, Inc.

%#codegen

properties (SetAccess = private)
    %Queue Buffer to store packets
    Queue
    
    %MaxPackets Maximum number of packets that can be queued
    MaxPackets
    
    %MaxPacketSize Maximum size of packet in the queue
    MaxPacketSize
    
    %CurrentSize Current size of queue
    CurrentSize
end

properties (Access = private)
    %pLengths Lengths of the packets in queue, indexed similar to the queue
    pLengths
    
    %pRear Rear index of queue
    pRear
    
    %pFront Front index of queue
    pFront
end
  
methods
    % Constructor
    function obj = bleQueue(maxPackets, maxPacketSize)
        % Validate number of input arguments
        narginchk(2, 2);
        
        % Validate queue size
        validateattributes(maxPackets, {'numeric'}, ...
            {'scalar', 'integer', 'positive'}, mfilename, 'maxPackets');
        obj.MaxPackets = maxPackets;
        
        % Validate packet size
        validateattributes(maxPacketSize, {'numeric'}, ...
            {'scalar', 'integer', 'positive'}, ...
            mfilename, 'maxPacketSize');
        obj.MaxPacketSize = maxPacketSize;
        
        % Create a queue (cell array)
        obj.Queue = cell(maxPackets, 1);
        obj.pLengths = zeros(maxPackets, 1);
        
        % Initialize queue size, front and rear indexes
        obj.CurrentSize = 0;
        obj.pRear = 0;
        obj.pFront = 1;
        
        % Initialize for codegen
        for idx = 1:numel(obj.Queue)
            obj.Queue{idx} = zeros(obj.MaxPacketSize, 1);
        end
    end
    
    % Add packet to the queue
    function flag = enqueue(obj, data)
        % Validate packet size
        dataLen = numel(data);
        if dataLen <= 0 || dataLen > obj.MaxPacketSize
            error(['Packet size must be in the range of '...
                '[1, MAXPACKETSIZE]']);
        end
        % Queue can accommodate more data
        if ~obj.isFull
            data = reshape(data, [], 1);
            obj.pRear = obj.pRear + 1;
            obj.Queue{obj.pRear} = data;
            obj.pLengths(obj.pRear) = dataLen;
            obj.CurrentSize = obj.CurrentSize + 1;
            if (obj.pRear == obj.MaxPackets)
                obj.pRear = 0;
            end
            % Data is enqueued
            flag = true;
        else
            % Data is not enqueued
            fprintf('Queue is full. Cannot accommodate more packets.\n');
            flag = false;
        end
    end
    
    % Remove data from queue
    function [flag, data] = dequeue(obj)
        % Initialize
        data = zeros(1, 0);
        % Queue is non-empty
        if ~obj.isEmpty
            data = obj.Queue{obj.pFront};
            obj.pLengths(obj.pFront) = 0;
            obj.pFront = obj.pFront + 1;
            obj.CurrentSize = obj.CurrentSize - 1;
            if (obj.pFront == obj.MaxPackets + 1)
                obj.pFront = 1;
            end
            % Data is dequeued
            flag = true;
        else
            % Data is not dequeued
            if obj.isEmpty
                fprintf('Queue is empty. Cannot dequeue any packet.\n');
            end
            flag = false;
        end
    end
    
    % Check whether queue is empty or not
    function flag = isEmpty(obj)
        flag = (obj.CurrentSize == 0);
    end
    
    % Check whether queue is full or not
    function flag = isFull(obj)
        flag = (obj.CurrentSize == obj.MaxPackets);
    end
    
    % Check whether specified value is present in queue or not
    function flag = hasValue(obj, value)
        flag = false;
        if ~obj.isEmpty
            value = reshape(value, [], 1);
            nonZerosIdxs = find(obj.pLengths);
            % Search for the given value in queue
            for idx = 1:numel(nonZerosIdxs)
                index = nonZerosIdxs(idx);
                qValueLen = obj.pLengths(index);
                if qValueLen == numel(value)
                    qValue = obj.Queue{index}(1:qValueLen);
                    if isequal(qValue, value)
                        flag = true;
                    end
                end
            end
        end
    end
end
end
