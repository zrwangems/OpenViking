---
type: simulink-block
title: 'Loop Filter'
family: 'pll'
product_id: 'msblks'
product_name: 'Mixed-Signal Blockset'
documentation_release: R2025b
official_category: 'PLL / Building Blocks'
documentation_page: 'loopfilter'
documentation_source_path: 'ref/loopfilter.html'
language: zh-CN
chinese_source: worker-translation
---

# Loop Filter

## 端口

### 输入

### **in** — 输入电流标量

输入电流，指定为标量。在锁相环 (PLL) 系统中，**in** 端口连接到 Charge Pump 模块的输出，该模块提供电流值。

**数据类型：** `double`
### 输出

### **out** — 输出电压标量

输出电压，指定为标量。在 PLL 系统中，**out** 端口连接到 VCO 模块的输入端口，并向 VCO 提供控制电压。

**数据类型：** `double`

## 参数

### 配置

### **环路滤波器类型** — 环路滤波器的阶数 `3rd Order passive`（默认）| `2nd Order passive` | `4th Order passive`

环路滤波器的阶数。模拟二阶、三阶或四阶无源 RC 环路滤波器。

#### 编程用法

- 使用 `get_param(gcb,'FilterType')` 查看
  **环路滤波器类型**的当前阶数。
- 使用 `set_param(gcb,'FilterType',value)`
  将 **环路滤波器类型**设置为特定阶数。

### **C1 (F)** — 电容 1 `14.5661e-15`（默认）| 正实数标量

电容值 C1，指定为以 farads 为单位的正实数标量。

#### 编程用法

- 使用 `get_param(gcb,'C1')` 查看
  **C1 (F)** 的当前值。
- 使用 `set_param(gcb,'C1',value)` 将
  **C1 (F)** 设置为特定值。

**数据类型：** `double`

### **C2 (F)** — 电容 2 `160.276e-15`（默认）| 正实数标量

电容值 C2，指定为以 farads 为单位的正实数标量。

#### 编程用法

- 使用 `get_param(gcb,'C2')` 查看
  **C2 (F)** 的当前值。
- 使用 `set_param(gcb,'C2',value)` 将
  **C2 (F)** 设置为特定值。

**数据类型：** `double`

### **C3 (F)** — 电容 3 `1.0452e-15`（默认）| 正实数标量

电容值 C3，指定为以 farads 为单位的正实数标量。

#### 依赖关系

要启用此参数，请在 **环路滤波器类型** 中选择 `3rd Order passive` 或 `4th Order passive`。

#### 编程用法

- 使用 `get_param(gcb,'C3')` 查看
  **C3 (F)** 的当前值。
- 使用 `set_param(gcb,'C3',value)` 将
  **C3 (F)** 设置为特定值。

**数据类型：** `double`

### **C4 (F)** — 电容 4 `1e-12`（默认）| 正实数标量

电容值 C4，指定为以 farads 为单位的正实数标量。

#### 依赖关系

要启用此参数，请在 **环路滤波器类型** 中选择 `4th Order passive`。

#### 编程用法

- 使用 `get_param(gcb,'C4')` 查看
  **C4 (F)** 的当前值。
- 使用 `set_param(gcb,'C4',value)` 将
  **C4 (F)** 设置为特定值。

**数据类型：** `double`

### **R2 (ohms)** — 电阻 2 `3.9955e6`（默认）| 正实数标量

电阻值 R2，指定为以 ohms 为单位的正实数标量。

#### 编程用法

- 使用 `get_param(gcb,'R2')` 查看
  **R2 (ohms)** 的当前值。
- 使用 `set_param(gcb,'R2',value)` 将
  **R2 (ohms)** 设置为特定值。

**数据类型：** `double`

### **R3 (ohms)** — 电阻 3 `51.0435e6`（默认）| 正实数标量

电阻值 R3，指定为以 ohms 为单位的正实数标量。

#### 依赖关系

要启用此参数，请在 **环路滤波器类型** 中选择 `3rd Order passive` 或 `4th Order passive`。

#### 编程用法

- 使用 `get_param(gcb,'R3')` 查看
  **R3 (ohms)** 的当前值。
- 使用 `set_param(gcb,'R3',value)` 将
  **R3 (ohms)** 设置为特定值。

**数据类型：** `double`

### **R4 (ohms)** — 电阻 4 `12e3`（默认）| 正实数标量

电阻值 R4，指定为以 ohms 为单位的正实数标量。

#### 依赖关系

要启用此参数，请在 **环路滤波器类型** 中选择 `4th Order passive`。

#### 编程用法

- 使用 `get_param(gcb,'R4')` 查看
  **R4 (ohms)** 的当前值。
- 使用 `set_param(gcb,'R4',value)` 将
  **R4 (ohms)** 设置为特定值。

**数据类型：** `double`

### **启用增加的缓冲区大小** — 启用增加的缓冲区大小 off（默认）| on

选中以在仿真期间启用增加的缓冲区大小。这会增加 Loop Filter 模块内部 Convert Sample Time 子系统的缓冲区大小。默认情况下，此选项处于未选中状态。

### **缓冲区大小** — 仿真期间可用的输入缓冲的样本数 `1000`（默认）| 正整数标量

仿真期间可用的输入缓冲的样本数，指定为正整数标量。这会设置 Loop Filter 模块内部 Convert Sample Time 子系统的缓冲区大小。

选择不同的仿真求解器或采样策略可能会改变生成准确输出样本所需的输入样本数。将 **缓冲区大小** 设置为足够大的值，以使输入缓冲区包含所需的所有输入样本。

#### 依赖关系

仅当在 **配置** 选项卡中选中 **启用增加的缓冲区大小** 选项时，此参数才可用。

#### 编程用法

- 使用 `get_param(gcb,'NBuffer')` 查看
  **缓冲区大小**的当前值。
- 使用 `set_param(gcb,'NBuffer',value)` 将
  **缓冲区大小**设置为特定值。

**数据类型：** `double`

### 损伤

### **启用损伤** — 将电路损伤添加到仿真 off（默认）| on

选中以将电路损伤添加到仿真。默认情况下，此选项处于禁用状态。

### **工作温度 (℃)** — 用于确定热噪声水平的温度 `30`（默认）| 标量

电阻的温度，指定为以 degree Celsius 为单位的标量。**工作温度 (℃)** 确定热（Johnson）噪声的水平。

#### 依赖关系

要启用此参数，请在 **损伤** 选项卡中选择 **启用损伤**。

#### 编程用法

- 使用 `get_param(gcb,'Temperature')` 查看
  **工作温度 (℃)** 的当前值。
- 使用
  `set_param(gcb,'Temperature',value)` 将
  **工作温度 (℃)** 设置为特定值。

**数据类型：** `double`

## 所属库

Mixed-Signal Blockset / PLL / Building Blocks

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2019a 中引入**

## 描述

对二阶、三阶或四阶无源环路滤波器建模

Loop Filter 子系统模块是一种无源滤波器，其阶数可在二阶到四阶之间变化。在锁相环 (PLL) 系统中，该子系统对 Charge Pump 模块的输出进行滤波，并将控制电压提供给 VCO 模块，以生成所需频率信号。

**n 阶无源环路滤波器**
