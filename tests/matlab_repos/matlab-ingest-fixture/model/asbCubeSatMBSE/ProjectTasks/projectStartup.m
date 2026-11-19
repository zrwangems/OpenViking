function projectStartup
% projectStartup Initialize CubeSat MBSE Model

%  Copyright 2021-2025 The MathWorks, Inc.


% Close model asbCubeSat opened by referenced CubeSat Simulation Project startup
    if bdIsLoaded("asbCubeSat")
        close_system("asbCubeSat");
    end

    % Open Architecture model
    open_system("asbCubeSatArchModel");

end
