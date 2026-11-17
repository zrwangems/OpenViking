---
type: simulink-block
title: 'PVCCS'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Additional Components / SPICE Sources'
documentation_page: 'pvccs'
documentation_source_path: 'ref/pvccs.html'
language: zh-CN
chinese_source: worker-translation
---

# PVCCS

## 端口

### 守恒端口

### **p1** — 控制输入电气的正电压

与控制输入的正电压 PVCCS 相关联的电气守恒端口。

### **n1** — 控制输入电气的负电压

与控制输入的负电压 PVCCS 相关联的电气守恒端口。

### **p2** — 正输出电压电气

与 PVCCS 正输出电压相关联的电气守恒端口。

### **n2** — 负输出电压电气

与 PVCCS 负输出电压相关联的电气守恒端口。

## 参数

### **Polynomial coefficients** — 多项式系数 `[0, 1]`（默认）

将输入电压与输出电流关联起来的多项式系数，如前一节所述。

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

多项式电压控制电流源

PVCCS（多项式电压控制电流源）模块表示一个电流源，其输出电流值是输入端口两端电压的多项式函数。以下方程描述了通过该源的电流随时间变化的函数关系：

- 如果您为 **Polynomial coefficients** 参数指定一个 *n* 元素的多项式系数向量：

  Iout=p(0)+p(1)\*Vin+...+p(n−1)\*Vinn−1+p(n)\*Vinn
- 如果您为 **Polynomial coefficients** 参数指定一个标量系数：

  Iout=p\*Vin

其中：

- *Vin* 是输入端口两端的电压。
- *p* 是 **Polynomial coefficients** 参数值。

该模块内部使用一个小电导来防止数值仿真问题。该电导连接设备的输出端口，并具有电导 *GMIN*：

- 默认情况下，*GMIN* 与 Environment Parameters 模块的 **GMIN** 参数匹配，其默认值为 `1e–12`。
- 要更改 *GMIN*，请向您的模型添加 Environment Parameters 并将 **GMIN** 参数设置为所需值。
