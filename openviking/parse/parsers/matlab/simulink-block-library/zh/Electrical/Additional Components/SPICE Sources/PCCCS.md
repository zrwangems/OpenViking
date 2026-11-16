---
type: simulink-block
title: 'PCCCS'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Additional Components / SPICE Sources'
documentation_page: 'pcccs'
documentation_source_path: 'ref/pcccs.html'
language: zh-CN
chinese_source: worker-translation
---

# PCCCS

## 端口

### 守恒

### **p1** — 控制输入电气的正电压

与 PCCCS 控制输入的正电压关联的电气守恒端口。

### **n1** — 控制输入电气的负电压

与 PCCCS 控制输入的负电压关联的电气守恒端口。

### **p2** — 正输出电压电气

与 PCCCS 正输出电压关联的电气守恒端口。

### **n2** — 负输出电压电气

与 PCCCS 负输出电压关联的电气守恒端口。

## 参数

### **Polynomial coefficients** — 多项式系数 `[0, 1]`（默认）

用于将输入电流与输出电流关联的多项式系数，如上一节所述。

### **Include parallel conductance, GMIN** — 是否包含并联电导 `Yes`（默认） | `No`

指定电流源是否包含并联电导。并联电导 *GMIN* 的值取决于您的模型是否包含 Environment Parameters 模块。

下表显示了并联电导 *GMIN* 的可能值：

**并联电导 GMIN 的值**

| Include parallel conductance, GMIN | | | | |
| --- | --- | --- | --- | --- |
| *`Yes`* | | *`No`* | | |
| **模型包含 Environment Parameters 模块** | **模型不包含 Environment Parameters 模块** | 不包含并联电导 *GMIN*，并且它不影响电流源。 | | |
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

多项式电流控制电流源

PCCCS（Polynomial Current-Controlled Current Source）模块表示一个电流源，其输出电流值是流过输入端口的电流的多项式函数。以下方程描述了流过该源的电流随时间变化的函数关系：

- 如果您为 **Polynomial coefficients** 参数指定一个 *n* 元素的多项式系数向量：

  Iout=p(0)+p(1)\*Iin+...+p(n−1)\*Iinn−1+p(n)\*Iinn
- 如果您为 **Polynomial coefficients** 参数指定一个标量系数：

  Iout=p\*Iin

其中：

- *Iin* 是流过输入端口的电流。
- *p* 是 **Polynomial coefficients** 参数值。

该模块内部使用一个小电导来防止数值仿真问题。该电导连接设备的输出端口，并且其电导为 *GMIN*：

- 默认情况下，*GMIN* 与 Environment Parameters 模块的 **GMIN** 参数匹配，其默认值为 `1e–12`。
- 要更改 *GMIN*，请将 Environment Parameters 模块添加到您的模型，并将 **GMIN** 参数设置为所需值。
