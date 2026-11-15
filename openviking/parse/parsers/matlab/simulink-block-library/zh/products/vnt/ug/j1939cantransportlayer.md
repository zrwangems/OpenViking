---
type: simulink-block
title: 'J1939 CAN Transport Layer'
family: 'vnt'
product_id: 'vnt'
product_name: 'Vehicle Network Toolbox'
documentation_release: R2025b
official_category: 'J1939 Communication'
documentation_page: 'j1939cantransportlayer'
documentation_source_path: 'ug/j1939cantransportlayer.html'
language: zh-CN
chinese_source: official
---

# J1939 CAN Transport Layer

## 端口

R2025b 官方文档未提供。

## 参数

### **配置名称** — J1939 网络配置名称 配置列表选项

与此传输层模块关联的 J1939 Network Configuration 模块的名称。

### **设备** — CAN 设备 设备列表选项

CAN 设备，从所有连接的 CAN 设备中选择。

### **总线速度** — CAN 总线的速度 `250000` (默认) | `500000`

以每秒位数为单位的 CAN 总线速度，指定为 J1939 协议支持的两种速率之一，即 250000 或 500000。默认值为 250000。

### **采样时间** — 仿真刷新率 `0.01` (默认) | 数值

仿真刷新率，指定为仿真期间模块的采样时间。此值定义在仿真期间 J1939 CAN Transport Layer 模块运行的频率。有关仿真采样时间的信息，请参阅硬件接口模型中的计时。如果该模块位于触发子系统内或继承采样时间，请指定值 `-1`。您还可以为采样时间指定一个 MATLAB® 变量。默认值为 `0.01` 仿真秒。

## 所属库

Vehicle Network Toolbox / J1939 Communication

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

R2025b 官方文档未提供。

## 版本历史

**在 R2015b 中推出**

## 描述

通过 CAN 传输 J1939 报文

J1939 CAN Transport Layer 模块允许通过 CAN 总线进行 J1939 通信。该模块将用户定义的 J1939 网络配置与连接的 CAN 设备相关联。对模型中的每个 J1939 Network Configuration 模块使用一个模块。

### 其他支持的功能

J1939 通信模块支持使用 Simulink® 加速和快速加速模式。使用此功能，可以加快 Simulink 模型的执行速度。有关此功能的详细信息，请参阅加速 (Simulink)。

J1939 通信模块还支持具有有限部署功能的代码生成。代码生成需要 Microsoft® C++ 编译器。
