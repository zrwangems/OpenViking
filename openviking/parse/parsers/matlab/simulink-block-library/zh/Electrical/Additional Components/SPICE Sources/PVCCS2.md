---
type: simulink-block
title: 'PVCCS2'
family: 'additional-components'
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

### 守恒

### **1+** — 第一个控制输入的正电压（电气）

与 PVCCS2 第一个控制输入的正电压关联的电气守恒端口。

### **1-** — 第一个控制输入的负电压（电气）

与 PVCCS2 第一个控制输入的负电压关联的电气守恒端口。

### **2+** — 第二个控制输入的正电压（电气）

与 PVCCS2 第二个控制输入的正电压关联的电气守恒端口。

### **2-** — 第二个控制输入的负电压（电气）

与 PVCCS2 第二个控制输入的负电压关联的电气守恒端口。

### **+** — 正输出电压（电气）

与 PVCCS2 正输出电压关联的电气守恒端口。

### **-** — 负输出电压（电气）

与 PVCCS2 负输出电压关联的电气守恒端口。

## 参数

### **多项式系数** — 多项式系数 `[ 0 1 1 ]` (默认)

将输入电压与输出电流关联起来的多项式系数，如上一节所述。

### **包含并联电导，GMIN** — 是否包含并联电导 `Yes` (默认) | `No`

指定电流源是否包含并联电导。并联电导 *GMIN* 的值取决于模型是否包含 Environment Parameters 模块。

下表列出了并联电导 *GMIN* 的可能值：

**并联电导 GMIN 的值**

| 包含并联电导，GMIN | | | | |
| --- | --- | --- | --- | --- |
| *`Yes`* | | *`No`* | | |
| **模型包含 Environment Parameters 模块** | **模型不包含 Environment Parameters 模块** | 未包含并联电导 *GMIN*，并且它不影响电流源。 | | |
| *GMIN* 等于 Environment Parameters 模块中 **GMIN** 参数的值。 | *GMIN* = `1e-12` `Ohm` |

## 所属库

Simscape / Electrical / Additional Components / SPICE Sources

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2009a 中引入**

## 描述

具有两个控制输入的多项式压控电流源

PVCCS2（Two-Input Polynomial Voltage-Controlled Current Source）模块表示一个电流源，其输出电流值是各对控制输入端口两端电压的多项式函数。以下方程描述流过该源的电流作为时间的函数：

Iout=p1+p2\*Vin1+p3\*Vin2+p4\*Vin12+p5Vin1\*Vin2+p6\*Vin22+…

其中：

- *Vin1* 是第一个输入端口对两端的电压。
- *Vin2* 是第二个输入端口对两端的电压。
- *p* 是 **多项式系数** 参数值。

该模块内部使用一个小电导来防止数值仿真问题。该电导连接设备的输出端口，并具有电导 *GMIN*：

- 默认情况下，*GMIN* 与 Environment Parameters 模块的 **GMIN** 参数匹配，其默认值为 `1e–12`。
- 要更改 *GMIN*，请将 Environment Parameters 模块添加到模型中，并将 **GMIN** 参数设置为所需值。
