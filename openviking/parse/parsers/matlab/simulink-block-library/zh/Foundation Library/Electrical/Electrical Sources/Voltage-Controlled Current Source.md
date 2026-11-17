---
type: simulink-block
title: 'Voltage-Controlled Current Source'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Electrical / Electrical Sources'
documentation_page: 'voltagecontrolledcurrentsource'
documentation_source_path: 'ref/voltagecontrolledcurrentsource.html'
language: zh-CN
chinese_source: worker-translation
---

# Voltage-Controlled Current Source

## 端口
```yaml
ports: []
```

该模块有四个电气守恒端口。模块左侧的连接 + 和 – 是控制端口。另外两个端口是提供输出电流的电气端子。箭头指示电流流动的正方向。
## 参数
```yaml
parameters: []
```

**Transconductance K**
:   跨导，即输出电流变化量除以引起该变化的输入电压变化量。默认值为 `1` 1/Ω。
## 所属库

R2025b 中未记录。

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2007a 中引入**

## 描述

线性压控电流源

Voltage-Controlled Current Source 模块对线性压控电流源进行建模，用以下方程描述：

I=K·(V(+)−V(−))

其中

|  |  |
| --- | --- |
| *`I`* | 电流 |
| *`K`* | 跨导 |
| *`V(+)`*,*`V(-)`* | 施加在 + 和 – 控制端口上的电压 |

要使用该模块，请将模块左侧的 + 和 – 端口（控制端口）连接到控制电压源。模块右侧的两个端口（输出端口）生成输出电流。箭头指示电流流动的正方向。

### 变量

要在仿真之前为模块变量设置优先级和初始目标值，请使用模块对话框或属性检查器中的 **Initial Targets** 部分。有关详细信息，请参阅 Set Priority and Initial Target for Block Variables。

标称值提供了一种指定模型中变量预期幅值的方法。使用基于标称值的系统缩放可提高仿真鲁棒性。标称值可以来自不同来源，其中之一是模块对话框或属性检查器中的 **Nominal Values** 部分。有关详细信息，请参阅 Modify Nominal Values for a Block Variable。
