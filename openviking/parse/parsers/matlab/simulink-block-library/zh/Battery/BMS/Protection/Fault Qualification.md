---
type: simulink-block
title: 'Fault Qualification'
family: 'simscape-battery'
product_id: 'simscape-battery'
product_name: 'Battery'
documentation_release: R2025b
official_category: 'BMS / Protection'
documentation_page: 'faultqualification'
documentation_source_path: 'ref/faultqualification.html'
language: zh-CN
chinese_source: worker-translation
---

# Fault Qualification

## 端口
```yaml
ports:
- name: Symptom
  summary: 症状标志 0 | 1 | 0 或 1 值的向量
  direction: input
- name: Error
  summary: 错误标志 0 | 1 | 0 或 1 值的向量
  direction: output
```

### 输入

### **Symptom** — 症状标志 `0` | `1` | `0` 或 `1` 值的向量

表示电池存在需要判定的症状。如果此输入等于 `1`，则电池存在症状。

### 输出

### **Error** — 错误标志 `0` | `1` | `0` 或 `1` 值的向量

表示电池存在错误。如果此输出等于 `1`，则电池存在错误。此端口的大小等于 **Symptom** 输入端口的大小。
## 参数
```yaml
parameters:
- name: Qualification time (s)
  summary: 错误确认时间 2（默认值）| 正标量
  group: ''
- name: Disqualification time (s)
  summary: 错误取消确认时间 4（默认值）| 非负标量
  group: ''
- name: Sample time (-1 for inherited)
  summary: 模块采样时间 -1（默认值）| 0 | 正整数
  group: ''
```

### **Qualification time (s)** — 错误确认时间 `2`（默认值）| 正标量

确认错误所需的时间，以秒为单位。

### **Disqualification time (s)** — 错误取消确认时间 `4`（默认值）| 非负标量

取消确认错误所需的时间，以秒为单位。如果将此参数设置为 `0`，则模块不会取消确认错误。

### **Sample time (-1 for inherited)** — 模块采样时间 `-1`（默认值）| 0 | 正整数

连续模块执行之间的时间。在执行期间，模块产生输出，并在适当的情况下更新其内部状态。有关详细信息，请参阅 What Is Sample Time? 和 Specify Sample Time。

对于继承的离散时间操作，请将此参数指定为 `-1`。对于离散时间操作，请将此参数指定为正整数。对于连续时间操作，请将此参数指定为 `0`。

如果此模块位于允许在连续操作和离散操作之间切换的掩码子系统或变体子系统中，请提升采样时间参数。提升采样时间参数可确保在模块的连续实现和离散实现之间正确切换。有关详细信息，请参阅 Promote Block Parameters on a Mask。
## 所属库

Simscape / Battery / BMS / Protection

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2022b 中引入**

### R2025a: 指定逻辑信号的向量化输入

**Symptom** 输入端口现在接受逻辑值 `0` 或 `1` 的向量。所有输入症状的确认时间和取消确认时间相同。

## 描述

故障确认算法

此模块实现故障确认算法。输入和输出端口是逻辑信号，您可以将它们指定为标量或向量。为防止错误取消确认，请将 **Disqualification time** 参数设置为 `0`。

此模块支持单精度和双精度浮点仿真。

**注意**

要启用继承的单精度浮点仿真，除 **Sample time (-1 for inherited)** 参数外，所有输入和参数的数据类型必须为 `single`。

您可以通过使用 **Sample time (-1 for inherited)** 参数在模块的连续实现和离散实现之间切换。要将模块配置为连续时间，请将 **Sample time (-1 for inherited)** 参数设置为 `0`。要将模块配置为离散时间，请将 **Sample time (-1 for inherited)** 参数设置为正的非零值，或设置为 `-1` 以从上游模块继承采样时间。

**注意**

此模块的连续时间实现仅在双精度浮点仿真中工作。如果您提供单精度浮点参数和输入，此模块会将它们转换为双精度浮点值以防止错误。

此图显示了模块的结构：

### 方程

此图展示了此模块的内部计数器与 **Error** 输出端口的工作方式：

故障确认以症状作为输入。当症状存在时，例如过压错误，输入为 `1`；当症状不存在时，输入为 `0`。当症状存在时，模块会递增内部计数器。当计数器达到与所需确认时间对应的最大值时，输出端口为 `1`。

你必须提供大于 `0` 的取消确认时间，以允许取消确认。当取消确认时间不为 `0` 且症状不存在时，模块会递减计数器，直到其达到 `0`。当计数器为 `0` 时，输出端口为 `0`。
