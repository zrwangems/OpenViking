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
```yaml
ports:
- name: +
  summary: 正极端口电气
  direction: conserving
- name: '-'
  summary: 负极端口电气
  direction: conserving
```

### 守恒端口

### **+** — 正极端口电气

与脉冲电流源正极端口关联的电气守恒端口。

### **-** — 负极端口电气

与脉冲电流源负极端口关联的电气守恒端口。
## 参数
```yaml
parameters:
- name: Initial value, I1
  summary: 初始输出电流 0 A（默认）
  group: ''
- name: Pulse value, I2
  summary: 高电平输出电流 0 A（默认）
  group: ''
- name: Pulse delay time, TD
  summary: 脉冲延迟时间 0 s（默认）
  group: ''
- name: Pulse rise time, TR
  summary: 脉冲上升时间 1e-9 s（默认）| 非负标量
  group: ''
- name: Pulse fall time, TF
  summary: 脉冲下降时间 1e-9 s（默认）| 非负标量
  group: ''
- name: Pulse width, PW
  summary: 输出脉冲时间宽度 Inf s（默认）| 正标量
  group: ''
- name: Pulse period, PER
  summary: 输出脉冲周期 Inf s（默认）| 正标量
  group: ''
- name: Include parallel conductance, GMIN
  summary: 是否包含并联电导 Yes（默认）| No
  group: ''
```

### **Initial value, I1** — 初始输出电流 `0` `A`（默认）

时间零点的输出电流值，单位为 A。

### **Pulse value, I2** — 高电平输出电流 `0` `A`（默认）

输出为高电平时的输出电流值，单位为 A。

### **Pulse delay time, TD** — 脉冲延迟时间 `0` `s`（默认）

脉冲首次开始的时间，单位为 s。

### **Pulse rise time, TR** — 脉冲上升时间 `1e-9` `s`（默认）| 非负标量

输出电流从 **Initial value, I1** 值上升到 **Pulse value, I2** 值所需的时间。该值必须大于或等于 `0`。

### **Pulse fall time, TF** — 脉冲下降时间 `1e-9` `s`（默认）| 非负标量

输出电流从 **Pulse value, I2** 值下降到 **Initial value, I1** 值所需的时间。该值必须大于或等于 `0`。

### **Pulse width, PW** — 输出脉冲时间宽度 `Inf` `s`（默认）| 正标量

输出脉冲的时间宽度。该值必须大于 `0`。

### **Pulse period, PER** — 输出脉冲周期 `Inf` `s`（默认）| 正标量

输出脉冲的周期。对于默认值 `Inf``s`，该模块产生一个周期为无穷大的单脉冲。

### **Include parallel conductance, GMIN** — 是否包含并联电导 `Yes`（默认）| `No`

指定电流源是否包含并联电导。并联电导的值 *GMIN* 取决于您的模型是否包含 Environment Parameters 模块。

下表显示了并联电导 *GMIN* 的可能值：

**并联电导 GMIN 的值**

| Include parallel conductance, GMIN | | | | |
| --- | --- | --- | --- | --- |
| *`Yes`* | | *`No`* | | |
| **模型包含 Environment Parameters 模块** | **模型不包含 Environment Parameters 模块** | 不包含并联电导 *GMIN*，且它不影响电流源。 | | |
| *GMIN* 等于 Environment Parameters 模块中 **GMIN** 参数的值。 | *GMIN* = `1e-12` `Ohm` |
## 所属库

Simscape / Electrical / Sources Simscape / Electrical / Additional Components / SPICE Sources

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2008a 中引入**

## 描述

周期性方波电流源

Pulse Current Source 模块表示一个电流源，其输出电流值是时间的周期性方波脉冲函数，并且与源两端电压无关。以下方程描述了通过源的电流随时间的函数关系：

Iout(0)=I1

Iout(TD)=I1

Iout(TD+TR)=I2

Iout(TD+TR+PW)=I2

Iout(TD+TR+PW+TF)=I1

Iout(TD+PER)=I1

其中：

- *I1* 是时间零点的输出电流。
- *I2* 是输出为高电平时的输出电流。
- *TD* 是脉冲首次开始的时间。
- *TR* 是输出电流从 *I1* 上升到 *I2* 所需的时间。
- *TF* 是输出电流从 *I2* 下降到 *I1* 所需的时间。
- *PW* 是输出脉冲的时间宽度。
- *PER* 是输出脉冲的周期。

该模块通过线性插值确定中间时间点的值。

*PW* 和 *PER* 的指定值对模块输出有以下影响：

- 如果 *PW* 和 *PER* 均为无穷大，该模块在时间 *TD* 产生阶跃响应。
- 如果 *PER* 为无穷大且 *PW* 为有限值，该模块产生宽度为 *PW*、周期为无穷大的单脉冲。
- 如果 *PW* 为无穷大且 *PER* 为有限值，该模块产生阶跃响应，每 *PER* 秒出现宽度为 *TR*、值为 *I1* 的脉冲。
- 如果 *PW* > *PER*，该模块产生阶跃响应，每 *PER* 秒出现宽度为 *TR*、值为 *I1* 的脉冲。

该模块内部使用一个小电导以防止数值仿真问题。该电导连接器件的 + 和 - 端口，其电导值为 *GMIN*：

- 默认情况下，*GMIN* 与 Environment Parameters 模块的 **GMIN** 参数匹配，其默认值为 `1e–12``1/Ohm`。
- 要更改 *GMIN*，请将 Environment Parameters 模块添加到您的模型中，并将 **GMIN** 参数设置为所需值。
