---
type: simulink-block
title: 'Network Coupler (Voltage-Voltage)'
family: 'utilities'
product_id: 'utilities'
product_name: 'Utilities'
documentation_release: R2025b
official_category: 'Network Couplers'
documentation_page: 'networkcouplervoltagevoltage'
documentation_source_path: '../simscape/ref/networkcouplervoltagevoltage.html'
language: zh-CN
chinese_source: worker-translation
---

# Network Coupler (Voltage-Voltage)

## 端口

### 守恒端口

### **1** — 将此端口连接到变步长网络，或连接到具有较小采样时间的定步长网络 electrical | three-phase electrical | electrical node array

如果其中一个耦合网络以变步长运行，请将其连接到 Network Coupler (Voltage-Voltage) 模块的端口 **1**。如果两个网络都以定步长运行，请将此端口连接到具有较小采样时间的网络。如果两个网络都以变步长运行，或以相同步长的定步长运行，则模块极性无关紧要。

### **2** — 将此端口连接到具有较大采样时间的定步长网络 electrical | three-phase electrical | electrical node array

如果其中一个耦合网络以变步长运行，请将 Network Coupler (Voltage-Voltage) 模块的端口 **2** 连接到定步长网络。如果两个网络都以定步长运行，请将此端口连接到具有较大采样时间的网络。

## 参数

### 主要

### **Use three-phase electrical connections** — 断开三相电气端口之间的连接 off (default) | on

在断开三相电气端口之间的连接时，选中此复选框。由于顶层子系统未封装，您需要为 Port 1 Interface 和 Port 2 Interface 模块都选中此复选框。
选中此复选框会禁用 **Electrical node array size** 参数，因为端口 **1** 和 **2** 变为三相电气端口。

### **Electrical node array size** — 指定电气节点数量 `1` (default) | positive integer

指定连接到两个电气端口 **1** 和 **2** 的电气节点阵列的大小。由于顶层子系统未封装，您需要为 Port 1 Interface 和 Port 2 Interface 模块将此参数设置为相同的值。

如果您要断开的是常规电气连接，请保持默认值 `1` 不变。

#### 依赖关系

要启用此参数，请清除 **Use three-phase electrical connections** 复选框。

### **Port 1 voltage source resistance (ohms)** — 指定连接到 Network 1 的端口的电压源电阻 `0.1` (default) | positive scalar

指定连接到 Network 1 的内部电压源的电阻值。

### **Port 2 voltage source resistance (ohms)** — 指定连接到 Network 2 的端口的电压源电阻 `0.1` (default) | positive scalar

指定连接到 Network 2 的内部电压源的电阻值。由于顶层子系统未封装，您需要为 Port 1 Interface 和 Port 2 Interface 模块将此参数设置为相同的值。

### **Sampling type** — 为耦合网络选择采样类型场景 `Variable step at ports 1 and 2` (default) | `端口 1 使用可变步长，端口处使用固定步长 2` | `Fixed step both ports with common sample time` | `固定步长，两个端口，端口处采样更快 1`

选择耦合网络的采样方式：

- `Variable step at ports 1 and 2` — 两个网络均为变步长。
- `端口 1 使用可变步长，端口处使用固定步长 2` — Network 1 为变步长，Network 2 为定步长。
- `Fixed step both ports with common sample time` — 两个网络均为定步长，且步长相同。
- `固定步长，两个端口，端口处采样更快 1` — 两个网络均为定步长，且步长不同。

### **Port 1 network discrete sample time (s)** — 指定 Network 1 的采样时间 `0.0002` (default) | positive scalar

指定 Network 1 的采样时间，单位为秒。

#### 依赖关系

要启用此参数，请将 **Sampling type** 参数设置为 `Fixed step both ports with common sample time` 或 `固定步长，两个端口，端口处采样更快 1`。

### **Port 2 network discrete sample time (s)** — 指定 Network 2 的采样时间 `0.001` (default) | positive scalar

指定 Network 2 的采样时间，单位为秒。

#### 依赖关系

要启用此参数，请将 **采样类型** 参数设置为
`端口 1 使用可变步长，端口处使用固定步长 2` 或
`固定步长，两个端口，端口处采样更快
1`。

### **将定步长连接到变步长时使用预测** — 允许您启用预测（离散->连续）算法 关（默认）| 开

选中此复选框以启用预测（离散->连续）算法。
有关详细信息，请参阅预测和平滑。

#### 依赖关系

要显示此选项，请将 **采样类型** 参数设置为
`端口 1 使用可变步长，端口处使用固定步长
2`。

### **将变步长连接到定步长时使用平滑** — 允许您启用平滑（连续->离散）算法 关（默认）| 开

选中此复选框以启用平滑（连续->离散）算法。
有关详细信息，请参阅预测和平滑。

#### 依赖关系

要显示此选项，请将 **采样类型** 参数设置为
`端口 1 使用可变步长，端口处使用固定步长
2`。

### **平滑时间常数 (s)** — 指定一阶滤波器的时间常数 `0.01`（默认）| 正标量

指定一阶滤波器的时间常数（以秒为单位），平滑算法使用该滤波器去除不需要的高频信息。

#### 依赖关系

要启用此参数，请选中 **将变步长连接到定步长时使用平滑** 复选框。

### **将慢速连接到快速采样时间时使用预测** — 允许您启用预测（慢速->快速）算法 关（默认）| 开

选中此复选框以启用预测（慢速->快速）算法。有关详细信息，请参阅预测和平滑。

#### 依赖关系

要显示此选项，请将 **采样类型** 参数设置为
`固定步长，两个端口，端口处采样更快
1`。

### **将快速连接到慢速采样时间时使用平滑** — 允许您启用平滑（快速->慢速）算法 关（默认）| 开

选中此复选框以启用平滑（快速->慢速）算法。有关详细信息，请参阅预测和平滑。

#### 依赖关系

要显示此选项，请将 **采样类型** 参数设置为
`固定步长，两个端口，端口处采样更快
1`。

### **用于平滑的采样数** — 指定用于求平均的采样数 `1`（默认）| 正标量

平滑算法通过对最近 *N* 个采样求平均值来工作。
您使用此参数指定 *N*。

#### 依赖关系

要启用此参数，请选中 **将快速连接到慢速采样时间时使用平滑** 复选框。

### 分析

### **端口 1 的近似串联电阻 (ohms)** — 指定端口 1 的近似串联电阻 `0.1`（默认）| 正标量

指定端口 **1** 的近似串联电阻，以欧姆为单位。

### **端口 1 的近似串联电感 (H)** — 指定端口 1 的近似串联电感 `1e-3`（默认）| 正标量

指定端口 **1** 的近似串联电感，以 H 为单位。

### **端口 2 的近似串联电阻 (ohms)** — 指定端口 2 的近似串联电阻 `0.1`（默认）| 正标量

指定端口 **2** 的近似串联电阻，以欧姆为单位。

### **端口 2 的近似串联电感 (H)** — 指定端口 2 的近似串联电感 `1e-3`（默认）| 正标量

指定端口 **2** 的近似串联电感，以 H 为单位。

有关如何使用 **派生值** 部分的信息，请参阅使用派生值估算模块参数。

### 初始条件

### **端口 1 的初始电压 (V)** — 指定初始电压 `0`（默认）| 正标量

指定端口 **1** 电压的初始条件，以 V 为单位。

### **流入端口 1 的初始电流 (A)** — 指定初始电流 `0`（默认）| 正标量

指定流入端口 **1** 的电流的初始条件，以 A 为单位。

## 所属库

Simscape / Utilities / Network Couplers

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2022a 中引入**

### R2024a：断开电气节点数组之间的连接

该模块现在支持电气节点数组和三相连接。新增参数 **Electrical node array size** 允许您指定数组大小。或者，您可以使用新增复选框 **Use three-phase electrical connections**。如果您查看封装内部，Port 1 Interface 和 Port 2 Interface 子系统包含支持向量化电气节点的自定义模块，而非常规的 Foundation 库电气模块。

此更改没有兼容性影响。**Use three-phase electrical connections** 复选框和 **Electrical node array size** 参数的默认值对应于常规电气连接。如果您打开包含此模块的现有模型，仿真结果与之前版本相同。

## 描述

在电气连接处拆分网络

Network Coupler (Voltage-Voltage) 模块为您提供了一个起点，用于在电气连接处将一个 Simscape™ 网络拆分为两个耦合网络。当连接电缆建模为串联的电阻和电感，且网络的部分区域没有本地电气参考连接时，可使用此模块来拆分电力网络。此类场景中的电感不允许在接口处使用电流源，因此该模块向两个网络呈现电压源。

您不能简单地基于网络 1 的电压测量来驱动网络 2 的电压源（反之亦然），因为那样定义是循环的，且不包含对流入两个网络的电流的约束，而这些电流之和必须为零。为了引入对电流的约束，两个电压源具有附加的内部源电阻。

定义两个电压源值的离散时间方程为：

Vs1(n+1)=V2(n)+i2(n)R1Vs2(n+1)=V1(n)+i1(n)R2

其中：

- *V*s1、*V*s2 — 两个内部源的电压。
- *R*1、*R*2 — 两个内部源的电阻。
- *i*1、*i*2 — 从所连接网络流入源的电流。
- *V*1、*V*2 — 呈现给所连接网络的电压。
- *n* — 采样编号。

当任一侧都没有连接负载时，极点位于 `+-1`，即在单位圆上。所连接的网络可以起到稳定极点的作用（极点最终位于单位圆内），也可以起到失稳的作用（极点最终位于单位圆外）。

通常，当两个耦合网络的串联电感和电阻大致相等时效果最佳，因为这会产生最慢的一组闭环极点。

Network Coupler (Voltage-Voltage) 模块的两个端口接口都实现为电压源。因此，您不能将此模块连接到电压环路，例如一组串联的电压源和电容器，因为这将导致 Index-2 拓扑（更多信息，请参阅 Avoiding Numerical Simulation Issues）。

为了便于处理包含电气节点数组或三相连接的模型，Port 1 Interface 和 Port 2 Interface 子系统包含自定义模块，例如 Controlled Voltage Source 或 Current Sensor。这些自定义模块基于等效的 Foundation 库模块，但经过修改以支持向量化和三相电气节点。这些自定义模块的源文件位于以下命名空间中：

```
matlabroot/toolbox/physmod/simscape/library/m/+foundation/+internal/+couplers/+electrical
```

其中 *`matlabroot`* 是您机器上的 MATLAB® 根目录，可通过在 MATLAB 命令提示符下输入以下命令返回

```
matlabroot
```

该命名空间包含电压和电流源及传感器、电阻器和电气参考的源文件，并支持数组和三相。您可以使用这些模块来自定义您的网络耦合器配置。

### 在模型画布上使用该模块

当您将模块添加到模型并双击它时，Network Coupler (Voltage-Voltage) 子系统会打开。

Network Coupler (Voltage-Voltage) 子系统图

Port 1 Interface 模块包含打破代数环的动态特性。双击此模块可设置大多数 Network Coupler (Voltage-Voltage) 子系统参数并查看派生值。

然而，与大多数其他耦合器模块不同，Port 2 Interface 模块还有一个参数，**Port 2 voltage source resistance (ohms)**，您需要单独设置。

速率转换模块默认被注释掉。如果至少有一个耦合网络以固定步长运行，请取消注释它们。

### 使用派生值来估计模块参数

**分析**选项卡要求你提供两个耦合网络的串联电阻和电感信息，并就 *R1* 和 *R2* 的值提供建议，以确保稳定性。如果你的耦合网络中至少有一个包含开关，则使用最小的串联电阻值和最大的串联电感值。

对于大多数应用，遵循推荐值可以得到稳定的仿真，但有时你可能需要试验 *R1* 和 *R2* 的值。

**更新**按钮允许你在更改所连接网络的参数后重新计算派生值。
