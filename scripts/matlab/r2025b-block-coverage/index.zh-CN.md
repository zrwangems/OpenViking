# MathWorks R2025b 块库覆盖与缺口

完整性以每个官方产品的 `referencelist_block_cat.xml` 为准，递归保留所有子库以及 `block`、`simscapeblock`。条目数表示块在库中的出现次数，同一文档可以属于多个库。

- 官方产品目录条目：**75**
- 枚举到块库的产品：**75**
- 没有官方块库 XML 的产品：**0**（不是静默跳过，也不冒充第三方空库）
- 产品→库→块条目：**4565**
- 产品内独立文档路径：**3812**
- 已有完整英文文档：**3812**；中文文档：**3812**
- 待补完整英文文档：**0**；中文文档：**0**

第三方、硬件支持包和用户本机授权库不在公开产品总目录内，需要从用户 MATLAB 安装实例枚举，不能凭空生成。抓取失败、无权限和正文缺失都单独记为缺口，不把只有元数据的条目称为完整文档。

| 产品 | 库中块条目 | 独立文档路径 | 状态 |
| --- | ---: | ---: | --- |
| Simulink (`simulink`) | 511 | 350 | enumerated / 已枚举 |
| Aerospace Blockset (`aeroblks`) | 150 | 141 | enumerated / 已枚举 |
| Audio Toolbox (`audio`) | 50 | 49 | enumerated / 已枚举 |
| Automated Driving Toolbox (`driving`) | 34 | 33 | enumerated / 已枚举 |
| AUTOSAR Blockset (`autosar`) | 9 | 9 | enumerated / 已枚举 |
| Battery (`simscape-battery`) | 45 | 45 | enumerated / 已枚举 |
| C2000 Microcontroller Blockset (`ti-c2000`) | 533 | 105 | enumerated / 已枚举 |
| Communications Toolbox (`comm`) | 180 | 174 | enumerated / 已枚举 |
| Communications Toolbox HDL Support (`communications-toolbox-hdl-support`) | 25 | 25 | enumerated / 已枚举 |
| Computer Vision Toolbox (`vision`) | 74 | 73 | enumerated / 已枚举 |
| Control System Toolbox (`control`) | 24 | 24 | enumerated / 已枚举 |
| Data Acquisition Toolbox (`daq`) | 6 | 6 | enumerated / 已枚举 |
| DDS Blockset (`dds`) | 2 | 2 | enumerated / 已枚举 |
| Deep Learning Toolbox (`deeplearning`) | 87 | 81 | enumerated / 已枚举 |
| Driveline (`sdl`) | 100 | 100 | enumerated / 已枚举 |
| DSP HDL Toolbox (`dsphdl`) | 18 | 17 | enumerated / 已枚举 |
| DSP System Toolbox (`dsp`) | 237 | 219 | enumerated / 已枚举 |
| DSP System Toolbox HDL Support (`dsp-system-toolbox-hdl-support`) | 27 | 27 | enumerated / 已枚举 |
| Electrical (`sps`) | 405 | 401 | enumerated / 已枚举 |
| Embedded Coder (`ecoder`) | 14 | 14 | enumerated / 已枚举 |
| Fixed-Point Designer (`fixedpoint`) | 2 | 2 | enumerated / 已枚举 |
| Fixed-Point Designer HDL Support (`fixed-point-designer-hdl-support`) | 42 | 42 | enumerated / 已枚举 |
| Fluids (`hydro`) | 207 | 207 | enumerated / 已枚举 |
| Foundation Library (`simscape`) | 272 | 272 | enumerated / 已枚举 |
| Fuzzy Logic Toolbox (`fuzzy`) | 19 | 19 | enumerated / 已枚举 |
| HDL Coder (`hdlcoder`) | 262 | 185 | enumerated / 已枚举 |
| HDL Verifier (`hdlverifier`) | 8 | 4 | enumerated / 已枚举 |
| Image Acquisition Toolbox (`imaq`) | 1 | 1 | enumerated / 已枚举 |
| Industrial Communication Toolbox (`icomm`) | 6 | 6 | enumerated / 已枚举 |
| Instrument Control Toolbox (`instrument`) | 10 | 10 | enumerated / 已枚举 |
| libsb2sl (`libsb2sl`) | 9 | 9 | enumerated / 已枚举 |
| Lidar Toolbox (`lidar`) | 1 | 1 | enumerated / 已枚举 |
| Mixed-Signal Blockset (`msblks`) | 47 | 47 | enumerated / 已枚举 |
| Model Predictive Control Toolbox (`mpc`) | 11 | 11 | enumerated / 已枚举 |
| Motor Control Blockset (`mcb`) | 77 | 77 | enumerated / 已枚举 |
| Motor Control Blockset HDL Support (`motor-control-blockset-hdl-support`) | 29 | 29 | enumerated / 已枚举 |
| Multibody (`sm`) | 73 | 73 | enumerated / 已枚举 |
| Navigation Toolbox (`nav`) | 11 | 11 | enumerated / 已枚举 |
| Network Couplers (`network-couplers`) | 14 | 14 | enumerated / 已枚举 |
| Phased Array System Toolbox (`phased`) | 80 | 80 | enumerated / 已枚举 |
| Powertrain Blockset (`autoblks`) | 48 | 45 | enumerated / 已枚举 |
| Radar Toolbox (`radar`) | 12 | 12 | enumerated / 已枚举 |
| Reinforcement Learning (`reinforcement-learning`) | 2 | 2 | enumerated / 已枚举 |
| Report Generator (`report-generator`) | 0 | 0 | enumerated / 已枚举 |
| Requirements Toolbox (`slrequirements`) | 2 | 2 | enumerated / 已枚举 |
| RF Blockset (`simrf`) | 100 | 98 | enumerated / 已枚举 |
| Robotics System Toolbox (`robotics`) | 39 | 39 | enumerated / 已枚举 |
| Robust Control Toolbox (`robust`) | 2 | 2 | enumerated / 已枚举 |
| ROS Toolbox (`ros`) | 37 | 30 | enumerated / 已枚举 |
| Satellite Communications Toolbox (`satcom`) | 2 | 2 | enumerated / 已枚举 |
| Sensor Fusion and Tracking Toolbox (`fusion`) | 20 | 20 | enumerated / 已枚举 |
| SerDes Toolbox (`serdes`) | 18 | 18 | enumerated / 已枚举 |
| Signal Integrity Toolbox (`signal-integrity`) | 1 | 1 | enumerated / 已枚举 |
| SimEvents (`simevents`) | 30 | 30 | enumerated / 已枚举 |
| Simscape (`simscape-root`) | 0 | 0 | enumerated / 已枚举 |
| Simulink 3D Animation (`sl3d`) | 20 | 20 | enumerated / 已枚举 |
| Simulink Coder (`rtw`) | 14 | 14 | enumerated / 已枚举 |
| Simulink Control Design (`slcontrol`) | 37 | 34 | enumerated / 已枚举 |
| Simulink Design Optimization (`sldo`) | 11 | 8 | enumerated / 已枚举 |
| Simulink Design Verifier (`sldv`) | 9 | 9 | enumerated / 已枚举 |
| Simulink Desktop Real-Time (`sldrt`) | 20 | 20 | enumerated / 已枚举 |
| Simulink Extras (`simulink-extras`) | 29 | 22 | enumerated / 已枚举 |
| Simulink Fault Analyzer (`fault-analyzer`) | 4 | 4 | enumerated / 已枚举 |
| Simulink Real-Time (`slrealtime`) | 78 | 76 | enumerated / 已枚举 |
| Simulink Test (`sltest`) | 5 | 5 | enumerated / 已枚举 |
| SoC Blockset (`soc`) | 41 | 41 | enumerated / 已枚举 |
| Stateflow (`stateflow`) | 4 | 4 | enumerated / 已枚举 |
| Statistics and Machine Learning Toolbox (`stats`) | 29 | 29 | enumerated / 已枚举 |
| System Identification Toolbox (`ident`) | 14 | 14 | enumerated / 已枚举 |
| UAV Toolbox (`uav`) | 31 | 31 | enumerated / 已枚举 |
| Utilities (`utilities`) | 24 | 24 | enumerated / 已枚举 |
| Vehicle Dynamics Blockset (`vdynblks`) | 64 | 56 | enumerated / 已枚举 |
| Vehicle Network Toolbox (`vnt`) | 28 | 28 | enumerated / 已枚举 |
| Vision HDL Toolbox (`visionhdl`) | 31 | 30 | enumerated / 已枚举 |
| Wireless HDL Toolbox (`wireless-hdl`) | 47 | 47 | enumerated / 已枚举 |
