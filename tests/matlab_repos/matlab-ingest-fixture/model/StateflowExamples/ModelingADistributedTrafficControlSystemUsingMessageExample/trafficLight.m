classdef trafficLight < handle
    
    properties
        offColors;
        onColors; 
        pColors;
        
    end
    
    properties
        axes;
        modelName;
        pedButton;
        trafficButton;
        pedLamp;
        lights;
        lightNumber;
        left;
    end
    
    methods
        function this = trafficLight(varargin)
            this.modelName = varargin{1};
            this.lightNumber= varargin{2};
            this.left=varargin{3};
            
            
            this.axes = axes('Color','none', ...
                'XLim',[1 400], ...
                'YLim',[1 600], ...
                'XColor','none', ...
                'YColor','none', ...
                'DataAspectRatio',[1 1 1], ...
                'XTick',[], ...
                'YTick',[], ...
                'Position',[this.left 0 0.6 1]);
            
            this.offColors(1,:)=[141/255 7/255 7/255];
            this.onColors(1,:)=[1 0 0];
            this.offColors(2,:)=[198/255 190/255 89/255];
            this.onColors(2,:)=[1 1 0];
            this.offColors(3,:)=[91/255 141/255 113/255];
            this.onColors(3,:)=[0 1 0];
            this.pColors(1,:)=[141/255 7/255 7/255];
            this.pColors(2,:)=[1 1 0];
            this.pColors(3,:)=[0 1 0];
            
            this.draw();
        end
        
        function pedLampChange(this,color)
            this.pedLamp.FaceColor=this.pColors(color,:);
        end
        
        function trafficLampOn(this,lamp)
            this.lights{lamp}.FaceColor=this.onColors(lamp,:);
        end
        
        function trafficLampOff(this,lamp)
            this.lights{lamp}.FaceColor=this.offColors(lamp,:);
        end
        
        function draw(this)
            xPos=100;
            yPos=0;
            border=20;
            post=rectangle('Parent',this.axes, ...
                'Position',[xPos+20+border yPos 60 180], ...
                'FaceColor',[220/255 220/255 220/255]);
            
            box=rectangle('Parent',this.axes, ...
                'Position',[xPos yPos+180 100+(border*2) 380], ...
                'FaceColor',[220/255 220/255 220/255]);
            
            this.pedButton = rectangle('Parent',this.axes, ...
                'Position',[xPos+30+border yPos+50 40 50], ...
                'FaceColor',[148/255 148/255 148/255], ...
                'Curvature',[0.6,0.6]);
            
            set(this.pedButton,'ButtonDownFcn',{@trafficLight.pedPress, this.modelName, this.lightNumber});
            
            
            this.pedLamp=rectangle('Parent',this.axes, ...
                'Position',[xPos+border yPos+110 100 50], ...
                'FaceColor',this.pColors(1,:));
             
            this.lights{1} = rectangle('Parent',this.axes, ...
                'Position',[xPos+border yPos+420 100 100], ...
                'FaceColor',this.offColors(1,:), ...
                'Curvature',[1,1]);
            
            this.lights{2} = rectangle('Parent',this.axes, ...
                'Position',[xPos+border yPos+310 100 100], ...
                'FaceColor',this.offColors(2,:), ...
                'Curvature',[1,1]);
            
            this.lights{3}= rectangle('Parent',this.axes, ...
                'Position',[xPos+border yPos+200 100 100], ...
                'FaceColor',this.offColors(3,:), ...
                'Curvature',[1,1]);
        end
    end
    
    methods (Static)
        function trafficPress(~,~,modelName,sensor)
            strButton=num2str(sensor);
            val=get_param([modelName '/UI' strButton],'value');
            if (strcmp(val,'1'))
                set_param([modelName '/UI' strButton], 'value', '0');
            else
                set_param([modelName '/UI' strButton], 'value', '1');
            end
        end
        
        function pedPress(~,~,modelName,light)
            strButton=num2str(light);
            val=get_param([modelName '/UI/PedButton' strButton],'value');
            if (strcmp(val,'1'))
                set_param([modelName '/UI/PedButton' strButton], 'value', '0');
            else
                set_param([modelName '/UI/PedButton' strButton], 'value', '1');
            end
        end
    end
end

