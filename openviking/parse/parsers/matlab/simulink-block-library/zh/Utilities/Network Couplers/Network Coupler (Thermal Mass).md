---
type: simulink-block
title: 'Network Coupler (Thermal Mass)'
family: 'utilities'
product_id: 'utilities'
product_name: 'Utilities'
documentation_release: R2025b
official_category: 'Network Couplers'
documentation_page: 'networkcouplerthermalmass'
documentation_source_path: '../simscape/ref/networkcouplerthermalmass.html'
language: zh-CN
chinese_source: worker-translation
---

# Network Coupler (Thermal Mass)

## 端口

### 守恒端口

### **1** — 将此端口连接到变步长网络，或连接到具有较小采样时间的定步长网络 thermal | thermal node array

如果耦合网络之一以变步长运行，请将其连接到 Network Coupler (Thermal Mass) 模块的端口 **1**。
如果两个网络均以定步长运行，请将此端口连接到具有较小采样时间的网络。如果两个网络均以变步长运行，或以相同步长的定步长运行，则模块极性无关紧要。

### **2** — 将此端口连接到具有较大采样时间的定步长网络 thermal | thermal node array

如果耦合网络之一以变步长运行，请将 Network Coupler (Thermal Mass) 模块的端口 **2** 连接到定步长网络。如果两个网络均以定步长运行，请将此端口连接到具有较大采样时间的网络。

## 参数

### 主要

### **Thermal node array size** — 指定热节点数量 `1`（默认）| 正整数

指定连接到两个热端口 **1** 和 **2** 的热节点数组的大小。由于顶层子系统未封装，您需要为 Port 1 Interface 和 Port 2 Interface 模块将此参数设置为相同的值。

如果您要断开常规热连接，请将默认值 `1` 保持不变。但是，某些模型使用热节点数组，例如，将使用 Simscape Battery 建模的电池包连接到相应的冷却板。在这种情况下，电池包中有多个热节点，它们在冷却板上有对应的热节点。您可以使用 Network Coupler (Thermal Mass) 模块来分隔两个网络，以便对热部分使用较慢的采样时间，对电气部分使用较快的采样时间。在此类模型中使用 Network Coupler (Thermal Mass) 模块有助于加速桌面仿真，并使模型更容易部署到实时硬件。

### **Thermal mass (J/K)** — 指定热质量值 `100`（默认）| 正标量

指定热质量值。使用被替换的 Thermal Mass 模块中的 **Mass** 和 **Specific heat** 参数来计算此值。**Analysis** 选项卡也提供有关选择合适热质量值的帮助。有关详细信息，请参阅 Using the Derived Values to Estimate Block Parameters。

### **Sampling type** — 为耦合网络选择采样类型场景 `Variable step at ports 1 and 2`（默认）| `端口 1 使用可变步长，端口 2 使用固定步长 2` | `Fixed step both ports with common sample time` | `两个端口均使用固定步长，且端口 2 的采样更快 1`

选择耦合网络的采样方式：

- `Variable step at ports 1 and 2` — 两个网络均为变步长。
- `端口 1 使用可变步长，端口 2 使用固定步长 2` — 网络 1 为变步长，网络 2 为定步长。
- `Fixed step both ports with common sample time` — 两个网络均为定步长，且步长相同。
- `两个端口均使用固定步长，且端口 2 的采样更快 1` — 两个网络均为定步长，且步长不同。

### **Port 1 network discrete sample time (s)** — 指定网络 1 的采样时间 `0.02`（默认）| 正标量

指定网络 1 的采样时间，以秒为单位。

#### 依赖关系

要启用此参数，请将 **Sampling type** 参数设置为 `Fixed step both ports with common sample time` 或 `两个端口均使用固定步长，且端口 2 的采样更快 1`。

### **Port 2 network discrete sample time (s)** — 指定网络 2 的采样时间 `0.1`（默认）| 正标量

指定网络 2 的采样时间，以秒为单位。

#### 依赖关系

要启用此参数，请将 **Sampling type** 参数设置为 `端口 1 使用可变步长，端口 2 使用固定步长 2` 或 `两个端口均使用固定步长，且端口 2 的采样更快 1`。

### **Use prediction when connecting fixed step to variable step** — 允许您启用或关闭预测（离散->连续）算法 关闭（默认）| 开启

选中此复选框以启用预测（离散->连续）算法。
有关详细信息，请参阅 Prediction and Smoothing。

#### 依赖关系

要显示此选项，请将 **Sampling type** 参数设置为
`端口 1 使用可变步长，端口 2 使用固定步长
2`。

### **Use smoothing when connecting variable step to fixed step** — 允许您启用或关闭平滑（连续->离散）算法 关闭（默认）| 开启

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

### **Use prediction when connecting slow to fast sample times** — 允许您启用或关闭预测（慢->快）算法 关闭（默认）| 开启

选中此复选框以启用预测（慢->快）算法。有关
详细信息，请参阅 Prediction and Smoothing。

#### 依赖关系

要显示此选项，请将 **Sampling type** 参数设置为
`两个端口均使用固定步长，且端口 2 的采样更快
1`。

### **Use smoothing when connecting fast to slow sample times** — 允许您启用或关闭平滑（快->慢）算法 关闭（默认）| 开启

选中此复选框以启用平滑（快->慢）算法。有关
详细信息，请参阅 Prediction and Smoothing。

#### 依赖关系

要显示此选项，请将 **Sampling type** 参数设置为
`两个端口均使用固定步长，且端口 2 的采样更快
1`。

### **Number of samples over which to smooth** — 指定用于求平均的样本数 `1`（默认）| 正标量

平滑算法通过对最近 *N* 个样本求平均来工作。
您可以使用此参数指定 *N*。

#### 依赖关系

要启用此参数，请选中 **Use smoothing when connecting
fast to slow sample times** 复选框。

### 分析

### **Approximate connected network thermal conductance (W/K)** — 指定连接网络的近似热导 `1`（默认）| 正标量

指定连接网络的近似热导，以 W/K 为单位。如果两个网络的热导
不同，请提供较高的值。

#### 依赖关系

要启用此参数，请将 **Sampling type** 参数
设置为 `端口 1 使用可变步长，端口 2 使用固定步长 2`、
`Fixed step both ports with common sample time` 或
`两个端口均使用固定步长，且端口 2 的采样更快
1`。

有关如何使用 **Derived values** 部分的信息，请参阅 Using the Derived Values to Estimate Block Parameters。

### 初始条件

### **Initial temperature (K)** — 指定热质量的初始温度 `300`（默认）| 正标量

指定热质量温度的初始条件，以 K 为单位。

## 所属库

Simscape / Utilities / Network Couplers

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2022a 中引入**

### R2023b：断开热节点数组之间的连接

Network Coupler (Thermal Mass) 模块现在支持热节点数组。新参数 **Thermal node array size** 允许您指定数组大小。如果您查看掩码内部，Port 1 Interface 和 Port 2 Interface 子系统包含支持向量化热节点的自定义模块，而不是常规的 Foundation 库热模块。

此更改没有兼容性影响。**Thermal node array size** 参数的默认值对应于常规热连接。如果您打开包含此模块的现有模型，仿真结果与之前版本相同。

## 描述

在热连接处拆分网络

Network Coupler (Thermal Mass) 模块使用热质量来断开网络连接。如果您的现有网络已经建模了合适的热质量，则将其替换为网络耦合器模块。否则，使用 Network Coupler (Thermal Mass) 模块向系统引入新的热质量。

Network Coupler (Thermal Mass) 模块的两个端口接口都实现为温度源。因此，您不能将此模块直接连接到热质量或其他温度源，因为这将导致 Index-2 拓扑（有关详细信息，请参阅 Avoiding Numerical Simulation Issues）。

为了便于处理包含热节点数组的模型（例如 Simscape™ Battery™ 模型），Port 1 Interface 和 Port 2 Interface 子系统包含自定义模块，例如 Controlled Temperature Source 或 Heat Flow Rate Sensor。这些自定义模块基于等效的 Foundation 库模块，但经过修改以支持向量化热节点。这些自定义模块的源文件位于以下包目录中：

```
matlabroot/toolbox/physmod/simscape/library/m/+foundation/+internal/+couplers/+thermal
```

其中 *`matlabroot`* 是您机器上的 MATLAB® 根目录，可通过在 MATLAB 命令提示符下输入以下命令返回

```
matlabroot
```

该包包含热流和温度源与传感器以及支持数组的热参考的源文件。您可以使用这些模块来自定义您的网络耦合器配置。

### 在模型画布上使用该模块

当您将模块添加到模型并双击它时，Network Coupler (Thermal Mass) 子系统会打开。

Network Coupler (Thermal Mass) 子系统图

Port 1 Interface 模块包含断开代数环的动态特性。双击此模块可设置所有 Network Coupler (Thermal Mass) 子系统参数并查看派生值。

速率转换模块默认通过注释禁用。如果至少一个耦合网络以固定步长运行，请取消注释它们。

### 使用派生值估算模块参数

在 Port 1 Interface 模块对话框的 **Analysis** 选项卡上，**Derived values** 部分包含一个推荐值列表，您可以在指定模块参数时使用这些值。例如，使用 **Recommended max discrete sample time (s)** 派生值来验证您的 **Port 1 network discrete sample time (s)** 和 **Port 2 network discrete sample time (s)** 参数值在可接受范围内。

派生值列表基于所选的模块配置。

如果两个网络都以变步长运行，则 **Analysis** 选项卡为空，并且您指定的热质量值没有限制。

如果一个或两个网络以固定步长运行，则 **Analysis** 选项卡通过要求您为连接的网络提供近似热导值，来帮助您选择合适的热质量值。如果两个网络的热导不同，请提供较高的值。然后，**Update** 按钮会提供要使用的最大推荐离散采样时间。
