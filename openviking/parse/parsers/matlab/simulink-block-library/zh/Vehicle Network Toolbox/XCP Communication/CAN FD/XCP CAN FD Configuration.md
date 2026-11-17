---
type: simulink-block
title: 'XCP CAN FD Configuration'
family: 'vnt'
product_id: 'vnt'
product_name: 'Vehicle Network Toolbox'
documentation_release: R2025b
official_category: 'XCP Communication / CAN FD'
documentation_page: 'xcpcanfdconfiguration'
documentation_source_path: 'ug/xcpcanfdconfiguration.html'
language: zh-CN
chinese_source: worker-translation
---

# XCP CAN FD Configuration

## 端口

R2025b 中未记录。

## 参数

### **Config name** — 指定 XCP CAN FD 会话名称 `'CAN FD_Config1'`（默认）

为您的 XCP CAN FD 会话指定一个唯一名称。

### **A2L File** — 选择 A2L 文件 文件名

点击 **Browse** 为您的 XCP CAN FD 会话选择 A2L 文件。

### **Enable seed/key security** — 选择建立连接所需的密钥 `off`（默认）| `on`

如果您的服务器需要安全密钥才能建立连接，请选择此选项。使用 **File (\*DLL)** 参数指定包含种子/密钥定义的 DLL 文件。**注意：** Linux® 系统不支持种子/密钥安全功能。

### **File (\*.DLL)** — 选择种子和密钥安全文件 文件名

如果您选择了 **Enable seed/key security**（`EnableSecurity`），此字段将启用。点击 **Browse** 选择包含种子和密钥安全算法的文件，该算法用于解锁 XCP 服务器模块。此参数在 Vehicle Network Toolbox™ 的 Windows 桌面仿真中可用。

**File (\*.DLL)** 参数指定包含种子和密钥安全算法的 DLL 文件名，该算法用于解锁 XCP 服务器模块。该文件根据 ASAM 标准定义，定义了从给定种子生成访问密钥的算法。有关文件格式和 API 的信息，请参阅 Vector 网页 Steps to Use Seed&Key Option in CANape 或 National Instruments™ CAN ECU Measurement and Calibration Toolkit User Manual 中的 "Seed and Key Algorithm"。**注意：** DLL 必须与 MATLAB 具有相同的位数（64 位）。

### **User-defined connect mode** — 允许特殊连接模式 `off`（默认）| `on`

选择此选项以允许特殊（用户定义的）连接模式。当为 `off` 时，仅支持正常模式连接。

### **Output connection status** — 显示连接状态 `off`（默认）| `on`

选择此选项以显示与服务器模块的连接状态。选择此选项会添加一个新的输出端口。

## 所属库

Vehicle Network Toolbox / XCP Communication / CAN FD Simulink Real-Time / XCP / CAN FD

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

XCP 通信模块支持代码生成，但部署可移植性有限，仅能在主机或 Simulink Real-Time™ 目标上运行。

代码生成需要与代码生成目标兼容的 C++ 编译器。有关更多信息，请参阅 Supported and Compatible Compilers。

## 版本历史

**在 R2022b 中引入**

### R2024b：新参数：User-defined connect mode

参数 **User-defined connect mode** 允许使用特殊连接模式。

## 描述

配置 XCP 服务器连接

XCP CAN FD Configuration 模块使用 A2L 文件和 ASAP2 数据库中指定的参数来建立 XCP 服务器连接。

在采集或激励数据之前，请在 XCP CAN FD Configuration 中指定要使用的 A2L 文件。使用一个 XCP CAN FD Configuration 来配置一个用于数据采集或激励的服务器连接。如果您添加了 XCP CAN FD Data Acquisition 和 XCP CAN FD Data Stimulation 模块，您的模型会检查是否存在对应的 XCP CAN FD Configuration 模块。如果没有对应的 XCP CAN FD Configuration 模块，模型编辑器会提示您添加一个。

XCP CAN FD 通信模块支持 Simulink® 加速模式和快速加速模式。您可以使用这些模式加速 Simulink 模型的执行。有关这些仿真模式的更多信息，请参阅 Acceleration (Simulink)。
