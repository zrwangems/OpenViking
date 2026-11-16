---
type: simulink-block
title: 'Passive Balancing Interface'
family: 'simscape-battery'
product_id: 'simscape-battery'
product_name: 'Simscape Battery'
documentation_release: R2025b
official_category: 'Deployment and Hardware-in-the-Loop Simulation'
documentation_page: 'passivebalancinginterface'
documentation_source_path: 'ref/passivebalancinginterface.html'
language: zh-CN
chinese_source: worker-translation
---

# Passive Balancing Interface

## 端口

### 输入

### **Ibat** — 流经每个均衡电路的电流，A physical signal | scalar or vector

流经连接到电池每个并联组件的均衡电路的电流，以安培为单位；如果 **Number of balancing circuits** 为 `1`，则指定为标量，否则指定为向量。此向量的大小必须等于 **Number of balancing circuits** 参数的值。
### 输出

### **Vbat** — 每个均衡电路两端的电压，V physical signal | scalar or vector

电压，以伏特为单位，为连接到电池每个并联组件的均衡电路两端的电压；如果 **Number of balancing circuits** 为 `1`，则返回标量，否则返回向量。此向量的大小等于 **Number of balancing circuits** 参数的值。
### 守恒

### **+** — 正极端子 electrical array of nodes

与接口正极端子关联的 electrical array-of-nodes 守恒端口。此端口的大小等于 **Number of balancing circuits** 参数的值。

如果使用 `ParallelAssembly`、`Module`、`ModuleAssembly` 或 `Pack` 对象创建模块，请将 `BalancingStrategy` 属性设置为 `"External"`，并将此端口连接到电池生成的模块的 **+BUS** 端口。

### **-** — 负极端子 electrical array of nodes

与接口负极端子关联的 electrical array-of-nodes 守恒端口。此端口的大小等于 **Number of balancing circuits** 参数的值。

如果使用 `ParallelAssembly`、`Module`、`ModuleAssembly` 或 `Pack` 对象创建模块，请将 `BalancingStrategy` 属性设置为 `"External"`，并将此端口连接到电池生成的模块的 **-BUS** 端口。

## 参数

要以交互方式编辑模块参数，请使用 Property Inspector。在 Simulink® Toolstrip 的 **Simulation** 选项卡上，在 **Prepare** 库中，选择 **Property Inspector**。

### **Number of balancing circuits** — 均衡电路数量 1（默认）| positive scalar

接口所连接的均衡电路数量。此参数的值影响此模块所有端口的大小，并且必须等于电池中并联组件的数量或串联连接的总数。

## 所属库

Simscape / Battery / HIL

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2024a 中引入**

## 描述

用于电池与电芯监控电路之间电芯均衡的接口

Passive Balancing Interface 模块提供了一种抽象化的向量化接口，用于在电池与电芯监控电路之间进行电芯均衡。可将此模块与桌面仿真和硬件在环电池仿真硬件配合使用。

电芯监控电路是一种电子电路，连接到电池电芯或并联组件。您可以使用此电路来均衡模块或电池包内部的电压或荷电状态 (SOC)。在现实世界中，您将此设备部署在电池与电池管理系统 (BMS) 控制之间。

此图表示现实世界中的设备、电压和电流。

表示现实世界设备、电压和电流的图

为避免损坏电池并在标准运行条件和故障条件下测试电芯均衡算法，您可以使用硬件在环电池仿真硬件。您可以使用抽象接口将被动均衡 BMS 连接、设置并配置到仿真电池。

在此图中：

- 蓝色表示现实世界中的设备、电压和电流。
- 绿色表示现实世界与仿真设备、电压和电流之间的接口。
- 橙色表示仿真设备、电压和电流。

表示现实世界与仿真设备、电压和电流，以及现实世界与仿真之间接口的图

Passive Balancing Interface 模块提供了电力电子设备的抽象表示，而无需对其进行详细建模。例如，如果电池包的各组成部分具有不同水平的温度或电压，您可以使用此模块来检查 BMS 在运行场景后是否正确均衡电池包。
