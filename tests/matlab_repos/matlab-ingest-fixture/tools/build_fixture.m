% build_fixture.m —— 重建本项目里由 MATLAB 生成的文件
%
% 前提：MATLAB R2025b，工程根目录下运行。
% 代码生成对象是官方 VirtualVehicle 工程里的真实控制器模型
% EvPowertrainController2EM（966 个块），先把它所在的工程目录加入路径，
% 再临时脱开厂商配置引用、换成本地 GRT 配置后构建。
%
% 覆盖：代码生成与仿真缓存、受保护模型、MDF/MF4/BLF、工具箱、
%       自动备份、工程归档、格式合成项。
% 说明：build/ 与 cache/ 由 MATLAB 在构建和仿真时创建，本脚本不手工建目录。

root = pwd;
if ~isfile(fullfile(root, 'MatlabIngestFixture.prj'))
    error('build_fixture:noProject', '请在工程根目录运行本脚本');
end
proj = openProject(root);
vv = fullfile(root, 'model', 'VirtualVehicle');
addpath(genpath(vv));
model = 'EvPowertrainController2EM';
modelFile = fullfile(vv, 'VirtualVehicle', 'Controller', [model '.slx']);

%% 1 代码生成与仿真缓存
load_system(modelFile);
cs = Simulink.ConfigSet;
set_param(cs, 'SystemTargetFile', 'grt.tlc', 'RetainRTWFile', 'on', ...
    'StartTime', '0', 'StopTime', '10', ...
    'SolverType', 'Fixed-step', 'Solver', 'FixedStepDiscrete', 'FixedStep', '0.01', ...
    'UnderspecifiedInitializationDetection', 'Simplified');
attachConfigSet(model, cs, true);
setActiveConfigSet(model, cs.Name);
Simulink.fileGenControl('set', ...
    'CodeGenFolder', fullfile(root, 'build'), ...
    'CacheFolder', fullfile(root, 'cache'), ...
    'createDir', true);
slbuild(model);

%% 2 受保护模型
Simulink.ModelReference.protect(model, 'Path', fullfile(root, 'packages'));

%% 3 自动备份 .autosave：制造未保存改动后更新模型，让 Simulink 写备份
set_param([model '/Energy Management'], 'Position', [100 100 300 300]);
set_param(model, 'SimulationCommand', 'update');
pause(2);
close_system(model, 0);

%% 4 FMU：从官方 autoblks 包内提取
siZip = fullfile(matlabroot, 'toolbox', 'autoblks', 'autoblksreference', 'SI.zip');
if isfile(siZip)
    tmp = tempname;
    mkdir(tmp);
    unzip(siZip, tmp);
    copyfile(fullfile(tmp, 'Plant', 'FMUs', 'VvcFmuEngExl.fmu'), ...
        fullfile(root, 'packages', 'VvcFmuEngExl.fmu'), 'f');
end

%% 5 MDF / MF4 / BLF
T = readtable(fullfile(root, 'config', 'outages.csv'));
tt = timetable(T.Loss, T.Customers, 'RowTimes', seconds((0:height(T) - 1)'), ...
    'VariableNames', {'Loss', 'Customers'});
mdfWrite(fullfile(root, 'data', 'ingest_measurement.mf4'), tt);
mdfWrite(fullfile(root, 'data', 'ingest_measurement.mdf'), tt);

msgs = canMessage(500, false, 8);
for k = 2:3
    msgs(k) = canMessage(500 + k, false, 8);
end
for k = 1:3
    msgs(k).Data = uint8(mod((k:k + 7), 255));
end
blfwrite(fullfile(root, 'data', 'ingest_canlog.blf'), ...
    canMessageTimetable(msgs), 1, "CAN");

%% 6 工具箱
tbdir = fullfile(root, 'packages', 'toolbox_src');
if ~exist(tbdir, 'dir')
    mkdir(tbdir);
end
copyfile(fullfile(root, 'model', 'asbCubeSatMBSE', 'ProjectTasks', 'projectStartup.m'), tbdir, 'f');
copyfile(fullfile(root, 'model', 'asbCubeSatMBSE', 'CubeSatMBSEModel', ...
    'ModelConfiguration', 'detectChangeOrbitalElements.m'), tbdir, 'f');
f = dir(fullfile(tbdir, '*'));
opts = matlab.addons.toolbox.ToolboxOptions(tbdir, "ingest-fixture-toolbox");
opts.ToolboxName = "Ingest Fixture Toolbox";
opts.ToolboxVersion = "1.0";
opts.ToolboxFiles = string(fullfile({f.folder}, {f.name}));
opts.OutputFile = fullfile(root, 'packages', 'IngestFixtureToolbox.mltbx');
matlab.addons.toolbox.packageToolbox(opts);

%% 7 格式合成项：dbc / ldf / hex / s19 / 安装包
script = fullfile(root, 'tools', 'make_artifacts.py');
py = 'D:\anaconda3\envs\Agentpy\python.exe';
if isfile(script)
    if isfile(py)
        system(sprintf('"%s" "%s"', py, script));
    else
        warning('build_fixture:noPython', '未找到 Agentpy，跳过格式合成项');
    end
end

%% 8 编辑器自动备份 .asv（关闭文档会删除，这里留存副本）
s = settings();
s.matlab.editor.backup.FileExtensionToAppend.PersonalValue = '.asv';
s.matlab.editor.backup.Frequency.PersonalValue = 0.01;
s.matlab.editor.backup.SaveIntoSourceFolder.PersonalValue = true;
srcFile = fullfile(root, 'src', 'detectChangeOrbitalElements.m');
srcOrig = fullfile(root, 'model', 'asbCubeSatMBSE', 'CubeSatMBSEModel', ...
    'ModelConfiguration', 'detectChangeOrbitalElements.m');
copyfile(srcOrig, srcFile, 'f');
doc = matlab.desktop.editor.openDocument(srcFile);
doc.Text = [doc.Text sprintf('\n%% asv probe\n')];
pause(8);
bak = strrep(srcFile, '.m', '.asv');
if isfile(bak)
    copyfile(bak, fullfile(root, 'derived', 'ingest_editor_backup.asv'), 'f');
end
doc.close();
copyfile(srcOrig, srcFile, 'f');

%% 9 刷新工程文件清单并导出工程归档
addFolderIncludingChildFiles(proj, root);
mlproj = fullfile(root, 'packages', 'MatlabIngestFixture.mlproj');
if isfile(mlproj)
    delete(mlproj);
end
export(proj, mlproj);

fprintf('完成：生成物已写入 build/、cache/、data/、packages/、derived/\n');
