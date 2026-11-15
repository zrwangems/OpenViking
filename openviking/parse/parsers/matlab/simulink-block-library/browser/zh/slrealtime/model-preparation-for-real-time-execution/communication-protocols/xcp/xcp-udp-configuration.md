---
type: simulink-block
title: 'XCP UDP Configuration'
family: 'slrealtime'
product_id: 'slrealtime'
product_name: 'Simulink Real-Time'
documentation_release: R2025b
official_category: 'Model Preparation for Real-Time Execution / Communication Protocols / XCP'
documentation_page: 'xcpudpconfiguration'
documentation_source_path: 'io_ref/xcpudpconfiguration.html'
language: zh-CN
chinese_source: worker-translation
---

# XCP UDP Configuration

## 端口

R2025b 中未记录。

## 参数

### **配置名称** — 指定 XCP UDP 会话名称 `'UDP_Config1'`（默认）

为您的 XCP 会话指定唯一名称。

### **A2L 文件** — 选择 A2L 文件的文件名

点击 **Browse** 为您的 XCP 会话选择 A2L 文件。

### **启用种子/密钥安全** — 选择建立连接所需的密钥 `off`（默认）| `on`

如果您的服务器需要安全密钥来建立连接，请选择此选项。选择包含种子/密钥定义的文件以启用安全。**注意：** Linux® 系统不支持种子/密钥安全。

### **文件 (\*.DLL)** — 选择用于种子和密钥安全的文件名

如果选择**启用种子/密钥安全**，则启用此字段。点击 **Browse** 选择包含种子和密钥安全算法的文件，该算法用于解锁 XCP 服务器模块。此参数在 Vehicle Network Toolbox 的 Windows Desktop Simulation 中可用。

### **用户定义的连接模式** — 允许特殊连接模式 `off`（默认）| `on`

选择此选项以允许特殊（用户定义的）连接模式。当为 `off` 时，仅支持正常模式连接。

### **输出连接状态** — 显示连接状态 `off`（默认）| `on`

选择此选项以显示与服务器模块的连接状态。选择此选项会添加一个新的输出端口。

### **禁用 CTR 错误检测** — 禁用 CTR 错误检测方案 `on`（默认）| `off`

为了检测丢失的数据包，模块可以检查每个 XCP 数据包头部中的计数器值。当为 `on` 时，数据包头部的计数器错误检测被禁用。当为 `off` 时，启用计数器**错误检测方案**。

### **错误检测方案** — 选择 CTR 错误检测方案 `One counter for all CTOs and DTOs`（默认）| `Separate counters for (RES,ERR,EV,SERV) and (DAQ)` | `Separate counters for (RES,ERR), (EV,SERV) and (DAQ)`

为了检测丢失的数据包，模块可以检查每个 XCP 数据包头部中的计数器值并应用错误检测方案。

### **采样时间** — 模块的采样时间 `-1`（默认）| numeric

输入基本采样时间或基本采样时间的倍数。`-1` 表示继承采样时间。有关仿真采样定时的信息，请参阅 What Is Sample Time?。

### **本地 IP 地址** — 客户端 IP 地址 `x.x.x.x`

输入要连接到的 IP 地址。

### **本地端口** — 客户端 IP 端口 `1–65535`

**本地 IP 地址**和**本地端口**的组合必须唯一。

范围 `5500` 到 `5560` 内的端口保留用于 Simulink Real-Time 通信。

## 所属库

Vehicle Network Toolbox / XCP Communication / UDP Simulink Real-Time / XCP / UDP

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

XCP 通信模块支持代码生成，但部署可移植性有限，仅在主机或 Simulink Real-Time™ 目标上运行。

代码生成需要与代码生成目标兼容的 C++ 编译器。有关更多信息，请参阅 Supported and Compatible Compilers。

## 版本历史

**在 R2019a 中引入**

### R2024b：新参数：用户定义的连接模式

参数**用户定义的连接模式**允许特殊连接模式。

## 描述

配置 XCP UDP 服务器连接

XCP UDP Configuration 模块使用 A2L 文件和 ASAP2 数据库中指定的参数来建立 XCP 服务器连接。

在采集或激励数据之前，请指定要在 XCP UDP Configuration 中使用的 A2L 文件。使用一个 XCP UDP Configuration 为一个服务器连接配置数据采集或激励。如果您添加 XCP UDP Data Acquisition 和 XCP UDP Data Stimulation 模块，模型会检查是否存在对应的 XCP UDP Configuration 模块。如果没有对应的 XCP UDP Configuration 模块，模型会提示您添加一个。

XCP UDP 通信模块支持 Simulink® 加速模式和快速加速模式。您可以使用这些模式加速 Simulink 模型的执行。有关这些仿真模式的更多信息，请参阅 Acceleration。
