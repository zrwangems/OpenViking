---
type: simulink-block
title: 'VR Text Output'
family: 'sl3d'
product_id: 'sl3d'
product_name: 'Simulink 3D Animation'
documentation_release: R2025b
official_category: 'Classic Virtual Reality World'
documentation_page: 'vrtextoutput'
documentation_source_path: 'vrtextoutput.html'
language: zh-CN
chinese_source: worker-translation
---

# VR Text Output

## 端口

R2025b 中未提供文档。

## 参数

**关联的 VRML 文件** — 虚拟世界 3D 文件，用于指定文本输出到的虚拟世界。

**关联的 Text 节点** — 虚拟世界中文本输出到的 Text 节点。

**格式字符串** — 输出文本使用的格式。此模块使用 `sprintf()` 对输出字符串进行格式化。与 `sprintf()` 一样，它以向量化方式工作，格式字符串会循环用于输入向量的各个分量。此模块不支持 `%c` 和 `%s` 转换格式，因为 Simulink 产品中的信号不能同时包含字符和字符串。

**采样时间** — 输入采样时间，或输入 `-1` 以使用继承的采样时间。

**确保仿真期间查看器窗口处于打开状态** — 选中此复选框，以确保仿真期间 Simulink 3D Animation Viewer 处于打开状态。

## 所属库

R2025b 中未提供文档。

## 模块特性

R2025b 中未提供文档。

## 扩展功能

### C/C++ 代码生成

使用 Simulink® Coder™ 生成 C 和 C++ 代码。

对实际数据类型或功能的支持取决于模块实现。

## 版本历史

**在 R2006b 中引入**

### R2023b：将移除

`VR Text Output` 将在未来版本中移除。请改用 `sim3d` 类和 Simulation 3D 模块，实现 MATLAB® 和 Simulink 与 Unreal Engine® 3D 仿真环境之间的接口。要开始使用，请参阅“在 Unreal Engine 环境中创建 3D 仿真”。

## 描述

（将移除）允许在虚拟现实场景中以文本形式显示 Simulink 信号值

VR Text Output 可以在虚拟现实场景中以文本形式显示 Simulink 信号值。

文本渲染对虚拟世界查看器而言是一项高负荷任务，因此输出文本时，渲染速度通常会下降。文本输出越复杂，这种影响越明显。如果将 Simulink 模型的输出限制为仅输出发生变化的信号值（例如模型中的字幕），或者使用更多静态文本节点，则可以提高性能。

要打开模块参数对话框，请双击该模块。
