function tl_gui(method, varargin)

persistent fig t modelName; 

if isempty(fig) || ~ishandle(fig)
    switch method
        case 'init'
            % go through
        case 'reset'
            % GUI was closed, need to reopen
            method = 'init';
        case 'close'
            % Already closed. Do nothing.
            return;
        otherwise
            % Figure closed. Stop simulation
            set_param('sf_msg_traffic_light', 'SimulationCommand', 'Stop');
            return;
    end
end

switch method
    case 'init'
        
        modelName = varargin{1};
        
        % Initialize the UI figure
        fig = figure('Name','Traffic Lights', 'DoubleBuffer', 'on');
        oldUnits = get(fig,'Units');
        set(fig,'Units','normalized');
        ratioXY = 400/600;
        height = 0.8;
        width = ratioXY * height;
        left = (1 - width) / 2;
        top = (1 - height)/ 2;
        set(fig,'Position',[left top width height]);
        set(fig,'Units',oldUnits);
        screenSize = get(0, 'ScreenSize');
        set(fig,'position',[880 screenSize(4)-685-75 439 685])
        
        t{1}=trafficLight(modelName,'1',0);
        t{2}=trafficLight(modelName,'2',0.5);
        l = t{1};
        l.trafficLampOn(1);
        l = t{2};
        l.trafficLampOn(3);
    
    case 'reset'
        l = t{1};
        l.trafficLampOn(1);
        l.trafficLampOff(2);
        l.trafficLampOff(3);
        l = t{2};
        l.trafficLampOff(1);
        l.trafficLampOff(2);
        l.trafficLampOn(3);
    case 'onp'
        light=varargin{1};
        color=varargin{2}+1;
        l=t{light};
        l.pedLampChange(color);

    case 'ont'
        light=varargin{1};
        lamp=varargin{2};
       
        l=t{light};
        switch lamp
            case 0  % Red
                l.trafficLampOff(2);
                l.trafficLampOff(3);
                l.trafficLampOn(1);
            case 1  % Yellow
                l.trafficLampOff(1);
                l.trafficLampOff(3);
                l.trafficLampOn(2);
            case 2  % Green
                l.trafficLampOff(1);
                l.trafficLampOff(2);
                l.trafficLampOn(3);
        end
        
        

    case 'off'
        light=varargin{1};
        lamp=varargin{2};
        l=t{light};
        l.trafficLampOff(lamp+1);
    case 'close'
        % Close UI figure when simulation is stopped
        if(~isempty(fig) && ishandle(fig))
            close(fig);
            t{1}.delete();
            t{2}.delete();
        end
        
end
