---
type: simulink-block
title: 'Interface (PB-Translational)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Translational / Utilities'
documentation_page: 'interfacepbtranslational'
documentation_source_path: 'ref/interfacepbtranslational.html'
language: zh-CN
chinese_source: worker-translation
---

# Interface (PB-Translational)

## 端口
```yaml
ports:
- name: Bpb
  summary: 左侧基于位置的机械平移端口
  direction: conserving
- name: Fpb
  summary: 右侧基于位置的机械平移端口
  direction: conserving
- name: F
  summary: 右侧非基于位置的机械平移端口
  direction: conserving
- name: B
  summary: 左侧非基于位置的机械平移端口
  direction: conserving
```

### 守恒端口

### **Bpb** — 左侧基于位置的机械平移端口

基于位置的机械平移守恒端口，表示通过该接口的一个通道点。将此端口连接到另一个模块的基于位置的机械平移端口。

#### 依赖关系

要启用此端口，请将 **Position-based port** 参数设置为 `Base`。

### **Fpb** — 右侧基于位置的机械平移端口

基于位置的机械平移守恒端口，表示通过该接口的一个通道点。将此端口连接到另一个模块的基于位置的机械平移端口。

#### 依赖关系

要启用此端口，请将 **Position-based port** 参数设置为 `Follower`。

### **F** — 右侧非基于位置的机械平移端口

机械平移守恒端口，表示通过该接口的一个通道点。将此端口连接到另一个模块的常规非基于位置的机械平移端口。

#### 依赖关系

要启用此端口，请将 **Position-based port** 参数设置为 `Base`。

### **B** — 左侧非基于位置的机械平移端口

机械平移守恒端口，表示通过该接口的一个通道点。将此端口连接到另一个模块的常规非基于位置的机械平移端口。

#### 依赖关系

要启用此端口，请将 **Position-based port** 参数设置为 `Follower`。
## 参数
```yaml
parameters:
- name: Position-based port
  summary: 接口方向 Base（默认）| Follower
  group: ''
```

### **Position-based port** — 接口方向 `Base`（默认）| `Follower`

指定模块方向：

- `Base` — 暴露基于位置的端口 **Bpb**（在默认方向下位于模块图标左侧），以及右侧的机械平移端口 **F**。模块正方向为从端口 **Bpb** 到端口 **F**。
- `Follower` — 暴露基于位置的端口 **Fpb**（在默认方向下位于模块图标右侧），以及左侧的机械平移端口 **B**。模块正方向为从端口 **B** 到端口 **Fpb**。
## 所属库

Simscape / Foundation Library / Translational / Utilities

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2024b 中引入**

## 描述

连接基于位置和非基于位置的机械平移端口

Interface (PB-Translational) 模块表示基于位置和非基于位置的机械平移网络之间的刚性连接。端口速度相等。接口处的力大小相等、方向相反。

**Position-based port** 参数值决定模块方向。将模块正方向与所连接的基于位置网络的正方向对齐。
