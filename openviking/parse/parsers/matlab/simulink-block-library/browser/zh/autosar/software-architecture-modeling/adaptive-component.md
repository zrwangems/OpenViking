---
type: simulink-block
title: 'Adaptive Component'
family: 'autosar'
product_id: 'autosar'
product_name: 'AUTOSAR Blockset'
documentation_release: R2025b
official_category: 'Software Architecture Modeling'
documentation_page: 'adaptivecomponent'
documentation_source_path: 'ref/adaptivecomponent.html'
language: zh-CN
chinese_source: worker-translation
---

# Adaptive Component

## 端口

### 输入

### **输入端口** — 组件需求端口 标量 | 向量 | 矩阵

AUTOSAR 软件组件端口接口中的需求端口。

如果将组件模块链接到实现模型，则模块和模型的端口接口（包括端口数量）匹配。

### **客户端端口** — 服务接口上的组件客户端端口 标量 | 向量 | 矩阵

服务接口上的客户端端口，用于 AUTOSAR 方法通信，实现服务消费者。

如果将组件模块链接到实现模型，则模块和模型的端口接口（包括端口数量）匹配。

### 输出

### **输出端口** — 组件提供端口 标量 | 向量 | 矩阵

AUTOSAR 软件组件端口接口中的提供端口。

如果将组件模块链接到实现模型，则模块和模型的端口接口（包括端口数量）匹配。

### **服务器端口** — 服务接口上的组件服务器端口 标量 | 向量 | 矩阵

服务接口上的服务器端口，用于 AUTOSAR 方法通信，实现服务提供者。

如果将组件模块链接到实现模型，则模块和模型的端口接口（包括端口数量）匹配。

## 参数

在 R2025b 中未提供文档。

## 所属库

AUTOSAR Blockset

## 模块特性

在 R2025b 中未提供文档。

## 扩展功能

在 R2025b 中未提供文档。

## 版本历史

**在 R2023a 中引入**

## 描述

在 AUTOSAR 架构模型中为自适应软件组件建模

在 AUTOSAR 架构模型中，您使用组合编辑器以及 Simulink® 工具条中的**建模**选项卡来添加并连接组合与组件。使用 Adaptive Component 模块将自适应软件组件添加到 AUTOSAR 自适应软件设计。

要添加并连接 AUTOSAR 组件：

- 在**建模**选项卡中，通过将**平台**设置为 `Adaptive` 来配置架构模型的平台种类。
- 对于设计所需的每个组件，从**建模**选项卡或画布左侧的选板中，添加一个 Adaptive Component 模块。您可以在属性检查器中查看组件**种类**。对于自适应组件，组件种类为 `AdaptiveApplication`。
- 添加组件需求端口和提供端口。要添加每个组件端口，请点击 Adaptive Component 模块的边缘。当端口控件出现时，为需求端口选择**输入**或**客户端**，或者为提供端口选择**输出**或**服务器**。
- 要将 Adaptive Component 模块连接到其他模块，请用信号线连接模块端口。
- 要将 Adaptive Component 模块连接到架构或组合模型的根端口，请从组件端口拖一条线到包含该组件的模型边界。释放连接将在边界处创建一个根端口。
- 使用属性检查器配置其他 AUTOSAR 属性。

添加并连接 AUTOSAR 组件后，通过创建、导入或链接模型来向 AUTOSAR 组件添加 Simulink 行为。

如果您有 Requirements Toolbox™ 软件，则可以将 AUTOSAR 架构模型中的组件链接到 Simulink 需求。

每个 Adaptive Component 模块都表示一个自适应应用程序。部署时，每个自适应组件都被视为一个可执行文件。
