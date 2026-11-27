classdef(Enumeration) trafficComms < Simulink.IntEnumType
  enumeration
    SAFE(0) 
    REQ_STOP(1)
    REQ_PED(2)
    STOPPED(3)
    PED(4)
    FLOWING(5)
  end
end 