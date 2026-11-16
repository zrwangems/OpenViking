---
type: simulink-block
title: 'Network Coupler (Capacitor)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Simscape'
documentation_release: R2025b
official_category: 'Foundation Block Libraries / Utilities / Network Couplers'
documentation_page: 'networkcouplercapacitor'
documentation_source_path: 'ref/networkcouplercapacitor.html'
language: zh-CN
chinese_source: worker-translation
---

# Network Coupler (Capacitor)

## 端口

### 守恒

### **1** — 将此端口连接到变步长网络，或连接到具有较小采样时间的定步长网络 electrical | three-phase electrical | electrical node array

如果其中一个耦合网络以变步长运行，请将其连接到 Network Coupler (Capacitor) 模块的端口
**1**。如果两个网络都以定步长运行，请将此端口连接到具有较小采样时间的网络。如果两个网络都以变步长运行，或以相同步长的定步长运行，则模块极性无关紧要。

### **2** — 将此端口连接到具有较大采样时间的定步长网络 electrical | three-phase electrical | electrical node array

如果其中一个耦合网络以变步长运行，请将 Network Coupler (Capacitor) 模块的端口
**2** 连接到定步长网络。如果两个网络都以定步长运行，请将此端口连接到具有较大采样时间的网络。

## 参数

### 主要

### **Use three-phase electrical connections** — 在三相电气端口之间断开连接 off（默认）| on

当在三相电气端口之间断开连接时，选择此复选框。由于顶层子系统未屏蔽，您需要为 Port 1 Interface 和 Port 2 Interface 模块都选择此复选框。
选择此复选框会禁用 **Electrical node array size** 参数，因为端口 **1** 和 **2** 变为三相电气端口。

### **Electrical node array size** — 指定电气节点数量 `1`（默认）| positive integer

指定连接到两个电气端口 **1** 和 **2** 的电气节点数组大小。由于顶层子系统未屏蔽，您需要将此参数设置为与 Port 1 Interface 和 Port 2 Interface 模块相同的值。

如果要断开常规电气连接，请保留默认值 `1` 不变。

#### 依赖关系

要启用此参数，请清除 **Use three-phase electrical connections** 复选框。

### **Capacitance (F)** — 指定电容值 `1000e-6`（默认）| positive scalar

指定电容值。使用被替换的 Capacitor 模块中的 **Capacitance** 参数值，必要时将其转换为 F。

### **Sampling type** — 选择耦合网络的采样类型场景 `Variable step at ports 1 and 2`（默认）| `Variable step at port 1 and fixed step at port 2` | `Fixed step both ports with common sample time` | `Fixed step both ports with faster sampling at port 1`

选择耦合网络的采样方式：

- `Variable step at ports 1 and 2` — 两个网络均为变步长。
- `Variable step at port 1 and fixed step at port 2` — Network 1 为变步长，Network 2 为定步长。
- `Fixed step both ports with common sample time` — 两个网络均为定步长，且步长相同。
- `Fixed step both ports with faster sampling at port 1` — 两个网络均为定步长，且步长不同。

### **Port 1 network discrete sample time (s)** — 指定 Network 1 的采样时间 `0.0002`（默认）| positive scalar

指定 Network 1 的采样时间，以秒为单位。

#### 依赖关系

要启用此参数，请将 **Sampling type** 参数设置为 `Fixed step both ports with common sample time` 或 `Fixed step both ports with faster sampling at port 1`。

### **Port 2 network discrete sample time (s)** — 指定 Network 2 的采样时间 `0.001`（默认）| positive scalar

指定 Network 2 的采样时间，以秒为单位。

#### 依赖关系

要启用此参数，请将 **Sampling type** 参数设置为 `Variable step at port 1 and fixed step at port 2` 或 `Fixed step both ports with faster sampling at port 1`。

### **Use prediction when connecting fixed step to variable step** — 允许您启用预测（discrete->continuous）算法 off（默认）| on

选择此复选框以启用预测（discrete->continuous）算法。
有关详细信息，请参阅 Prediction and Smoothing。

#### 依赖关系

要显示此选项，请将 **Sampling type** 参数设置为 `Variable step at port 1 and fixed step at port 2`。

### **Use smoothing when connecting variable step to fixed step** — 允许您启用平滑（continuous->discrete）算法 off（默认）| on

选择此复选框以启用平滑（continuous->discrete）算法。
有关详细信息，请参阅 Prediction and Smoothing。

#### 依赖关系

要显示此选项，请将 **Sampling type** 参数设置为 `Variable step at port 1 and fixed step at port 2`。

### **Smoothing time constant (s)** — 指定一阶滤波器的时间常数 `0.01`（默认）| positive scalar

指定一阶滤波器的时间常数，以秒为单位，平滑算法使用该滤波器去除不需要的高频信息。

#### 依赖关系

要启用此参数，请选择 **Use smoothing when connecting variable step to fixed step** 复选框。

### **Use prediction when connecting slow to fast sample times** — 允许您启用预测（slow->fast）算法 off（默认）| on

选择此复选框以启用预测（slow->fast）算法。有关更多信息，请参阅 Prediction and Smoothing。

#### 依赖关系

要显示此选项，请将 **Sampling type** 参数设置为 `Fixed step both ports with faster sampling at port 1`。

### **Use smoothing when connecting fast to slow sample times** — 允许您启用平滑（fast->slow）算法 off（默认）| on

选择此复选框以启用平滑（fast->slow）算法。有关更多信息，请参阅 Prediction and Smoothing。

#### 依赖关系

要显示此选项，请将 **Sampling type** 参数设置为 `Fixed step both ports with faster sampling at port 1`。

### **Number of samples over which to smooth** — 指定用于求平均的样本数 `1`（默认）| positive scalar

平滑算法通过对最近 *N* 个样本求平均来工作。
您使用此参数指定 *N*。

#### 依赖关系

要启用此参数，请选择 **Use smoothing when connecting fast to slow sample times** 复选框。

### 分析

### **Approximate connected network resistance (ohms)** — 指定所连接网络的近似电阻 `10`（默认）| positive scalar

指定所连接网络的近似电阻，以 ohm 为单位。如果两个网络的电阻不同，请提供较低的值。

#### 依赖关系

要启用此参数，请将 **Sampling type** 参数设置为 `Variable step at port 1 and fixed step at port 2`、`Fixed step both ports with common sample time` 或 `Fixed step both ports with faster sampling at port 1`。

有关如何使用 **Derived values** 部分的信息，请参阅 Using the Derived Values to Estimate Block Parameters。

### 初始条件

### **Initial voltage (V)** — 指定电容器两端的初始电压 `0`（默认）| positive scalar

指定电容器两端电压的初始条件，以 V 为单位。

## 所属库

Simscape / Utilities / Network Couplers

## 模块特性

Not documented in R2025b.

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2022a 中引入**

### R2024a：断开电气节点数组之间的连接

此模块现在支持电气节点数组和三相连接。新参数 **Electrical node array size** 允许您指定数组大小。
或者，您可以使用新复选框 **Use three-phase electrical connections**。如果查看掩码下方，Port 1 Interface 和
Port 2 Interface 子系统包含自定义模块，这些模块支持向量化电气节点，而不是常规 Foundation library 电气模块。

此更改没有兼容性影响。**Use three-phase electrical connections** 复选框和 **Electrical node array size** 参数的默认值对应于常规电气连接。如果您打开包含此模块的现有模型，仿真结果与之前版本相同。

## 描述

通过在电气连接处替换电容器来拆分网络

Network Coupler (Capacitor) 模块使用连接到电气参考的电容器来断开网络连接。此模块可用于断开 DC-DC 连接的返回路径。但是，它不太适合表示典型的对地杂散电容，因为产生的时间常数会非常快，需要不切实际的采样时间。您指定的电容值通常需要为几百微法的数量级。有关详细信息，请参阅 Using the Derived Values to Estimate Block Parameters。

Network Coupler (Capacitor) 模块的两个端口接口都实现为电压源。因此，您不能将此模块连接到电压回路，例如一组串联连接的电压源和电容器，因为这将导致 Index-2 拓扑（有关详细信息，请参阅 Avoiding Numerical Simulation Issues）。

为了便于处理包含电气节点数组或三相连接的模型，Port 1 Interface 和 Port 2 Interface 子系统包含自定义模块，例如 Controlled Voltage Source 或 Current Sensor。这些自定义模块基于等效的 Foundation library 模块，但经过修改以支持向量化和三相电气节点。这些自定义模块的源文件位于以下命名空间中：

`matlabroot/toolbox/physmod/simscape/library/m/+foundation/+internal/+couplers/+electrical`

其中 *`matlabroot`* 是您计算机上的 MATLAB® 根目录，通过输入

`matlabroot`

在 MATLAB 命令提示符处返回。该命名空间包含电压和电流源及传感器的源文件，以及一个支持数组和三相的电阻和一个电气参考。您可以使用这些模块来自定义您的网络耦合器配置。

### 在模型画布上使用模块

当您将模块添加到模型并双击它时，Network Coupler (Capacitor) 子系统会打开。

Network Coupler (Capacitor) 子系统图

Port 1 Interface 模块包含用于断开代数环的动态特性。双击此模块可设置所有 Network Coupler (Capacitor) 子系统参数并查看派生值。

默认情况下，rate transition 模块被注释通过。如果至少一个耦合网络以定步长运行，则取消注释它们。

### 使用派生值估计模块参数

在 Port 1 Interface 模块对话框的 **Analysis** 选项卡上，**Derived values** 部分包含推荐值列表，您可以在指定模块参数时使用这些值。例如，使用 **Recommended max discrete sample time (s)** 派生值来验证您的 **Port 1 network discrete sample time (s)** 和 **Port 2 network discrete sample time (s)** 参数值在可接受限制内。

派生值列表基于所选的模块配置。

如果两个网络都以变步长运行，则 **Analysis** 选项卡为空，并且对您指定的电容值没有限制。

如果一个或两个网络以定步长运行，则 **Analysis** 选项卡通过要求您提供所连接网络的近似电阻值，帮助选择适合的电容值。如果两个网络的电阻不同，请提供较低的值。然后，**Update** 按钮会提供要使用的最大推荐离散采样时间。
