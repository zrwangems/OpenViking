classdef StreamingMode < Simulink.IntEnumType
    enumeration     
        PAUSE(0),
        PLAY(1),
        REW(2),
        FF(3)
    end    
end