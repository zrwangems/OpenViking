---
type: simulink-block
title: 'Translational Spring (PB)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Simscape'
documentation_release: R2025b
official_category: 'Foundation Block Libraries / Position-Based Mechanical Translational Models / Elements'
documentation_page: 'translationalspringpb'
documentation_source_path: 'ref/translationalspringpb.html'
language: zh-CN
chinese_source: worker-translation
---

# Translational Spring (PB)

## 端口

### 守恒

### **B** — 基础端口，基于位置的机械平移

基于位置的机械平移守恒端口，表示基础连接。

### **F** — 跟随端口，基于位置的机械平移

基于位置的机械平移守恒端口，表示跟随连接。对于正 length，端口 **F** 的位置比端口 **B** 的位置更正。

## 参数

### **弹簧刚度** — 弹簧刚度系数 `1e5 N/m`（默认） | 标量

弹簧刚度系数。

## 所属库

Simscape / Foundation Library / Translational / Elements

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2024b 中引入**

## 描述

用于基于位置的机械平移系统的理想弹簧

Translational Spring (PB) 模块表示理想平移弹簧。弹簧变形是 length 与静止长度之差。正变形会增加 length。

f=−K⋅δ

δ=length−lengthrest

length=xF−xB

其中：

- *f* 是通过弹簧传递的力。
- *K* 是弹簧刚度。
- *δ* 是弹簧变形。
- *length* 是弹簧长度。
- *length*rest 是弹簧静止长度。
- *x*B 和 *x*F 分别是端口 **B** 和 **F** 的绝对位置。
- *power\_dissipated* 是通过阻尼器耗散的功率。

连接 **B** 和 **F** 是基于位置的机械平移守恒端口。弹簧力从端口 **B** 作用于端口 **F**。正弹簧力沿正方向驱动端口 **F**。如果 length 为正，正弹簧力对应于弹簧处于压缩状态。有关详细信息，请参阅双端口模块方向和力流约定。

### 变量

要在仿真前设置模块变量的优先级和初始目标值，请使用模块对话框或属性检查器中的 **初始目标** 部分。有关详细信息，请参阅设置模块变量的优先级和初始目标。

标称值提供了一种指定模型中变量预期量级的方法。使用基于标称值的系统缩放可提高仿真稳健性。标称值可以来自不同来源，其中之一是模块对话框或属性检查器中的 **标称值** 部分。有关详细信息，请参阅修改模块变量的标称值。

初始化模块的正确方式取决于其在模块图中的位置：

- 通常，将任意两个变量指定为高优先级目标，例如，
  **Force** 和 **Length**，或 **Rest
  length** 和 **Deformation**。例外是
  **Force** 和 **Deformation**，因为这两个
  变量彼此成正比。
- 如果弹簧与已知力串联，则仅将
  **Length** 或 **Rest length** 指定为高优先级
  目标。
- 如果弹簧与已知长度并联，则仅将
  **Force**、**Deformation** 或 **Rest
  length** 指定为高优先级目标。
- 如果弹簧与已知力串联且与已知长度并联，
  则不要指定任何高优先级目标。
