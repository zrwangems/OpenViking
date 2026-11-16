---
type: simulink-block
title: 'Adapter'
family: 'systemcomposer'
product_id: 'systemcomposer'
product_name: 'System Composer'
documentation_release: R2025b
official_category: 'Architectures, Requirements, and Allocations / Author Architecture Models'
documentation_page: 'adapter'
documentation_source_path: 'ref/adapter.html'
language: zh-CN
chinese_source: worker-translation
---

# Adapter

## 端口

### 输入

### **Source** — 来自组件接口的输入连接

如果连接到源组件，则端口上的接口应兼容。

### 输出

### **Destination** — 到组件接口的输出连接

如果连接到目标组件，则端口上的接口应兼容。

## 参数

R2025b 中未记录。

## 所属库

R2025b 中未记录。

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2019a 中引入**

## 描述

连接具有不同接口的组件

Adapter 模块允许您连接接口定义不同的组件的源端口和目标端口。

Adapter 模块

要添加或连接 System Composer™ 组件：

- 从 **Modeling** 选项卡或选项板中添加 Adapter 模块。Adapter 模块具有 `In` 和 `Out` 端口。
- 单击并拖动端口以创建连接。将每个端口连接到另一个组件。您还可以创建一个新组件来完成连接。
- 在两个具有不同接口的端口之间插入 Adapter 模块。您可以在每个端口上的接口元素之间创建映射。

要在接口之间进行映射、应用接口转换，并为架构模型进入总线创建模式：

- 双击 Adapter 模块以打开 Interface Adapter 对话框。在该对话框中，您可以创建和编辑输入接口与输出接口之间的映射，并将 **Apply Interface conversion** 参数设置为 `UnitDelay` 以打破代数环，或设置为 `RateTransition` 以协调引用模型的不同采样时间速率。当输出接口未定义时，您可以在总线创建模式中使用输入接口来编写自有输出接口。

当您具有带信号线或消息线的 Simulink® 组件行为时，要为架构模型合并消息连接，并为软件架构模型合并信号或消息连接：

- 通过双击该模块以打开 Interface Adapter，手动配置 Adapter 模块。将 **Apply Interface conversion** 参数设置为 `Merge`。
- 对于软件架构模型，从工具条中添加 Merge 模块，这是一个用于合并的预配置 Adapter 模块。
