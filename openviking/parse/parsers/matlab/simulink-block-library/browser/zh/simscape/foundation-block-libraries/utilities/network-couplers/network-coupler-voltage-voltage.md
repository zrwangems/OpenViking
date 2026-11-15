---
type: simulink-block
title: 'Network Coupler (Voltage-Voltage)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Simscape'
documentation_release: R2025b
official_category: 'Foundation Block Libraries / Utilities / Network Couplers'
documentation_page: 'networkcouplervoltagevoltage'
documentation_source_path: 'ref/networkcouplervoltagevoltage.html'
language: zh-CN
chinese_source: worker-translation
---

# Network Coupler (Voltage-Voltage)

## 端口

### 守恒

### **1** — 将此端口连接到可变步长网络，或连接到具有较小采样时间的固定步长网络 electrical | three-phase electrical | electrical node array

如果其中一个耦合网络以可变步长运行，请将其连接到 Network Coupler (Voltage-Voltage) 模块的端口 **1**。如果两个网络都以固定步长运行，请将此端口连接到采样时间较小的网络。如果两个网络都以可变步长运行，或以相同步长的固定步长运行，则模块极性无关紧要。

### **2** — 将此端口连接到具有较大采样时间的固定步长网络 electrical | three-phase electrical | electrical node array

如果其中一个耦合网络以可变步长运行，请将 Network Coupler (Voltage-Voltage) 模块的端口 **2** 连接到固定步长网络。如果两个网络都以固定步长运行，请将此端口连接到采样时间较大的网络。

## 参数

### 主

### **使用三相电气连接** — 断开三相电气端口之间的连接 off (默认) | on

在断开三相电气端口之间的连接时，选中此复选框。由于顶层子系统未封装，您需要为 Port 1 Interface 和 Port 2 Interface 模块都选中此复选框。
选中此复选框会禁用 **电气节点数组大小** 参数，因为端口 **1** 和 **2** 变为三相电气端口。

### **电气节点数组大小** — 指定电气节点数 `1` (默认) | 正整数

指定连接到两个电气端口 **1** 和 **2** 的电气节点数组的大小。由于顶层子系统未封装，您需要为 Port 1 Interface 和 Port 2 Interface 模块将此参数设置为相同的值。

如果要断开常规电气连接，请保留 `1` 的默认值不变。

#### 依赖关系

启用此参数需清除 **使用三相电气连接** 复选框。

### **端口 1 电压源电阻 (ohms)** — 指定连接到 Network 1 的端口的电压源电阻 `0.1` (默认) | 正标量

指定连接到 Network 1 的内部电压源的电阻值。

### **端口 2 电压源电阻 (ohms)** — 指定连接到 Network 2 的端口的电压源电阻 `0.1` (默认) | 正标量

指定连接到 Network 2 的内部电压源的电阻值。由于顶层子系统未封装，您需要为 Port 1 Interface 和 Port 2 Interface 模块将此参数设置为相同的值。

### **采样类型** — 为耦合网络选择采样类型场景 `Variable step at ports 1 and 2` (默认) | `Variable step at port 1 and fixed step at port 2` | `Fixed step both ports with common sample time` | `Fixed step both ports with faster sampling at port 1`

选择耦合网络的采样方式：

- `Variable step at ports 1 and 2` — 两个网络均为可变步长。
- `Variable step at port 1 and fixed step at port 2` — Network 1 为可变步长，Network 2 为固定步长。
- `Fixed step both ports with common sample time` — 两个网络均为固定步长，且步长相同。
- `Fixed step both ports with faster sampling at port 1` — 两个网络均为固定步长，且步长不同。

### **端口 1 网络离散采样时间 (s)** — 指定 Network 1 的采样时间 `0.0002` (默认) | 正标量

指定 Network 1 的采样时间，以秒为单位。

#### 依赖关系

启用此参数需将 **采样类型** 参数设置为 `Fixed step both ports with common sample time` 或 `Fixed step both ports with faster sampling at port 1`。

### **端口 2 网络离散采样时间 (s)** — 指定 Network 2 的采样时间 `0.001` (默认) | 正标量

指定 Network 2 的采样时间，以秒为单位。

#### 依赖关系

启用此参数需将 **采样类型** 参数设置为 `Variable step at port 1 and fixed step at port 2` 或 `Fixed step both ports with faster sampling at port 1`。

### **在将固定步长连接到可变步长时使用预测** — 允许启用 prediction (discrete->continuous) 算法 off (默认) | on

选中此复选框以启用 prediction (discrete->continuous) 算法。有关更多信息，请参阅 Prediction and Smoothing。

#### 依赖关系

要显示此选项，请将 **采样类型** 参数设置为 `Variable step at port 1 and fixed step at port 2`。

### **在将可变步长连接到固定步长时使用平滑** — 允许启用 smoothing (continuous->discrete) 算法 off (默认) | on

选中此复选框以启用 smoothing (continuous->discrete) 算法。有关更多信息，请参阅 Prediction and Smoothing。

#### 依赖关系

要显示此选项，请将 **采样类型** 参数设置为 `Variable step at port 1 and fixed step at port 2`。

### **平滑时间常数 (s)** — 指定一阶滤波器的时间常数 `0.01` (默认) | 正标量

指定平滑算法用于去除不需要的高频信息的一阶滤波器的时间常数，以秒为单位。

#### 依赖关系

启用此参数需选中 **在将可变步长连接到固定步长时使用平滑** 复选框。

### **在将慢采样时间连接到快采样时间时使用预测** — 允许启用 prediction (slow->fast) 算法 off (默认) | on

选中此复选框以启用 prediction (slow->fast) 算法。有关更多信息，请参阅 Prediction and Smoothing。

#### 依赖关系

要显示此选项，请将 **采样类型** 参数设置为 `Fixed step both ports with faster sampling at port 1`。

### **在将快采样时间连接到慢采样时间时使用平滑** — 允许启用 smoothing (fast->slow) 算法 off (默认) | on

选中此复选框以启用 smoothing (fast->slow) 算法。有关更多信息，请参阅 Prediction and Smoothing。

#### 依赖关系

要显示此选项，请将 **采样类型** 参数设置为 `Fixed step both ports with faster sampling at port 1`。

### **用于平滑的采样数** — 指定用于平均的采样数 `1` (默认) | 正标量

平滑算法通过对最后 *N* 个采样求平均来工作。您使用此参数指定 *N*。

#### 依赖关系

启用此参数需选中 **在将快采样时间连接到慢采样时间时使用平滑** 复选框。

### 分析

### **端口 1 的近似串联电阻 (ohms)** — 指定端口 1 的近似串联电阻 `0.1` (默认) | 正标量

指定端口 **1** 的近似串联电阻，以 ohms 为单位。

### **端口 1 的近似串联电感 (H)** — 指定端口 1 的近似串联电感 `1e-3` (默认) | 正标量

指定端口 **1** 的近似串联电感，以 H 为单位。

### **端口 2 的近似串联电阻 (ohms)** — 指定端口 2 的近似串联电阻 `0.1` (默认) | 正标量

指定端口 **2** 的近似串联电阻，以 ohms 为单位。

### **端口 2 的近似串联电感 (H)** — 指定端口 2 的近似串联电感 `1e-3` (默认) | 正标量

指定端口 **2** 的近似串联电感，以 H 为单位。

有关如何使用 **推导值** 部分的信息，请参阅使用推导值估算模块参数。

### 初始条件

### **端口 1 的初始电压 (V)** — 指定初始电压 `0` (默认) | 正标量

指定端口 **1** 处电压的初始条件，以 V 为单位。

### **流入端口 1 的初始电流 (A)** — 指定初始电流 `0` (默认) | 正标量

指定流入端口 **1** 的电流的初始条件，以 A 为单位。

## 所属库

Simscape / Utilities / Network Couplers

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**R2022a 中引入**

### R2024a: 断开电气节点数组之间的连接

该模块现在支持电气节点数组和三相连接。新参数 **电气节点数组大小** 允许您指定数组大小。或者，您可以使用新复选框 **使用三相电气连接**。如果在封装下查看，Port 1 Interface 和 Port 2 Interface 子系统包含支持向量化电气节点的自定义模块，而不是常规 Foundation library 电气模块。

此更改没有兼容性影响。**使用三相电气连接** 复选框和 **电气节点数组大小** 参数的默认值对应于常规电气连接。如果打开包含此模块的现有模型，仿真结果与以前版本相同。

## 描述

在电气连接处拆分网络

Network Coupler (Voltage-Voltage) 模块为您提供了一个起点，用于在电气连接处将一个 Simscape™ 网络拆分为两个耦合网络。使用此模块可拆分这样的电力网络：其中连接电缆建模为串联连接的电阻和电感，并且网络的某些部分没有局部电气参考连接。此类场景中的电感不允许在接口处使用电流源，因此该模块向两个网络呈现电压源。

您不能简单地基于 Network 1 的电压测量来驱动 Network 2 的电压源（反之亦然），因为那样定义是循环的，并且不包含对流入两个网络的电流的约束，而这些电流之和必须为零。为了引入对电流的约束，两个电压源添加了内部电源电阻。

定义两个电压源值的离散时间方程为：

Vs1(n+1)=V2(n)+i2(n)R1  
Vs2(n+1)=V1(n)+i1(n)R2

其中：

- *V*s1、*V*s2 — 两个内部电源的电压。
- *R*1、*R*2 — 两个内部电源的电阻。
- *i*1、*i*2 — 从所连接网络流入电源的电流。
- *V*1、*V*2 — 呈现给所连接网络的电压。
- *n* — 采样编号。

当任一侧都没有连接负载时，极点在 `+-1` 处，即位于单位圆上。所连接网络可以起到稳定极点的作用（极点最终位于单位圆内），也可以起到失稳作用（极点最终位于单位圆外）。

通常，当两个耦合网络的串联电感和电阻大致相等时最佳，因为这会得到最慢的一组闭环极点。

Network Coupler (Voltage-Voltage) 模块的两个端口接口都实现为电压源。因此，不能将此模块连接到电压回路，例如一组串联连接的电压源和电容器，因为这将导致 Index-2 拓扑（有关更多信息，请参阅 Avoiding Numerical Simulation Issues）。

为了便于处理包含电气节点数组或三相连接的模型，Port 1 Interface 和 Port 2 Interface 子系统包含自定义模块，例如 Controlled Voltage Source 或 Current Sensor。这些自定义模块基于等效的 Foundation library 模块，但经过修改以支持向量化和三相电气节点。这些自定义模块的源文件位于以下命名空间：

    matlabroot/toolbox/physmod/simscape/library/m/+foundation/+internal/+couplers/+electrical

其中 *`matlabroot`* 是您机器上的 MATLAB® 根目录，通过输入以下内容返回

    matlabroot

在 MATLAB 命令提示符下。该命名空间包含电压和电流源及传感器的源文件，以及一个电阻器和一个具有数组和三相支持的电气参考。您可以使用这些模块自定义您的网络耦合器配置。

### 在模型画布上使用模块

当您将模块添加到模型并双击它时，Network Coupler (Voltage-Voltage) 子系统会打开。

Network Coupler (Voltage-Voltage) 子系统图

Port 1 Interface 模块包含用于打破代数环的动态特性。双击此模块可设置大多数 Network Coupler (Voltage-Voltage) 子系统参数并查看推导值。

但是，与大多数其他耦合器模块不同，Port 2 Interface 模块还有一个参数 **端口 2 电压源电阻 (ohms)**，您需要单独设置。

Rate Transition 模块默认处于 commented through 状态。如果至少一个耦合网络以固定步长运行，请取消注释它们。

### 使用推导值估算模块参数

**分析** 选项卡会询问您有关两个耦合网络的串联电阻和电感的信息，并提供关于 *R1* 和 *R2* 值的建议，以确保稳定性。如果您的至少一个耦合网络具有开关，则使用最小的串联电阻值和最大的串联电感值。

对于大多数应用，遵循推荐值可获得稳定仿真，但有时您可能需要试验 *R1* 和 *R2* 的值。

**更新** 按钮允许您在更改所连接网络的参数后重新计算推导值。
