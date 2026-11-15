---
type: simulink-block
title: 'Network Coupler (Flexible Shaft)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Simscape'
documentation_release: R2025b
official_category: 'Foundation Block Libraries / Utilities / Network Couplers'
documentation_page: 'networkcouplerflexibleshaft'
documentation_source_path: 'ref/networkcouplerflexibleshaft.html'
language: zh-CN
chinese_source: worker-translation
---

# Network Coupler (Flexible Shaft)

## 端口

### 守恒

### **1** — 将此端口连接到可变步长网络，或连接到具有较小采样时间的定步长网络 mechanical rotational

如果其中一个耦合网络以可变步长运行，请将其连接到 Network Coupler (Flexible Shaft) 模块的端口
**1**。
如果两个网络均以定步长运行，请将此端口连接到采样时间较小的网络。如果两个网络均以可变步长运行，或以相同步长的定步长运行，则模块极性无关紧要。

### **2** — 将此端口连接到具有较大采样时间的定步长网络 mechanical rotational

如果其中一个耦合网络以可变步长运行，请将 Network Coupler (Flexible Shaft) 模块的端口
**2** 连接到定步长网络。如果两个网络均以定步长运行，请将此端口连接到采样时间较大的网络。

## 参数

### 主要

### **Separate using** — 选择分离类型 `an actual shaft compliance`（默认）| `an added numerical compliance`

选择如何分离耦合网络：

- `an actual shaft compliance` — 在实际柔性轴所在点拆分网络。使用轴柔度来提高耦合网络的稳定性。
- `an added numerical compliance` — 添加数值柔度，并使用它来提高耦合网络的稳定性。

### **Shaft stiffness (Nm/rad)** — 指定柔性轴的刚度 `250`（默认）| positive scalar

如果要替换模型中的实际弹簧和阻尼器，请指定弹簧刚度。使用被替换的 Rotational Spring 模块中的 **Spring rate** 参数值，必要时将其转换为 Nm/rad。

#### 依赖关系

要启用此参数，请将 **Separate using** 参数设置为 `an actual shaft compliance`。

### **Shaft damping (Nm/(rad/s))** — 指定柔性轴的阻尼系数 `20`（默认）| positive scalar

如果要替换模型中的实际弹簧和阻尼器，请指定阻尼系数。使用被替换的 Rotational Damper 模块中的 **Damping coefficient** 参数值，必要时将其转换为 Nm/(rad/s)。

#### 依赖关系

要启用此参数，请将 **Separate using** 参数设置为 `an actual shaft compliance`。

### **Sampling type** — 为耦合网络选择采样类型场景 `Variable step at ports 1 and 2`（默认）| `Variable step at port 1 and fixed step at port 2` | `Fixed step both ports with common sample time` | `Fixed step both ports with faster sampling at port 1`

选择耦合网络的采样方式：

- `Variable step at ports 1 and 2` — 两个网络均为可变步长。
- `Variable step at port 1 and fixed step at port 2` — Network 1 为可变步长，Network 2 为定步长。
- `Fixed step both ports with common sample time` — 两个网络均为定步长，且步长相同。
- `Fixed step both ports with faster sampling at port 1` — 两个网络均为定步长，且步长不同。

### **Separator time constant (s)** — 指定滤波器时间常数 `0.001`（默认）| positive scalar

指定滤波器时间常数（以秒为单位），以消除代数环。

#### 依赖关系

要启用此参数，请将 **Sampling type** 参数设置为 `Variable step at ports 1 and 2`。

### **Port 1 network discrete sample time (s)** — 指定 Network 1 的采样时间 `0.001`（默认）| positive scalar

指定 Network 1 的采样时间（以秒为单位）。

#### 依赖关系

要启用此参数，请将 **Sampling type** 参数设置为 `Fixed step both ports with common sample time` 或 `Fixed step both ports with faster sampling at port 1`。

### **Port 2 network discrete sample time (s)** — 指定 Network 2 的采样时间 `0.01`（默认）| positive scalar

指定 Network 2 的采样时间（以秒为单位）。

#### 依赖关系

要启用此参数，请将 **Sampling type** 参数设置为 `Variable step at port 1 and fixed step at port 2` 或 `Fixed step both ports with faster sampling at port 1`。

### **Use prediction when connecting fixed step to variable step** — 使您能够启用预测（discrete->continuous）算法 off（默认）| on

选中此复选框以启用预测（discrete->continuous）算法。
有关详细信息，请参阅预测和平滑。

#### 依赖关系

要显示此选项，请将 **Sampling type** 参数设置为 `Variable step at port 1 and fixed step at port 2`。

### **Use smoothing when connecting variable step to fixed step** — 使您能够启用平滑（continuous->discrete）算法 off（默认）| on

选中此复选框以启用平滑（continuous->discrete）算法。
有关详细信息，请参阅预测和平滑。

#### 依赖关系

要显示此选项，请将 **Sampling type** 参数设置为 `Variable step at port 1 and fixed step at port 2`。

### **Smoothing time constant (s)** — 指定一阶滤波器的时间常数 `0.01`（默认）| positive scalar

指定平滑算法用于消除不需要的高频信息的一阶滤波器的时间常数（以秒为单位）。

#### 依赖关系

要启用此参数，请选中 **Use smoothing when connecting variable step to fixed step** 复选框。

### **Use prediction when connecting slow to fast sample times** — 使您能够启用预测（slow->fast）算法 off（默认）| on

选中此复选框以启用预测（slow->fast）算法。有关详细信息，请参阅预测和平滑。

#### 依赖关系

要显示此选项，请将 **Sampling type** 参数设置为 `Fixed step both ports with faster sampling at port 1`。

### **Use smoothing when connecting fast to slow sample times** — 使您能够启用平滑（fast->slow）算法 off（默认）| on

选中此复选框以启用平滑（fast->slow）算法。有关详细信息，请参阅预测和平滑。

#### 依赖关系

要显示此选项，请将 **Sampling type** 参数设置为 `Fixed step both ports with faster sampling at port 1`。

### **Number of samples over which to smooth** — 指定用于求平均的采样数 `1`（默认）| positive scalar

平滑算法通过对最后 *N* 个采样求平均来工作。您使用此参数指定 *N*。

#### 依赖关系

要启用此参数，请选中 **Use smoothing when connecting fast to slow sample times** 复选框。

### 分析

### **Approximate inertia at port 1 (kg\*m^2)** — 指定 port 1 处的近似惯性 `1`（默认）| positive scalar

指定端口 **1** 处的近似惯性，以 kg\*m^2 为单位。

### **Approximate inertia at port 2 (kg\*m^2)** — 指定 port 2 处的近似惯性 `1`（默认）| positive scalar

指定端口 **2** 处的近似惯性，以 kg\*m^2 为单位。

有关如何使用 **Derived values** 部分的信息，请参阅使用派生值估计模块参数。

### 初始条件

### **Initial transmitted torque (Nm)** — 指定轴传递的初始扭矩 `0`（默认）| positive scalar

指定轴传递扭矩的初始条件，以 N\*m 为单位。

## 所属库

Simscape / Utilities / Network Couplers

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2022a 中引入**

## 描述

在机械旋转连接处拆分网络

Network Coupler (Flexible Shaft) 模块为您提供了一个起点，用于在机械旋转连接处将 Simscape™ 网络拆分为两个耦合网络。

Network Coupler (Flexible Shaft) 模块通过在两个网络之间添加柔度来工作。假定耦合器模块两侧各有一个惯性。请勿将模块端口直接连接到扭矩源。可以将模块端口连接到理想角速度源。

如果您的模型已有柔性轴（建模为 Rotational Spring 模块与 Rotational Damper 模块并联），则使用 Network Coupler (Flexible Shaft) 模块直接替换这两个模块。这样可以避免再添加一个用于分离网络的柔度。如果模型中没有可使用的现有柔度，则通过在机械旋转连接处插入 Network Coupler (Flexible Shaft) 模块，并将其 **Separate using** 参数设置为 `an added numerical compliance`，来添加数值柔度。

### 在模型画布上使用模块

当您将模块添加到模型并双击它时，Network Coupler (Flexible Shaft) 子系统会打开。

Network Coupler (Flexible Shaft) 子系统图

Port 1 Interface 模块包含用于打破代数环的动态特性。双击此模块可设置所有 Network Coupler (Flexible Shaft) 子系统参数并查看派生值。

默认情况下，速率转换模块被注释掉。如果至少一个耦合网络以定步长运行，请取消注释它们。

### 使用派生值估计模块参数

在 Port 1 Interface 模块对话框的 **Analysis** 选项卡上，**Derived values** 部分包含一个推荐值列表，您可以在指定模块参数时使用这些值。例如，使用 **Recommended max discrete sample time (s)** 派生值来验证您的 **Port 1 network discrete sample time (s)** 和 **Port 2 network discrete sample time (s)** 参数值在可接受范围内。

派生值列表基于所选的模块配置。例如：

- 如果您使用现有柔度，模块会使用有关所连接网络的惯性信息以及该柔度，来推荐最大滤波器时间常数或最大离散采样时间。为此，模块会计算整体网络动态时间常数，并推荐与最快时间常数相称的时间常数（**Recommended max filter time constant (s)**）或采样时间（**Recommended max discrete sample time (s)**）值。
- 如果您要添加数值柔度，模块会基于所连接网络的惯性和指定的采样时间或滤波器时间常数，计算所需的刚度和阻尼。它还提供最快可跟踪时间常数的估计值。如果 **Calculated fastest trackable time constant (s)** 值对于您的应用来说太慢，则必须减小为相关模块参数指定的值，例如 **Separator time constant (s)**、**Port 1 network discrete sample time (s)** 或 **Port 2 network discrete sample time (s)**。

**Update** 按钮允许您在更改所连接网络的参数后重新计算派生值。
