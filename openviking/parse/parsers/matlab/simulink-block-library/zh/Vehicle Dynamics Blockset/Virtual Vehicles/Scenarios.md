---
type: simulink-block
title: 'Scenarios'
family: 'vdynblks'
product_id: 'vdynblks'
product_name: 'Vehicle Dynamics Blockset'
documentation_release: R2025b
official_category: 'Virtual Vehicles'
documentation_page: 'scenarios'
documentation_source_path: 'ref/scenarios.html'
language: zh-CN
chinese_source: worker-translation
---

# Scenarios

## 端口

### 输入

### **ExtDrvRef** — 外部驾驶员参考 `Bus`

外部驾驶员参考信号。

#### 依赖项

要创建此端口，请选择 **Driver reference**。

### **ExtDrvCmd** — 外部驾驶员命令 `Bus`

外部驾驶员命令信号。

#### 依赖项

要创建此端口，请选择 **Driver reference**。

### **VehFdbk** — 车辆反馈 `Bus`

包含车辆反馈信号的 Bus，包括速度、加速度和方向盘扭矩。

### 输出

### **Vis** — 可视化参考信号 `Bus`

包含可视化参考信号的 Bus，包括纵向和横向位移以及转向。

### **VehRef** — 车辆参考信号 `Bus`

包含车辆参考信号的 Bus，包括纵向和横向位移以及转向。

### **Fdbk** — 车辆位置反馈信号 `Bus`

包含车辆位移反馈信号的 Bus。

## 参数

### **Driver reference** — 启用外部驾驶员输入 `off`（默认）| `on`

指定以创建外部驾驶员参考输入端口 `ExtDrvRef`。

### **Driver commands** — 启用外部驾驶员命令 `off`（默认）| `on`

指定以创建外部驾驶员命令输入端口 `ExtDrvCmd`。

## 所属库

未在 R2025b 中记录。

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2024b 中引入**

## 描述

配置场景

Scenarios 模块实现驾驶员场景。该子系统包含变体，用于生成特定机动的驾驶员参考速度、路径和动作信号。选择 **Driver reference** 以输入外部驾驶员参考信号。选择 **Driver commands** 以输入外部驾驶员信号。

此外，您可以在运行时通过将工作区变量 `ExtDrvRefSwitch` 和 `ExtDrvCmdsSwitch` 设置为 `true` 或 `false` 来控制外部或内部生成的信号。当运行需要外部和内部机动的多个仿真，或覆盖标称模型生成的信号时，请考虑使用这些开关值。
