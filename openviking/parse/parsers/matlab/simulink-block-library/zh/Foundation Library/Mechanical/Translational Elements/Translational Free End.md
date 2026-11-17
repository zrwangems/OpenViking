---
type: simulink-block
title: 'Translational Free End'
family: 'mechanical'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Mechanical / Translational Elements'
documentation_page: 'translationalfreeend'
documentation_source_path: 'ref/translationalfreeend.html'
language: zh-CN
chinese_source: worker-translation
---

# Translational Free End

## 端口

### 守恒

### **V** — 零力机械平移

可自由移动且无作用力的机械平移守恒端口。

## 参数

在 R2025b 中未记录。

## 所属库

Simscape / Foundation Library / Mechanical / Translational Elements

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成

使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2012b 中引入**

### R2019b：不再需要对未连接端口进行封端

不再需要此模块。从 R2019b 开始，已取消禁止在 Simscape™ 模型中使用未连接守恒端口的限制。现在，如果使守恒端口保持未连接，物理网络会将此端口处的所有 Through 变量设置为 0。但是，您仍可使用端接模块来提高图的可读性。

没有计划移除端接模块。所有使用这些模块的现有模型的工作方式与先前版本相同。

## 描述

零力平移端口端接器

Translational Free End 模块表示一个可自由移动、无作用力的机械平移端口。

您可以使用此模块端接其他模块上您希望保持未连接的机械平移端口。这不是必需的，因为如果使守恒端口保持未连接，物理网络会将此端口处的所有 Through 变量设置为 0。但是，端接模块可提高图的可读性。

您还可以使用此模块设置节点处的初始平移速度。

### 变量

要在仿真之前设置模块变量的优先级和初始目标值，请使用模块对话框或属性检查器中的 **初始目标** 部分。有关详细信息，请参阅为模块变量设置优先级和初始目标。

标称值提供了一种指定模型中变量预期量值的方法。使用基于标称值的系统缩放可以提高仿真稳健性。标称值可以来自不同来源，其中之一是模块对话框或属性检查器中的 **标称值** 部分。有关详细信息，请参阅修改模块变量的标称值。
