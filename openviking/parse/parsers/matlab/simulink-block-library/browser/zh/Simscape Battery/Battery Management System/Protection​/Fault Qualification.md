---
type: simulink-block
title: 'Fault Qualification'
family: 'simscape-battery'
product_id: 'simscape-battery'
product_name: 'Simscape Battery'
documentation_release: R2025b
official_category: 'Battery Management System / Protection\u200b'
documentation_page: 'faultqualification'
documentation_source_path: 'ref/faultqualification.html'
language: zh-CN
chinese_source: worker-translation
---

# Fault Qualification

## 端口

### 输入

### **Symptom** — Symptom 标志 `0` | `1` | `0` 或 `1` 值的向量

指示电池有需要鉴定的征兆。如果此输入等于 `1`，则电池存在征兆。
### 输出

### **Error** — Error 标志 `0` | `1` | `0` 或 `1` 值的向量

指示电池存在错误。如果此输出等于 `1`，则电池存在错误。此端口的大小等于 **Symptom** 输入端口的大小。

## 参数

### **Qualification time (s)** — 错误鉴定时间 `2`（默认） | 正标量

对错误进行鉴定所需的时间，以秒为单位。

### **Disqualification time (s)** — 错误取消鉴定时间 `4`（默认） | 非负标量

对错误进行取消鉴定所需的时间，以秒为单位。如果将此参数设置为 `0`，模块不会取消鉴定该错误。

### **Sample time (-1 for inherited)** — 模块采样时间 `-1`（默认） | 0 | 正整数

连续模块执行之间的时间。执行期间，模块产生输出，并（如果适用）更新其内部状态。有关详细信息，请参阅 What Is Sample Time? 和 Specify Sample Time。

对于继承的离散时间操作，将此参数指定为 `-1`。对于离散时间操作，将此参数指定为正整数。对于连续时间操作，将此参数指定为 `0`。

如果此模块位于允许在连续操作和离散操作之间切换的掩码子系统或变体子系统中，请提升采样时间参数。提升采样时间参数可确保在模块的连续实现和离散实现之间正确切换。有关详细信息，请参阅 Promote Block Parameters on a Mask。

## 所属库

Simscape / Battery / BMS / Protection

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2022b 中引入**

### R2025a：指定逻辑信号的向量化输入

**Symptom** 输入端口现在接受逻辑值 `0` 或 `1` 的向量。所有输入征兆的鉴定和取消鉴定时间相同。

## 描述

故障鉴定算法

此模块实现故障鉴定算法。输入和输出端口是逻辑信号，您可以将其指定为标量或向量。为防止错误取消鉴定，请将 **Disqualification time** 参数设置为 `0`。

此模块支持 single-precision 和 double-precision 浮点仿真。

**注意**

要启用继承的 single-precision 浮点仿真，除 **Sample time (-1 for inherited)** 参数外，所有输入和参数的数据类型都必须为 `single`。

您可以使用 **Sample time (-1 for inherited)** 参数在模块的连续实现和离散实现之间切换。要将模块配置为连续时间，请将 **Sample time (-1 for inherited)** 参数设置为 `0`。要将模块配置为离散时间，请将 **Sample time (-1 for inherited)** 参数设置为正的非零值，或设置为 `-1` 以从上溯模块继承采样时间。

**注意**

此模块的连续时间实现仅在 double-precision 浮点仿真中有效。如果您提供 single-precision 浮点参数和输入，此模块会将它们转换为 double-precision 浮点值以防止错误。

下图显示此模块的结构：

### 方程

下图显示此模块的内部计数器和 **Error** 输出端口如何工作：

故障鉴定将征兆作为输入。当存在征兆（例如过压错误）时，输入为 `1`；当不存在征兆时，输入为 `0`。当存在征兆时，模块递增内部计数器。当计数器达到与所需鉴定时间对应的最大值时，输出端口为 `1`。

必须提供大于 `0` 的取消鉴定时间以允许取消鉴定。当取消鉴定时间不为 `0` 且不存在征兆时，模块递减计数器，直到它达到 `0`。当计数器为 `0` 时，输出端口为 `0`。
