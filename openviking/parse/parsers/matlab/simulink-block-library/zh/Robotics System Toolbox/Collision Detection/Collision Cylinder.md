---
type: simulink-block
title: 'Collision Cylinder'
family: 'robotics'
product_id: 'robotics'
product_name: 'Robotics System Toolbox'
documentation_release: R2025b
official_category: 'Collision Detection'
documentation_page: 'collisioncylinderblock'
documentation_source_path: 'ref/collisioncylinderblock.html'
language: zh-CN
chinese_source: worker-translation
---

# Collision Cylinder

## 端口
```yaml
ports:
- name: Radius
  summary: 圆柱半径 标量
  direction: input
- name: Length
  summary: 圆柱长度 标量
  direction: input
- name: Pose
  summary: 碰撞几何体的位姿 矩阵
  direction: input
- name: CollGeom
  summary: 碰撞几何体 总线
  direction: output
- name: ExitFlag
  summary: 碰撞圆柱尺寸的有效性 标量
  direction: output
  data_types: uint16
```

### 输入

### **Radius** — 圆柱半径 标量

圆柱的半径，指定为正标量。单位为米。

### **Length** — 圆柱长度 标量

圆柱的长度，指定为非负标量。单位为米。

### **Pose** — 碰撞几何体的位姿 矩阵

碰撞几何体相对于世界坐标系的位姿，指定为 4×4 齐次矩阵。

### 输出

### **CollGeom** — 碰撞几何体 总线

碰撞几何体，以总线形式返回。

要执行碰撞检测，请将此输出连接到 Check Collision 模块作为输入。

### **ExitFlag** — 碰撞圆柱尺寸的有效性 标量

碰撞圆柱尺寸的有效性，以整数标量形式返回，其中每一位数字表示一个维度的有效性：

- **第一位数字** — **Radius** 端口处半径的有效性。
- **第二位数字** — **Length** 端口处长度的有效性。

这些数字中的每一个可以是以下值之一：

- `4` — 指定的维度值不是数值。
- `3` — 指定的维度值不是实数。
- `2` — 指定的维度值非有限。
- `1` — 指定的半径不是正数，或指定的长度为负数。
- `0` — 指定的维度值有效。

例如，如果 exit flag 为 `10`，则圆柱的半径无效，因为它不是正数。

要在运行时验证尺寸，请选择 **Enable Runtime Input Dimensions Error** 参数。

**数据类型：** `uint16`
## 参数
```yaml
parameters:
- name: Enable Runtime Input Dimensions Error
  summary: 碰撞圆柱尺寸的验证 on（默认）| off
  group: ''
- name: Simulate using
  summary: 要运行的仿真类型 Code generation（默认）| Interpreted execution
  group: ''
```

要以交互方式编辑模块参数，请使用 Property Inspector。在 Simulink® 工具条的 **Simulation** 选项卡上，在 **Prepare** 库中，选择 **Property Inspector**。

### **Enable Runtime Input Dimensions Error** — 碰撞圆柱尺寸的验证 `on`（默认）| `off`

选择此参数以启用碰撞圆柱尺寸的运行时验证，并在 **Radius** 或 **Length** 无效时返回错误。

如果清除此参数，模块在仿真期间不会报错，而是使用 **ExitFlag** 端口来标识无效的圆柱尺寸。

### **Simulate using** — 要运行的仿真类型 `Code generation`（默认）| `Interpreted execution`

- `Code generation` — 使用生成的 C 代码仿真模型。首次运行仿真时，Simulink 会为该模块生成 C 代码。只要模型不变，该模块会在后续仿真中重用该 C 代码。
- `Interpreted execution` — 使用 MATLAB® 解释器仿真模型。有关详细信息，请参阅 Interpreted Execution vs. Code Generation (Simulink)。
## 所属库

Robotics System Toolbox / Collision Detection

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

Collision Cylinder 模块支持在禁用动态内存分配的情况下进行代码生成。有关禁用动态内存分配的详细信息，请参阅 Dynamic memory allocation in MATLAB functions (Simulink)。

## 版本历史

**在 R2025a 中引入**

## 描述

创建圆柱碰撞几何体

Collision Cylinder 模块输出一个圆柱碰撞几何体，该几何体与其体坐标系的 *z* 轴对齐，并且体坐标系的原点位于圆柱的中心。
