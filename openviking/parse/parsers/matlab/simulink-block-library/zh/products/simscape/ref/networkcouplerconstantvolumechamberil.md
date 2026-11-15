---
type: simulink-block
title: 'Network Coupler (Constant Volume Chamber (IL))'
family: 'simscape'
product_id: 'simscape'
product_name: 'Simscape'
documentation_release: R2025b
official_category: 'Foundation Block Libraries / Utilities / Network Couplers'
documentation_page: 'networkcouplerconstantvolumechamberil'
documentation_source_path: 'ref/networkcouplerconstantvolumechamberil.html'
language: zh-CN
chinese_source: worker-translation
---

# Network Coupler (Constant Volume Chamber (IL))

## 端口

### 守恒

### **1** — 将本端口连接到变步长网络，或连接到具有更小采样时间的固定步长网络 isothermal liquid

如果耦合网络之一以变步长运行，请将其连接到 Network Coupler (Constant Volume Chamber (IL)) 模块的端口 **1**。如果两个网络均以固定步长运行，请将此端口连接到具有更小采样时间的网络。如果两个网络均以变步长运行，或以相同步长以固定步长运行，则模块极性无关紧要。

### **2** — 将本端口连接到具有更大采样时间的固定步长网络 isothermal liquid

如果耦合网络之一以变步长运行，请将 Network Coupler (Constant Volume Chamber (IL)) 模块的端口 **2** 连接到固定步长网络。如果两个网络均以固定步长运行，请将此端口连接到具有更大采样时间的网络。

## 参数

### 主要

### **Volume (m^3)** — 指定腔体总容积 `0.001`（默认）| 正标量

指定腔体总容积，单位为 m^3。由于顶层子系统未封装，需要为 Port 1 Interface 和 Port 2 Interface 模块将此参数设置为相同的值。

### **Sampling type** — 选择耦合网络的采样类型场景 `Variable step at ports 1 and 2`（默认）| `Variable step at port 1 and fixed step at port 2` | `Fixed step both ports with common sample time` | `Fixed step both ports with faster sampling at port 1`

选择耦合网络的采样方式：

- `Variable step at ports 1 and 2` — 两个网络均为变步长。
- `Variable step at port 1 and fixed step at port 2` — 网络 1 为变步长，网络 2 为固定步长。
- `Fixed step both ports with common sample time` — 两个网络均为固定步长，且步长相同。
- `Fixed step both ports with faster sampling at port 1` — 两个网络均为固定步长，且步长不同。

### **Port 1 network discrete sample time (s)** — 指定 Network 1 的采样时间 `0.02`（默认）| 正标量

指定 Network 1 的采样时间，单位为秒。

#### 依赖关系

要启用此参数，请将 **Sampling type** 参数设置为 `Fixed step both ports with common sample time` 或 `Fixed step both ports with faster sampling at port 1`。

### **Port 2 network discrete sample time (s)** — 指定 Network 2 的采样时间 `0.1`（默认）| 正标量

指定 Network 2 的采样时间，单位为秒。

#### 依赖关系

要启用此参数，请将 **Sampling type** 参数设置为 `Variable step at port 1 and fixed step at port 2` 或 `Fixed step both ports with faster sampling at port 1`。

### **Use prediction when connecting fixed step to variable step** — 允许启用预测（discrete->continuous）算法 off（默认）| on

选中此复选框以启用预测（discrete->continuous）算法。有关详细信息，请参阅预测和平滑。

#### 依赖关系

要显示此选项，请将 **Sampling type** 参数设置为 `Variable step at port 1 and fixed step at port 2`。

### **Use smoothing when connecting variable step to fixed step** — 允许启用平滑（continuous->discrete）算法 off（默认）| on

选中此复选框以启用平滑（continuous->discrete）算法。有关详细信息，请参阅预测和平滑。

#### 依赖关系

要显示此选项，请将 **Sampling type** 参数设置为 `Variable step at port 1 and fixed step at port 2`。

### **Smoothing time constant (s)** — 指定一阶滤波器的时间常数 `0.01`（默认）| 正标量

指定时间常数，单位为秒，用于平滑算法去除不需要的高频信息的一阶滤波器。

#### 依赖关系

要启用此参数，请选中 **Use smoothing when connecting variable step to fixed step** 复选框。

### **Use prediction when connecting slow to fast sample times** — 允许启用预测（slow->fast）算法 off（默认）| on

选中此复选框以启用预测（slow->fast）算法。有关详细信息，请参阅预测和平滑。

#### 依赖关系

要显示此选项，请将 **Sampling type** 参数设置为 `Fixed step both ports with faster sampling at port 1`。

### **Use smoothing when connecting fast to slow sample times** — 允许启用平滑（fast->slow）算法 off（默认）| on

选中此复选框以启用平滑（fast->slow）算法。有关详细信息，请参阅预测和平滑。

#### 依赖关系

要显示此选项，请将 **Sampling type** 参数设置为 `Fixed step both ports with faster sampling at port 1`。

### **Number of samples over which to smooth** — 指定用于平均的样本数 `1`（默认）| 正标量

平滑算法通过对最后 *N* 个样本求平均值来工作。您可以使用此参数指定 *N*。

#### 依赖关系

要启用此参数，请选中 **Use smoothing when connecting fast to slow sample times** 复选框。

### 分析

### **Approximate connected network flow conductance (kg/s/Pa)** — 指定近似连接网络流导 `1e-6`（默认）| 正标量

指定近似连接网络流导，即单位压差的质量流量，单位为 kg/s/Pa。

#### 依赖关系

要启用此参数，请将 **Sampling type** 参数设置为 `Variable step at port 1 and fixed step at port 2`、`Fixed step both ports with common sample time` 或 `Fixed step both ports with faster sampling at port 1`。

### **Approximate fluid density (kg/m^3)** — 指定连接网络中的近似流体密度 `1000`（默认）| 正标量

指定连接网络中的近似流体密度，单位为 kg/m^3。

#### 依赖关系

要启用此参数，请将 **Sampling type** 参数设置为 `Variable step at port 1 and fixed step at port 2`、`Fixed step both ports with common sample time` 或 `Fixed step both ports with faster sampling at port 1`。

### **Approximate fluid bulk modulus (Pa)** — 指定连接网络中的近似流体体积模量 `2e9`（默认）| 正标量

指定连接网络中的近似流体体积模量，单位为 Pa。

#### 依赖关系

要启用此参数，请将 **Sampling type** 参数设置为 `Variable step at port 1 and fixed step at port 2`、`Fixed step both ports with common sample time` 或 `Fixed step both ports with faster sampling at port 1`。

有关如何使用 **Derived values** 部分的信息，请参阅使用派生值估计模块参数。

### 初始条件

### **Initial pressure (MPa)** — 指定初始压力 `0.101325`（默认）| 正标量

指定腔体中压力的初始条件，单位为 MPa。

## 所属库

Simscape / Utilities / Network Couplers

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ Code Generation

使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2022a 中引入**

### R2023b: 默认参数值已更改

**Volume** 参数的默认值已更改，以匹配对应的 Foundation 库模块 Constant Volume Chamber (IL) 的默认值。

| 参数名 | 旧值 | 新值 |
| --- | --- | --- |
| **Volume** | `0.01` | `0.01` |

此更改无兼容性影响。如果打开包含此模块的现有模型，参数值和仿真结果与以前版本相同。

## 描述

在等温液体连接处拆分网络

Network Coupler (Constant Volume Chamber (IL)) 模块使用一定体积的流体来断开两个网络之间的连接。如果您现有网络已经建模了合适的流体体积，则将其替换为流体网络耦合器模块。否则，使用 Network Coupler (Constant Volume Chamber (IL)) 模块向系统中引入新的流体体积。尽量使流体体积能够代表您分割网络处系统部分的尺寸，例如使用连接管道的体积。如果体积太小，将需要更小的步长，这会使实时部署更加困难。

Network Coupler (Constant Volume Chamber (IL)) 模块的两个端口接口均实现为压力源。因此，不能将此模块直接连接到另一个流体体积或压力源，因为这会引发 Index-2 拓扑（有关详细信息，请参阅避免数值仿真问题）。

### 在模型画布上使用模块

将模块添加到模型并双击它时，Network Coupler (Constant Volume Chamber (IL)) 子系统将打开。

Network Coupler (Constant Volume Chamber (IL)) 子系统图

Port 1 Interface 模块包含用于断开代数环的动态特性。双击此模块可设置大多数 Network Coupler (Constant Volume Chamber (IL)) 子系统参数，并查看派生值。

但是，与大多数其他耦合器模块不同，Port 2 Interface 模块还有一个参数 **Volume (m^3)**，需要单独设置。

Network Coupler (Constant Volume Chamber (IL)) 模块使用自定义 Simscape™ 组件 `partialChamberIL.ssc` 的两个副本实现恒定容积腔体。这些部分腔体中的每一个都对完整腔体进行建模，但仅计算由其流体端口流入所引起的压力导数。构成耦合器子系统一部分的 Simulink® 积分器随后对两个导数求和并积分。正是该 Simulink 积分器用于断开代数压力约束，如果直接连接两个流体网络，该约束将会存在。

**注意**

- 两个子系统请求的 **Volume (m^3)** 参数在两种情况下均为腔体总容积，而不是一半容积。
- 网络耦合器模块会断开两个网络之间流体属性数据的传输。因此，必须为两个网络都附加流体属性模块，并将每个实例的流体属性值设置为相同。

速率转换模块默认被注释穿透。如果至少一个耦合网络以固定步长运行，请取消注释它们。

### 使用派生值估计模块参数

在 Port 1 Interface 模块对话框的 **Analysis** 选项卡上，**Derived values** 部分包含一组推荐值，可在指定模块参数时使用。例如，使用 **Recommended max discrete sample time (s)** 派生值来验证 **Port 1 network discrete sample time (s)** 和 **Port 2 network discrete sample time (s)** 参数值是否处于可接受范围内。

派生值列表基于所选的模块配置。

如果两个网络均以变步长运行，则 **Analysis** 选项卡为空，并且对指定的流体体积值没有限制。

如果一个或两个网络以固定步长运行，则 **Analysis** 选项卡会提供有关推荐使用的最大离散采样时间的建议。为此，必须提供有关连接网络的一些附加信息：

- 近似连接网络流导，即单位压差的质量流量。
- 近似流体密度。
- 近似流体体积模量。

这些值只需是近似值，因为它们不会影响模型。它们仅用于提供有关推荐最大离散采样时间的建议。

**Update** 按钮允许您在更改连接网络的参数后重新计算派生值。
