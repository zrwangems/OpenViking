---
type: simulink-block
title: 'Network Coupler (Voltage-Current)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Simscape'
documentation_release: R2025b
official_category: 'Foundation Block Libraries / Utilities / Network Couplers'
documentation_page: 'networkcouplervoltagecurrent'
documentation_source_path: 'ref/networkcouplervoltagecurrent.html'
language: zh-CN
chinese_source: worker-translation
---

# Network Coupler (Voltage-Current)

## 端口

### 守恒

### **1** — 将此端口连接到变步长网络，或连接到具有较小采样时间的定步长网络 electrical | three-phase electrical | electrical node array

如果其中一个耦合网络以变步长运行，请将其连接到 Network Coupler (Voltage-Current) 模块的端口 **1**。如果两个网络都以定步长运行，请将此端口连接到具有较小采样时间的网络。如果两个网络都以变步长运行，或以相同步长的定步长运行，则模块极性无关紧要。

### **2** — 将此端口连接到具有较大采样时间的定步长网络 electrical | three-phase electrical | electrical node array

如果其中一个耦合网络以变步长运行，请将 Network Coupler (Voltage-Current) 模块的端口 **2** 连接到定步长网络。如果两个网络都以定步长运行，请将此端口连接到具有较大采样时间的网络。

## 参数

### 主要

### **使用三相电气连接** — 断开三相电气端口之间的连接 off（默认） | on

当断开三相电气端口之间的连接时，选中此复选框。由于顶层子系统未被屏蔽，您需要为 Port 1 Interface 和 Port 2 Interface 模块都选中此复选框。选中此复选框会禁用 **电气节点数组大小** 参数，因为端口 **1** 和 **2** 变为三相电气端口。

### **电气节点数组大小** — 指定电气节点数 `1`（默认） | 正整数

指定连接到两个电气端口 **1** 和 **2** 的电气节点数组大小。由于顶层子系统未被屏蔽，您需要为 Port 1 Interface 和 Port 2 Interface 模块都将此参数设置为相同的值。

如果要断开常规电气连接，请保持默认值 `1` 不变。

#### 依赖关系

要启用此参数，请清除 **使用三相电气连接** 复选框。

### **采样类型** — 为耦合网络选择采样类型场景 `Variable step at ports 1 and 2`（默认） | `Variable step at port 1 and fixed step at port 2` | `Fixed step both ports with common sample time` | `Fixed step both ports with faster sampling at port 1`

选择耦合网络的采样方式：

- `Variable step at ports 1 and 2` — 两个网络均为变步长。
- `Variable step at port 1 and fixed step at port 2` — 网络 1 为变步长，网络 2 为定步长。
- `Fixed step both ports with common sample time` — 两个网络均为定步长，且步长相同。
- `Fixed step both ports with faster sampling at port 1` — 两个网络均为定步长，但步长不同。

### **分离器时间常数 (s)** — 指定滤波器时间常数 `1e-3`（默认） | 正标量

指定滤波器时间常数，以秒为单位，用于消除代数环。

#### 依赖关系

要启用此参数，请将 **采样类型** 参数设置为 `Variable step at ports 1 and 2`。

### **端口 1 网络离散采样时间 (s)** — 指定网络 1 的采样时间 `0.0002`（默认） | 正标量

指定网络 1 的采样时间，以秒为单位。

#### 依赖关系

要启用此参数，请将 **采样类型** 参数设置为 `Fixed step both ports with common sample time` 或 `Fixed step both ports with faster sampling at port 1`。

### **端口 2 网络离散采样时间 (s)** — 指定网络 2 的采样时间 `0.001`（默认） | 正标量

指定网络 2 的采样时间，以秒为单位。

#### 依赖关系

要启用此参数，请将 **采样类型** 参数设置为 `Variable step at port 1 and fixed step at port 2` 或 `Fixed step both ports with faster sampling at port 1`。

### **将定步长连接到变步长时使用预测** — 允许您启用预测（discrete->continuous）算法 off（默认） | on

选中此复选框以启用预测（discrete->continuous）算法。有关更多信息，请参阅预测和平滑。

#### 依赖关系

要显示此选项，请将 **采样类型** 参数设置为 `Variable step at port 1 and fixed step at port 2`。

### **将变步长连接到定步长时使用平滑** — 允许您启用平滑（continuous->discrete）算法 off（默认） | on

选中此复选框以启用平滑（continuous->discrete）算法。有关更多信息，请参阅预测和平滑。

#### 依赖关系

要显示此选项，请将 **采样类型** 参数设置为 `Variable step at port 1 and fixed step at port 2`。

### **平滑时间常数 (s)** — 指定一阶滤波器的时间常数 `0.01`（默认） | 正标量

指定一阶滤波器的时间常数，以秒为单位，平滑算法使用该滤波器去除不需要的高频信息。

#### 依赖关系

要启用此参数，请选中 **将变步长连接到定步长时使用平滑** 复选框。

### **将慢采样时间连接到快采样时间时使用预测** — 允许您启用预测（slow->fast）算法 off（默认） | on

选中此复选框以启用预测（slow->fast）算法。有关更多信息，请参阅预测和平滑。

#### 依赖关系

要显示此选项，请将 **采样类型** 参数设置为 `Fixed step both ports with faster sampling at port 1`。

### **将快采样时间连接到慢采样时间时使用平滑** — 允许您启用平滑（fast->slow）算法 off（默认） | on

选中此复选框以启用平滑（fast->slow）算法。有关更多信息，请参阅预测和平滑。

#### 依赖关系

要显示此选项，请将 **采样类型** 参数设置为 `Fixed step both ports with faster sampling at port 1`。

### **用于平滑的采样点数** — 指定用于平均的采样点数 `1`（默认） | 正标量

平滑算法通过对最后 *N* 个采样点求平均值来工作。您可以使用此参数指定 *N*。

#### 依赖关系

要启用此参数，请选中 **将快采样时间连接到慢采样时间时使用平滑** 复选框。

### 分析

有关如何使用 **派生值** 部分的信息，请参阅使用派生值估计模块参数。

### 初始条件

### **初始电流 (A)** — 指定耦合器传输的初始电流 `0`（默认） | 正标量

指定耦合器传输的电流的初始条件，以 A 为单位。

### **初始电压 (V)** — 指定耦合器两端的初始电压 `0`（默认） | 正标量

指定耦合器两端电压的初始条件，以 V 为单位。

## 所属库

Simscape / Utilities / Network Couplers

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2022a 中引入**

### R2024a: 断开电气节点数组之间的连接

该模块现在支持电气节点数组和三相连接。新参数 **电气节点数组大小** 允许您指定数组大小。或者，您可以使用新复选框 **使用三相电气连接**。如果在封装下查看，Port 1 Interface 和 Port 2 Interface 子系统包含支持向量化电气节点的自定义模块，而不是常规的 Foundation library 电气模块。

此更改没有兼容性影响。**使用三相电气连接** 复选框和 **电气节点数组大小** 参数的默认值对应于常规电气连接。如果您打开包含此模块的现有模型，仿真结果与以前版本相同。

## 描述

在电气连接处拆分网络

Network Coupler (Voltage-Current) 模块为您提供了一个起点，用于在电气连接处将 Simscape™ 网络拆分为两个耦合网络。当 Network 1（如命名约定中所述）具有串联连接的电感器或电流源，而 Network 2 没有时，请使用此模块。

此模块会改变系统行为，因为它添加了一个一阶滞后以消除代数环。

Network Coupler (Current-Voltage) 模块的端口 1 接口实现为电压源。因此，您不能将此端口连接到电压回路，例如一组串联连接的电压源和电容器，因为这将导致 Index-2 拓扑（有关更多信息，请参阅避免数值仿真问题）。端口 2 接口实现为电流源。因此，您不能将此端口连接到串联连接的电感器或电流源，因为这也会导致 Index-2 拓扑。

为了便于处理包含电气节点数组或三相连接的模型，Port 1 Interface 和 Port 2 Interface 子系统包含自定义模块，例如 Controlled Voltage Source 或 Current Sensor。这些自定义模块基于等效的 Foundation library 模块，但经过修改以支持向量化和三相电气节点。这些自定义模块的源文件位于以下命名空间：

    matlabroot/toolbox/physmod/simscape/library/m/+foundation/+internal/+couplers/+electrical

其中 *`matlabroot`* 是您计算机上的 MATLAB® 根目录，正如在 MATLAB 命令提示符下输入以下内容所返回的：

    matlabroot

该命名空间包含电压和电流源及传感器、电阻器以及支持数组和三相的电气参考的源文件。您可以使用这些模块来自定义您的网络耦合器配置。

### 在模型画布上使用该模块

当您将该模块添加到模型并双击它时，Network Coupler (Voltage-Current) 子系统会打开。

Network Coupler (Voltage-Current) 子系统图

Port 1 Interface 模块包含消除代数环的动态特性。双击此模块可设置所有 Network Coupler (Voltage-Current) 子系统参数并查看派生值。

默认情况下，速率转换模块被注释掉。如果至少一个耦合网络以定步长运行，请取消注释它们。

### 使用派生值估计模块参数

在 Port 1 Interface 模块对话框的 **分析** 选项卡上，**派生值** 部分包含 **计算出的最快可跟踪时间常数 (s)** 值，该值基于耦合器滞后的影响。如果两个网络均为变步长，则可直接指定滤波器时间常数作为模块参数。如果至少一个网络为定步长，则该模块会根据您指定的采样时间自动计算时间常数，且 **派生值** 部分会显示 **计算出的滤波器时间常数 (s)** 值。

**更新** 按钮允许您在更改所连接网络的参数后重新计算派生值。
