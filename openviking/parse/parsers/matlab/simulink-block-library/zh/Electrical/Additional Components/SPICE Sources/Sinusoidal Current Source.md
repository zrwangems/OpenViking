---
type: simulink-block
title: 'Sinusoidal Current Source'
family: 'sps'
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
```yaml
ports:
- name: +
  summary: 正极端口 electrical
  direction: conserving
- name: '-'
  summary: 负极端口 electrical
  direction: conserving
```

### 守恒端口

### **+** — 正极端口 electrical

与正弦电流源正极端口关联的电气守恒端口。

### **-** — 负极端口 electrical

与正弦电流源负极端口关联的电气守恒端口。
## 参数
```yaml
parameters:
- name: Current offset, IO
  summary: 电流偏移 0 A（默认）
  group: ''
- name: Sinusoidal amplitude, IA
  summary: 正弦幅值 0 A（默认）
  group: ''
- name: Sinusoidal frequency, FREQ
  summary: 正弦频率 1e6 Hz（默认）
  group: ''
- name: Time delay, TD
  summary: 时间延迟 0 s（默认）
  group: ''
- name: Damping factor, DF
  summary: 阻尼因子 0 1/s（默认）| 非负标量
  group: ''
- name: Include parallel conductance, GMIN
  summary: 是否包含并联电导 Yes（默认）| No
  group: ''
```

### **Current offset, IO** — 电流偏移 `0` `A`（默认）

输出电流中与时间无关部分的幅值。

### **Sinusoidal amplitude, IA** — 正弦幅值 `0` `A`（默认）

输出电流中正弦部分的幅值。

### **Sinusoidal frequency, FREQ** — 正弦频率 `1e6` `Hz`（默认）

输出正弦波的频率。该值可以小于 `0`。

### **Time delay, TD** — 时间延迟 `0` `s`（默认）

正弦波首次开始的时间。小于 `0` 的值表示 180 度的相移。

### **Damping factor, DF** — 阻尼因子 `0` `1/s`（默认）| 非负标量

用于产生输出电流的正弦波的指数阻尼因子。如果 *DF* 大于或等于 `0`，则对于大于 *TD* 的时间，方程中的指数部分始终为阻尼。该值必须大于或等于 `0`。

### **Include parallel conductance, GMIN** — 是否包含并联电导 `Yes`（默认）| `No`

指定电流源是否包含并联电导。并联电导 *GMIN* 的值取决于您的模型是否包含 Environment Parameters 模块。

下表显示了并联电导 *GMIN* 的可能值：

**并联电导 GMIN 的值**

| Include parallel conductance, GMIN | | | | |
| --- | --- | --- | --- | --- |
| *`Yes`* | | *`No`* | | |
| **模型包含 Environment Parameters 模块** | **模型不包含 Environment Parameters 模块** | 不包含并联电导 *GMIN*，且它不影响电流源。 | | |
| *GMIN* 等于 Environment Parameters 模块中 **GMIN** 参数的值。 | *GMIN* = `1e-12` `Ohm` |
## 所属库

Simscape / Electrical / Additional Components / SPICE Sources

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2008a 中引入**

## 描述

阻尼正弦电流源

Sinusoidal Current Source 模块表示一个阻尼正弦电流源，其输出电流与源端子两端的电压无关。以下方程描述了通过源的电流随时间的变化：

Iout(Time≤TD)=IOIout(Time>TD)=IO+IA\*e−(Time−TD)\*DF\*sin(2π\*FREQ\*(Time−TD))

其中：

- *I0* 是 **Current offset, IO** 参数值。
- *IA* 是 **Sinusoidal amplitude, IA** 参数值。
- *FREQ* 是 **Sinusoidal frequency, FREQ** 参数值。
- *TD* 是 **Time delay, TD** 参数值。
- *DF* 是 **Damping factor, DF** 参数值。

该模块内部使用一个小电导来防止数值仿真问题。该电导连接器件的 + 和 - 端口，并具有电导 *GMIN*：

- 默认情况下，*GMIN* 与 Environment Parameters 模块的 **GMIN** 参数匹配，其默认值为 `1e–12`。
- 要更改 *GMIN*，请将 Environment Parameters 模块添加到您的模型中，并将 **GMIN** 参数设置为所需的值。
