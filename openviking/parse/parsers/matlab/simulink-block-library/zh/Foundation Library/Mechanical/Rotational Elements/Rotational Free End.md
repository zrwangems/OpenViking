---
type: simulink-block
title: 'Rotational Free End'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Mechanical / Rotational Elements'
documentation_page: 'rotationalfreeend'
documentation_source_path: 'ref/rotationalfreeend.html'
language: zh-CN
chinese_source: worker-translation
---

# Rotational Free End

## 端口

### 守恒

### **W** — 零扭矩机械旋转

机械旋转守恒端口，自由旋转且无扭矩。

## 参数

未在 R2025b 中记录。

## 所属库

Simscape / Foundation Library / Mechanical / Rotational Elements

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2012b 中引入**

### R2019b: 不再需要封端未连接端口

不再需要此模块。从 R2019b 开始，已取消禁止 Simscape™ 模型中存在未连接守恒端口的限制。现在，如果将守恒端口保持未连接，物理网络会将该端口处的所有 Through 变量设置为 0。但是，您仍可以使用 Terminator 模块来提高图的可读性。

没有计划移除 Terminator 模块。所有使用这些模块的现有模型的工作方式都与以前版本相同。

## 描述

零扭矩旋转端口终结器

Rotational Free End 模块表示一个机械旋转端口，该端口自由旋转且无扭矩。

您可以使用此模块来端接其他模块上您希望保持未连接的机械旋转端口。这不是必需的，因为如果您将守恒端口保持未连接，物理网络会将该端口处的所有 Through 变量设置为 0。但是，Terminator 模块可提高图的可读性。

您还可以使用此模块设置节点处的初始旋转速度。

### 变量

要在仿真前设置模块变量的优先级和初始目标值，请使用模块对话框或 Property Inspector 中的 **Initial Targets** 部分。有关详细信息，请参阅设置模块变量的优先级和初始目标。

标称值提供了一种在模型中指定变量预期幅值的方法。使用基于标称值的系统缩放可提高仿真稳健性。标称值可以来自不同来源，其中之一是模块对话框或 Property Inspector 中的 **Nominal Values** 部分。有关详细信息，请参阅修改模块变量的标称值。
