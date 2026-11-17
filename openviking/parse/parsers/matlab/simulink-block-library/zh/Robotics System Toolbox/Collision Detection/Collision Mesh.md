---
type: simulink-block
title: 'Collision Mesh'
family: 'robotics'
product_id: 'robotics'
product_name: 'Robotics System Toolbox'
documentation_release: R2025b
official_category: 'Collision Detection'
documentation_page: 'collisionmeshblock'
documentation_source_path: 'ref/collisionmeshblock.html'
language: zh-CN
chinese_source: worker-translation
---

# Collision Mesh

## 端口

### 输入

### **Vertices** — 网格顶点矩阵

网格的顶点，指定为 *N*×3 矩阵，其中 *N* 是顶点数，必须大于或等于 1。
**Vertices** 的每一行表示三维空间中一个点的坐标。
注意，其中一些点可以位于所构造的凸网格内部。

### **Pose** — 碰撞几何体的位姿矩阵

碰撞几何体相对于世界坐标系的位姿，指定为 4×4 齐次矩阵。
### 输出

### **CollGeom** — 碰撞几何体总线

碰撞几何体，以总线形式返回。

要执行碰撞检测，请将此输出作为输入连接到 Check Collision 模块。

### **ExitFlag** — 碰撞网格顶点有效性标量

碰撞网格顶点的有效性，返回为以下值之一：

- `4` — Vertices 矩阵包含非数值。
- `3` — Vertices 矩阵包含非实数
  值。
- `2` — Vertices 矩阵包含非有限值。
- `1` — Vertices 矩阵没有三列。
- `0` — 顶点有效。

要在运行时验证顶点，请选择 **Enable
Runtime Input Dimensions Error** 参数。

**数据类型：** `uint16`

## 参数

要以交互方式编辑模块参数，请使用
Property Inspector。在 Simulink® 工具条的 **Simulation** 选项卡上，在
**Prepare** 库中，选择 **Property
Inspector**。

### **Enable Runtime Input Dimensions Error** — 碰撞网格顶点验证 `on`（默认）| `off`

选择此参数以启用碰撞网格顶点的运行时验证，并在 **Vertices** 无效时返回错误。

如果清除此参数，模块在仿真期间不会报错，而是使用 **ExitFlag** 端口来标识无效的网格顶点。

### **Simulate using** — 要运行的仿真类型 `Code generation`（默认）| `Interpreted execution`

- `Code generation` — 使用生成的 C 代码仿真模型。首次运行仿真时，Simulink 会为该模块生成 C 代码。只要模型不变，该模块会在后续仿真中重用该 C 代码。
- `Interpreted execution` — 使用 MATLAB® 解释器仿真模型。有关详细信息，请参阅 Interpreted Execution vs. Code Generation (Simulink)。

## 所属库

Robotics System Toolbox / Collision Detection

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

Collision Mesh 模块支持在禁用动态内存分配的情况下进行代码生成。有关禁用动态内存分配的详细信息，请参阅 Dynamic memory allocation in MATLAB functions (Simulink)。

## 版本历史

**在 R2025a 中引入**

## 描述

创建凸网格碰撞几何体

Collision Mesh 模块使用相对于世界坐标系中指定位姿的三维顶点列表输出凸网格碰撞几何体。
