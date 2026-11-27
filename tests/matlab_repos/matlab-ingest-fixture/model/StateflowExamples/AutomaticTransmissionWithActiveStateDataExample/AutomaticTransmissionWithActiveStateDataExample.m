%% Simulate Chart as a Simulink Block with Local Events
% This example provides a more complex design for an automatic transmission
% system. The Stateflow chart appears as a block in a Simulink model. The
% other blocks in the model represent related automotive components. The
% chart interfaces with the other blocks by sharing data through input and
% output connections. To open the chart, click the arrow in the bottom left
% corner of the |shift_logic| block.

% Copyright 2009-2020 The MathWorks, Inc. 

%%

model = 'sf_car';
load_system(model);

% Delete all annotations at the top level of the model.
ah = find_system(model, 'FindAll', 'on', 'type', 'annotation');
for i = 1:length(ah)
   ao = get_param(ah(i), 'Object');
   ao.delete;
end

open_system(model);
close_system([model '/Scope1'])
close_system([model '/Scope2'])

%%
% This chart combines state hierarchy, parallelism, active state data,
% local events, and temporal logic.
%
% * *Hierarchy:* The state |gear_state| contains a modified version of the
% four-speed automatic transmission chart. The state |selection_state|
% contains substates that represent the steady state, upshifting, and
% downshifting modes of operation. When circumstances require a shift to a
% higher or lower gear, these states become active.
% * *Parallelism:* The parallel states |gear_state| and |selection_state|
% appear as rectangles with a dashed border. These states operate
% simultaneously, even as the substates inside them turn on and off.
% * *Active State Data:* The output value |gear| reflects the choice of
% gears during simulation. The chart generates this value from the active
% substate in |gear_state|.
% * *Local Events:* In place of Boolean conditions, this chart uses the
% local events |UP| and |DOWN| to trigger the transitions between gears.
% These events originate from the |<docid:stateflow_ref#send send>|
% commands in |selection_state| when the speed of the car goes outside the
% range of operation for the selected gear. The Simulink function |calc_th|
% determines the boundary values for the range of operation based on the
% selected gear and the engine speed.
% * *Temporal Logic:* To prevent a rapid succession of gear changes,
% |selection_state| uses the temporal logic operator
% |<docid:stateflow_ref#after after>| to delay the broadcasting of the |UP|
% and |DOWN| events. The state broadcasts one of these events only if a
% change of gears is required for longer than some predetermined time
% |TWAIT|.

% Set up charts with white background
set_param(0,'ExportBackgroundColorMode','white');

open_system([model '/shift_logic'],'force')

%%
% To run a simulation of the model:
% 
% # Double-click the *User Inputs* block. In the Signal Editor dialog box,
% select a predefined brake-to-throttle profile from the *Active Scenario*
% list. The default profile is |Passing Maneuver|.
% # Click *Run*. In the Stateflow Editor, chart animation highlights the
% active states during the simulation. To slow down the animation, in the
% *Debug* tab, select |Slow| from the *Animation Speed* drop-down list.
% # In the Scope blocks, examine the results of the simulation. Each scope
% displays a graph of its input signals during simulation.

sim(model)
open_system([model '/Scope2'])
