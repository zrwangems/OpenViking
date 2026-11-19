# MATLAB 全扩展名入库测试项目（Ingest Fixture）

给 OpenViking `feat/matlab` 分支的 `add_resource` 做 MATLAB 项目入库测试用。目标是让一个**能正常打开的 MATLAB 工程**里同时出现 `matlab-ingest-plan.html` 列的 65 种扩展名，覆盖可读文本、ZIP 容器、数据/目标二进制、Windows 原生、加密保护、派生缓存六类。

- 生成环境：MATLAB R2025b（25.2.0.2998904）+ Microsoft Visual C++ 2022，Windows 11 x64
- 覆盖率：65/65；另有 `png`、`tmw`、`dmr`、`py` 等真实副产物
- 主案例：官方 **VirtualVehicle** 整车工程（12 个子工程、248 个 `.slx`、38 个 `.sldd`）与官方 **CubeSat MBSE** 工程模板，均为真实工程规模的模型（主配置模型 966～1592 个块）

## 目录

```text
model/      官方 CubeSat MBSE 工程模板 + 官方 VirtualVehicle 整车工程（主案例）
src/        代码与二进制素材（.m .mlx .mlapp .p .mexw64 .c/.h .cpp/.hpp .ssc/.sscp .tlc .mdl .asv）
data/       数据（.mat .fig .csv .mdf .mf4 .blf）
config/     配置与描述（.json .xml .yaml .yml .ini .txt .md .html .a2l .arxml .dbc .ldf .csv）
bin/        原生二进制（.dll .exe .lib .obj .pdb .elf .hex .s19 .bin）
packages/   安装包与归档（.mltbx .mlappinstall .mlpkginstall .jar .ctf .sltx .fmu .slxp .mlproj）
templates/  官方构建模板（.mk .tmf .map）
build/      代码生成产物：MATLAB 生成，含 slprj/、*_grt_rtw/、.rtw/.rsp/.bat/.c/.h/.exe
cache/      仿真缓存：MATLAB 生成，含 .slxc
derived/    编辑器自动备份 .asv
tools/      复现脚本
```

`build/` 与 `cache/` 不是手工创建的目录，由 `Simulink.fileGenControl` 指向后由 MATLAB 在构建/仿真时生成；`.autosave` 由 Simulink 在模型更新时自动备份。

## 65 种扩展名来源

来源等级：**官方拷贝** = 直接取 MATLAB 安装目录或官方示例工程里的文件；**官方流程生成** = 用 MATLAB 官方 API/构建流程产出；**官方派生** = 用官方二进制转换；**格式合成** = MATLAB 无对应产出能力，按公开格式规范写最小合法文件。

### 可读文本（29）

| 扩展名 | 位置 | 来源 | 说明 |
|---|---|---|---|
| .m | model/asbCubeSatMBSE、model/VirtualVehicle | 官方拷贝 | 工程脚本与函数 |
| .mdl | src/slctrlobsolete.mdl | 官方拷贝 | Control Toolbox 老格式模型 |
| .ssc | src/ee_BSC019N02KS.ssc | 官方拷贝 | Simscape 组件源码 |
| .tlc | src/ert.tlc | 官方拷贝 | 代码生成模板 |
| .c | src/arrayProduct.c、build/*_grt_rtw/*.c | 官方拷贝 + 官方流程生成 | MEX 示例与生成的控制器代码 |
| .h | src/mex.h、build/*_grt_rtw/*.h | 官方拷贝 + 官方流程生成 | MEX API 头与生成头文件 |
| .cpp | src/arrayProduct.cpp | 官方拷贝 | C++ MEX 官方示例 |
| .hpp | src/MatlabCppSharedLib.hpp | 官方拷贝 | C++ 接口头 |
| .mk | templates/makefile_gnu.mk | 官方拷贝 | GRT 构建模板 |
| .bat | build/EvPowertrainController2EM_grt_rtw/*.bat | 官方流程生成 | 构建脚本 |
| .rsp | build/EvPowertrainController2EM_grt_rtw/*.rsp | 官方流程生成 | 编译/链接响应文件 |
| .rtw | build/EvPowertrainController2EM_grt_rtw/*.rtw | 官方流程生成 | 代码生成中间文件（RetainRTWFile） |
| .tmf | templates/sldrt.tmf | 官方拷贝 | 目标 makefile 模板 |
| .map | templates/libMatlabCppSharedLib25_2.map | 官方拷贝 | 链接映射表 |
| .html | config/3p-landing.html | 官方拷贝 | 帮助文档页 |
| .prj | MatlabIngestFixture.prj、model/VirtualVehicle/*.prj | 官方流程生成 + 官方拷贝 | 本工程定义 + 官方 12 个子工程定义 |
| .asv | derived/ingest_editor_backup.asv | 官方流程生成 | 编辑器自动备份（关闭文档会删除，已留存副本） |
| .xml | config/VersionInfo.xml、resources/project/*.xml | 官方拷贝 + 工程生成 | 工程元数据由 MATLAB 写 |
| .json | config/compcontents.json | 官方拷贝 | 产品清单 |
| .yaml | config/mapping_rules.yaml | 官方拷贝 | ROS 2 接口映射 |
| .yml | config/distroprefs.yml | 官方拷贝 | Perl 模块配置 |
| .csv | config/outages.csv | 官方拷贝 | 官方示例数据 |
| .txt | config/trademarks.txt | 官方拷贝 | 官方文本 |
| .ini | config/msa.ini | 官方拷贝 | 官方配置文件 |
| .arxml | config/AUTOSAR_BaseTypes.arxml | 官方拷贝 | AUTOSAR 基础类型 |
| .dbc | config/ingest_can.dbc | 格式合成 | 最小合法 CAN 数据库 |
| .ldf | config/ingest_lin.ldf | 格式合成 | 最小合法 LIN 描述文件 |
| .a2l | config/RecordLayoutsColumnDir13.a2l | 官方拷贝 | ASAP2 记录布局 |
| .md | config/README.md | 官方拷贝 | 第三方组件说明 |

### ZIP/工具容器（16）

| 扩展名 | 位置 | 来源 | 说明 |
|---|---|---|---|
| .slx | model/asbCubeSatMBSE、model/VirtualVehicle | 官方拷贝 | CubeSat 模型 + VirtualVehicle 整车/控制器/悬架等 248 个模型 |
| .sldd | model/VirtualVehicle/VehicleData/Dictionaries/*.sldd | 官方拷贝 | 数据字典（含 18 MB 的环境字典） |
| .mlx | model/asbCubeSatMBSE/MissionAnalysis/*.mlx | 官方拷贝 | 官方 Live Script |
| .mlapp | src/bertool.mlapp | 官方拷贝 | Communications Toolbox App |
| .mlproj | packages/MatlabIngestFixture.mlproj | 官方流程生成 | `export(proj,...)` 工程归档 |
| .mltbx | packages/IngestFixtureToolbox.mltbx | 官方流程生成 | `packageToolbox` |
| .mlappinstall | packages/IngestFixtureApp.mlappinstall | 格式合成 | 参照 .mltbx 的 OPC 结构 |
| .sltx | packages/asbCubeSatMBSEProject.sltx | 官方拷贝 | 官方工程模板原件 |
| .mlpkginstall | packages/IngestFixtureSupport.mlpkginstall | 格式合成 | 最小支持包结构 |
| .slreqx | model/asbCubeSatMBSE/CubeSatRequirements/*.slreqx | 官方拷贝 | 需求集 |
| .slmx | model/asbCubeSatMBSE/CubeSatRequirements/asbCubeSatArchModel.slmx | 官方拷贝 | 需求链接文件 |
| .mldatx | model/asbCubeSatMBSE/MissionAnalysis/SystemTests/systemTests.mldatx | 官方拷贝 | Simulink Test 文件 |
| .sfx | model/TargetStateChart.sfx | 官方拷贝 | Stateflow 相关容器 |
| .fmu | packages/VvcFmuEngExl.fmu | 官方拷贝 | 取自 autoblks SI.zip 内的官方 FMU |
| .ctf | packages/mps_check.ctf | 官方拷贝 | Compiler 组件包 |
| .jar | packages/addons.jar | 官方拷贝 | Java 库 |

### 数据/目标二进制（10）

| 扩展名 | 位置 | 来源 | 说明 |
|---|---|---|---|
| .hex | bin/ingest_firmware.hex | 官方派生 | 由官方 bin 转 Intel HEX，取前 8 KB |
| .s19 | bin/ingest_firmware.s19 | 官方派生 | 同上转 Motorola S3 记录 |
| .mat | data/flames.mat、model/VirtualVehicle/**/*.mat | 官方拷贝 | 官方示例与标定数据 |
| .fig | data/teapotdemo.fig | 官方拷贝 | 官方图窗 |
| .mdf | data/ingest_measurement.mdf | 官方流程生成 | `mdfWrite`，数据源自官方 outages.csv |
| .mf4 | data/ingest_measurement.mf4 | 官方流程生成 | 同上，MDF4 |
| .blf | data/ingest_canlog.blf | 官方流程生成 | `blfwrite` 写入构造的 CAN 报文 |
| .elf | bin/visionzynq-target-eventhandler.elf | 官方拷贝 | SoC/Zynq 目标 ELF |
| .bin | bin/snapshot_blob.bin | 官方拷贝 | 官方二进制 |

### Windows 原生（6）

| 扩展名 | 位置 | 来源 | 说明 |
|---|---|---|---|
| .mexw64 | src/componentinfo.mexw64 | 官方拷贝 | Compiler 提供的 MEX |
| .dll | bin/fmu2ProxyWrapper.dll | 官方拷贝 | FMI 代理 DLL |
| .exe | bin/AddOnInstaller.exe、build/EvPowertrainController2EM.exe | 官方拷贝 + 官方流程生成 | 后者由真实控制器模型生成 |
| .lib | bin/GecodeDriver.lib | 官方拷贝 | 导入库 |
| .obj | bin/lcccrt0.obj、build/*_grt_rtw/*.obj | 官方拷贝 + 官方流程生成 | 目标文件 |
| .pdb | bin/libMatlabCppSharedLib25_2.pdb | 官方拷贝 | 调试符号 |

### 加密/保护（4）

| 扩展名 | 位置 | 来源 | 说明 |
|---|---|---|---|
| .ctf | packages/mps_check.ctf | 官方拷贝 | 见上 |
| .p | src/autoblkscheckparams.p | 官方拷贝 | P-code |
| .slxp | packages/EvPowertrainController2EM.slxp | 官方流程生成 | 对真实控制器调用 `Simulink.ModelReference.protect` |
| .sscp | src/add_rf.sscp | 官方拷贝 | 受保护 Simscape 组件 |

### 派生/缓存（2）

| 扩展名 | 位置 | 来源 | 说明 |
|---|---|---|---|
| .slxc | cache/EvPowertrainController2EM.slxc | 官方流程生成 | 仿真缓存，`fileGenControl` 指定 cache 目录后由仿真产生 |
| .autosave | model/VirtualVehicle/.../EvPowertrainController2EM.slx.autosave | 官方流程生成 | 模型更新时 Simulink 自动备份 |

## 复现

`tools/build_fixture.m` 覆盖 MATLAB 侧可复现步骤：对 `EvPowertrainController2EM` 做代码生成（临时脱开配置引用、`UnderspecifiedInitializationDetection=Simplified`）、生成缓存、提取官方 FMU、写 MDF/MF4/BLF、打包工具箱、生成受保护模型、导出工程归档、触发 `.autosave`；`tools/make_artifacts.py` 负责格式合成与派生项。

代码生成前会把 `model/VirtualVehicle` 全部加入路径，让控制器模型能解析到数据字典。

## 已知偏差

- `.dbc`、`.ldf`、`.mlappinstall`、`.mlpkginstall` 官方既无现成文件也无编程式产出接口，按公开格式写的最小合法文件。
- `.hex`、`.s19` 由官方 `.bin` 转换而来，不是目标编译器产物。
- `.asv` 是编辑器自动备份，MATLAB 在文档关闭时会删除，这里留的是关闭前的副本。
- 代码生成与受保护模型使用临时脱开的配置集（GRT 目标、定步长），官方 `.slx` 文件本身已恢复为原样，未把构建配置写回。
- `build/`、`cache/`、`*.slx.autosave` 均为 MATLAB 自动生成，未手工创建。
