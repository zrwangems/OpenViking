---
type: simulink-block
title: 'Pulse Current Source'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Additional Components / SPICE Sources'
documentation_page: 'pulsecurrentsource'
documentation_source_path: 'ref/pulsecurrentsource.html'
language: zh-CN
chinese_source: worker-translation
---

# Pulse Current Source

## 端口

### Conserving

### **+** — 正极端子 electrical

与脉冲电流源正极端子关联的电气守恒端口。

### **-** — 负极端子 electrical

与脉冲电流源负极端子关联的电气守恒端口。

## 参数

### **初始值，I1** — 初始输出电流 `0` `A`（默认值）

时间为零时的输出电流值，单位为 A。

### **脉冲值，I2** — 高输出电流 `0` `A`（默认值）

输出为高电平时的输出电流值，单位为 A。

### **脉冲延迟时间，TD** — 脉冲延迟时间 `0` `s`（默认值）

脉冲首次开始的时间，单位为 s。

### **脉冲上升时间，TR** — 脉冲上升时间 `1e-9` `s`（默认值） | 非负标量

输出电流从 **初始值，I1** 值上升到 **脉冲值，I2** 值所需的时间。该值必须大于或等于 `0`。

### **脉冲下降时间，TF** — 脉冲下降时间 `1e-9` `s`（默认值） | 非负标量

输出电流从 **脉冲值，I2** 值下降到 **初始值，I1** 值所需的时间。该值必须大于或等于 `0`。

### **脉冲宽度，PW** — 输出脉冲时间宽度 `Inf` `s`（默认值） | 正标量

输出脉冲的时间宽度。该值必须大于 `0`。

### **脉冲周期，PER** — 输出脉冲周期 `Inf` `s`（默认值） | 正标量

输出脉冲的周期。对于默认值 `Inf``s`，模块产生一个周期为无穷大的单脉冲。

### **包含并联电导，GMIN** — 是否包含并联电导 `Yes`（默认值） | `No`

指定电流源是否包含并联电导。并联电导 *GMIN* 的值取决于您的模型是否包含 Environment Parameters 模块。

此表显示了并联电导 *GMIN* 的可能值：

**并联电导 GMIN 的值**

| 包含并联电导，GMIN | | | | |
| --- | --- | --- | --- | --- |
| *`Yes`* | | *`No`* | | |
| **模型包含 Environment Parameters 模块** | **模型不包含 Environment Parameters 模块** | 不包含并联电导 *GMIN*，并且它不影响电流源。 | | |
| *GMIN* 等于 Environment Parameters 模块中 **GMIN** 参数的值。 | *GMIN* = `1e-12` `Ohm` |

## 所属库

Simscape / Electrical / Sources Simscape / Electrical / Additional Components / SPICE Sources

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2008a 中引入**

## 描述

周期性方波电流源

Pulse Current Source 模块表示一种电流源，其输出电流值是随时间变化的周期性方波脉冲，并且与源端子两端的电压无关。以下方程描述了流经源的电流随时间的变化：

Iout(0)=I1

Iout(TD)=I1

Iout(TD+TR)=I2

Iout(TD+TR+PW)=I2

Iout(TD+TR+PW+TF)=I1

Iout(TD+PER)=I1

其中：

- *I1* 是时间为零时的输出电流。
- *I2* 是输出为高电平时的输出电流。
- *TD* 是脉冲首次开始的时间。
- *TR* 是输出电流从 *I1* 上升到 *I2* 所需的时间。
- *TF* 是输出电流从 *I2* 下降到 *I1* 所需的时间。
- *PW* 是输出脉冲的时间宽度。
- *PER* 是输出脉冲的周期。

模块通过线性插值确定中间时间点处的值。

为 *PW* 和 *PER* 指定的值对模块输出有以下影响：

- 如果 *PW* 和 *PER* 均为无穷大，则模块在时间 *TD* 处产生阶跃响应。
- 如果 *PER* 为无穷大且 *PW* 为有限值，则模块产生一个宽度为 *PW*、周期为无穷大的单脉冲。
- 如果 *PW* 为无穷大且 *PER* 为有限值，则模块产生阶跃响应，其中每 *PER* 秒出现宽度为 *TR* 的脉冲并降至值 *I1*。
- 如果 *PW* > *PER*，则模块产生阶跃响应，其中每 *PER* 秒出现宽度为 *TR* 的脉冲并降至值 *I1*。

模块内部使用一个小电导来防止数值仿真问题。该电导连接器件的 + 和 - 端口，并具有电导 *GMIN*：

- 默认情况下，*GMIN* 与 Environment Parameters 模块的 **GMIN** 参数匹配，该参数的默认值为 `1e–12``1/Ohm`。
- 要更改 *GMIN*，请将 Environment Parameters 模块添加到您的模型，并将 **GMIN** 参数设置为所需值。
