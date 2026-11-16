---
type: simulink-block
title: 'Foster Thermal Model'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Electrical Block Libraries / Passive / Thermal'
documentation_page: 'fosterthermalmodel'
documentation_source_path: 'ref/fosterthermalmodel.html'
language: zh-CN
chinese_source: worker-translation
---

# Foster Thermal Model

## 端口

### 守恒

### **A** — 左侧结热

与左侧结关联的热守恒端口。

### **B** — 右侧结热

与右侧结关联的热守恒端口。

## 参数

### **热阻数据** — 热阻值 `[ 0.0016 0.0043 0.0013 0.0014 ]` `K/W`（默认）

半导体模块的热阻值，*Rthermal*，指定为向量。

### **热时间常数数据** — 热时间常数数据 `[ 0.0068 0.064 0.32 2 ]` `s`（默认）

半导体模块的热时间常数值，*τ*，指定为向量。

### **从稳态开始** — 热时间常数数据 `On`（默认） | `Off`

是否将模块初始化为稳态。

## 所属库

Simscape / Electrical / Passive / Thermal

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**R2016a 中引入**

## 描述

通过半导体模块的热传递

**注意**

Foster Thermal Model 模块表示 Tj 和 Tc 端口之间温降的端到端行为模型。此模块不预测端口 **B** 处的热流率。您也不能使用额外模块扩展此模型。要预测端口 B 处的热流率并使用额外模块扩展模型，请使用 Cauer Thermal Model 模块，并选择 **使用 Foster 系数数据参数化 Cauer 模型** 参数。

Foster Thermal Model 模块表示通过半导体模块的热传递。该图显示四阶 Foster Thermal Model 模块的等效电路。*Tj* 是结温，*Tc* 是基板温度或环境温度。

Foster 热模型包含一个或多个 Foster 热模型元件实例。该图显示 Foster 热模型元件的等效电路。

热元件数等于表示的阶数。对于一阶模型，使用标量模块参数。对于 *n* 阶模型，使用长度为 *n* 的行向量。描述 Foster 热模型的其他术语包括：

- 部分分式电路
- Pi 模型

一阶 Foster 热模型元件的定义方程为：

Cthermal=τRthermal

以及

QAB=TABRthermal+CthermaldTABdt,

其中：

- *Cthermal* 是热容。
- *τ* 是热时间常数。
- *Rthermal* 是热阻。
- *QAB* 是穿过材料的热流。
- *TAB* 是材料层之间的温差。

### 初始条件

您可以将模型初始化为稳态，或指定初始节点温度。要将模块初始化为稳态，请将 **从稳态开始** 参数设置为 `On`。要指定初始节点温度并启用 **初始目标** 部分，请将 **从稳态开始** 设置为 `Off`。第一个节点温度对应于端口 A 中的温度。

### 变量

要在仿真之前为模块变量设置优先级和初始目标值，请使用模块对话框或属性检查器中的 **初始目标** 部分。有关详细信息，请参阅 设置模块变量的优先级和初始目标。

标称值提供了一种在模型中指定变量预期量级的方法。使用基于标称值的系统缩放可提高仿真稳健性。标称值可以来自不同来源，其中之一是模块对话框或属性检查器中的 **标称值** 部分。有关详细信息，请参阅 按标称值进行系统缩放。
