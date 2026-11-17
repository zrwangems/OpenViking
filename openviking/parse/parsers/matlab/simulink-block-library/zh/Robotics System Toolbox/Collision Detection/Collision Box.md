---
type: simulink-block
title: 'Collision Box'
family: 'robotics'
product_id: 'robotics'
product_name: 'Robotics System Toolbox'
documentation_release: R2025b
official_category: 'Collision Detection'
documentation_page: 'collisionboxblock'
documentation_source_path: 'ref/collisionboxblock.html'
language: zh-CN
chinese_source: worker-translation
---

# Collision Box

## 端口
```yaml
ports:
- name: X
  summary: 沿 *x* 轴的盒几何体长度 标量
  direction: input
- name: Y
  summary: 沿 *y* 轴的盒几何体长度 标量
  direction: input
- name: Z
  summary: 沿 *z* 轴的盒几何体长度 标量
  direction: input
- name: Pose
  summary: 碰撞几何体的位姿 矩阵
  direction: input
- name: CollGeom
  summary: 碰撞几何体 总线
  direction: output
- name: ExitFlag
  summary: 碰撞盒尺寸的有效性 标量
  direction: output
  data_types: uint16
```

### 输入

### **X** — 沿 *x* 轴的盒几何体长度 标量

盒几何体沿 *x* 轴的边长，指定为正标量。单位为米。

### **Y** — 沿 *y* 轴的盒几何体长度 标量

盒几何体沿 *y* 轴的边长，指定为正标量。单位为米。

### **Z** — 沿 *z* 轴的盒几何体长度 标量

盒几何体沿 *z* 轴的边长，指定为正标量。单位为米。

### **Pose** — 碰撞几何体的位姿 矩阵

碰撞几何体相对于世界坐标系的位姿，指定为 4×4 齐次矩阵。

### 输出

### **CollGeom** — 碰撞几何体 总线

碰撞几何体，以总线形式返回。

要执行碰撞检测，请将此输出连接到 Check Collision 模块作为输入。

### **ExitFlag** — 碰撞盒尺寸的有效性 标量

碰撞盒尺寸的有效性，以整数标量形式返回，其中每一位数字表示一个维度的有效性：

- **第一位数字** — **X** 端口处 *x* 轴长度的有效性。
- **第二位数字** — **Y** 端口处 *y* 轴长度的有效性。
- **第三位数字** — **Z** 端口处 *z* 轴长度的有效性。

这些数字中的每一个可以是以下值之一：

- `4` — 指定的维度值不是数值。
- `3` — 指定的维度值不是实数。
- `2` — 指定的维度值是非有限值。
- `1` — 指定的维度值不是正数。
- `0` — 指定的维度值是有效的。

例如，如果 exit flag 为 `230`，则盒的 *x* 长度为非有限值，*y* 长度不是实数值，*z* 长度是有效的。

要在运行时验证维度，请选择 **Enable Runtime Input Dimensions Error** 参数。

**数据类型：** `uint16`
## 参数
```yaml
parameters:
- name: Enable Runtime Input Dimensions Error
  summary: 碰撞盒尺寸的验证 on（默认）| off
  group: ''
- name: Simulate using
  summary: 要运行的仿真类型 Code generation（默认）| Interpreted execution
  group: ''
```

要以交互方式编辑模块参数，请使用 Property Inspector。在 Simulink® 工具条的 **Simulation** 选项卡上，在 **Prepare** 库中，选择 **Property Inspector**。

### **Enable Runtime Input Dimensions Error** — 碰撞盒尺寸的验证 `on`（默认）| `off`

选择此参数以启用碰撞盒尺寸的运行时验证，并在 **X**、**Y** 或 **Z** 无效时返回错误。

如果清除此参数，模块在仿真期间不会报错，而是使用 **ExitFlag** 端口来标识无效的盒尺寸。

### **Simulate using** — 要运行的仿真类型 `Code generation`（默认）| `Interpreted execution`

- `Code generation` — 使用生成的 C 代码仿真模型。首次运行仿真时，Simulink 会为该模块生成 C 代码。只要模型不变，该模块会在后续仿真中重用该 C 代码。
- `Interpreted execution` — 使用 MATLAB® 解释器仿真模型。有关详细信息，请参阅 Interpreted Execution vs. Code Generation (Simulink)。
## 所属库

Robotics System Toolbox / Collision Detection

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

Collision Box 模块支持在禁用动态内存分配的情况下进行代码生成。有关禁用动态内存分配的详细信息，请参阅 Dynamic memory allocation in MATLAB functions (Simulink)。

## 版本历史

**在 R2025a 中引入**

## 描述

创建盒碰撞几何体

Collision Box 模块输出一个盒碰撞几何体，该几何体与其体固定坐标系轴对齐，并且体固定坐标系的原点位于盒的中心。
