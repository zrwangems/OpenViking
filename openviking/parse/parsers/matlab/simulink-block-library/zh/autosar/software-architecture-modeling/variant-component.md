---
type: simulink-block
title: 'Variant Component'
family: 'autosar'
product_id: 'autosar'
product_name: 'AUTOSAR Blockset'
documentation_release: R2025b
official_category: 'Software Architecture Modeling'
documentation_page: 'variantcomponent'
documentation_source_path: 'ref/variantcomponent.html'
language: zh-CN
chinese_source: worker-translation
---

# Variant Component

## 端口

### 输入

### **Source** — 变体选项接口的输入

Variant Component 模块的输入必须与该模块所含变体选项的输入匹配。

### 输出

### **Destination** — 变体选项接口的输出

Variant Component 模块的输出必须与该模块所含变体选项的输出匹配。

## 参数

在 R2025b 中未记录。

## 所属库

AUTOSAR Blockset

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成

使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2025a 中引入**

## 描述

AUTOSAR 架构模型的条件变体

使用 Variant Component 模块管理 AUTOSAR 架构模型内的变体。

右键点击 Variant Component 模块，然后选择 **Add Variant Choice**，即可向 Variant Component 模块添加变体选项。

要控制活动的变体选项，请右键点击 Variant Component 模块，然后选择 **Variant** > **Label Mode Active Choice**。

对于 AUTOSAR 架构模型，活动的变体选项被视为顶层组件或组合模块。生成代码并导出 ARXML 时，只有在导出和代码生成时处于活动状态的变体选项才具有描述。
