---
type: simulink-block
title: 'Exponential Current Source'
family: 'additional-components'
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

### 守恒

### **+** — 正电压电气

与直流电流源正电压关联的电气守恒端口

### **-** — 负电压电气

与直流电流源负电压关联的电气守恒端口

## 参数

### **初始值, I1** — 输出电流初始值 `0` `A`（默认）

时间零点的输出电流值，单位为 A。

### **脉冲值, I2** — 输出电流渐近值 `0` `A`（默认）

输出为高时输出电流的渐近值，单位为 A。

### **上升延迟时间, TDR** — 上升延迟时间 `0` `s`（默认）

上升时间延迟，单位为 s。

### **上升时间, TR** — 上升时间 `1e-9` `s`（默认） | 正标量

输出电流从 **初始值, I1** 值上升到 **脉冲值, I2** 值所需的时间。

### **下降延迟时间, TDF** — 下降延迟时间 `0` `s`（默认）

下降时间延迟。默认值为 `0``s`，与 SPICE 默认值不同。

### **下降时间, TF** — 下降时间 `1e-9` `s`（默认） | 正标量

输出电流从 **脉冲值, I2** 值下降到 **初始值, I1** 值所需的时间。

### **包括并联电导, GMIN** — 是否包括并联电导 `Yes`（默认） | `No`

指定电流源是否包括并联电导。并联电导 *GMIN* 的值取决于模型是否包含 Environment Parameters 模块。

下表显示了并联电导 *GMIN* 的可能值：

**并联电导 GMIN 的值**

| 包括并联电导, GMIN | | | | |
| --- | --- | --- | --- | --- |
| *`Yes`* | | *`No`* | | |
| **模型包含 Environment Parameters 模块** | **模型不包含 Environment Parameters 模块** | 并联电导 *GMIN* 未包括，且不影响电流源。 | | |
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

- *I1* 是 **初始值, I1**
  参数值。
- *I2* 是 **脉冲值, I2**
  参数值。
- *TDR* 是 **上升延迟时间, TDR**
  参数值。
- *TR* 是 **上升时间, TR** 参数
  值。
- *TDF* 是 **下降延迟时间, TDF**
  参数值。
- *TF* 是 **下降时间, TF**
  参数值。

该模块内部使用一个小电导来防止数值仿真问题。该电导连接设备的 **+** 和 **-** 端口，并具有电导 *GMIN*：

- 默认情况下，*GMIN* 与 Environment Parameters
  模块的 **GMIN**
  参数匹配，其默认值为 `1e–12`。
- 要更改 *GMIN*，请将 Environment
  Parameters 模块添加到模型中，并将
  **GMIN** 参数设置为所需值。
