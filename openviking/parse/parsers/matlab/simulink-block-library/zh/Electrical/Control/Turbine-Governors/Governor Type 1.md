---
type: simulink-block
title: 'Governor Type 1'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Control / Turbine-Governors'
documentation_page: 'governortype1'
documentation_source_path: 'ref/governortype1.html'
language: zh-CN
chinese_source: worker-translation
---

# Governor Type 1

## 端口

### 输入

### **speed\_pu** — 涡轮转速标量

涡轮转速，以标幺值表示，指定为标量。

**数据类型：** `single` | `double`

### **Pref** — 转速参考偏置标量

转速负载参考的偏置，指定为标量。将此端口连接到涡轮负载控制器模块（例如 Controller LCFB1 模块）的 **Pref** 输出端口。

**数据类型：** `single` | `double`
### 输出

### **Pmech(HP)** — 高压机械功率标量

高压机械功率，以标量形式返回。

**数据类型：** `single` | `double`

### **Pmech(LP)** — 低压机械功率标量

低压机械功率，以标量形式返回。

**数据类型：** `single` | `double`

## 参数

### 常规

### **Speed reference (pu)** — 转速参考 `1`（默认）| 标量

标幺转速参考。

### **Initial torque (pu)** — 初始转矩 `0.45`（默认）| 标量

仿真开始时的标幺初始转矩。

### **Sample time (-1 for inherited)** — 模块采样时间 `-1`（默认）| `0` | 正标量

连续模块执行之间的时间。在执行期间，模块产生输出，并在适当的情况下更新其内部状态。有关详细信息，请参阅 What Is Sample Time? 和 Specify Sample Time。

对于继承的离散时间操作，将此参数设置为 `-1`。对于离散时间操作，将此参数设置为正整数。对于连续时间操作，将此参数设置为 `0`。

如果此模块位于支持在连续操作和离散操作之间切换的掩码子系统或变体子系统中，请提升此参数以确保在模块的连续实现和离散实现之间正确切换。有关详细信息，请参阅 Promote Block Parameters on a Mask。

### 调速器

### **Governor gain (1/droop), K (pu)** — 调速器增益 `20`（默认）| 标量

调速器的标幺增益。

### **Lag time constant, T\_1 (s)** — 调速器滞后时间常数 `0.2`（默认）| 标量

等效滞后时间常数。此参数与图中标记为“Lead-Lag”的模块相关联。当附加滞后动态可忽略时，将此参数设置为 `0`。

### **Lead time constant, T\_2 (s)** — 调速器超前时间常数 `0`（默认）| 标量

等效超前时间常数。此参数与图中标记为“Lead-Lag”的模块相关联。当附加超前动态可忽略时，将此参数设置为 `0`。

### **Valve position time constant, T\_3 (s)** — 阀门位置时间常数 `0.1`（默认）| 标量

阀门位置的时间常数，以秒为单位。

### **Maximum valve opening rate, U\_o (pu/s)** — 阀门最大开启速率 `0.1`（默认）| 标量

阀门的标幺最大开启速率。

### **Maximum valve closing rate, U\_c (pu/s)** — 阀门最大关闭速率 `-0.1`（默认）| 标量

阀门的标幺最大关闭速率。

### **Maximum valve opening, on MW capability, P\_max (pu)** — 基于 MW 能力的阀门最大开度 `0.98`（默认）| 标量

基于 MW 能力的阀门标幺最大开度。

### **Minimum valve opening, on MW capability, P\_min (pu)** — 基于 MW 能力的阀门最小开度 `0`（默认）| 标量

基于 MW 能力的阀门标幺最小开度。

### **Time constant for steam inlet, T\_4 (s)** — 进汽时间常数 `0.25`（默认）| 标量

进汽汽包的时间常数，以秒为单位。此参数与图中标记为“Low-Pass Filter”的模块相关联。

### **HP fraction, K\_1** — 高压轴功率占比 `0.22`（默认）| 标量

第一次锅炉通道后的高压轴功率占比。

### **LP fraction, K2** — 低压轴功率占比 `0`（默认）| 标量

第一次锅炉通道后的低压轴功率占比。

### **Time constant for second boiler pass, T\_5 (s)** — 第二次锅炉通道时间常数 `4`（默认）| 标量

第二次锅炉通道的时间常数，以秒为单位。此参数与图中标记为“Low-Pass Filter1”的模块相关联。

### **HP fraction, K\_3** — 高压轴功率占比 `0.22`（默认）| 标量

第二次锅炉通道后的高压轴功率占比。

### **LP fraction, K\_4** — 低压轴功率占比 `0`（默认）| 标量

第二次锅炉通道后的低压轴功率占比。

### **Time constant for third boiler pass, T\_6 (s)** — 第三次锅炉通道时间常数 `4`（默认）| 标量

第三次锅炉通道的时间常数，以秒为单位。此参数与图中标记为“Low-Pass Filter2”的模块相关联。

### **HP fraction, K\_5** — 高压轴功率占比 `0.3`（默认）| 标量

第三次锅炉通道后的高压轴功率占比。

### **LP fraction, K\_6** — 低压轴功率占比 `0`（默认）| 标量

第三次锅炉通道后的低压轴功率占比。

### **Time constant for fourth boiler pass, T\_7 (s)** — 第四次锅炉通道时间常数 `0.4`（默认）| 标量

第四次锅炉通道的时间常数，以秒为单位。此参数与图中标记为“Low-Pass Filter3”的模块相关联。

### **HP fraction, K\_7** — 高压轴功率占比 `0.26`（默认）| 标量

第四次锅炉通道后的高压轴功率占比。

### **LP fraction, K\_8** — 低压轴功率占比 `0`（默认）| 标量

第四次锅炉通道后的低压轴功率占比。

### **Deadband** — 死区宽度 `0.02`（默认）| 标量

有意设置的死区宽度。

## 所属库

Simscape / Electrical / Control / Turbine-Governors

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020a 中引入**

## 描述

IEEE 类型 1 线性化速度调节汽轮机模型

Governor Type 1 模块对 IEEEG1 汽轮机-调速器模型 IEEEG1 进行建模。

此模块允许对交叉复合机组进行建模，并且具有两组涡轮占比：

- **LP Fraction, K\_2**、**LP Fraction, K\_4**、**LP Fraction, K\_6**、**LP Fraction, K\_8** 用于低压（LP）。
- **HP Fraction, K\_1**、**HP Fraction, K\_3**、**HP Fraction, K\_5**、**HP Fraction, K\_7** 用于高压（HP）。

您可以使用 **Sample time (-1 for inherited)** 参数在模块的连续实现和离散实现之间切换。要将调速器配置为连续时间，请将 **Sample time (-1 for inherited)** 属性设置为 `0`。要将调速器配置为离散时间，请将 **Sample time (-1 for inherited)** 属性设置为正的非零值，或设置为 `-1` 以从上游模块继承采样时间。

此图说明了模块的整体结构：
