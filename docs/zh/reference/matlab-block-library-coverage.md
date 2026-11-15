# MathWorks R2025b 块库覆盖与缺口

完整性以每个官方产品的 `referencelist_block_cat.xml` 为准，递归保留所有子库以及 `block`、`simscapeblock`。条目数表示块在库中的出现次数，同一文档可以属于多个库。

- 官方产品目录条目：**133**
- 枚举到块库的产品：**74**
- 没有官方块库 XML 的产品：**59**（不是静默跳过，也不冒充第三方空库）
- 产品→库→块条目：**5431**
- 产品内独立文档路径：**4603**
- 已有完整英文文档：**4603**；中文文档：**4603**
- 待补完整英文文档：**0**；中文文档：**0**

第三方、硬件支持包和用户本机授权库不在公开产品总目录内，需要从用户 MATLAB 安装实例枚举，不能凭空生成。抓取失败、无权限和正文缺失都单独记为缺口，不把只有元数据的条目称为完整文档。

| 产品 | 库中块条目 | 独立文档路径 | 状态 |
| --- | ---: | ---: | --- |
| 5G Toolbox (`5g`) | 1 | 1 | enumerated / 已枚举 |
| Aerospace Blockset (`aeroblks`) | 247 | 205 | enumerated / 已枚举 |
| Aerospace Toolbox (`aerotbx`) | 0 | 0 | no block XML / 无块库 XML |
| Antenna Toolbox (`antenna`) | 0 | 0 | no block XML / 无块库 XML |
| Audio Toolbox (`audio`) | 54 | 52 | enumerated / 已枚举 |
| Powertrain Blockset (`autoblks`) | 64 | 63 | enumerated / 已枚举 |
| AUTOSAR Blockset (`autosar`) | 31 | 29 | enumerated / 已枚举 |
| Bioinformatics Toolbox (`bioinfo`) | 0 | 0 | no block XML / 无块库 XML |
| Bluetooth Toolbox (`bluetooth`) | 1 | 1 | enumerated / 已枚举 |
| Polyspace Bug Finder (`bugfinder`) | 0 | 0 | no block XML / 无块库 XML |
| IEC Certification Kit (`certkitiec`) | 0 | 0 | no block XML / 无块库 XML |
| Cloud Integrations (`cloudcenter`) | 0 | 0 | no block XML / 无块库 XML |
| Polyspace Code Prover (`codeprover`) | 0 | 0 | no block XML / 无块库 XML |
| MATLAB Coder (`coder`) | 27 | 27 | enumerated / 已枚举 |
| Communications Toolbox (`comm`) | 216 | 197 | enumerated / 已枚举 |
| MATLAB Compiler (`compiler`) | 0 | 0 | no block XML / 无块库 XML |
| MATLAB Compiler SDK (`compiler_sdk`) | 0 | 0 | no block XML / 无块库 XML |
| Control System Toolbox (`control`) | 41 | 25 | enumerated / 已枚举 |
| Curve Fitting Toolbox (`curvefit`) | 0 | 0 | no block XML / 无块库 XML |
| Data Acquisition Toolbox (`daq`) | 6 | 6 | enumerated / 已枚举 |
| Database Toolbox (`database`) | 0 | 0 | no block XML / 无块库 XML |
| Datafeed Toolbox (`datafeed`) | 0 | 0 | no block XML / 无块库 XML |
| DDS Blockset (`dds`) | 2 | 2 | enumerated / 已枚举 |
| Deep Learning HDL Toolbox (`deep-learning-hdl`) | 3 | 3 | enumerated / 已枚举 |
| Deep Learning Toolbox (`deeplearning`) | 72 | 66 | enumerated / 已枚举 |
| Automated Driving Toolbox (`driving`) | 33 | 32 | enumerated / 已枚举 |
| DSP System Toolbox (`dsp`) | 267 | 222 | enumerated / 已枚举 |
| DSP HDL Toolbox (`dsphdl`) | 18 | 18 | enumerated / 已枚举 |
| Embedded Coder (`ecoder`) | 273 | 194 | enumerated / 已枚举 |
| Econometrics Toolbox (`econ`) | 0 | 0 | no block XML / 无块库 XML |
| Spreadsheet Link (`exlink`) | 0 | 0 | no block XML / 无块库 XML |
| Simulink Fault Analyzer (`fault-analyzer`) | 4 | 4 | enumerated / 已枚举 |
| Financial Toolbox (`finance`) | 0 | 0 | no block XML / 无块库 XML |
| Financial Instruments Toolbox (`fininst`) | 0 | 0 | no block XML / 无块库 XML |
| Fixed-Point Designer (`fixedpoint`) | 47 | 47 | enumerated / 已枚举 |
| Sensor Fusion and Tracking Toolbox (`fusion`) | 20 | 20 | enumerated / 已枚举 |
| Fuzzy Logic Toolbox (`fuzzy`) | 20 | 19 | enumerated / 已枚举 |
| Global Optimization Toolbox (`gads`) | 0 | 0 | no block XML / 无块库 XML |
| GPU Coder (`gpucoder`) | 0 | 0 | no block XML / 无块库 XML |
| HDL Coder (`hdlcoder`) | 51 | 51 | enumerated / 已枚举 |
| HDL Verifier (`hdlverifier`) | 11 | 8 | enumerated / 已枚举 |
| Simscape Fluids (`hydro`) | 214 | 208 | enumerated / 已枚举 |
| Industrial Communication Toolbox (`icomm`) | 6 | 6 | enumerated / 已枚举 |
| System Identification Toolbox (`ident`) | 22 | 14 | enumerated / 已枚举 |
| Image Processing Toolbox (`images`) | 0 | 0 | no block XML / 无块库 XML |
| Image Acquisition Toolbox (`imaq`) | 1 | 1 | enumerated / 已枚举 |
| Installation and Licensing (`install`) | 0 | 0 | no block XML / 无块库 XML |
| Instrument Control Toolbox (`instrument`) | 18 | 10 | enumerated / 已枚举 |
| Lidar Toolbox (`lidar`) | 1 | 1 | enumerated / 已枚举 |
| LTE Toolbox (`lte`) | 1 | 1 | enumerated / 已枚举 |
| Mapping Toolbox (`map`) | 0 | 0 | no block XML / 无块库 XML |
| MATLAB (`matlab`) | 0 | 0 | no block XML / 无块库 XML |
| MATLAB and Simulink Online Courses (`matlab-and-simulink-online-courses`) | 0 | 0 | no block XML / 无块库 XML |
| MATLAB Copilot (`matlab-copilot`) | 0 | 0 | no block XML / 无块库 XML |
| MATLAB Online Server (`matlab-online-server`) | 0 | 0 | no block XML / 无块库 XML |
| MATLAB Parallel Server (`matlab-parallel-server`) | 0 | 0 | no block XML / 无块库 XML |
| MATLAB Test (`matlab-test`) | 0 | 0 | no block XML / 无块库 XML |
| MATLAB Grader (`matlabgrader`) | 0 | 0 | no block XML / 无块库 XML |
| MATLAB Mobile (`matlabmobile`) | 0 | 0 | no block XML / 无块库 XML |
| Model-Based Calibration Toolbox (`mbc`) | 0 | 0 | no block XML / 无块库 XML |
| Motor Control Blockset (`mcb`) | 83 | 83 | enumerated / 已枚举 |
| Medical Imaging Toolbox (`medical-imaging`) | 0 | 0 | no block XML / 无块库 XML |
| Model Predictive Control Toolbox (`mpc`) | 20 | 11 | enumerated / 已枚举 |
| MATLAB Production Server (`mps`) | 0 | 0 | no block XML / 无块库 XML |
| Mixed-Signal Blockset (`msblks`) | 47 | 47 | enumerated / 已枚举 |
| Navigation Toolbox (`nav`) | 12 | 11 | enumerated / 已枚举 |
| Optimization Toolbox (`optim`) | 0 | 0 | no block XML / 无块库 XML |
| Parallel Computing Toolbox (`parallel-computing`) | 0 | 0 | no block XML / 无块库 XML |
| Partial Differential Equation Toolbox (`pde`) | 0 | 0 | no block XML / 无块库 XML |
| Phased Array System Toolbox (`phased`) | 84 | 80 | enumerated / 已枚举 |
| Simulink PLC Coder (`plccoder`) | 52 | 52 | enumerated / 已枚举 |
| Polyspace Access (`polyspace_access`) | 0 | 0 | no block XML / 无块库 XML |
| Polyspace Products for Ada (`polyspace_ada`) | 0 | 0 | no block XML / 无块库 XML |
| Polyspace Test (`polyspace_test`) | 0 | 0 | no block XML / 无块库 XML |
| Predictive Maintenance Toolbox (`predmaint`) | 0 | 0 | no block XML / 无块库 XML |
| DO Qualification Kit (`qualkitdo`) | 0 | 0 | no block XML / 无块库 XML |
| Radar Toolbox (`radar`) | 28 | 28 | enumerated / 已枚举 |
| Reinforcement Learning Toolbox (`reinforcement-learning`) | 6 | 2 | enumerated / 已枚举 |
| RF Toolbox (`rf`) | 0 | 0 | no block XML / 无块库 XML |
| RF PCB Toolbox (`rfpcb`) | 0 | 0 | no block XML / 无块库 XML |
| Risk Management Toolbox (`risk`) | 0 | 0 | no block XML / 无块库 XML |
| RoadRunner (`roadrunner`) | 0 | 0 | no block XML / 无块库 XML |
| RoadRunner Scenario (`roadrunner-scenario`) | 0 | 0 | no block XML / 无块库 XML |
| Robotics System Toolbox (`robotics`) | 56 | 51 | enumerated / 已枚举 |
| Robust Control Toolbox (`robust`) | 4 | 3 | enumerated / 已枚举 |
| ROS Toolbox (`ros`) | 65 | 33 | enumerated / 已枚举 |
| MATLAB Report Generator (`rptgen`) | 0 | 0 | no block XML / 无块库 XML |
| Simulink Report Generator (`rptgenext`) | 0 | 0 | no block XML / 无块库 XML |
| Simulink Coder (`rtw`) | 190 | 184 | enumerated / 已枚举 |
| Satellite Communications Toolbox (`satcom`) | 3 | 3 | enumerated / 已枚举 |
| Simscape Driveline (`sdl`) | 146 | 100 | enumerated / 已枚举 |
| SerDes Toolbox (`serdes`) | 18 | 18 | enumerated / 已枚举 |
| Signal Processing Toolbox (`signal`) | 0 | 0 | no block XML / 无块库 XML |
| Signal Integrity Toolbox (`signal-integrity`) | 2 | 1 | enumerated / 已枚举 |
| SimBiology (`simbio`) | 0 | 0 | no block XML / 无块库 XML |
| SimEvents (`simevents`) | 36 | 29 | enumerated / 已枚举 |
| RF Blockset (`simrf`) | 130 | 100 | enumerated / 已枚举 |
| Simscape (`simscape`) | 276 | 275 | enumerated / 已枚举 |
| Simscape Battery (`simscape-battery`) | 54 | 54 | enumerated / 已枚举 |
| Simulink (`simulink`) | 839 | 579 | enumerated / 已枚举 |
| Simulink 3D Animation (`sl3d`) | 36 | 36 | enumerated / 已枚举 |
| Simulink Check (`slcheck`) | 0 | 0 | no block XML / 无块库 XML |
| Simulink Code Inspector (`slci`) | 0 | 0 | no block XML / 无块库 XML |
| Simulink Compiler (`slcompiler`) | 0 | 0 | no block XML / 无块库 XML |
| Simulink Control Design (`slcontrol`) | 63 | 49 | enumerated / 已枚举 |
| Simulink Coverage (`slcoverage`) | 0 | 0 | no block XML / 无块库 XML |
| Simulink Design Optimization (`sldo`) | 11 | 8 | enumerated / 已枚举 |
| Simulink Desktop Real-Time (`sldrt`) | 20 | 20 | enumerated / 已枚举 |
| Simulink Design Verifier (`sldv`) | 15 | 10 | enumerated / 已枚举 |
| Simulink Real-Time (`slrealtime`) | 108 | 87 | enumerated / 已枚举 |
| Requirements Toolbox (`slrequirements`) | 2 | 2 | enumerated / 已枚举 |
| Simulink Test (`sltest`) | 7 | 6 | enumerated / 已枚举 |
| Simscape Multibody (`sm`) | 96 | 75 | enumerated / 已枚举 |
| Simscape Multibody Link (`smlink`) | 0 | 0 | no block XML / 无块库 XML |
| SoC Blockset (`soc`) | 108 | 94 | enumerated / 已枚举 |
| Simscape Electrical (`sps`) | 422 | 416 | enumerated / 已枚举 |
| Stateflow (`stateflow`) | 10 | 4 | enumerated / 已枚举 |
| Statistics and Machine Learning Toolbox (`stats`) | 98 | 35 | enumerated / 已枚举 |
| Symbolic Math Toolbox (`symbolic`) | 0 | 0 | no block XML / 无块库 XML |
| System Composer (`systemcomposer`) | 14 | 12 | enumerated / 已枚举 |
| Text Analytics Toolbox (`textanalytics`) | 0 | 0 | no block XML / 无块库 XML |
| ThingSpeak (`thingspeak`) | 0 | 0 | no block XML / 无块库 XML |
| C2000 Microcontroller Blockset (`ti-c2000`) | 132 | 117 | enumerated / 已枚举 |
| UAV Toolbox (`uav`) | 70 | 70 | enumerated / 已枚举 |
| Vehicle Dynamics Blockset (`vdynblks`) | 89 | 89 | enumerated / 已枚举 |
| Computer Vision Toolbox (`vision`) | 84 | 77 | enumerated / 已枚举 |
| Vision HDL Toolbox (`visionhdl`) | 38 | 34 | enumerated / 已枚举 |
| Vehicle Network Toolbox (`vnt`) | 31 | 31 | enumerated / 已枚举 |
| Wavelet Toolbox (`wavelet`) | 0 | 0 | no block XML / 无块库 XML |
| MATLAB Web App Server (`webappserver`) | 0 | 0 | no block XML / 无块库 XML |
| Wireless HDL Toolbox (`wireless-hdl`) | 51 | 51 | enumerated / 已枚举 |
| Wireless Testbench (`wireless-testbench`) | 2 | 2 | enumerated / 已枚举 |
| WLAN Toolbox (`wlan`) | 1 | 1 | enumerated / 已枚举 |
