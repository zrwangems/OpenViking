---
type: simulink-block
title: 'DC Current Source'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Additional Components / SPICE Sources'
documentation_page: 'dccurrentsource'
documentation_source_path: 'ref/dccurrentsource.html'
language: zh-CN
chinese_source: worker-translation
---

# DC Current Source

## 端口
```yaml
ports:
- name: +
  summary: 正电压电端口
  direction: conserving
- name: '-'
  summary: 负电压电端口
  direction: conserving
```

### 守恒端口

### **+** — 正电压电端口

与直流电流源正电压相关联的电守恒端口

### **-** — 负电压电端口

与直流电流源负电压相关联的电守恒端口
## 参数
```yaml
parameters:
- name: Constant value, DC
  summary: 直流输出电流 0 A（默认）
  group: ''
- name: Include parallel conductance, GMIN
  summary: 是否包含并联电导 Yes（默认）| No
  group: ''
```

### **Constant value, DC** — 直流输出电流 `0` `A`（默认）

直流输出电流的值，单位为 A。

### **Include parallel conductance, GMIN** — 是否包含并联电导 `Yes`（默认）| `No`

指定电流源是否包含并联电导。并联电导 *GMIN* 的值取决于您的模型是否包含 Environment Parameters 模块。

下表显示了并联电导 *GMIN* 的可能取值：

**并联电导 GMIN 的取值**

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

恒定电流源

DC Current Source 模块表示一个恒定电流源，其输出电流值与其端子两端的电压无关。

该模块内部使用一个小电导来防止数值仿真问题。该电导连接器件的 + 和 - 端口，其电导为 *GMIN*：

- 默认情况下，*GMIN* 与 Environment Parameters 模块的 **GMIN** 参数一致，其默认值为 1e–12。
- 要更改 *GMIN*，请将 Environment Parameters 模块添加到您的模型中，并将 **GMIN** 参数设置为所需的值。
