---
type: simulink-block
title: 'PVCCS2'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Additional Components / SPICE Sources'
documentation_page: 'pvccs2'
documentation_source_path: 'ref/pvccs2.html'
language: zh-CN
chinese_source: worker-translation
---

# PVCCS2

## 端口

### 守恒端口

### **1+** — 第一个控制输入的正电压

与 PVCCS2 第一个控制输入的正电压关联的电气守恒端口。

### **1-** — 第一个控制输入的负电压

与 PVCCS2 第一个控制输入的负电压关联的电气守恒端口。

### **2+** — 第二个控制输入的正电压

与 PVCCS2 第二个控制输入的正电压关联的电气守恒端口。

### **2-** — 第二个控制输入的负电压

与 PVCCS2 第二个控制输入的负电压关联的电气守恒端口。

### **+** — 正输出电压

与 PVCCS2 正输出电压关联的电气守恒端口。

### **-** — 负输出电压

与 PVCCS2 负输出电压关联的电气守恒端口。

## 参数

### **Polynomial coefficients** — 多项式系数 `[ 0 1 1 ]`（默认值）

将输入电压与输出电流关联的多项式系数，如前一节所述。

### **Include parallel conductance, GMIN** — 是否包含并联电导 `Yes`（默认值） | `No`

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

**在 R2009a 中引入**

## 描述

具有两个控制输入的多项式压控电流源

PVCCS2（双输入多项式压控电流源）模块表示一个电流源，其输出电流值是各对控制输入端口电压的多项式函数。以下方程描述了通过该电流源的电流随时间的变化：

Iout=p1+p2\*Vin1+p3\*Vin2+p4\*Vin12+p5Vin1\*Vin2+p6\*Vin22+…

其中：

- *Vin1* 是第一对输入端口两端的电压。
- *Vin2* 是第二对输入端口两端的电压。
- *p* 是 **Polynomial coefficients** 参数值。

该模块内部使用一个小电导来防止数值仿真问题。该电导连接器件的输出端口，其电导值为 *GMIN*：

- 默认情况下，*GMIN* 与 Environment Parameters 模块的 **GMIN** 参数匹配，其默认值为 `1e–12`。
- 要更改 *GMIN*，请将 Environment Parameters 模块添加到您的模型中，并将 **GMIN** 参数设置为所需的值。
