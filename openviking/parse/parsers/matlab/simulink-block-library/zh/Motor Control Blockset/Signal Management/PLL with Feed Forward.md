---
type: simulink-block
title: 'PLL with Feed Forward'
family: 'signal-management'
product_id: 'mcb'
product_name: 'Motor Control Blockset'
documentation_release: R2025b
official_category: 'Signal Management'
documentation_page: 'pllwithfeedforward'
documentation_source_path: 'ref/pllwithfeedforward.html'
language: zh-CN
chinese_source: worker-translation
---

# PLL with Feed Forward

## 端口

### 输入

### **α** — *α*-轴信号标量

沿 *α*-轴的输入信号。

**数据类型：** `single` | `double` | `fixed point`

### **β** — *β*-轴信号标量

沿 *β*-轴的输入信号。

**数据类型：** `single` | `double` | `fixed point`

### **Rst** — 外部复位脉冲标量

用于复位模块的外部脉冲。

**数据类型：** `single` | `double` | `fixed point`

### **ParameterBus** — PLL with Feed Forward bus 的计算参数

PLL with Feed Forward 模块的计算参数。该输入端口接受以下参数：

- **最大应用频率 (Hz)**
- **输出滤波器截止频率 (Hz)**
- **查找表数据点数量**
- **比例 (P)**
- **积分 (I)**

将此端口与 Compute Parameter 模块一起使用，以在运行时最优地更新上述模块参数。

#### 依赖关系

要启用此端口，请选择 **高级选项** 部分中提供的 **使用输入端口获取计算参数（运行时电机切换）** 参数。

**数据类型：** `single` | `double`

### 输出

### **θ** — 角位置标量

模块根据正交输入信号计算得到的角位置（以 degrees、radians 或 per-unit 为单位）。

#### 依赖关系

要启用此端口，请将 **位置输出** 参数设置为 `Angular position`。

**数据类型：** `single` | `double` | `fixed point`

### **Sin θ** — 角位置的正弦标量

计算得到的角位置的正弦等效值。

#### 依赖关系

要启用此端口，请将 **位置输出** 参数设置为 `Sine and Cosine Position`。

**数据类型：** `single` | `double` | `fixed point`

### **Cos θ** — 角位置的余弦标量

计算得到的角位置的余弦等效值。

#### 依赖关系

要启用此端口，请将 **位置输出** 参数设置为 `Sine and Cosine Position`。

**数据类型：** `single` | `double` | `fixed point`

### **ω** — 角频率标量

正交输入信号的角频率（以 degrees/sec、radians/sec 或 hertz 为单位）。

**数据类型：** `single` | `double` | `fixed point`

## 参数

### **启用输入归一化** — 启用模块以归一化输入 `on`（默认） | `off`

仅当选择此参数时，模块才会归一化 **α** 和 **β** 正交输入信号。

### **使用输入端口获取计算参数（运行时电机切换）** — 用于启用输入端口以接受计算参数的选项 `off`（默认） | on

选择此参数以启用 **ParameterBus** 输入端口，并禁用以下参数：

- **最大应用频率 (Hz)**
- **输出滤波器截止频率 (Hz)**
- **查找表数据点数量**
- **比例 (P)**
- **积分 (I)**

此参数使您能够将输入端口与 Compute Parameter 模块一起使用，以在运行时最优地更新模块参数。

### **位置输出** — 位置输出的类型 `Angular position`（默认） | `Sine and Cosine Position`

模块应生成的位置输出类型：

- `Angular position` — 选择此选项可使用正弦-余弦查找表计算角位置（**θ**）。
- `Sine and Cosine Position` — 选择此选项可使用基于振荡器的算法计算角位置的正弦和余弦等效值（**sin θ** 和 **cos θ**）。

### **离散步长 (s)** — 模块再次执行前的采样时间 `50e-6`（默认） | 标量

模块连续执行实例之间的固定时间间隔（以 seconds 为单位）。

### PLL 参数

### **频率比** — 输出信号频率与输入信号频率之比 `1`（默认） | 标量

模块输出信号频率与输入信号频率之比。

### **最大应用频率 (Hz)** — 最大适用输入频率 `7500`（默认） | 标量

输入信号可能的最大频率（以 hertz 为单位）。

### **输出滤波器截止频率 (Hz)** — 低通滤波器截止频率 `15`（默认） | 标量

模块用于对估计角频率进行滤波的低通滤波器的截止频率（以 hertz 为单位）。

### **查找表数据点数量** — 查找表数组的大小 `1024`（默认） | 标量

模块提供给内部使用的 SinCos Embedded Optimized 模块的查找表数组大小。此参数接受 125 到 4095 之间的值。

#### 依赖关系

要启用此参数，请将 **位置输出** 设置为 `Angular position`。

### **比例 (P)** — 比例控制器增益 `942.4778`（默认） | 标量

模块用于计算角频率的 PID 控制器的比例增益（*Kp*）。

### **积分 (I)** — 积分控制器增益 `222066.099`（默认） | 标量

模块用于计算角频率的 PID 控制器的积分增益（*Ki*）。

点击 **计算默认参数** 可计算近似的比例增益（*Kp*）和积分增益（*Ki*），并更新这些字段。

### 数据类型

### **位置单位** — 位置输出的单位 `Degrees`（默认） | `Radians` | `Per-unit`

位置输出的单位。

#### 依赖关系

要启用此参数，请将 **位置输出** 设置为 `Angular position`。

### **位置数据类型** — 位置输出的数据类型 `single`（默认） | `double` | `fixed point`

位置输出的数据类型。

### **频率单位** — 角频率输出的单位 `Degrees/sec`（默认） | `Radians/sec` | `Hz`

角频率输出的单位。

### **频率数据类型** — 角频率输出的数据类型 `single`（默认） | `double` | `fixed point`

角频率输出的数据类型。

### **表数据类型** — 正弦-余弦查找表的数据类型 `single`（默认） | `double` | `fixed point`

模块使用的正弦-余弦查找表的数据类型。

#### 依赖关系

要启用此参数，请将 **位置输出** 设置为 `Angular position`。

## 所属库

Motor Control Blockset / Signal Management

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

**限制**

该模块不支持 16-bit fixed-point 输入。

## 版本历史

**R2023b 中引入**

## 描述

根据正交正弦信号计算位置和角频率

PLL with Feed Forward 模块根据两个正交正弦信号计算角位置（θ）或其正弦和余弦等效值（sin θ、cos θ）以及角频率（ω）。

除角频率外，模块使用正弦-余弦查找表计算角位置，或使用基于振荡器的算法计算位置的正弦和余弦等效值。您可以使用 **位置输出** 参数输出角位置或其正弦和余弦等效值。

两个正交正弦输入信号必须具有相同的峰值幅度。如果输入未在 [-1,1] 范围内归一化，请选择 **启用输入归一化** 参数。

下图展示了模块输入与输出之间的关系：

有关模块算法的更多信息，请参阅算法。

**注意**

该模块不支持 16-bit fixed-point 输入。

此外，您可以使用高级选项启用 **ParameterBus** 输入端口，该端口可与 Compute Parameter 模块一起使用，以在运行时最优地更新模块参数。当电机参数可能随时间变化时（例如，在构建可能需要在运行时切换电机的应用时），您可以使用此功能。
