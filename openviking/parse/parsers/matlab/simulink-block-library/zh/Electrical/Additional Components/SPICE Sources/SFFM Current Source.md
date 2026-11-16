---
type: simulink-block
title: 'SFFM Current Source'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Additional Components / SPICE Sources'
documentation_page: 'sffmcurrentsource'
documentation_source_path: 'ref/sffmcurrentsource.html'
language: zh-CN
chinese_source: worker-translation
---

# SFFM Current Source

## 端口

### 守恒

### **+** — 正极端子电气

与 SFFM Current Source 正极端子关联的电气守恒端口。

### **-** — 负极端子电气

与 SFFM Current Source 负极端子关联的电气守恒端口。

## 参数

### **电流偏移, IO** — 电流偏移 `0` `A`（默认）

输出电流中与时间无关的部分的幅值。

### **电流幅值, IA** — 电流幅值 `0` `A`（默认）

输出电流正弦部分的幅值。

### **载波频率, FC** — 载波频率 `0` `Hz`（默认）| 非负标量

载波的频率。该值必须大于或等于 `0`。

### **调制指数, MI** — 调制指数 `0`（默认）| 非负标量

调制信号围绕其未调制电平变化的量。该值必须大于或等于 `0`。

### **信号频率, FS** — 信号频率 `0` `Hz`（默认）| 非负标量

调制信号的频率。该值必须大于或等于 `0`。

### **包含并联电导, GMIN** — 是否包含并联电导 `Yes`（默认）| `No`

指定电流源是否包含并联电导。并联电导 *GMIN* 的值取决于您的模型是否包含 Environment Parameters 模块。

下表显示了并联电导 *GMIN* 的可能值：

**并联电导 GMIN 的值**

| 包含并联电导, GMIN | | | | |
| --- | --- | --- | --- | --- |
| *`Yes`* | | *`No`* | | |
| **模型包含 Environment Parameters 模块** | **模型不包含 Environment Parameters 模块** | 未包含并联电导 *GMIN*，且它不影响电流源。 | | |
| *GMIN* 等于 Environment Parameters 模块中 **GMIN** 参数的值。 | *GMIN* = `1e-12` `Ohm` |

## 所属库

Simscape / Electrical / Additional Components / SPICE Sources

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2008a 中引入**

## 描述

单频调频电流源

SFFM Current Source 模块表示一个调频交流电流源，其输出电流值与其端子两端的电压无关。以下方程将流经该源的电流描述为时间的函数：

Iout = IO+IA\*sin((2π\*FC\*Time)+MI\*sin(2π\*FS\*Time))

其中：

- *I0* 是 **电流偏移, IO** 参数的值。
- *IA* 是 **电流幅值, IA** 参数的值。
- *FC* 是 **载波频率, FC** 参数的值。
- *MI* 是 **调制指数, MI** 参数的值。
- *FS* 是 **信号频率, FS** 参数的值。

该模块在内部使用一个小电导以防止数值仿真问题。该电导连接器件的 + 和 - 端口，并具有电导 *GMIN*：

- 默认情况下，*GMIN* 与 Environment Parameters 模块的 **GMIN** 参数匹配，其默认值为 1e–12。
- 要更改 *GMIN*，请将 Environment Parameters 模块添加到您的模型，并将 **GMIN** 参数设置为所需值。
