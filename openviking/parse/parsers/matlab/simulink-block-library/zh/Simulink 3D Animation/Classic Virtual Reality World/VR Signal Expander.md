---
type: simulink-block
title: 'VR Signal Expander'
family: 'sl3d'
product_id: 'sl3d'
product_name: 'Simulink 3D Animation'
documentation_release: R2025b
official_category: 'Classic Virtual Reality World'
documentation_page: 'vrsignalexpander'
documentation_source_path: 'vrsignalexpander.html'
language: zh-CN
chinese_source: worker-translation
---

# VR Signal Expander

## 端口

在 R2025b 中未提供文档。

## 参数

**输出宽度** — 指定输出向量的长度。

**输出信号索引** — 用于指示输入信号在输出中所处位置的向量。其余位置由 VR Placeholder 信号填充。

例如，假设您有一个包含两个信号的输入向量，并希望生成一个包含四个信号的输出向量，其中第一个输入信号位于位置 2，第二个输入信号位于位置 4。在 **输出宽度** 框中，输入 `4`；在 **输出信号索引** 框中，输入 `[2,4]`。第一个和第三个输出信号未指定。

## 所属库

在 R2025b 中未提供文档。

## 模块特性

在 R2025b 中未提供文档。

## 扩展功能

在 R2025b 中未提供文档。

## 版本历史

**在 R2006a 之前引入**

### R2023b: 将被移除

`VR Signal Expander` 将在未来版本中移除。请改用 `sim3d` 类和 Simulation 3D 模块，将 MATLAB® 和 Simulink 与 Unreal Engine® 3D 仿真环境进行交互。要开始使用，请参阅在 Unreal Engine 环境中创建 3D 仿真。

## 描述

（将被移除）将输入向量扩展为完全限定的虚拟世界字段向量

VR Signal Expander 模块使用来自输入端口的一些值创建预定义长度的向量，并用占位符信号值填充其余位置。

要打开模块参数对话框，请双击该模块。
