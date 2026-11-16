---
type: simulink-block
title: 'USS System'
family: 'robust'
product_id: 'robust'
product_name: 'Robust Control Toolbox'
documentation_release: R2025b
official_category: 'Uncertain System Representation / Uncertain Models in Simulink'
documentation_page: 'usssystem'
documentation_source_path: 'ref/usssystem.html'
language: zh-CN
chinese_source: worker-translation
---

# USS System

## 端口

R2025b 中未提供文档。

## 参数

### USS 系统变量

在 USS 系统变量中输入不确定对象（USS、UMAT、`ureal` 或 `ultidyn`）。

### 初始状态（标称动态）

如果 USS 系统变量的标称值具有状态，则在 `Initial states (nominal dynamics).` 中输入这些状态的初始条件。

### 不确定性值

不确定元素的值由 `Uncertainty value` 菜单控制。如果选择 `Nominal`，则使用不确定对象的标称值。如果选择 `User defined`，则必须在 `User-defined uncertainty (struct)` 对话框中输入 MATLAB® 结构体。结构体的字段名应与 USS 系统变量中不确定原子的名称相对应，而字段的值则是用于不确定对象的值（使用命令 `usubs`）。如果其中一些值是 SS 对象，则这些状态称为不确定性状态。

不确定性状态的顺序由 USS 系统变量的 Uncertainty 属性中原子的顺序决定。状态维数由 `User-defined uncertainty` 结构体中的实际数据决定。`User-defined uncertainty` 结构体中的任何额外字段都会被忽略。

### 用户定义的不确定性 (struc)

如果从 `Uncertainty value` 弹出菜单中选择 `User defined`，则在 `User-defined uncertainty (struct)` 中输入的结构体数据必须包含与 USS 系统变量的每个不确定原子相对应的字段。额外字段将被忽略。`usimsamp` 为 Simulink® 模型中的每个原子生成一个随机实例。它返回一个结构体，适合输入到 `User-defined uncertainty (struct)` 中。

### 初始状态（不确定动态）

在 `Initial states (uncertain dynamics)` 中输入不确定性状态的初始条件。

## 所属库

R2025b 中未提供文档。

## 模块特性

R2025b 中未提供文档。

## 扩展功能

R2025b 中未提供文档。

## 版本历史

**在 R2007a 中引入**

## 描述

（不推荐）将不确定系统导入 Simulink

USS System 模块接受包含 `ureal` 和 `ultidyn` 不确定对象的 USS 和 UMAT，以及 `ureal` 和 `ultidyn` 对象。在仿真或线性化中使用不确定系统的一个实例。在内部，USS 模型会转换为其等效的状态空间形式以进行求值。
