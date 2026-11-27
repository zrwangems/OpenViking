function setupModelForDoc(model)

% Unlock libraries
set_param(model, 'Lock', 'off');

% Set up charts with white background
set_param(0,'ExportBackgroundColorMode','white')

% If model is not a library, update to show bus signals
if get_param(model,"LibraryType")=="None" & ...
        model~="sfGetStartedParallel" & model~="sf_aircraft" & ...
        model~="sfManufacturingSystem"
    set_param(model,SimulationCommand="Update")
end

% Delete title and copyright annotations at the top level of the model
ah = find_system(model,FindAll="on",type="annotation");
for i = 1:length(ah)
    an = get_param(ah(i),"Name");
    if contains(an,"Copyright") || contains(an,"showExample")
        ao = get_param(ah(i), 'Object');
        ao.delete;
    end
end
end