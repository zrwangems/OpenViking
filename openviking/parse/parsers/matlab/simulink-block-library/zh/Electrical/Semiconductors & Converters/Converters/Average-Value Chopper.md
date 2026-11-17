---
type: simulink-block
title: 'Average-Value Chopper'
family: 'semiconductors-converters'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Semiconductors & Converters / Converters'
documentation_page: 'averagevaluechopper'
documentation_source_path: 'ref/averagevaluechopper.html'
language: zh-CN
chinese_source: worker-translation
---

# Average-Value Chopper

## 端口

### 守恒

### **DutyCycle** — 占空比 电气 | 标量

与占空比关联的电气守恒端口。

**数据类型：** `double`

### **1+** — 直流电压 1 的正极 电气 | 标量

与第一个直流电压的正极端子关联的电气守恒端口。

**数据类型：** `double`

### **1-** — 直流电压 1 的负极 电气 | 标量

与第一个直流电压的负极端子关联的电气守恒端口。

**数据类型：** `double`

### **2+** — 直流电压 2 的正极 电气 | 标量

与第二个直流电压的正极端子关联的电气守恒端口。

**数据类型：** `double`

### **2-** — 直流电压 2 的负极 电气 | 标量

与第二个直流电压的负极端子关联的电气守恒端口。

**数据类型：** `double`

## 参数

### **斩波器类型** — 斩波器类别 `Class A - first quadrant` (默认) | `Class B - second quadrant` | `Class C - first and second quadrant` | `Class D - first and fourth quadrant` | `Class E - four quadrant`

斩波器类别。

### **转换器效率** — 转换器效率参数化 `Constant` (默认) | `Tabulated`

指定转换器效率的参数化。如果选择 `Tabulated`，导通损耗将取决于所提供的输出电流。

### **效率 (%)** — 转换器效率 100 (默认) | 标量

转换器的效率，以百分比表示。

#### 依赖关系

要启用此参数，请将 **转换器效率** 设置为 `Constant`。

### **输出电流向量** — 输出电流向量 [0, 2, 5] `A` (默认) | 至少包含两个元素的行向量

输出电流向量。

#### 依赖关系

要启用此参数，请将 **转换器效率** 设置为 `Tabulated`。

### **效率向量 (%)** — 效率向量 [90, 95, 98] (默认) | 至少包含两个元素的行向量

针对 **输出电流向量** 中指定的每个输出电流，以百分比表示效率向量。此参数的大小必须与 **输出电流向量** 相同。

#### 依赖关系

要启用此参数，请将 **转换器效率** 设置为 `Tabulated`。

## 所属库

Simscape / Electrical / Semiconductors & Converters / Converters

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2018b 中引入**

## 描述

平均值斩波器

Average-Value Chopper 模块表示一个受控的平均值斩波器。使用占空比输入在两侧之间转换电能。该图显示了该模块的等效电路。

### 方程

输入电流和输出电压取决于您指定的斩波器类别。

**电压和电流方程**

| 斩波器类别 | 象限 | 输出电压, v2 | | | 输入电流, i1 | | |
| --- | --- | --- | --- | --- | --- | --- | --- |
| i2<0 | i2=0 | i2>0 | i2<0 | i2=0 | i2>0 |
| **A** | 第1象限 | v2=v1 | v2=DutyCycle⋅v1 | | i1=i2 | i1=DutyCycle⋅i2 | |
| **B** | 第2象限 | v2=(1−DutyCycle)⋅v1 | | v2=0 | i1=(1−DutyCycle)⋅i2 | | i1=0 |
| **C** | 第1和第2象限 | v2=DutyCycle⋅v1 | | | i1=DutyCycle⋅i2 | | |
| **D** | 第1和第4象限 | v2=v1 | v2=(2⋅DutyCycle−1)⋅v1 | | i1=i2 | i1=(2⋅DutyCycle−1)⋅i2 | |
| **E** | 四象限 | v2=(2⋅DutyCycle−1)⋅v1 | | | i1=(2⋅DutyCycle−1)⋅i2 | | |

### 限制与假设

- 输入电压 *v1* 为正。
- 忽略功率损耗。
- Average-Value Chopper 模块表示一个无动态的受控平均值斩波器的理想实现，适用于低保真度仿真。对于更高保真度的模型，请使用 One-Quadrant Chopper、Two-Quadrant Chopper 或 Four-Quadrant Chopper 模块。
