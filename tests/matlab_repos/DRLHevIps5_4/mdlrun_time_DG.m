clc;clear;close all
warning('off')
addpath(genpath(pwd))
cfg = Simulink.fileGenControl('getConfig');
work_dir = pwd;
cfg.CacheFolder = fullfile(work_dir,'Simulation cache folder');
cfg.CodeGenFolder  = fullfile(work_dir,'Simulation cache folder');
Simulink.fileGenControl('setConfig', 'config', cfg);
cyc_name = 'WLTC'; % CLTCP WLTC
switch cyc_name
    case 'CLTCP'
        load('CLTCP.mat');
        cyc_time =Cycle(:,1);
        cyc_vel =Cycle(:,2);
        clear Cycle
    case 'WLTC'
        load('WLTC.mat');
        cyc_time =WLTC(:,1);
        cyc_vel =WLTC(:,2);
        clear WLTC
end
ts = 1;
load("Eng_param")
rho_gas = 0.739;           % 95汽油密度 kg/L
Price_gas = 7.14;          % 92汽油油价 RMB/L
Price_elec = 1;            % 充电电价 RMB/kWh
k_gas = 1;                 % 油耗惩罚权重
k_elec = 1;                % 电耗惩罚权重
k_SOCpen = 1.2;            % SOC惩罚权重
k_actsmo = 5e-2;           % action平滑性惩罚权重
rew_Zoom = 1;              % 奖励函数缩放系数
en_gas = 1;                % 油耗奖励参数使能
en_elec = 1;               % 电耗奖励参数使能
en_SOCpen = 1;             % SOC惩罚参数使能
en_actsmo = 1;             % 动作平滑惩罚参数使能

obs_max = 1e4*[0.0020, 0.0090, 0.0100, 0.0100, 8.4000, 0.0100,...
               0.0056, 0.1011, 2.8000,      0, 0.0001, 0.0132,...
               0.0740, 2.6065, 0.0339, 0.0949, 0.0117, 2.4444];
obs_min = 1e4*[0.0010, 0.0070,      0,      0, 0.8400,      0,...
                    0, -0.0005,     0, -2.8000,     0, -0.0032...
              -0.0694, -2.7092, -0.0030,    0, -0.0001, -2.7647];

obsInfo = rlNumericSpec([18 1], ...
                        LowerLimit=zeros(18,1), ...
                        UpperLimit=ones(18,1));
obsInfo.Name = "observation";
obsInfo.Description = "EMS input";
actInfo = rlNumericSpec([1 1], ...
                        LowerLimit=0,...
                        UpperLimit=1);
actInfo.Name = "action";
initOpts = rlAgentInitializationOptions(NumHiddenUnit=256);
actorOptions = rlOptimizerOptions( ...
    LearnRate                 = 3e-4, ...
    GradientThreshold         = 1, ...
    L2RegularizationFactor    = 1e-4);

criticOptions = rlOptimizerOptions( ...
    LearnRate                 = 1e-3, ...
    GradientThreshold         = 1, ...
    L2RegularizationFactor    = 1e-4);

agentOptions = rlSACAgentOptions(...
    SampleTime                = ts,...
    MiniBatchSize             = 256,...
    ActorOptimizerOptions     = actorOptions,...
    CriticOptimizerOptions    = criticOptions,...
    ExperienceBufferLength    = 1e6,...
    DiscountFactor            = 0.99);
DRLEMSagent = rlSACAgent(obsInfo,actInfo,initOpts,agentOptions);
VCU_Mode_Change(3)% 更改VCU模式
stop_time = cyc_time(end);
% load_system("DRLHevIps.slx")
% open_system('DRLHevIps/Data Info/Operating condition signal')
% open_system('DRLHevIps/Data Info/Power Element Rotation speed')
% open_system('DRLHevIps/Data Info/Power Element Torque')
% open_system('DRLHevIps/Data Info/Energy Signal')
% open_system('DRLHevIps/Data Info/TP Emissions')
% open_system('DRLHevIps/Data Info/Reward Single')
tic
% sim("DRLHevIps.slx")
toc

% ccc = (WhlTrqCmd*0.30609-EngTrqCmd*0.7222)*0.37931-MotTrqCmd;
% % plot(ccc)
% 
% numRows = length(WhlTrqCmd);
% file_name = 'Result/VehicleData_Output.xlsx';
% colNames = {'EngSpdFdbk (rad/s)', 'EngTrqCmd (Nm)', 'GenTrqCmd (Nm)', 'MotTrqCmd (Nm)', 'WhlTrqCmd (Nm)', 'WhlSpd (rad/s)'};
% data = [EngSpdFdbk, EngTrqCmd, GenTrqCmd, MotTrqCmd, WhlTrqCmd, WhlSpd];
% T = array2table(data, 'VariableNames', colNames);
% fprintf('正在生成包含 %d 行数据的 Excel 文件，请稍候...\n', numRows);
% writetable(T, file_name);
% fprintf('文件生成成功：%s\n', file_name);
% % plot(EngSpdFdbk)

function VCU_Mode_Change(param)
    HevIpsDictionaryObj = Simulink.data.dictionary.open('HevIps.sldd');
    HevIpsDataSectObj = getSection(HevIpsDictionaryObj, 'Design Data');
    signalObj = getEntry(HevIpsDataSectObj, 'VCU_Mode');
    signalValue = getValue(signalObj);
    signalValue.Value = param;
    setValue(signalObj, signalValue);
    saveChanges(HevIpsDictionaryObj);
end

