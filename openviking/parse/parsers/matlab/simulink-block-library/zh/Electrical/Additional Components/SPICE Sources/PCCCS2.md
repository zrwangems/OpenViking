---
type: simulink-block
title: 'PCCCS2'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Additional Components / SPICE Sources'
documentation_page: 'pcccs2'
documentation_source_path: 'ref/pcccs2.html'
language: zh-CN
chinese_source: worker-translation
---

# PCCCS2

## 端口

### 守恒

### **1+** — 第一个控制输入的正电压

与 PCCCS2 的第一个控制输入正电压关联的电气守恒端口。

### **1-** — 第一个控制输入的负电压

与 PCCCS2 的第一个控制输入负电压关联的电气守恒端口。

### **2+** — 第二个控制输入的正电压

与 PCCCS2 的第二个控制输入正电压关联的电气守恒端口。

### **2-** — 第二个控制输入的负电压

与 PCCCS2 的第二个控制输入负电压关联的电气守恒端口。

### **+** — 正输出电压

与 PCCCS2 正输出电压关联的电气守恒端口。

### **-** — 负输出电压

与 PCCCS2 负输出电压关联的电气守恒端口。

## 参数

### **多项式系数** — 多项式系数 `[ 0 1 1 ]`（默认）

将输入电流与输出电流关联起来的多项式系数，如上一节所述。

### **包括并联电导，GMIN** — 是否包括并联电导 `Yes`（默认） | `No`

指定电流源是否包括并联电导。并联电导 *GMIN* 的值取决于模型是否包含 Environment Parameters 模块。

**并联电导 GMIN 的值**

| 包括并联电导，GMIN | | | | |
| --- | --- | --- | --- | --- |
| *`Yes`* | | *`No`* | | |
| **模型包含 Environment Parameters 模块** | **模型不包含 Environment Parameters 模块** | 不包含并联电导 *GMIN*，并且它不影响电流源。 | | |
| *GMIN* 等于 Environment Parameters 模块中 **GMIN** 参数的值。 | *GMIN* = `1e-12` `Ohm` |

## 所属库

Simscape / Electrical / Additional Components / SPICE Sources

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成
使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2009a 中引入**

## 描述

具有两个控制输入的多项式电流控制电流源

PCCCS2（Two-Input Polynomial Current-Controlled Current Source）模块表示一个电流源，其输出电流值是流过各对控制输入端口的电流的多项式函数。以下方程描述了通过该电流源的电流随时间变化的关系：

Iout=p1+p2\*Iin1+p3\*Iin2+p4\*Iin12+p5Iin1\*Iin2+p6\*Iin22+…

其中：

- *Iin1* 是通过第一对输入端口的电流。
- *Iin2* 是通过第二对输入端口的电流。
- *p* 是 **多项式系数** 参数值。

该模块内部使用一个小电导来防止数值仿真问题。该电导连接设备的输出端口，并具有电导 *GMIN*：

- 默认情况下，*GMIN* 与 Environment Parameters 模块的 **GMIN** 参数匹配，其默认值为 `1e–12`。
- 要更改 *GMIN*，请向模型中添加 Environment Parameters 模块，并将 **GMIN** 参数设置为所需值。
