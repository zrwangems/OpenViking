---
type: simulink-block
title: 'Network Coupler (Inductor)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Simscape'
documentation_release: R2025b
official_category: 'Foundation Block Libraries / Utilities / Network Couplers'
documentation_page: 'networkcouplerinductor'
documentation_source_path: 'ref/networkcouplerinductor.html'
language: zh-CN
chinese_source: worker-translation
---

# Network Coupler (Inductor)

## 端口

### 守恒

### **1** — 将此端口连接到可变步长网络，或连接到具有较小小采样时间的固定步长网络 电气 | 三相电气 | 电气节点数组

如果其中一个耦合网络以可变步长运行，请将其连接到 Network Coupler (Inductor) 模块的端口 **1**。如果两个网络都以固定步长运行，请将此端口连接到具有较小采样时间的网络。如果两个网络都以可变步长运行，或者以相同步长的固定步长运行，则模块极性无关紧要。

### **2** — 将此端口连接到具有较大采样时间的固定步长网络 电气 | 三相电气 | 电气节点数组

如果其中一个耦合网络以可变步长运行，请将 Network Coupler (Inductor) 模块的端口 **2** 连接到固定步长网络。如果两个网络都以固定步长运行，请将此端口连接到具有较大采样时间的网络。

## 参数

### 主

### **使用三相电气连接** — 在三相电气端口之间断开连接 off（默认）| on

在三相电气端口之间断开连接时，请选中此复选框。由于顶层子系统未封装，您需要为 Port 1 Interface 和 Port 2 Interface 模块都选中此复选框。
选中此复选框会禁用 **电气节点数组大小** 参数，因为端口 **1** 和 **2** 变为三相电气端口。

### **电气节点数组大小** — 指定电气节点数量 `1`（默认）| 正整数

指定连接到两个电气端口 **1** 和 **2** 的电气节点数组的大小。由于顶层子系统未封装，您需要为 Port 1 Interface 和 Port 2 Interface 模块将此参数设置为相同的值。

如果要断开常规电气连接，请保留默认值 `1` 不变。

#### 依赖关系

要启用此参数，请清除 **使用三相电气连接** 复选框。

### **电感 (H)** — 指定电感值 `1e-3`（默认）| 正标量

指定电感值。使用被替换的 Inductor 模块中的 **电感** 参数值，必要时将其转换为 H。

### **采样类型** — 为耦合网络选择采样类型场景 `Variable step at ports 1 and 2`（默认）| `Variable step at port 1 and fixed step at port 2` | `Fixed step both ports with common sample time` | `Fixed step both ports with faster sampling at port 1`

选择耦合网络的采样方式：

- `Variable step at ports 1 and 2` — 两个网络均为可变步长。
- `Variable step at port 1 and fixed step at port 2` — 网络 1 为可变步长，网络 2 为固定步长。
- `Fixed step both ports with common sample time` — 两个网络均为固定步长，且步长相同。
- `Fixed step both ports with faster sampling at port 1` — 两个网络均为固定步长，且步长不同。

### **端口 1 网络离散采样时间 (s)** — 指定网络 1 的采样时间 `0.0002`（默认）| 正标量

指定网络 1 的采样时间，单位为秒。

#### 依赖关系

要启用此参数，请将 **采样类型** 参数设置为 `Fixed step both ports with common sample time` 或 `Fixed step both ports with faster sampling at port 1`。

### **端口 2 网络离散采样时间 (s)** — 指定网络 2 的采样时间 `0.001`（默认）| 正标量

指定网络 2 的采样时间，单位为秒。

#### 依赖关系

要启用此参数，请将 **采样类型** 参数设置为 `Variable step at port 1 and fixed step at port 2` 或 `Fixed step both ports with faster sampling at port 1`。

### **将固定步长连接到可变步长时使用预测** — 允许启用预测（离散->连续）算法 off（默认）| on

选中此复选框以启用预测（离散->连续）算法。有关详细信息，请参阅预测和平滑。

#### 依赖关系

要显示此选项，请将 **采样类型** 参数设置为 `Variable step at port 1 and fixed step at port 2`。

### **将可变步长连接到固定步长时使用平滑** — 允许启用平滑（连续->离散）算法 off（默认）| on

选中此复选框以启用平滑（连续->离散）算法。有关详细信息，请参阅预测和平滑。

#### 依赖关系

要显示此选项，请将 **采样类型** 参数设置为 `Variable step at port 1 and fixed step at port 2`。

### **平滑时间常数 (s)** — 指定一阶滤波器的时间常数 `0.01`（默认）| 正标量

指定平滑算法用于去除不需要的高频信息的一阶滤波器的时间常数，单位为秒。

#### 依赖关系

要启用此参数，请选中 **将可变步长连接到固定步长时使用平滑** 复选框。

### **将慢采样时间连接到快采样时间时使用预测** — 允许启用预测（慢->快）算法 off（默认）| on

选中此复选框以启用预测（慢->快）算法。有关详细信息，请参阅预测和平滑。

#### 依赖关系

要显示此选项，请将 **采样类型** 参数设置为 `Fixed step both ports with faster sampling at port 1`。

### **将快采样时间连接到慢采样时间时使用平滑** — 允许启用平滑（快->慢）算法 off（默认）| on

选中此复选框以启用平滑（快->慢）算法。有关详细信息，请参阅预测和平滑。

#### 依赖关系

要显示此选项，请将 **采样类型** 参数设置为 `Fixed step both ports with faster sampling at port 1`。

### **用于平滑的样本数** — 指定用于平均的样本数 `1`（默认）| 正标量

平滑算法通过对最近 *N* 个样本求平均值来工作。您使用此参数指定 *N*。

#### 依赖关系

要启用此参数，请选中 **将快采样时间连接到慢采样时间时使用平滑** 复选框。

### 分析

### **连接的近似网络电阻 (ohms)** — 指定连接网络的近似电阻 `0.1`（默认）| 正标量

指定连接网络的近似电阻，单位为 ohm。如果两个网络的电阻不同，请提供较低的值。

#### 依赖关系

要启用此参数，请将 **采样类型** 参数设置为 `Variable step at port 1 and fixed step at port 2`、`Fixed step both ports with common sample time` 或 `Fixed step both ports with faster sampling at port 1`。

有关如何使用 **推导值** 部分的信息，请参阅使用推导值估计模块参数。

### 初始条件

### **初始电流 (A)** — 指定由电感传输的初始电流 `0`（默认）| 正标量

指定由电感传输的电流的初始条件，单位为 A。

## 所属库

Simscape / Utilities / Network Couplers

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2022a 中引入**

### R2024a：断开电气节点数组之间的连接

该模块现在支持电气节点数组和三相连接。新参数 **电气节点数组大小** 允许您指定数组大小。或者，您可以使用新复选框 **使用三相电气连接**。如果在封装下查看，Port 1 Interface 和 Port 2 Interface 子系统包含支持向量化电气节点的自定义模块，而不是常规的 Foundation 库电气模块。

此更改没有兼容性影响。**使用三相电气连接** 复选框和 **电气节点数组大小** 参数的默认值对应于常规电气连接。如果您打开包含此模块的现有模型，仿真结果与以前的版本相同。

## 描述

通过替换电感来在电气连接处拆分网络

Network Coupler (Inductor) 模块使用线路电感来断开网络连接。它可用于断开交流和直流网络连接。

Network Coupler (Inductor) 模块的两个端口接口都实现为电流源。因此：

- 不能将其他电感或电流源与 Network Coupler (Inductor) 模块串联，因为这会引发 Index-2 拓扑（有关详细信息，请参阅避免数值仿真问题）。如果可能，请将所有串联电感集中到一个模块中，并使用此模块拆分网络。
- 通过 Network Coupler (Inductor) 模块建立的连接不传递参考信息。如果使用此模块拆分两个网络之间的所有连接，则两个网络都必须至少包含一个 Electrical Reference 模块。如果不是这种情况，请考虑对至少一个连接使用其他电气耦合器模块之一。

为便于处理包含电气节点数组或三相连接的模型，Port 1 Interface 和 Port 2 Interface 子系统包含自定义模块，例如 Controlled Voltage Source 或 Current Sensor。这些自定义模块基于等效的 Foundation 库模块，但经过修改以支持向量化和三相电气节点。这些自定义模块的源文件位于以下命名空间中：

`matlabroot/toolbox/physmod/simscape/library/m/+foundation/+internal/+couplers/+electrical`

其中 *`matlabroot`* 是您计算机上的 MATLAB® 根目录，可通过在 MATLAB 命令提示符下输入

`matlabroot`

返回。该命名空间包含电压和电流源及传感器、电阻器以及支持数组和三相的电气参考的源文件。您可以使用这些模块自定义您的网络耦合器配置。

### 在模型画布上使用模块

当您将该模块添加到模型并双击它时，会打开 Network Coupler (Inductor) 子系统。

Network Coupler (Inductor) 子系统图

Port 1 Interface 模块包含打破代数环的动态特性。双击此模块可设置所有 Network Coupler (Inductor) 子系统参数并查看推导值。

默认情况下，速率转换模块被注释掉。如果至少一个耦合网络以固定步长运行，请取消注释它们。

### 使用推导值估计模块参数

在 Port 1 Interface 模块对话框的 **分析** 选项卡上，**推导值** 部分包含一列建议值，您可以在指定模块参数时使用这些值。例如，使用 **建议最大离散采样时间 (s)** 推导值来验证您的 **端口 1 网络离散采样时间 (s)** 和 **端口 2 网络离散采样时间 (s)** 参数值是否在可接受的限值内。

推导值列表基于所选的模块配置。

如果两个网络都以可变步长运行，则 **分析** 选项卡为空，并且对您指定的电感值没有限制。

如果一个或两个网络以固定步长运行，则由电感和连接的网络电阻产生的 RL 时间常数不得快于固定步长速率能够充分采样的程度。**分析** 选项卡会根据指定的电感值和连接的近似网络电阻值，提供有关建议最大采样时间的帮助。如果两个网络的电阻不同，请提供较低的值。

**更新** 按钮允许您在更改连接网络的参数后重新计算推导值。
