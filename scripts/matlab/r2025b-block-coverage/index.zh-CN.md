# MathWorks R2025b 块库覆盖与缺口

完整性以每个官方产品的 `referencelist_block_cat.xml` 为准，递归保留所有子库以及 `block`、`simscapeblock`。条目数表示块在库中的出现次数，同一文档可以属于多个库。

- 官方产品目录条目：**60**
- 枚举到块库的产品：**60**
- 没有官方块库 XML 的产品：**0**（不是静默跳过，也不冒充第三方空库）
- 产品→库→块条目：**3899**
- 产品内独立文档路径：**3404**
- 已有完整英文文档：**3404**；中文文档：**3404**
- 待补完整英文文档：**0**；中文文档：**0**

第三方、硬件支持包和用户本机授权库不在公开产品总目录内，需要从用户 MATLAB 安装实例枚举，不能凭空生成。抓取失败、无权限和正文缺失都单独记为缺口，不把只有元数据的条目称为完整文档。

| 产品 | 库中块条目 | 独立文档路径 | 状态 |
| --- | ---: | ---: | --- |
| Simulink (`simulink`) | 341 | 333 | enumerated / 已枚举 |
| Aerospace Blockset (`aeroblks`) | 247 | 205 | enumerated / 已枚举 |
| Audio Toolbox (`audio`) | 54 | 52 | enumerated / 已枚举 |
| Automated Driving Toolbox (`driving`) | 33 | 32 | enumerated / 已枚举 |
| AUTOSAR Blockset (`autosar`) | 31 | 29 | enumerated / 已枚举 |
| C2000 Microcontroller Blockset (`ti-c2000`) | 132 | 117 | enumerated / 已枚举 |
| Communications Toolbox (`comm`) | 216 | 197 | enumerated / 已枚举 |
| Computer Vision Toolbox (`vision`) | 84 | 77 | enumerated / 已枚举 |
| Control System Toolbox (`control`) | 41 | 25 | enumerated / 已枚举 |
| Data Acquisition Toolbox (`daq`) | 6 | 6 | enumerated / 已枚举 |
| DDS Blockset (`dds`) | 2 | 2 | enumerated / 已枚举 |
| Deep Learning Toolbox (`deeplearning`) | 72 | 66 | enumerated / 已枚举 |
| DSP HDL Toolbox (`dsphdl`) | 18 | 18 | enumerated / 已枚举 |
| DSP System Toolbox (`dsp`) | 267 | 222 | enumerated / 已枚举 |
| Embedded Coder (`ecoder`) | 273 | 194 | enumerated / 已枚举 |
| Fixed-Point Designer (`fixedpoint`) | 47 | 47 | enumerated / 已枚举 |
| Fuzzy Logic Toolbox (`fuzzy`) | 20 | 19 | enumerated / 已枚举 |
| HDL Coder (`hdlcoder`) | 51 | 51 | enumerated / 已枚举 |
| HDL Verifier (`hdlverifier`) | 11 | 8 | enumerated / 已枚举 |
| Image Acquisition Toolbox (`imaq`) | 1 | 1 | enumerated / 已枚举 |
| Industrial Communication Toolbox (`icomm`) | 6 | 6 | enumerated / 已枚举 |
| Instrument Control Toolbox (`instrument`) | 18 | 10 | enumerated / 已枚举 |
| Lidar Toolbox (`lidar`) | 1 | 1 | enumerated / 已枚举 |
| Mixed-Signal Blockset (`msblks`) | 47 | 47 | enumerated / 已枚举 |
| Model Predictive Control Toolbox (`mpc`) | 20 | 11 | enumerated / 已枚举 |
| Motor Control Blockset (`mcb`) | 83 | 83 | enumerated / 已枚举 |
| Navigation Toolbox (`nav`) | 12 | 11 | enumerated / 已枚举 |
| Phased Array System Toolbox (`phased`) | 84 | 80 | enumerated / 已枚举 |
| Powertrain Blockset (`autoblks`) | 64 | 63 | enumerated / 已枚举 |
| Radar Toolbox (`radar`) | 28 | 28 | enumerated / 已枚举 |
| Reinforcement Learning Toolbox (`reinforcement-learning`) | 6 | 2 | enumerated / 已枚举 |
| Requirements Toolbox (`slrequirements`) | 2 | 2 | enumerated / 已枚举 |
| RF Blockset (`simrf`) | 130 | 100 | enumerated / 已枚举 |
| Robotics System Toolbox (`robotics`) | 56 | 51 | enumerated / 已枚举 |
| Robust Control Toolbox (`robust`) | 4 | 3 | enumerated / 已枚举 |
| ROS Toolbox (`ros`) | 65 | 33 | enumerated / 已枚举 |
| Satellite Communications Toolbox (`satcom`) | 3 | 3 | enumerated / 已枚举 |
| Sensor Fusion and Tracking Toolbox (`fusion`) | 20 | 20 | enumerated / 已枚举 |
| SerDes Toolbox (`serdes`) | 18 | 18 | enumerated / 已枚举 |
| Signal Integrity Toolbox (`signal-integrity`) | 2 | 1 | enumerated / 已枚举 |
| SimEvents (`simevents`) | 36 | 29 | enumerated / 已枚举 |
| Simscape (`simscape`) | 276 | 275 | enumerated / 已枚举 |
| Simulink 3D Animation (`sl3d`) | 36 | 36 | enumerated / 已枚举 |
| Simulink Coder (`rtw`) | 190 | 184 | enumerated / 已枚举 |
| Simulink Control Design (`slcontrol`) | 63 | 49 | enumerated / 已枚举 |
| Simulink Design Optimization (`sldo`) | 11 | 8 | enumerated / 已枚举 |
| Simulink Design Verifier (`sldv`) | 15 | 10 | enumerated / 已枚举 |
| Simulink Desktop Real-Time (`sldrt`) | 20 | 20 | enumerated / 已枚举 |
| Simulink Fault Analyzer (`fault-analyzer`) | 4 | 4 | enumerated / 已枚举 |
| Simulink Real-Time (`slrealtime`) | 108 | 87 | enumerated / 已枚举 |
| Simulink Test (`sltest`) | 7 | 6 | enumerated / 已枚举 |
| SoC Blockset (`soc`) | 108 | 94 | enumerated / 已枚举 |
| Stateflow (`stateflow`) | 10 | 4 | enumerated / 已枚举 |
| Statistics and Machine Learning Toolbox (`stats`) | 98 | 35 | enumerated / 已枚举 |
| System Identification Toolbox (`ident`) | 22 | 14 | enumerated / 已枚举 |
| UAV Toolbox (`uav`) | 70 | 70 | enumerated / 已枚举 |
| Vehicle Dynamics Blockset (`vdynblks`) | 89 | 89 | enumerated / 已枚举 |
| Vehicle Network Toolbox (`vnt`) | 31 | 31 | enumerated / 已枚举 |
| Vision HDL Toolbox (`visionhdl`) | 38 | 34 | enumerated / 已枚举 |
| Wireless HDL Toolbox (`wireless-hdl`) | 51 | 51 | enumerated / 已枚举 |
