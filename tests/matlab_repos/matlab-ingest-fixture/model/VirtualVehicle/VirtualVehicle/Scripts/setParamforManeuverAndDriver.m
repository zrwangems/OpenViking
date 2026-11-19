function out = setParamforManeuverAndDriver(model, Maneuver, ManeuverOption, Driver, TestID, in,configfile,licStatus)

%   Copyright 2021-2025 The MathWorks, Inc.
simTime=VirtualAssembly.getDefaultStoptime(Maneuver,ManeuverOption);
in=setModelParameter(in,StopTime=num2str(simTime));

DriverTypePath = [model,'/Driver Commands'];
DriverType = 'driverType';
in=in.setBlockParameter(DriverTypePath,DriverType,Driver);

ManeuverMaskPath = [model,'/Scenarios/Reference Generator'];
in=in.setBlockParameter(ManeuverMaskPath,'LabelModeActiveChoice',Maneuver);


%% set scenario
plant=get_param([model,'/Vehicle'],'LabelModeActiveChoice');
plantmodel=[model,'/Vehicle/',plant];
%get scenario
%ManeuverMaskPath=[model,'/Scenarios/Reference Generator'];
in=in.setBlockParameter(ManeuverMaskPath,'LabelModeActiveChoice',Maneuver);
%get trailer path
Trailer=get_param([plantmodel,'/Trailer'],'LabelModeActiveChoice');
ManeuverMaskPath3D = [model,'/Visualization/3D Engine'];
GrndFdbkPath = [model,'/Environment/Ground Feedback'];
Scope=[model,'/Visualization/Scope Type'];
XYPlotter=[model,'/Visualization/Vehicle XY Plotter'];


if strcmp(Maneuver,'Drive Cycle')

    ManeuverMaskPath = [ManeuverMaskPath,'/Drive Cycle/Drive Cycle Source'];
    in=in.setBlockParameter(ManeuverMaskPath,'cycleVar',ManeuverOption);
    in=in.setBlockParameter(Scope,'LabelModeActiveChoice','0');
    in=in.setBlockParameter(XYPlotter,'LabelModeActiveChoice','2');
    in=in.setBlockParameter(ManeuverMaskPath3D,'LabelModeActiveChoice','NoEngine3D');
    in=in.setBlockParameter(GrndFdbkPath,'LabelModeActiveChoice','0');

    maskparamap={'ScnLongVelUnit','outUnit'};

elseif contains(Maneuver,'Wide Open Throttle')

    ManeuverMaskPath = [ManeuverMaskPath,'/WOT/Drive Cycle Source'];

    in=in.setBlockParameter([model, '/Visualization/Scope Type'],'LabelModeActiveChoice','0');
    if licStatus
        in=in.setBlockParameter(ManeuverMaskPath3D,'LabelModeActiveChoice','NoEngine3D');
    end
    in=in.setBlockParameter(GrndFdbkPath,'LabelModeActiveChoice','0');
    in=in.setBlockParameter(XYPlotter,'LabelModeActiveChoice','2');
    in=in.setBlockParameter(Scope,'LabelModeActiveChoice','0');
    maskparamap={'ScnLongVelUnit','outUnit'};
else

    ManeuverMaskPath = [ManeuverMaskPath,'/',Maneuver,'/',Maneuver];
    % Switch scope based on the maneuver , and Trun on XY
    % Plotter for all scenes besides Drivecycle and WOT
    % This applies to both 3D Scene on and off cases

    switch Maneuver
        case 'Double Lane Change'
            in=in.setBlockParameter(Scope,'LabelModeActiveChoice','1');
            if strcmp(Trailer,'NoTrailer')
                in=in.setBlockParameter(XYPlotter,'LabelModeActiveChoice','1');
            else
                in=in.setBlockParameter(XYPlotter,'LabelModeActiveChoice','3');
            end

        case 'Constant Radius'
            in=in.setBlockParameter(Scope,'LabelModeActiveChoice','2');
            if strcmp(Trailer,'NoTrailer')
                in=in.setBlockParameter(XYPlotter,'LabelModeActiveChoice','1');
            else
                in=in.setBlockParameter(XYPlotter,'LabelModeActiveChoice','3');
            end
        otherwise
            in=in.setBlockParameter(Scope,'LabelModeActiveChoice','0');
            if strcmp(Trailer,'NoTrailer')
                in=in.setBlockParameter(XYPlotter,'LabelModeActiveChoice','0');
            else
                in=in.setBlockParameter(XYPlotter,'LabelModeActiveChoice','3');
            end
    end

    if strcmp(ManeuverOption,'Enabled')
        % 3d engine enabled
        in=in.setBlockParameter(ManeuverMaskPath3D,'LabelModeActiveChoice','Engine3D');
        in=in.setBlockParameter(GrndFdbkPath,'LabelModeActiveChoice','1');
        ManeuverMaskPath3DScene=[model,'/Visualization/3D Engine/3D Engine/Simulation 3D Scene Configuration'];
        ManeuverMaskPath3DVehicle=[model,'/Visualization/3D Engine/3D Engine/Simulation 3D Vehicle'];
        ManeuverMaskPath3DTrailer=[model,'/Visualization/3D Engine/3D Engine/Trailer'];
        if strcmp(Trailer,'NoTrailer')
            in=in.setBlockParameter(ManeuverMaskPath3DTrailer, 'OverrideUsingVariant', 'No Trailer');
            in=in.setBlockParameter(ManeuverMaskPath3DVehicle, 'PassVehMesh', 'Muscle car');
        else
            in=in.setBlockParameter(ManeuverMaskPath3DTrailer, 'OverrideUsingVariant', 'One-Axle Trailer');
            in=in.setBlockParameter(ManeuverMaskPath3DVehicle, 'PassVehMesh', 'Small pickup truck');
        end


        if strcmp(Maneuver,'Double Lane Change')
            in=in.setBlockParameter(ManeuverMaskPath3DScene,'SceneDesc','Double lane change');
        else
            in=in.setBlockParameter(ManeuverMaskPath3DScene,'SceneDesc','Open surface');
        end

    else
        in=in.setBlockParameter(ManeuverMaskPath3D,'LabelModeActiveChoice','NoEngine3D');
        in=in.setBlockParameter(GrndFdbkPath,'LabelModeActiveChoice','0');
    end

    maskparamap={'ScnSteerDir','steerDir';...
        'ScnLongVelUnit','velRefUnit';...
        };

end

in=in.setVariable("TestID",TestID);


run(configfile);
testdata=ConfigInfos.TestPlan{TestID}.Data;
if ~isempty(testdata)
    for i = 1 : size(testdata,1)

        index=find(strcmp(testdata{i,1},maskparamap(:,1)),1);

        if ~isempty(index)
            if licStatus
                in=in.setBlockParameter(ManeuverMaskPath,maskparamap{index,2},testdata{i,2});
            else
                in=in.setBlockParameter(ManeuverMaskPath,'outUnit',testdata{i,2});
            end
        else
            if strcmp(testdata{i,1},'ScnSimTime')
                if ischar(testdata{i,2})
                    stime=testdata{i,2};
                else
                    stime=num2str(testdata{i,2});
                end
                in=setModelParameter(in,StopTime=stime);
            else
                newvalue=str2num(testdata{i,2});
                if isempty(newvalue)
                    in=in.setVariable(testdata{i,1},testdata{i,2});
                else
                    in=in.setVariable(testdata{i,1},newvalue);
                end
            end
        end

    end
end

out=in;
end


