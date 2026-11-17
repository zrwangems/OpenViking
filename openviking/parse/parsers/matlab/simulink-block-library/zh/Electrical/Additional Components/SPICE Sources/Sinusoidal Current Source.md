---
type: simulink-block
title: 'Sinusoidal Current Source'
family: 'additional-components'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Additional Components / SPICE Sources'
documentation_page: 'sinusoidalcurrentsource'
documentation_source_path: 'ref/sinusoidalcurrentsource.html'
language: zh-CN
chinese_source: worker-translation
---

# Sinusoidal Current Source

## 端口

### 守恒

### **+** — 正极端子（电气）

与正弦电流源正极端子关联的电气守恒端口。

### **-** — 负极端子（电气）

与正弦电流源负极端子关联的电气守恒端口。

## 参数

### **电流偏移, IO** — 电流偏移 `0` `A`（默认值）

输出电流中与时间无关部分的大小。

### **正弦振幅, IA** — 正弦振幅 `0` `A`（默认值）

输出电流中正弦部分的大小。

### **正弦频率, FREQ** — 正弦频率 `1e6` `Hz`（默认值）

输出正弦波的频率。该值可以小于 `0`。

### **时间延迟, TD** — 时间延迟 `0` `s`（默认值）

正弦波首次开始的时间。小于 `0` 的值表示 180 度相移。

### **阻尼因子, DF** — 阻尼因子 `0` `1/s`（默认值） | nonnegative scalar

用于生成输出电流的正弦波的指数阻尼因子。如果 *DF* 大于或等于 `0`，则对于大于 *TD* 的时间，方程中的指数部分始终为阻尼。该值必须大于或等于 `0`。

### **包含并联电导, GMIN** — 是否包含并联电导 `Yes`（默认值） | `No`

指定电流源是否包含并联电导。并联电导 *GMIN* 的值取决于您的模型是否包含 Environment Parameters 模块。

此表显示了并联电导 *GMIN* 的可能值：

**并联电导, GMIN 的值**

| 包含并联电导, GMIN | | | | |
| --- | --- | --- | --- | --- |
| *`Yes`* | | *`No`* | | |
| **模型包含 Environment Parameters 模块** | **模型不包含 Environment Parameters 模块** | 并联电导 *GMIN* 未包含，且不影响电流源。 | | |
| *GMIN* 等于 Environment Parameters 模块中 **GMIN** 参数的值。 | *GMIN* = `1e-12` `Ohm` |

## 所属库

Simscape / Electrical / Additional Components / SPICE Sources

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码

## 版本历史

**在 R2008a 中引入**

## 描述

阻尼正弦电流源

Sinusoidal Current Source 模块表示一个阻尼正弦电流源，其输出电流与源端子两端的电压无关。以下方程描述了流过源的电流随时间的函数关系：

Iout(Time≤TD)=IOIout(Time>TD)=IO+IA\*e−(Time−TD)\*DF\*sin(2π\*FREQ\*(Time−TD))

其中：

- *I0* 是 **电流偏移, IO** 参数值。
- *IA* 是 **正弦振幅, IA** 参数值。
- *FREQ* 是 **正弦频率, FREQ** 参数值。
- *TD* 是 **时间延迟, TD** 参数值。
- *DF* 是 **阻尼因子, DF** 参数值。

该模块内部使用一个小电导来防止数值仿真问题。该电导连接器件的 + 和 - 端口，并具有电导 *GMIN*：

- 默认情况下，*GMIN* 与 Environment Parameters 模块的 **GMIN** 参数匹配，其默认值为 `1e–12`。
- 要更改 *GMIN*，请向模型添加 Environment Parameters 模块，并将 **GMIN** 参数设置为所需值。
