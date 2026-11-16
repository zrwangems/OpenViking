---
type: simulink-block
title: 'DC Current Source'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Electrical Block Libraries / Additional Components / SPICE Sources'
documentation_page: 'dccurrentsource'
documentation_source_path: 'ref/dccurrentsource.html'
language: zh-CN
chinese_source: worker-translation
---

# DC Current Source

## 端口

### 守恒

### **+** — 正电压电气

与 DC Current Source 正电压关联的电气守恒端口

### **-** — 负电压电气

与 DC Current Source 负电压关联的电气守恒端口

## 参数

### **恒定值，DC** — DC 输出电流 `0` `A`（默认值）

DC 输出电流的值，单位为 A。

### **包含并联电导，GMIN** — 是否包含并联电导 `Yes`（默认值）| `No`

指定电流源是否包含并联电导。并联电导 *GMIN* 的值取决于您的模型是否包含 Environment Parameters 模块。

此表显示了并联电导 *GMIN* 的可能值：

**并联电导 GMIN 的值**

| 包含并联电导，GMIN | | | | |
| --- | --- | --- | --- | --- |
| *`Yes`* | | *`No`* | | |
| **模型包含 Environment Parameters 模块** | **模型不包含 Environment Parameters 模块** | 未包含并联电导 *GMIN*，并且它不影响电流源。 | | |
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

恒定电流源

DC Current Source 模块表示一个恒定电流源，其输出电流值与其端子两端的电压无关。

该模块内部使用小电导来防止数值仿真问题。该电导连接器件的 + 和 - 端口，并具有电导 *GMIN*：

- 默认情况下，*GMIN* 与 Environment Parameters 模块的 **GMIN** 参数匹配，其默认值为 1e–12。
- 要更改 *GMIN*，请将 Environment Parameters 模块添加到模型中，并将 **GMIN** 参数设置为所需值。
