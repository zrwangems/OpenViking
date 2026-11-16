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

### 守恒

### **1** — 将此端口连接到变步长网络，或连接到具有较小时步长的定步长网络 thermal | thermal node array

如果其中一个耦合网络以变步长运行，则将其连接到 Network Coupler (Thermal Mass) 模块的端口 **1**。
如果两个网络都以定步长运行，则将此端口连接到具有较小时步长的网络。如果两个网络都以变步长运行，或者以相同步长的定步长运行，则模块极性无关紧要。

### **2** — 将此端口连接到具有较大时步长的定步长网络 thermal | thermal node array

如果其中一个耦合网络以变步长运行，则将 Network Coupler (Thermal Mass) 模块的端口 **2** 连接到定步长网络。如果两个网络都以定步长运行，则将此端口连接到具有较大时步长的网络。

## 参数

### 主设置

### **Thermal node array size** — 指定热节点数量 `1` (default) | positive integer

指定连接到两个热端口 **1** 和 **2** 的热节点数组大小。由于顶层子系统未封装，您需要为 Port 1 Interface 和 Port 2 Interface 模块将此参数设置为相同的值。

如果要断开常规热连接，请将 `1` 的默认值保持不变。但是，某些模型使用热节点数组，例如，将使用 Simscape Battery 建模的电池组连接到相应的冷却板。在这种情况下，电池组中有多个热节点，在冷却板上有对应的热节点。您可以使用 Network Coupler (Thermal Mass) 模块分隔两个网络，以便对热部分使用较慢的采样时间，对电气部分使用较快的采样时间。在此类模型中使用 Network Coupler (Thermal Mass) 模块有助于加速桌面仿真，并使模型更容易部署到实时硬件。

### **Thermal mass (J/K)** — 指定热质量值 `100` (default) | positive scalar

指定热质量值。使用被替换的 Thermal Mass 模块中的 **Mass** 和 **Specific heat** 参数来计算此值。**分析**选项卡还提供有关选择合适热质量值的帮助。有关详细信息，请参阅使用派生值估计模块参数。

### **Sampling type** — 选择耦合网络的采样类型场景 `Variable step at ports 1 and 2` (default) | `Variable step at port 1 and fixed step at port 2` | `Fixed step both ports with common sample time` | `Fixed step both ports with faster sampling at port 1`

选择耦合网络的采样方式：

- `Variable step at ports 1 and 2` — 两个网络均为变步长。
- `Variable step at port 1 and fixed step at port 2` — Network 1 为变步长，Network 2 为定步长。
- `Fixed step both ports with common sample time` — 两个网络均为定步长，且步长相同。
- `Fixed step both ports with faster sampling at port 1` — 两个网络均为定步长，且步长不同。

### **Port 1 network discrete sample time (s)** — 指定 Network 1 的采样时间 `0.02` (default) | positive scalar

指定 Network 1 的采样时间，以秒为单位。

#### 依赖关系

要启用此参数，请将 **Sampling type** 参数设置为 `Fixed step both ports with common sample time` 或 `Fixed step both ports with faster sampling at port 1`。

### **Port 2 network discrete sample time (s)** — 指定 Network 2 的采样时间 `0.1` (default) | positive scalar

指定 Network 2 的采样时间，以秒为单位。

#### 依赖关系

要启用此参数，请将 **Sampling type** 参数设置为 `Variable step at port 1 and fixed step at port 2` 或 `Fixed step both ports with faster sampling at port 1`。

### **Use prediction when connecting fixed step to variable step** — 允许您启用预测（离散->连续）算法 off (default) | on

选中此复选框以启用预测（离散->连续）算法。有关详细信息，请参阅预测和平滑。

#### 依赖关系

要显示此选项，请将 **Sampling type** 参数设置为 `Variable step at port 1 and fixed step at port 2`。

### **Use smoothing when connecting variable step to fixed step** — 允许您启用平滑（连续->离散）算法 off (default) | on

选中此复选框以启用平滑（连续->离散）算法。有关详细信息，请参阅预测和平滑。

#### 依赖关系

要显示此选项，请将 **Sampling type** 参数设置为 `Variable step at port 1 and fixed step at port 2`。

### **Smoothing time constant (s)** — 指定一阶滤波器的时间常数 `0.01` (default) | positive scalar

指定平滑算法用于去除不需要的高频信息的一阶滤波器的时间常数，以秒为单位。

#### 依赖关系

要启用此参数，请选中 **Use smoothing when connecting variable step to fixed step** 复选框。

### **Use prediction when connecting slow to fast sample times** — 允许您启用预测（慢->快）算法 off (default) | on

选中此复选框以启用预测（慢->快）算法。有关详细信息，请参阅预测和平滑。

#### 依赖关系

要显示此选项，请将 **Sampling type** 参数设置为 `Fixed step both ports with faster sampling at port 1`。

### **Use smoothing when connecting fast to slow sample times** — 允许您启用平滑（快->慢）算法 off (default) | on

选中此复选框以启用平滑（快->慢）算法。有关详细信息，请参阅预测和平滑。

#### 依赖关系

要显示此选项，请将 **Sampling type** 参数设置为 `Fixed step both ports with faster sampling at port 1`。

### **Number of samples over which to smooth** — 指定用于平均的样本数 `1` (default) | positive scalar

平滑算法通过对最后 *N* 个样本求平均值来工作。您可以使用此参数指定 *N*。

#### 依赖关系

要启用此参数，请选中 **Use smoothing when connecting fast to slow sample times** 复选框。

### 分析

### **Approximate connected network thermal conductance (W/K)** — 指定连接网络的近似热导 `1` (default) | positive scalar

指定连接网络的近似热导，以 W/K 为单位。如果两个网络的热导不同，请提供较高的值。

#### 依赖关系

要启用此参数，请将 **Sampling type** 参数设置为 `Variable step at port 1 and fixed step at port 2`、`Fixed step both ports with common sample time` 或 `Fixed step both ports with faster sampling at port 1`。

有关如何使用 **派生值** 区域的信息，请参阅使用派生值估计模块参数。

### 初始条件

### **Initial temperature (K)** — 指定热质量的初始温度 `300` (default) | positive scalar

指定热质量温度的初始条件，以 K 为单位。

## 所属库

Simscape / Utilities / Network Couplers

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**R2022a 中引入**

### R2023b：断开热节点数组之间的连接

Network Coupler (Thermal Mass) 模块现在支持热节点数组。新参数 **Thermal node array size** 允许您指定数组大小。如果在封装下查看，Port 1 Interface 和 Port 2 Interface 子系统包含支持向量化热节点的自定义模块，而不是常规 Foundation library 热模块。

此更改对兼容性没有影响。**Thermal node array size** 参数的默认值对应于常规热连接。如果打开包含此模块的现有模型，仿真结果与之前版本相同。

## 描述

在热连接处拆分网络

Network Coupler (Thermal Mass) 模块使用热质量来断开网络连接。如果您现有网络中已经建模了合适的热质量，则将其替换为 Network Coupler 模块。否则，使用 Network Coupler (Thermal Mass) 模块向系统引入新的热质量。

Network Coupler (Thermal Mass) 模块的两个端口接口均实现为温度源。因此，不能将此模块直接连接到热质量或其他温度源，因为这将导致 Index-2 拓扑（有关详细信息，请参阅避免数值仿真问题）。

为便于处理包含热节点数组的模型（例如 Simscape™ Battery™ 模型），Port 1 Interface 和 Port 2 Interface 子系统包含自定义模块，例如 Controlled Temperature Source 或 Heat Flow Rate Sensor。这些自定义模块基于等效的 Foundation library 模块，但经过修改以支持向量化热节点。这些自定义模块的源文件位于以下包目录中：

```
matlabroot/toolbox/physmod/simscape/library/m/+foundation/+internal/+couplers/+thermal
```

其中 *`matlabroot`* 是您计算机上的 MATLAB® 根目录，可通过在 MATLAB 命令提示符下输入以下内容返回：

```
matlabroot
```

该包包含热流和温度源与传感器以及支持数组的热参考的源文件。您可以使用这些模块自定义您的 Network Coupler 配置。

### 在模型画布上使用模块

当您将该模块添加到模型并双击它时，会打开 Network Coupler (Thermal Mass) 子系统。

Network Coupler (Thermal Mass) 子系统图

Port 1 Interface 模块包含打破代数环的动态特性。双击此模块以设置所有 Network Coupler (Thermal Mass) 子系统参数并查看派生值。

默认情况下，速率转换模块已被注释掉。如果至少一个耦合网络以定步长运行，请取消注释它们。

### 使用派生值估计模块参数

在 Port 1 Interface 模块对话框的 **分析**选项卡上，**派生值**区域包含一个推荐值列表，您可以在指定模块参数时使用这些值。例如，使用 **推荐的最大离散采样时间 (s)** 派生值来验证您的 **Port 1 network discrete sample time (s)** 和 **Port 2 network discrete sample time (s)** 参数值是否在可接受范围内。

派生值列表基于所选的模块配置。

如果两个网络都以变步长运行，则 **分析**选项卡为空，并且对您指定的热质量值没有限制。

如果一个或两个网络以定步长运行，则 **分析**选项卡通过要求您为连接网络提供近似热导值，来帮助您选择合适的热质量值。如果两个网络的热导不同，请提供较高的值。然后，**更新**按钮会提供要使用的最大推荐离散采样时间。
