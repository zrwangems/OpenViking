---
type: simulink-block
title: 'Network Coupler (Flexible Shaft)'
family: 'utilities'
product_id: 'utilities'
product_name: 'Utilities'
documentation_release: R2025b
official_category: 'Network Couplers'
documentation_page: 'networkcouplerflexibleshaft'
documentation_source_path: '../simscape/ref/networkcouplerflexibleshaft.html'
language: zh-CN
chinese_source: worker-translation
---

# Network Coupler (Flexible Shaft)

## 端口
```yaml
ports:
- name: '1'
  summary: 将此端口连接到变步长网络，或连接到具有较小采样时间的定步长网络 机械旋转
  direction: unspecified
- name: '2'
  summary: 将此端口连接到具有较大采样时间的定步长网络 机械旋转
  direction: unspecified
```

### 守恒

### **1** — 将此端口连接到变步长网络，或连接到具有较小采样时间的定步长网络 机械旋转

如果其中一个耦合网络以变步长运行，请将其连接到 Network Coupler (Flexible Shaft) 模块的端口 **1**。
如果两个网络都以定步长运行，请将此端口连接到具有较小采样时间的网络。如果两个网络都以变步长运行，或以相同步长的定步长运行，则模块极性无关紧要。

### **2** — 将此端口连接到具有较大采样时间的定步长网络 机械旋转

如果其中一个耦合网络以变步长运行，请将 Network Coupler (Flexible Shaft) 模块的端口 **2** 连接到定步长网络。如果两个网络都以定步长运行，请将此端口连接到具有较大采样时间的网络。
## 参数
```yaml
parameters:
- name: Separate using
  summary: 选择分离类型 an actual shaft compliance（默认）| an added numerical compliance
  group: 主要
- name: Shaft stiffness (Nm/rad)
  summary: 指定柔性轴的刚度 250（默认）| 正标量
  group: 主要
- name: Shaft damping (Nm/(rad/s))
  summary: 指定柔性轴的阻尼系数 20（默认）| 正标量
  group: 主要
- name: Sampling type
  summary: 选择耦合网络的采样类型场景 Variable step at ports 1 and 2（默认）| 端口 1 为可变步长，端口处为固定步长 2 | Fixed step both ports with common sample
    time | 两个端口均为固定步长，且在端口处采样更快 1
  group: 主要
- name: Separator time constant (s)
  summary: 指定滤波器时间常数 0.001（默认）| 正标量
  group: 主要
- name: Port 1 network discrete sample time (s)
  summary: 指定网络 1 的采样时间 0.001（默认）| 正标量
  group: 主要
- name: Port 2 network discrete sample time (s)
  summary: 指定网络 2 的采样时间 0.01（默认）| 正标量
  group: 主要
- name: Use prediction when connecting fixed step to variable step
  summary: 允许您启用预测（离散->连续）算法 关（默认）| 开
  group: 主要
- name: Use smoothing when connecting variable step to fixed step
  summary: 允许您启用平滑（连续->离散）算法 关（默认）| 开
  group: 主要
- name: Smoothing time constant (s)
  summary: 指定一阶滤波器的时间常数 0.01（默认）| 正标量
  group: 主要
- name: Use prediction when connecting slow to fast sample times
  summary: 允许您启用预测（慢->快）算法 关（默认）| 开
  group: 主要
- name: Use smoothing when connecting fast to slow sample times
  summary: 允许您启用平滑（快->慢）算法 关（默认）| 开
  group: 主要
- name: Number of samples over which to smooth
  summary: 指定用于求平均的样本数 1（默认）| 正标量
  group: 主要
- name: Approximate inertia at port 1 (kg\*m^2)
  summary: 指定端口 1 处的近似惯量 1（默认）| 正标量
  group: 分析
- name: Approximate inertia at port 2 (kg\*m^2)
  summary: 指定端口 2 处的近似惯量 1（默认）| 正标量
  group: 分析
- name: Initial transmitted torque (Nm)
  summary: 指定轴传递的初始扭矩 0（默认）| 正标量
  group: 初始条件
```

### 主要

### **Separate using** — 选择分离类型 `an actual shaft compliance`（默认）| `an added numerical compliance`

选择如何分离耦合网络：

- `an actual shaft compliance` — 在存在实际柔性轴的位置拆分网络。使用轴柔度来提高耦合网络的稳定性。
- `an added numerical compliance` — 添加数值柔度并使用它来提高耦合网络的稳定性。

### **Shaft stiffness (Nm/rad)** — 指定柔性轴的刚度 `250`（默认）| 正标量

如果要替换模型中的实际弹簧和阻尼器，请指定弹簧刚度。使用被替换的 Rotational Spring 模块中的 **Spring rate** 参数值，必要时将其转换为 Nm/rad。

#### 依赖关系

要启用此参数，请将 **Separate using** 参数设置为 `an actual shaft compliance`。

### **Shaft damping (Nm/(rad/s))** — 指定柔性轴的阻尼系数 `20`（默认）| 正标量

如果要替换模型中的实际弹簧和阻尼器，请指定阻尼系数。使用被替换的 Rotational Damper 模块中的 **Damping coefficient** 参数值，必要时将其转换为 Nm/(rad/s)。

#### 依赖关系

要启用此参数，请将 **Separate using** 参数设置为 `an actual shaft compliance`。

### **Sampling type** — 选择耦合网络的采样类型场景 `Variable step at ports 1 and 2`（默认）| `端口 1 为可变步长，端口处为固定步长 2` | `Fixed step both ports with common sample time` | `两个端口均为固定步长，且在端口处采样更快 1`

选择耦合网络的采样方式：

- `Variable step at ports 1 and 2` — 两个网络均为变步长。
- `端口 1 为可变步长，端口处为固定步长 2` — 网络 1 为变步长，网络 2 为定步长。
- `Fixed step both ports with common sample time` — 两个网络均为定步长，且步长相同。
- `两个端口均为固定步长，且在端口处采样更快 1` — 两个网络均为定步长，且步长不同。

### **Separator time constant (s)** — 指定滤波器时间常数 `0.001`（默认）| 正标量

指定滤波器时间常数（以秒为单位），以消除代数环。

#### 依赖关系

要启用此参数，请将 **Sampling type** 参数设置为 `Variable step at ports 1 and 2`。

### **Port 1 network discrete sample time (s)** — 指定网络 1 的采样时间 `0.001`（默认）| 正标量

指定网络 1 的采样时间（以秒为单位）。

#### 依赖关系

要启用此参数，请将 **Sampling type** 参数设置为 `Fixed step both ports with common sample time` 或 `两个端口均为固定步长，且在端口处采样更快 1`。

### **Port 2 network discrete sample time (s)** — 指定网络 2 的采样时间 `0.01`（默认）| 正标量

指定网络 2 的采样时间（以秒为单位）。

#### 依赖关系

要启用此参数，请将 **Sampling type** 参数设置为
`端口 1 为可变步长，端口处为固定步长 2` 或
`两个端口均为固定步长，且在端口处采样更快
1`。

### **Use prediction when connecting fixed step to variable step** — 允许您启用预测（离散->连续）算法 关（默认）| 开

选中此复选框以启用预测（离散->连续）算法。
有关详细信息，请参阅 Prediction and Smoothing。

#### 依赖关系

要显示此选项，请将 **Sampling type** 参数设置为
`端口 1 为可变步长，端口处为固定步长
2`。

### **Use smoothing when connecting variable step to fixed step** — 允许您启用平滑（连续->离散）算法 关（默认）| 开

选中此复选框以启用平滑（连续->离散）算法。
有关详细信息，请参阅 Prediction and Smoothing。

#### 依赖关系

要显示此选项，请将 **Sampling type** 参数设置为
`端口 1 为可变步长，端口处为固定步长
2`。

### **Smoothing time constant (s)** — 指定一阶滤波器的时间常数 `0.01`（默认）| 正标量

指定一阶滤波器的时间常数（以秒为单位），平滑算法使用该滤波器去除不需要的高频信息。

#### 依赖关系

要启用此参数，请选中 **Use smoothing when connecting
variable step to fixed step** 复选框。

### **Use prediction when connecting slow to fast sample times** — 允许您启用预测（慢->快）算法 关（默认）| 开

选中此复选框以启用预测（慢->快）算法。有关
详细信息，请参阅 Prediction and Smoothing。

#### 依赖关系

要显示此选项，请将 **Sampling type** 参数设置为
`两个端口均为固定步长，且在端口处采样更快
1`。

### **Use smoothing when connecting fast to slow sample times** — 允许您启用平滑（快->慢）算法 关（默认）| 开

选中此复选框以启用平滑（快->慢）算法。有关
详细信息，请参阅 Prediction and Smoothing。

#### 依赖关系

要显示此选项，请将 **Sampling type** 参数设置为
`两个端口均为固定步长，且在端口处采样更快
1`。

### **Number of samples over which to smooth** — 指定用于求平均的样本数 `1`（默认）| 正标量

平滑算法通过对最近 *N* 个样本求平均值来工作。
您使用此参数指定 *N*。

#### 依赖关系

要启用此参数，请选中 **Use smoothing when connecting
fast to slow sample times** 复选框。

### 分析

### **Approximate inertia at port 1 (kg\*m^2)** — 指定端口 1 处的近似惯量 `1`（默认）| 正标量

指定端口 **1** 处的近似惯量，以 kg\*m^2 为单位。

### **Approximate inertia at port 2 (kg\*m^2)** — 指定端口 2 处的近似惯量 `1`（默认）| 正标量

指定端口 **2** 处的近似惯量，以 kg\*m^2 为单位。

有关如何使用 **Derived values** 部分的信息，请参阅 Using the Derived Values to Estimate Block Parameters。

### 初始条件

### **Initial transmitted torque (Nm)** — 指定轴传递的初始扭矩 `0`（默认）| 正标量

指定轴传递的扭矩的初始条件，以 N\*m 为单位。
## 所属库

Simscape / Utilities / Network Couplers

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2022a 中引入**

## 描述

在机械旋转连接处拆分网络

Network Coupler (Flexible Shaft) 模块为您提供了一个起点，用于在机械旋转连接处将 Simscape™ 网络拆分为两个耦合网络。

Network Coupler (Flexible Shaft) 模块的工作原理是在两个网络之间添加柔量。假设耦合器模块两侧均存在惯量。请勿将模块端口直接连接到扭矩源。您可以将模块端口连接到理想角速度源。

如果您的模型中已有柔性轴（建模为 Rotational Spring 模块与 Rotational Damper 模块并联），则可以使用 Network Coupler (Flexible Shaft) 模块直接替换这两个模块。这样可以避免为分离网络而额外添加第二个柔量。如果不存在可用的现有模型柔量，则可以通过在机械旋转连接处插入 Network Coupler (Flexible Shaft) 模块并将其 **Separate using** 参数设置为 `an added numerical compliance` 来添加数值柔量。

### 在模型画布上使用该模块

将模块添加到模型并双击它时，Network Coupler (Flexible Shaft) 子系统将打开。

Network Coupler (Flexible Shaft) 子系统图

Port 1 Interface 模块包含打破代数环的动态特性。双击此模块可设置所有 Network Coupler (Flexible Shaft) 子系统参数并查看派生值。

速率转换模块默认通过注释禁用。如果至少一个耦合网络以固定步长运行，请取消注释它们。

### 使用派生值估算模块参数

在 Port 1 Interface 模块对话框的 **Analysis** 选项卡上，**Derived values** 部分包含一个推荐值列表，您可以在指定模块参数时使用这些值。例如，使用 **Recommended max discrete sample time (s)** 派生值来验证您的 **Port 1 network discrete sample time (s)** 和 **Port 2 network discrete sample time (s)** 参数值是否在可接受范围内。

派生值列表基于所选的模块配置。例如：

- 如果您使用现有柔量，模块将使用有关所连接网络的惯量以及柔量的信息，来推荐最大滤波器时间常数或最大离散采样时间。为此，模块计算整体网络动态时间常数，并推荐与最快时间常数相匹配的时间常数（**Recommended max filter time constant (s)**）或采样时间（**Recommended max discrete sample time (s)**）值。
- 如果您添加数值柔量，模块将根据所连接网络的惯量和指定的采样时间或滤波器时间常数，计算所需的刚度和阻尼。它还提供最快可跟踪时间常数的估计值。如果 **Calculated fastest trackable time constant (s)** 值对于您的应用来说过慢，则必须减小您为相关模块参数指定的值，例如 **Separator time constant (s)**、**Port 1 network discrete sample time (s)** 或 **Port 2 network discrete sample time (s)**。

**Update** 按钮允许您在更改所连接网络的参数后重新计算派生值。
