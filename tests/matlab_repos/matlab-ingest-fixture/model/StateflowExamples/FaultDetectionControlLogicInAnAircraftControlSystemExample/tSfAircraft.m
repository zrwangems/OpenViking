classdef tSfAircraft < stateflowtest.TestCase
    % Tests for stateflows with events and C action language

    %   Copyright 2023 The MathWorks, Inc.
    
    methods(Test)
        function sfAircraft(testCase)
            import simulinktest.SimulationTester
            import simulinktest.constraints.SimulationOutputEquals;
            import matlab.unittest.fixtures.SuppressedWarningsFixture;
            
            testCase.applyFixture(...
                SuppressedWarningsFixture('Simulink:blocks:DerivativeNonContinuousInput'));

            oldModel = 'sf_aircraft_old';
            load_system(oldModel);

            tester = SimulationTester.forNormalMode(oldModel);
            tester.simulate(testCase);
            expVal = tester.Results.SimulationOutput;

            close_system(oldModel, 0);

            newModel = 'sf_aircraft';
            load_system(newModel);
            
            tester = SimulationTester.forNormalMode(newModel);
            tester.simulate(testCase);
            
            testCase.verifyThat(tester, SimulationOutputEquals(expVal));
            
            close_system(newModel, 0);
        end
    end
end