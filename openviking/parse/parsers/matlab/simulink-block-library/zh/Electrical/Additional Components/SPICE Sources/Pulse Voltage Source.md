---
type: simulink-block
title: 'Pulse Voltage Source'
family: 'additional-components'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Additional Components / SPICE Sources'
documentation_page: 'pulsevoltagesource'
documentation_source_path: 'ref/pulsevoltagesource.html'
language: zh-CN
chinese_source: worker-translation
---

# Pulse Voltage Source

## 端口

### 守恒

### **+** — 正电压电气

与脉冲电压源正电压相关联的电气守恒端口

### **-** — 负电压电气

与脉冲电压源负电压相关联的电气守恒端口

## 参数

### **初始值, V1** — 初始输出电压 `0` `V`（默认）

时间为零时的输出电压值，单位为 V。

### **脉冲值, V2** — 高电平输出电压 `0` `V`（默认）

输出为高电平时的输出电压值，单位为 V。

### **脉冲延迟时间, TD** — 脉冲延迟时间 `0` `s`（默认）

脉冲首次开始的时间，单位为 s。

### **脉冲上升时间, TR** — 脉冲上升时间 `1e-9` `s`（默认） | 非负标量

输出电压从 **初始值, V1** 的值上升到 **脉冲值, V2** 的值所需的时间。该值必须大于或等于 `0`。

### **脉冲下降时间, TF** — 脉冲下降时间 `1e-9` `s`（默认） | 非负标量

输出电压从 **脉冲值, V2** 的值下降到 **初始值, V1** 的值所需的时间。该值必须大于或等于 `0`。

### **脉冲宽度, PW** — 输出脉冲时间宽度 `Inf` `s`（默认） | 正标量

输出脉冲的时间宽度。该值必须大于 `0`。

### **脉冲周期, PER** — 输出脉冲周期 `Inf` `s`（默认） | 正标量

输出脉冲的周期。对于默认值 `Inf``s`，该模块产生一个周期为无限大的单个脉冲。

## 所属库

Simscape / Electrical / Sources Simscape / Electrical / Additional Components / SPICE Sources

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2008a 中引入**

## 描述

周期性方波电压源

Pulse Voltage Source 模块表示一个电压源，其输出电压值是随时间变化的周期性方波脉冲，并且与流过该源的电流无关。以下方程描述了输出电压随时间的变化：

Vout(0)=V1

Vout(TD)=V1

Vout(TD+TR)=V2

Vout(TD+TR+PW)=V2

Vout(TD+TR+PW+TF)=V1

Vout(TD+PER)=V1

其中：

- *V1* 是时间为零时的输出电压。
- *V2* 是输出为高电平时的输出电压。
- *TD* 是脉冲首次开始的时间。
- *TR* 是输出电压从 *V1* 上升到 *V2* 所需的时间。
- *TF* 是输出电压从 *V2* 下降到 *V1* 所需的时间。
- *PW* 是输出脉冲的时间宽度。
- *PER* 是输出脉冲的周期。

该模块通过线性插值确定中间时间点的值。

*PW* 和 *PER* 的指定值对模块输出有以下影响：

- 如果 *PW* 和 *PER* 均为无限大，则该模块在时间 *TD* 产生阶跃响应。
- 如果 *PER* 为无限大且 *PW* 为有限值，则该模块产生一个宽度为 *PW* 且周期为无限大的单个脉冲。
- 如果 *PW* 为无限大且 *PER* 为有限值，则该模块产生阶跃响应，其中每隔 *PER* 秒出现宽度为 *TR*、值为 *V1* 的脉冲。
- 如果 *PW* > *PER*，则该模块产生阶跃响应，其中每隔 *PER* 秒出现宽度为 *TR*、值为 *V1* 的脉冲。
