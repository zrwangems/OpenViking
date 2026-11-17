---
type: simulink-block
title: 'Passive Balancing Interface'
family: 'simscape-battery'
product_id: 'simscape-battery'
product_name: 'Battery'
documentation_release: R2025b
official_category: 'HIL'
documentation_page: 'passivebalancinginterface'
documentation_source_path: 'ref/passivebalancinginterface.html'
language: zh-CN
chinese_source: worker-translation
---

# Passive Balancing Interface

## 端口
```yaml
ports:
- name: Ibat
  summary: 流经每个均衡电路的电流，A 物理信号 | 标量或向量
  direction: input
- name: Vbat
  summary: 每个均衡电路两端的电压，V 物理信号 | 标量或向量
  direction: output
- name: +
  summary: 正极端子 电气节点数组
  direction: output
- name: '-'
  summary: 负极端子 电气节点数组
  direction: output
```

### 输入

### **Ibat** — 流经每个均衡电路的电流，A 物理信号 | 标量或向量

电流，以安培为单位，流经连接到电池每个并联组件的均衡电路，如果 **Number of balancing circuits** 为 `1`，则指定为标量，否则指定为向量。该向量的大小必须等于 **Number of balancing circuits** 参数的值。
### 输出

### **Vbat** — 每个均衡电路两端的电压，V 物理信号 | 标量或向量

电压，以伏特为单位，跨接在连接到电池每个并联组件的均衡电路两端，如果 **Number of balancing circuits** 为 `1`，则返回标量，否则返回向量。该向量的大小等于 **Number of balancing circuits** 参数的值。
### 守恒

### **+** — 正极端子 电气节点数组

与接口正极端子关联的电气节点数组守恒端口。该端口的大小等于 **Number of balancing circuits** 参数的值。

如果使用 `ParallelAssembly`、`Module`、`ModuleAssembly` 或 `Pack` 对象创建模块，请将 `BalancingStrategy` 属性设置为 `"External"`，并将此端口连接到电池生成模块的 **+BUS** 端口。

### **-** — 负极端子 电气节点数组

与接口负极端子关联的电气节点数组守恒端口。该端口的大小等于 **Number of balancing circuits** 参数的值。

如果使用 `ParallelAssembly`、`Module`、`ModuleAssembly` 或 `Pack` 对象创建模块，请将 `BalancingStrategy` 属性设置为 `"External"`，并将此端口连接到电池生成模块的 **-BUS** 端口。
## 参数
```yaml
parameters:
- name: Number of balancing circuits
  summary: 均衡电路数量 1（默认）| 正标量
  group: ''
```

要以交互方式编辑模块参数，请使用属性检查器。在 Simulink® 工具条的 **Simulation** 选项卡上，在 **Prepare** 库中，选择 **Property Inspector**。

### **Number of balancing circuits** — 均衡电路数量 1（默认）| 正标量

接口所连接的均衡电路数量。该参数的值影响此模块所有端口的大小，并且必须等于电池中并联组件的数量或串联连接的总数。
## 所属库

Simscape / Battery / HIL

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2024a 中引入**

## 描述

电池与电芯监控电路之间电芯均衡的接口

Passive Balancing Interface 模块为电池与电芯监控电路之间的电芯均衡提供了一个抽象的矢量化接口。可将此模块与桌面仿真和硬件在环电池仿真硬件配合使用。

电芯监控电路是一种连接到电池电芯或并联组件的电子电路。您可以使用此电路来使模块或电池包内部的电压或荷电状态 (SOC) 归一化。在实际应用中，您将此设备部署在电池与电池管理系统 (BMS) 控制之间。

下图表示实际设备、电压和电流。

表示实际设备、电压和电流的图

为了避免损坏电池，并在标准运行条件和故障条件下测试您的电芯均衡算法，您可以使用硬件在环电池仿真硬件。您可以使用抽象接口将被动均衡 BMS 连接、设置并配置到您的仿真电池。

在此图中：

- 蓝色表示实际设备、电压和电流。
- 绿色表示实际设备与仿真设备、电压和电流之间的接口。
- 橙色表示仿真设备、电压和电流。

表示实际设备和仿真设备、电压和电流以及实际与仿真之间接口的图

Passive Balancing Interface 模块提供了电力电子设备的抽象表示，无需对其进行详细建模。例如，如果您的电池包中各组成部分具有不同的温度或电压水平，您可以使用此模块来检查 BMS 在运行场景之后是否正确地对电池包进行均衡。
