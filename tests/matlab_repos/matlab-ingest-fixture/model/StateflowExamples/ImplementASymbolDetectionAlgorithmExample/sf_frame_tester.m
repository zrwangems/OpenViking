%% Test Symbol Detection Algorithm
% Generate a short signal consisting of several valid pulses and one
% transmission error.

f = sf_frame_search(pulse=0);        % create chart object
sendPulse(f,77);                     % frame marker
sendPulse(f,17);                     % A
sendPulse(f,47);                     % B
sendPulse(f,37);                     % transmission error
sendPulse(f,47);                     % B
sendPulse(f,17);                     % A
sendPulse(f,77);                     % frame marker
delete(f);                           % delete chart object

function sendPulse(f,n)
% Send a pulse of n ones and one zero to chart object f.

for i = 1:n
    step(f,pulse=1);
    printDot(1)
end

printDot(0)
step(f,pulse=0);

    function printDot(x)
        persistent k
        if isempty(k)
            k = 1;
        end
        
        if x == 0
            fprintf("\n");
            k = 1;
        elseif k == 50
            fprintf(".\n");
            k = 1;
        else
            fprintf(".");
            k = k+1;
        end
    end
end