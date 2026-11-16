---
type: simulink-block
title: 'Software Composition'
family: 'autosar'
product_id: 'autosar'
product_name: 'AUTOSAR Blockset'
documentation_release: R2025b
official_category: 'Software Architecture Modeling'
documentation_page: 'softwarecomposition'
documentation_source_path: 'ref/softwarecomposition.html'
language: zh-CN
chinese_source: worker-translation
---

# Software Composition

## 端口

### 输入

### **输入端口** — 组合需求端口 scalar | vector | matrix

AUTOSAR 软件组合端口接口中的需求端口。

### 输出

### **输出端口** — 组合提供端口 scalar | vector | matrix

AUTOSAR 软件组合端口接口中的提供端口。

### **客户端端口** — 服务接口上的组合客户端端口 scalar | vector | matrix

AUTOSAR 软件组合端口接口中的客户端端口。当您在 AUTOSAR 自适应架构中对方法通信建模时，支持客户端端口。

### **服务器端口** — 服务接口上的组合服务器端口 scalar | vector | matrix

AUTOSAR 软件组合端口接口中的服务器端口。当您在 AUTOSAR 自适应架构中对方法通信建模时，支持服务器端口。

## 参数

R2025b 中未记录。

## 所属库

AUTOSAR Blockset

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2019b 中引入**

### R2023a：用于自适应组件建模的客户端和服务器端口

当您在 AUTOSAR 自适应架构中对方法通信建模时，客户端和服务器端口可用并受支持。

## 描述

在 AUTOSAR 架构模型中对软件组合建模

在 AUTOSAR 架构模型中，您可以使用组合编辑器以及 Simulink® 工具条的 **Modeling** 选项卡来添加和连接组合与组件。使用 Software Composition 模块将嵌套软件组合添加到 AUTOSAR 软件设计。组合支持经典建模和自适应建模。

要添加并连接嵌套 AUTOSAR 组合：

- 从 **Modeling** 选项卡或画布左侧的选项板中，添加一个 Software Composition 模块。
- 添加组合需求端口和提供端口。要添加每个组合端口，请点击 Software Composition 模块的边缘。当端口控件出现时：

  - 对于经典建模，为需求端口选择 **Input**，或为提供端口选择 **Output**。
  - 对于自适应建模，为需求端口选择 **Input** 或 **Client**，或为提供端口选择 **Output** 或 **Server**。

  或者，打开 Software Composition 模块。要添加每个组合端口，请点击组合图的边界，并根据需要选择需求端口和提供端口。
- 要将 Software Composition 模块连接到其他模块，请用信号线连接模块端口。
- 要将 Software Composition 模块连接到架构或组合模型根端口，请从组合端口拖动一条线到包含该模块的模型边界。释放连接会在边界处创建一个根端口。
- 使用属性检查器配置其他 AUTOSAR 属性。

AUTOSAR 组合包含一组具有共同用途的 AUTOSAR 组件和组合。要填充组合，请打开 Software Composition 模块，并开始添加更多 Software Composition 模块以及 Classic Component 或 Adaptive Component 模块。不支持混用经典组件和自适应组件。
