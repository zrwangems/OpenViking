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

R2025b 中未提供文档。

## 所属库

R2025b 中未提供文档。

## 模块特性

R2025b 中未提供文档。

## 扩展功能

R2025b 中未提供文档。

## 版本历史

**在 R2019a 中引入**

## 描述

连接具有不同接口的组件

Adapter 模块允许您连接具有不同接口定义的组件的源端口和目标端口。

Adapter 模块

要添加或连接 System Composer™ 组件，请执行以下操作：

- 从 **Modeling** 选项卡或选项板中添加 Adapter 模块。Adapter 模块具有 `In` 和
  `Out` 端口。
- 单击并拖动端口以创建连接。将每个端口连接到另一个组件。您也可以创建一个新组件来完成该连接。
- 在具有不同接口的两个端口之间插入 Adapter 模块。
  您可以在各端口的接口元素之间创建映射。

要在架构模型中的接口之间进行映射、应用接口转换并进入总线创建模式，请执行以下操作：

- 双击 Adapter 模块以打开 Interface Adapter 对话框。在该对话框中，您可以创建和编辑输入接口与输出接口之间的映射，
  并将 **Apply Interface conversion** 参数设置为
  `UnitDelay` 以断开代数环，或设置为
  `RateTransition` 以协调引用模型的不同采样时间速率。当输出接口未定义时，您可以在总线创建模式下使用输入接口来创建自有输出接口。

当您的 Simulink® 组件行为带有信号线或消息线时，若要为架构模型合并消息连接，并为软件架构模型合并信号或消息连接，请执行以下操作：

- 通过双击该模块打开 Interface Adapter，手动配置 Adapter 模块。将
  **Apply Interface conversion** 参数设置为
  `Merge`。
- 对于软件架构模型，从工具条中添加 Merge
  模块，该模块是预先配置为用于合并的 Adapter 模块。
