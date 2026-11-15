---
type: simulink-block
title: 'Classic Component'
family: 'autosar'
product_id: 'autosar'
product_name: 'AUTOSAR Blockset'
documentation_release: R2025b
official_category: 'Software Architecture Modeling'
documentation_page: 'classiccomponent'
documentation_source_path: 'ref/classiccomponent.html'
language: zh-CN
chinese_source: official
---

# Classic Component

## 端口

### 输入

### **Input port** — 组件需型端口 标量 | 向量 | 矩阵

AUTOSAR 软件组件端口接口中的需型端口。

如果您将组件模块链接到实现模型，模块和模型的端口接口（包括端口数量）会进行匹配。
### 输出

### **Output port** — 组件供型端口 标量 | 向量 | 矩阵

AUTOSAR 软件组件端口接口中的供型端口。

如果您将组件模块链接到实现模型，模块和模型的端口接口（包括端口数量）会进行匹配。

## 参数

R2025b 官方文档未提供。

## 所属库

AUTOSAR Blockset

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

R2025b 官方文档未提供。

## 版本历史

**在 R2019b 中推出**

### R2023a: 软件组件模块名称已更改为 Classic 组件

Software Component 模块已重命名为 Classic Component 模块。

## 描述

在 AUTOSAR 架构模型中对经典软件组件进行建模

在 AUTOSAR 架构模型中，您使用组合编辑器和 Simulink® 工具条的**建模**选项卡来添加和连接组合与组件。使用 Classic Component 模块将经典软件组件添加到 AUTOSAR Classic 软件设计中。

要添加和连接 AUTOSAR 组件，请执行以下操作：

- 从**建模**选项卡中，通过将**平台**设置为 **Classic** 来配置架构模型的平台类型。
- 对于设计所需的每个组件，从**建模**选项卡或画布左侧的选项板中，添加一个 Classic Component 模块。您可以使用属性检查器设置组件**类型** - **Application**、**ComplexDeviceDriver**、**EcuAbstraction**、**SensorActuator** 或 **ServiceProxy**。（**Application** 和 **SensorActuator** 是常见类型。）
- 添加组件需型端口和供型端口。要添加每个组件端口，请点击 Classic Component 模块的边缘。当端口控件出现时，对需型端口选择**输入**，或对供型端口选择**输出**。
- 要将 Classic Component 模块连接到其他模块，请用信号线连接模块端口。
- 要将 Classic Component 模块连接到架构或组合模型根端口，请将一条信号线从组件端口拖到包含模型边界。释放连接会在边界处创建一个根端口。
- 使用属性检查器配置其他 AUTOSAR 属性。

在您添加和连接 AUTOSAR 组件后，通过创建、导入或链接模型向 AUTOSAR 组件添加 Simulink 行为。

如果您有 Requirements Toolbox™ 软件，您可以将 AUTOSAR 架构模型中的组件链接到 Simulink 需求。

*在 R2023a 之前的版本中: Classic Component 模块已命名为 Software Component。该模块经过重命名以区别于 Adaptive Component 模块，后者是在 R2023a 中引入的。*
