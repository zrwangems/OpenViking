---
type: simulink-block
title: 'Network Coupler (Voltage-Current)'
family: 'utilities'
product_id: 'network-couplers'
product_name: 'Network Couplers'
documentation_release: R2025b
official_category: 'Network Couplers'
documentation_page: 'networkcouplervoltagecurrent'
documentation_source_path: '../simscape/ref/networkcouplervoltagecurrent.html'
language: zh-CN
chinese_source: worker-translation
---

# Network Coupler (Voltage-Current)

## 端口
```yaml
ports:
- name: '1'
  summary: 将此端口连接到变步长网络，或连接到具有较小采样时间的定步长网络 electrical | three-phase electrical | electrical node array
  direction: unspecified
- name: '2'
  summary: 将此端口连接到具有较大采样时间的定步长网络 electrical | three-phase electrical | electrical node array
  direction: unspecified
```

### 守恒

### **1** — 将此端口连接到变步长网络，或连接到具有较小采样时间的定步长网络 electrical | three-phase electrical | electrical node array

如果其中一个耦合网络以变步长运行，请将其连接到 Network Coupler (Voltage-Current) 模块的端口 **1**。如果两个网络都以定步长运行，请将此端口连接到具有较小采样时间的网络。如果两个网络都以变步长运行，或以相同步长的定步长运行，则模块极性无关紧要。

### **2** — 将此端口连接到具有较大采样时间的定步长网络 electrical | three-phase electrical | electrical node array

如果其中一个耦合网络以变步长运行，请将 Network Coupler (Voltage-Current) 模块的端口 **2** 连接到定步长网络。如果两个网络都以定步长运行，请将此端口连接到具有较大采样时间的网络。
## 参数
```yaml
parameters:
- name: Use three-phase electrical connections
  summary: 断开三相电气端口之间的连接 off (default) | on
  group: 主要
- name: Electrical node array size
  summary: 指定电气节点数量 1 (default) | positive integer
  group: 主要
- name: Sampling type
  summary: 为耦合网络选择采样类型场景 Variable step at ports 1 and 2 (default) | 端口 1 使用可变步长，端口 2 使用固定步长 2 | Fixed step both ports with
    common sample time | 两个端口均使用固定步长，且端口 2 的采样更快 1
  group: 主要
- name: Separator time constant (s)
  summary: 指定滤波器时间常数 1e-3 (default) | positive scalar
  group: 主要
- name: Port 1 network discrete sample time (s)
  summary: 指定网络 1 的采样时间 0.0002 (default) | positive scalar
  group: 主要
- name: Port 2 network discrete sample time (s)
  summary: 指定网络 2 的采样时间 0.001 (default) | positive scalar
  group: 主要
- name: Use prediction when connecting fixed step to variable step
  summary: 允许您启用预测（离散->连续）算法 off（默认）| on
  group: 主要
- name: Use smoothing when connecting variable step to fixed step
  summary: 允许您启用平滑（连续->离散）算法 off（默认）| on
  group: 主要
- name: Smoothing time constant (s)
  summary: 指定一阶滤波器的时间常数 0.01（默认）| 正标量
  group: 主要
- name: Use prediction when connecting slow to fast sample times
  summary: 允许您启用预测（慢->快）算法 off（默认）| on
  group: 主要
- name: Use smoothing when connecting fast to slow sample times
  summary: 允许您启用平滑（快->慢）算法 off（默认）| on
  group: 主要
- name: Number of samples over which to smooth
  summary: 指定用于求平均的样本数 1（默认）| 正标量
  group: 主要
- name: Initial current (A)
  summary: 指定耦合器传输的初始电流 0（默认）| 正标量
  group: 初始条件
- name: Initial voltage (V)
  summary: 指定耦合器两端的初始电压 0（默认）| 正标量
  group: 初始条件
```

### 主要

### **Use three-phase electrical connections** — 断开三相电气端口之间的连接 off (default) | on

在断开三相电气端口之间的连接时，选中此复选框。由于顶层子系统未屏蔽，您需要为 Port 1 Interface 和 Port 2 Interface 模块都选中此复选框。
选中此复选框会禁用 **Electrical node array size** 参数，因为端口 **1** 和 **2** 变为三相电气端口。

### **Electrical node array size** — 指定电气节点数量 `1` (default) | positive integer

指定连接到两个电气端口 **1** 和 **2** 的电气节点数组的大小。由于顶层子系统未屏蔽，您需要为 Port 1 Interface 和 Port 2 Interface 模块将此参数设置为相同的值。

如果您要断开常规电气连接，请将默认值 `1` 保持不变。

#### 依赖关系

要启用此参数，请清除 **Use three-phase electrical connections** 复选框。

### **Sampling type** — 为耦合网络选择采样类型场景 `Variable step at ports 1 and 2` (default) | `端口 1 使用可变步长，端口 2 使用固定步长 2` | `Fixed step both ports with common sample time` | `两个端口均使用固定步长，且端口 2 的采样更快 1`

选择耦合网络的采样方式：

- `Variable step at ports 1 and 2` — 两个网络均为变步长。
- `端口 1 使用可变步长，端口 2 使用固定步长 2` — 网络 1 为变步长，网络 2 为定步长。
- `Fixed step both ports with common sample time` — 两个网络均为定步长，且步长相同。
- `两个端口均使用固定步长，且端口 2 的采样更快 1` — 两个网络均为定步长，且步长不同。

### **Separator time constant (s)** — 指定滤波器时间常数 `1e-3` (default) | positive scalar

指定滤波器时间常数（以秒为单位），以消除代数环。

#### 依赖关系

要启用此参数，请将 **Sampling type** 参数设置为 `Variable step at ports 1 and 2`。

### **Port 1 network discrete sample time (s)** — 指定网络 1 的采样时间 `0.0002` (default) | positive scalar

指定网络 1 的采样时间（以秒为单位）。

#### 依赖关系

要启用此参数，请将 **Sampling type** 参数设置为 `Fixed step both ports with common sample time` 或 `两个端口均使用固定步长，且端口 2 的采样更快 1`。

### **Port 2 network discrete sample time (s)** — 指定网络 2 的采样时间 `0.001` (default) | positive scalar

指定网络 2 的采样时间（以秒为单位）。

#### 依赖关系

要启用此参数，请将 **Sampling type** 参数设置为 `端口 1 使用可变步长，端口 2 使用固定步长 2` 或 `两个端口均使用固定步长，且端口 2 的采样更快 1`。

### **Use prediction when connecting fixed step to variable step** — 允许您启用预测（离散->连续）算法 off（默认）| on

选中此复选框以启用预测（离散->连续）算法。
有关详细信息，请参阅 Prediction and Smoothing。

#### 依赖关系

要显示此选项，请将 **Sampling type** 参数设置为
`端口 1 使用可变步长，端口 2 使用固定步长
2`。

### **Use smoothing when connecting variable step to fixed step** — 允许您启用平滑（连续->离散）算法 off（默认）| on

选中此复选框以启用平滑（连续->离散）算法。
有关详细信息，请参阅 Prediction and Smoothing。

#### 依赖关系

要显示此选项，请将 **Sampling type** 参数设置为
`端口 1 使用可变步长，端口 2 使用固定步长
2`。

### **Smoothing time constant (s)** — 指定一阶滤波器的时间常数 `0.01`（默认）| 正标量

指定平滑算法用于去除不需要的高频信息的一阶滤波器的时间常数，以秒为单位。

#### 依赖关系

要启用此参数，请选中 **Use smoothing when connecting
variable step to fixed step** 复选框。

### **Use prediction when connecting slow to fast sample times** — 允许您启用预测（慢->快）算法 off（默认）| on

选中此复选框以启用预测（慢->快）算法。有关
详细信息，请参阅 Prediction and Smoothing。

#### 依赖关系

要显示此选项，请将 **Sampling type** 参数设置为
`两个端口均使用固定步长，且端口 2 的采样更快
1`。

### **Use smoothing when connecting fast to slow sample times** — 允许您启用平滑（快->慢）算法 off（默认）| on

选中此复选框以启用平滑（快->慢）算法。有关
详细信息，请参阅 Prediction and Smoothing。

#### 依赖关系

要显示此选项，请将 **Sampling type** 参数设置为
`两个端口均使用固定步长，且端口 2 的采样更快
1`。

### **Number of samples over which to smooth** — 指定用于求平均的样本数 `1`（默认）| 正标量

平滑算法通过对最近 *N* 个样本求平均来工作。
您使用此参数指定 *N*。

#### 依赖关系

要启用此参数，请选中 **Use smoothing when connecting
fast to slow sample times** 复选框。

### Analysis

有关如何使用 **Derived values** 部分的信息，请参阅 Using the Derived Values to Estimate Block Parameters。

### 初始条件

### **Initial current (A)** — 指定耦合器传输的初始电流 `0`（默认）| 正标量

指定耦合器传输的电流的初始条件，以 A 为单位。

### **Initial voltage (V)** — 指定耦合器两端的初始电压 `0`（默认）| 正标量

指定耦合器两端电压的初始条件，以 V 为单位。
## 所属库

Simscape / Utilities / Network Couplers

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2022a 中引入**

### R2024a: 断开电气节点数组之间的连接

该模块现在支持电气节点数组和三相连接。新参数 **Electrical node array size** 允许您指定数组大小。或者，您可以使用新复选框 **Use three-phase electrical connections**。如果您查看掩码内部，Port 1 Interface 和 Port 2 Interface 子系统包含支持向量化电气节点的自定义模块，而不是常规的 Foundation 库电气模块。

此更改没有兼容性影响。**Use three-phase electrical connections** 复选框和 **Electrical node array size** 参数的默认值对应于常规电气连接。如果您打开包含此模块的现有模型，仿真结果与之前版本相同。

## 描述

在电气连接处拆分网络

Network Coupler (Voltage-Current) 模块为您提供了一个起点，用于在电气连接处将 Simscape™ 网络拆分为两个耦合网络。当网络 1（如命名约定中所述）具有串联电感或电流源，而网络 2 没有时，请使用此模块。

此模块会改变系统行为，因为它添加了一阶滞后以打破代数环。

Network Coupler (Current-Voltage) 模块的端口 1 接口实现为电压源。因此，您不能将此端口连接到电压环，例如一组串联的电压源和电容器，因为这会导致 Index-2 拓扑（更多信息，请参阅避免数值仿真问题）。端口 2 接口实现为电流源。因此，您不能将此端口连接到串联电感或电流源，因为这也会导致 Index-2 拓扑。

为了便于处理包含电气节点数组或三相连接的模型，Port 1 Interface 和 Port 2 Interface 子系统包含自定义模块，例如 Controlled Voltage Source 或 Current Sensor。这些自定义模块基于等效的 Foundation 库模块，但经过修改以支持向量化和三相电气节点。这些自定义模块的源文件位于以下命名空间中：

```
matlabroot/toolbox/physmod/simscape/library/m/+foundation/+internal/+couplers/+electrical
```

其中 *`matlabroot`* 是您机器上的 MATLAB® 根目录，可通过在 MATLAB 命令提示符下输入以下命令返回

```
matlabroot
```

该命名空间包含电压和电流源及传感器、电阻器以及支持数组和三相的电气参考的源文件。您可以使用这些模块来自定义您的网络耦合器配置。

### 在模型画布上使用该模块

当您将模块添加到模型并双击它时，Network Coupler (Voltage-Current) 子系统会打开。

Network Coupler (Voltage-Current) 子系统图

Port 1 Interface 模块包含打破代数环的动态特性。双击此模块可设置所有 Network Coupler (Voltage-Current) 子系统参数并查看派生值。

速率转换模块默认通过注释注释掉。如果至少一个耦合网络以固定步长运行，请取消注释它们。

### 使用派生值来估计模块参数

在 Port 1 Interface 模块对话框的**分析**选项卡上，**派生值**部分包含**计算得到的最快可跟踪时间常数 (s)** 值，该值基于耦合器延迟的影响。如果两个网络都是变步长，则直接指定滤波器时间常数，作为模块参数。如果至少一个网络是固定步长，则该模块会根据指定的采样时间自动计算时间常数，并且**派生值**部分会显示**计算得到的滤波器时间常数 (s)** 值。

**更新**按钮允许你在更改所连接网络的参数后重新计算派生值。
