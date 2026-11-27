classdef BatteryStates < Simulink.IntEnumType
  enumeration
    MIN(0)
    LOW(1)
    NORMAL(2)
    HIGH (3)
    MAX(4)
  end
end