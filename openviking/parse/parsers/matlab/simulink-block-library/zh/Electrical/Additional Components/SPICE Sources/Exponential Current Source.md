---
type: simulink-block
title: 'Exponential Current Source'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Additional Components / SPICE Sources'
documentation_page: 'exponentialcurrentsource'
documentation_source_path: 'ref/exponentialcurrentsource.html'
language: zh-CN
chinese_source: worker-translation
---

# Exponential Current Source

## 端口
```yaml
ports:
- name: +
  summary: 正电压电气端口
  direction: conserving
- name: '-'
  summary: 负电压电气端口
  direction: conserving
```

### 守恒端口

### **+** — 正电压电气端口

与直流电流源正电压相关联的电气守恒端口

### **-** — 负电压电气端口

与直流电流源负电压相关联的电气守恒端口
## 参数
```yaml
parameters:
- name: Initial value, I1
  summary: 输出电流初始值 0 A（默认值）
  group: ''
- name: Pulse value, I2
  summary: 输出电流渐近值 0 A（默认值）
  group: ''
- name: Rise delay time, TDR
  summary: 上升延迟时间 0 s（默认值）
  group: ''
- name: Rise time, TR
  summary: 上升时间 1e-9 s（默认值）| 正标量
  group: ''
- name: Fall delay time, TDF
  summary: 下降延迟时间 0 s（默认值）
  group: ''
- name: Fall time, TF
  summary: 下降时间 1e-9 s（默认值）| 正标量
  group: ''
- name: Include parallel conductance, GMIN
  summary: 是否包含并联电导 Yes（默认值）| No
  group: ''
```

### **Initial value, I1** — 输出电流初始值 `0` `A`（默认值）

时间零点时的输出电流值，单位为 A。

### **Pulse value, I2** — 输出电流渐近值 `0` `A`（默认值）

输出为高电平时输出电流的渐近值，单位为 A。

### **Rise delay time, TDR** — 上升延迟时间 `0` `s`（默认值）

上升时间延迟，单位为 s。

### **Rise time, TR** — 上升时间 `1e-9` `s`（默认值）| 正标量

输出电流从 **Initial Value, I1** 值上升到 **Pulse Value, I2** 值所需的时间。

### **Fall delay time, TDF** — 下降延迟时间 `0` `s`（默认值）

下降时间延迟。默认值为 `0``s`，与 SPICE 默认值不同。

### **Fall time, TF** — 下降时间 `1e-9` `s`（默认值）| 正标量

输出电流从 **Pulse value, I2** 值下降到 **Initial value, I1** 值所需的时间。

### **Include parallel conductance, GMIN** — 是否包含并联电导 `Yes`（默认值）| `No`

指定电流源是否包含并联电导。并联电导 *GMIN* 的值取决于您的模型是否包含 Environment Parameters 模块。

下表显示了并联电导 *GMIN* 的可能值：

**并联电导 GMIN 的值**

| Include parallel conductance, GMIN | | | | |
| --- | --- | --- | --- | --- |
| *`Yes`* | | *`No`* | | |
| **模型包含 Environment Parameters 模块** | **模型不包含 Environment Parameters 模块** | 不包含并联电导 *GMIN*，且其不影响电流源。 | | |
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

指数脉冲电流源

Exponential Current Source 模块表示一个电流源，其输出电流值是时间的指数脉冲函数，并且与源端子两端的电压无关。以下方程描述了通过源的电流随时间的变化：

Iout(0≤Time≤TDR))=I1Iout(TDR<Time≤TDF)=I1+(I2-I1)\*(1-e-(Time-TDR)/TR)Iout(TDF<Time)=I1+(I2-I1)\*(e-(Time-TDF)/TF-e-(Time-TDR)/TR)

其中：

- *I1* 是 **Initial value, I1** 参数值。
- *I2* 是 **Pulse value, I2** 参数值。
- *TDR* 是 **Rise delay time, TDR** 参数值。
- *TR* 是 **Rise time, TR** 参数值。
- *TDF* 是 **Fall delay time, TDF** 参数值。
- *TF* 是 **Fall time, TF** 参数值。

该模块内部使用一个小电导来防止数值仿真问题。该电导连接器件的 **+** 和 **-** 端口，其电导为 *GMIN*：

- 默认情况下，*GMIN* 与 Environment Parameters 模块的 **GMIN** 参数匹配，其默认值为 `1e–12`。
- 要更改 *GMIN*，请将 Environment Parameters 模块添加到您的模型中，并将 **GMIN** 参数设置为所需的值。
