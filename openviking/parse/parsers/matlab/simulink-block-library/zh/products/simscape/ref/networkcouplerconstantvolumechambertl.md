---
type: simulink-block
title: 'Network Coupler (Constant Volume Chamber (TL))'
family: 'simscape'
product_id: 'simscape'
product_name: 'Simscape'
documentation_release: R2025b
official_category: 'Foundation Block Libraries / Utilities / Network Couplers'
documentation_page: 'networkcouplerconstantvolumechambertl'
documentation_source_path: 'ref/networkcouplerconstantvolumechambertl.html'
language: zh-CN
chinese_source: worker-translation
---

# Network Coupler (Constant Volume Chamber (TL))

## 端口

### 守恒

### **1** — 将此外端口连接到可变步长网络，或连接到具有较小采样时间的固定步长网络 thermal liquid

如果其中一个耦合网络以可变步长运行，请将其连接到 Network Coupler (Constant Volume Chamber
(TL)) 模块的端口 **1**。如果两个网络都以固定步长运行，请将此外端口连接到具有较小采样时间的网络。如果两个网络都以可变步长运行，或以相同步长的固定步长运行，则模块极性无关紧要。

### **2** — 将此外端口连接到具有较大采样时间的固定步长网络 thermal liquid

如果其中一个耦合网络以可变步长运行，请将 Network Coupler (Constant Volume Chamber
(TL)) 模块的端口 **2** 连接到固定步长网络。如果两个网络都以固定步长运行，请将此外端口连接到具有较大采样时间的网络。

## 参数

### 主要

### **Volume (m^3)** — 指定腔室的总容积 `0.001` (默认) | positive scalar

指定腔室的总容积，单位为 m^3。由于顶层子系统未封装，您需要为 Port 1 Interface 和 Port 2 Interface 模块将此参数设置为相同的值。

### **Port cross-sectional area (m^2)** — 指定垂直于流动方向的入口面积 `0.01` (默认) | positive scalar

指定垂直于流动方向的腔室入口面积，单位为 m^2。由于顶层子系统未封装，您需要为 Port 1 Interface 和 Port 2 Interface 模块将此参数设置为相同的值。

### **Sampling type** — 为耦合网络选择采样类型场景 `Variable step at ports 1 and 2` (默认) | `Variable step at port 1 and fixed step at port 2` | `Fixed step both ports with common sample time` | `Fixed step both ports with faster sampling at port 1`

选择耦合网络的采样方式：

- `Variable step at ports 1 and 2` — 两个网络均为可变步长。
- `Variable step at port 1 and fixed step at port 2` — 网络 1 为可变步长，网络 2 为固定步长。
- `Fixed step both ports with common sample time` — 两个网络均为固定步长，且步长相同。
- `Fixed step both ports with faster sampling at port 1` — 两个网络均为固定步长，且步长不同。

### **Port 1 network discrete sample time (s)** — 指定 Network 1 的采样时间 `0.02` (默认) | positive scalar

指定 Network 1 的采样时间，单位为秒。

#### 依赖关系

要启用此参数，请将 **Sampling type** 参数设置为 `Fixed step both ports with common sample time` 或 `Fixed step both ports with faster sampling at port 1`。

### **Port 2 network discrete sample time (s)** — 指定 Network 2 的采样时间 `0.1` (默认) | positive scalar

指定 Network 2 的采样时间，单位为秒。

#### 依赖关系

要启用此参数，请将 **Sampling type** 参数设置为 `Variable step at port 1 and fixed step at port 2` 或 `Fixed step both ports with faster sampling at port 1`。

### **Use prediction when connecting fixed step to variable step** — 允许您启用预测（discrete->continuous）算法 off (默认) | on

选中此复选框以启用预测（discrete->continuous）算法。有关详细信息，请参阅预测和平滑。

#### 依赖关系

要显示此选项，请将 **Sampling type** 参数设置为 `Variable step at port 1 and fixed step at port 2`。

### **Use smoothing when connecting variable step to fixed step** — 允许您启用平滑（continuous->discrete）算法 off (默认) | on

选中此复选框以启用平滑（continuous->discrete）算法。有关详细信息，请参阅预测和平滑。

#### 依赖关系

要显示此选项，请将 **Sampling type** 参数设置为 `Variable step at port 1 and fixed step at port 2`。

### **Smoothing time constant (s)** — 指定一阶滤波器的时间常数 `0.01` (默认) | positive scalar

指定一阶滤波器的时间常数，单位为秒，平滑算法使用该滤波器去除不需要的高频信息。

#### 依赖关系

要启用此参数，请选中 **Use smoothing when connecting variable step to fixed step** 复选框。

### **Use prediction when connecting slow to fast sample times** — 允许您启用预测（slow->fast）算法 off (默认) | on

选中此复选框以启用预测（slow->fast）算法。有关详细信息，请参阅预测和平滑。

#### 依赖关系

要显示此选项，请将 **Sampling type** 参数设置为 `Fixed step both ports with faster sampling at port 1`。

### **Use smoothing when connecting fast to slow sample times** — 允许您启用平滑（fast->slow）算法 off (默认) | on

选中此复选框以启用平滑（fast->slow）算法。有关详细信息，请参阅预测和平滑。

#### 依赖关系

要显示此选项，请将 **Sampling type** 参数设置为 `Fixed step both ports with faster sampling at port 1`。

### **Number of samples over which to smooth** — 指定用于求平均的采样数 `1` (默认) | positive scalar

平滑算法通过对最近 *N* 个采样求平均值来工作。您通过此参数指定 *N*。

#### 依赖关系

要启用此参数，请选中 **Use smoothing when connecting fast to slow sample times** 复选框。

### 分析

### **Approximate connected network flow conductance (kg/s/Pa)** — 指定近似连接网络流导 `1e-6` (默认) | positive scalar

指定近似连接网络流导，即每单位压差的质量流量，单位为 kg/s/Pa。

#### 依赖关系

要启用此参数，请将 **Sampling type** 参数设置为 `Variable step at port 1 and fixed step at port 2`、`Fixed step both ports with common sample time` 或 `Fixed step both ports with faster sampling at port 1`。

### **Approximate fluid density (kg/m^3)** — 指定连接网络中的近似流体密度 `1000` (默认) | positive scalar

指定连接网络中的近似流体密度，单位为 kg/m^3。

#### 依赖关系

要启用此参数，请将 **Sampling type** 参数设置为 `Variable step at port 1 and fixed step at port 2`、`Fixed step both ports with common sample time` 或 `Fixed step both ports with faster sampling at port 1`。

### **Approximate fluid bulk modulus (Pa)** — 指定连接网络中的近似流体体积模量 `2e9` (默认) | positive scalar

指定连接网络中的近似流体体积模量，单位为 Pa。

#### 依赖关系

要启用此参数，请将 **Sampling type** 参数设置为 `Variable step at port 1 and fixed step at port 2`、`Fixed step both ports with common sample time` 或 `Fixed step both ports with faster sampling at port 1`。

有关如何使用 **派生值** 部分的信息，请参阅使用派生值估计模块参数。

### 初始条件

### **Initial pressure (MPa)** — 指定初始压力 `0.101325` (默认) | positive scalar

指定腔室压力的初始条件，单位为 MPa。

### **Initial temperature (K)** — 指定初始温度 `293.15` (默认) | positive scalar

指定腔室温度的初始条件，单位为 K。

## 所属库

Simscape / Utilities / Network Couplers

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2022a 中引入**

### R2023b: 默认参数值已更改

**Volume** 和 **Initial temperature** 参数的默认值已更改，以匹配对应的 Foundation library 模块 Constant Volume Chamber (TL) 的默认值。

| 参数名称 | 旧值 | 新值 |
| --- | --- | --- |
| **Volume** | `0.01` | `0.01` |
| **Initial temperature** | `300` | `293.15` |

此更改没有兼容性影响。如果打开包含此模块的现有模型，参数值和仿真结果与之前的版本相同。

## 描述

在 thermal liquid 连接处拆分网络

Network Coupler (Constant Volume Chamber (TL)) 模块使用一定体积的流体来断开两个网络之间的连接。如果您现有的网络中已经建模了合适体积的流体，请将其替换为流体网络耦合器模块。否则，使用 Network Coupler (Constant Volume Chamber (TL)) 模块向系统引入新的流体体积。尽量使流体体积能够代表您划分网络处系统部件的尺寸，例如，使用连接管道的体积。如果体积太小，则需要更小的步长，这会使实时部署更加困难。

Network Coupler (Constant Volume Chamber (TL)) 模块的两个端口接口都实现为压力和温度源。因此，您不能将此模块直接连接到另一个流体体积或压力源，因为这会形成 Index-2 拓扑（有关详细信息，请参阅避免数值仿真问题）。

### 在模型画布上使用该模块

将模块添加到模型并双击它时，Network Coupler (Constant Volume Chamber (TL)) 子系统会打开。

Network Coupler (Constant Volume Chamber (TL)) 子系统图

Port 1 Interface 模块包含用于打破代数环的动态特性。双击此模块可设置大多数 Network Coupler (Constant Volume Chamber (TL)) 子系统参数并查看派生值。

但是，与大多数其他耦合器模块不同，Port 2 Interface 模块还有两个参数 **Volume (m^3)** 和 **Port cross-sectional area (m^2)**，您需要分别设置。

Network Coupler (Constant Volume Chamber (TL)) 模块基于 Foundation library 的 Constant Volume Chamber (TL) 模块，且该模块暴露两个流体端口。耦合器模块使用自定义 Simscape™ 组件 `partialChamberTL.ssc` 的两个副本来实现恒定体积腔室。每个部分腔室都对完整腔室建模，但仅计算因其流体端口流入而产生的压力和温度导数。耦合器子系统还包含两个 Simulink® 积分器，一个用于压力，一个用于温度，它们对来自两个部分腔室的导数求和并积分。这些 Simulink 积分器还打破了相应的代数约束（一个用于压力，一个用于温度），如果直接连接两个流体网络，则这些约束会存在。

**注意**

- 两个子系统请求的 **Volume (m^3)** 参数在两种情况下都是腔室的总容积，而不是一半容积。
- 网络耦合器模块会中断两个网络之间流体属性数据的传输。因此，您必须为两个网络都附加流体属性模块，并将每个实例的流体属性值设置为相同。

默认情况下，rate transition 模块处于注释穿透状态。如果至少一个耦合网络以固定步长运行，请取消注释它们。

### 使用派生值估计模块参数

在 Port 1 Interface 模块对话框的 **分析** 选项卡上，**派生值** 部分包含一组建议值，您可以在指定模块参数时使用这些值。例如，使用 **Recommended max discrete sample time (s)** 派生值来验证您的 **Port 1 network discrete sample time (s)** 和 **Port 2 network discrete sample time (s)** 参数值是否在可接受范围内。

派生值列表基于所选的模块配置。

如果两个网络都以可变步长运行，则 **分析** 选项卡为空，并且对您指定的流体体积值没有限制。

如果一个或两个网络以固定步长运行，则 **分析** 选项卡会提供有关建议使用的最大离散采样时间的建议。为此，您必须提供有关连接网络的一些附加信息：

- 近似连接网络流导，即每单位压差的质量流量。
- 近似流体密度。
- 近似流体体积模量。

这些值只需要近似，因为它们不会影响模型。它们仅用于提供有关建议最大离散采样时间的建议。

在更改连接网络的参数后，**更新** 按钮可让您重新计算派生值。
