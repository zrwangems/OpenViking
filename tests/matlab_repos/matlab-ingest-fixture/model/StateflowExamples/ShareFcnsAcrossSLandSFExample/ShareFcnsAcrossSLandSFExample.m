%% Manage Queue for Shared Printer Server
% This example shows how to share functions to communicate between a
% Simulink(R) model and a Stateflow(R) chart. For instance, you can:
% 
% * Use a Stateflow chart to call a Simulink function that you define in
% your model.
% * Use a Function Caller block in your Simulink model to call a function
% that you define in your Stateflow chart.

% Copyright 2014-2023 The MathWorks, Inc.

%%
% This example models three computer clients that share a network printer.
% Each computer sends print jobs to a common queue for processing. Each
% computer client invokes the printer server with a call to the Simulink
% Function block |addPrintJob|. To add the print job to the work load, the
% |addPrintJob| function calls the graphical function |queuePrintJob| in
% the Stateflow chart. To model usage of printer ink, the chart processes
% the work and calls the Simulink Function block |printerInk|.

% Set up charts with white background
set_param(0,'ExportBackgroundColorMode','white');

model = 'slexPrinterExample';

load_system(model);

% Delete all annotations at the top level of the model
ah = find_system(model, 'FindAll', 'on', 'type', 'annotation');
for i = 1:length(ah)
   ao = get_param(ah(i), 'Object');
   ao.delete;
end

open_system(model);

%% Call a Simulink Function from Stateflow
% The function |printerInk| is defined in a Simulink Function block at the
% top level of the model. The function interface |printerInk(work)| defines
% one input argument. The Simulink Function, printerInk, also interacts
% with the model with signal lines through the inport |ink| and outport
% |ink'|. The state |Busy| matches the function signature for
% |printerInk(work)| by passing one input argument.

open_system([model '/Queueing and Processing Incoming Jobs']);

%% Export Stateflow Functions to Simulink
% In the chart |Queuing| and |Processing Incoming Jobs|, the properties *Export
% chart level functions* and *Treat exported functions as globally visible*
% are selected. These properties allow the Simulink function |addPrintJob| to
% call the chart graphical function, |queuePrintJob|.
