---
type: simulink-block
title: 'XCP UDP Configuration'
family: 'vnt'
product_id: 'vnt'
product_name: 'Vehicle Network Toolbox'
documentation_release: R2025b
official_category: 'XCP Communication / Communication in Simulink'
documentation_page: 'xcpudpconfiguration'
documentation_source_path: 'ug/xcpudpconfiguration.html'
language: zh-CN
chinese_source: official
---

# XCP UDP Configuration

## 端口

R2025b 官方文档未提供。

## 参数

### **配置名称** — 指定 XCP UDP 会话名称 `'UDP_Config1'` (默认)

为 XCP 会话指定唯一名称。

### **A2L 文件** — 选择 A2L 文件 文件名

点击**浏览**为 XCP 会话选择一个 A2L 文件。

### **启用种子/密钥安全性** — 选择建立连接所需的密钥 `off` (默认) | `on`

如果您的服务器需要安全密钥来建立连接，请选择此选项。选择一个包含种子/密钥定义的文件来启用安全性。**注意：**Linux® 系统不支持种子/密钥安全性。

### **文件(\*.DLL)** — 选择用于种子和密钥安全性的文件 文件名

如果选择**启用种子/密钥安全性**，则启用此字段。点击**浏览**以选择包含用于解锁 XCP 服务器模块的种子和密钥安全算法的文件。此参数在 Windows Desktop Simulation for Vehicle Network Toolbox 中可用。

### **用户定义的连接模式** — 允许特殊连接模式 `off` (默认) | `on`

选择此选项可允许使用特殊的（用户定义的）连接模式。当指定为 `off` 时，仅支持普通模式连接。

### **输出连接状态** — 显示连接状态 `off` (默认) | `on`

选择此选项可显示与服务器模块的连接的状态。选择此选项会添加一个新输出端口。

### **禁用 CTR 错误检测** — 禁用 CTR 错误检测方案 `on` (默认) | `off`

为了检测缺失数据包，模块可以检查每个 XCP 数据包头中的计数器值。当为 `on` 时，将禁用数据包头的计数器错误检测。当为 `off` 时，将启用**错误检测方案**。

### **错误检测方案** — 选择 CTR 错误检测方案 `One counter for all CTOs and DTOs` (默认) | `Separate counters for (RES,ERR,EV,SERV) and (DAQ)` | `Separate counters for (RES,ERR), (EV,SERV) and (DAQ)`

为了检测缺失数据包，模块可以检查每个 XCP 数据包头中的计数器值，并应用错误检测方案。

### **采样时间** — 模块的采样时间 `-1` (默认) | 数值

输入基础采样时间或基础采样时间的倍数。`-1` 表示继承采样时间。有关仿真采样时间的信息，请参阅硬件接口模型中的计时。

### **本地 IP 地址** — 客户端 IP 地址 `x.x.x.x`

输入您要连接到的 IP 地址。

### **本地端口** — 客户端 IP 端口 `1–65535`

**本地 IP 地址**和**本地端口**的组合必须唯一。

## 所属库

Vehicle Network Toolbox / XCP Communication / UDP Simulink Real-Time / XCP / UDP

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

XCP 通信模块支持仅在主机或 Simulink Real-Time™ 目标上运行的具有有限部署可移植性的代码生成。

代码生成需要与代码生成目标兼容的 C++ 编译器。有关详细信息，请参阅支持和兼容的编译器。

## 版本历史

**在 R2019a 中推出**

### R2024b: 新参数：用户定义的连接模式

参数**用户定义的连接模式**允许使用特殊连接模式。

## 描述

配置 XCP UDP 服务器连接

XCP UDP Configuration 模块使用 A2L 文件和 ASAP2 数据库中指定的参数来建立 XCP 服务器连接。

在采集或激励数据之前，请在 XCP UDP Configuration 中指定要使用的 A2L 文件。使用一个 XCP UDP Configuration 模块为数据采集或激励配置一个服务器连接。如果您添加 XCP UDP Data Acquisition 和 XCP UDP Data Stimulation 模块，您的模型会检查是否存在对应的 XCP UDP Configuration 模块。如果没有对应的 XCP UDP Configuration 模块，模型会提示您添加该模块。

XCP UDP 通信模块支持 Simulink® 加速模式和快速加速模式。使用这些模式可以加快 Simulink 模型的执行速度。有关这些仿真模式的详细信息，请参阅加速 (Simulink)。
