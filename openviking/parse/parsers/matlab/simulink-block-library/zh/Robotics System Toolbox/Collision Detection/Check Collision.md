---
type: simulink-block
title: 'Check Collision'
family: 'robotics'
product_id: 'robotics'
product_name: 'Robotics System Toolbox'
documentation_release: R2025b
official_category: 'Collision Detection'
documentation_page: 'checkcollisionblock'
documentation_source_path: 'ref/checkcollisionblock.html'
language: zh-CN
chinese_source: worker-translation
---

# Check Collision

## 端口
```yaml
ports:
- name: Geom1
  summary: 要检查的第一个碰撞几何体 bus
  direction: input
- name: Geom2
  summary: 要检查的第二个碰撞几何体 bus
  direction: input
- name: CollStatus
  summary: 碰撞状态 标量
  direction: output
- name: SepDist
  summary: 碰撞几何体之间的最小距离 标量
  direction: output
- name: WitnessPts
  summary: 每个几何体上的见证点 矩阵
  direction: output
```

### 输入

### **Geom1** — 要检查的第一个碰撞几何体 bus

第一个碰撞几何体，指定为由以下任意碰撞几何体模块创建的 bus：

- Collision
  Box
- Collision
  Capsule
- Collision
  Cylinder
- Collision
  Mesh
- Collision
  Sphere

### **Geom2** — 要检查的第二个碰撞几何体 bus

第二个碰撞几何体，指定为由以下任意碰撞几何体模块创建的 bus：

- Collision
  Box
- Collision
  Capsule
- Collision
  Cylinder
- Collision
  Mesh
- Collision
  Sphere
### 输出

### **CollStatus** — 碰撞状态 标量

碰撞状态，返回为布尔值 `0` 或
`1`。如果两个几何体发生碰撞，
**CollStatus** 输出 `1`。否则，该值为
`0`。

### **SepDist** — 碰撞几何体之间的最小距离 标量

两个碰撞几何体之间的最小距离，返回为标量。连接见证点 **WitnessPts** 的线段确定了两个几何体之间的最小距离。当两个几何体发生碰撞时，
**SepDist** 输出 `NaN`。

### **WitnessPts** — 每个几何体上的见证点 矩阵

每个几何体上的见证点，返回为 3×2 矩阵。第一列是几何体 **Geom1** 上见证点的位置，第二列是另一个几何体 **Geom2** 上见证点的位置。连接两个见证点的线段长度决定了 **SepDist** 端口的值。当两个几何体发生碰撞时，
**WitnessPts** 的每个元素均为 `NaN`。
## 参数
```yaml
parameters:
- name: Simulate using
  summary: 要运行的仿真类型 Code generation（默认）| Interpreted execution
  group: ''
```

要以交互方式编辑模块参数，请使用
Property Inspector。在 Simulink® 工具条的 **Simulation** 选项卡上，在
**Prepare** 库中，选择 **Property
Inspector**。

### **Simulate using** — 要运行的仿真类型 `Code generation`（默认）| `Interpreted execution`

- `Code generation` — 使用生成的 C 代码仿真模型。首次运行仿真时，Simulink 会为该模块生成 C 代码。只要模型不发生变化，该模块会在后续仿真中重用该 C 代码。
- `Interpreted execution` — 使用 MATLAB® 解释器仿真模型。有关详细信息，请参阅 Interpreted Execution vs. Code Generation (Simulink)。
## 所属库

Robotics System Toolbox / Collision Detection

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

Check Collision 模块支持在禁用动态内存分配的情况下进行代码生成。有关禁用动态内存分配的详细信息，请参阅 Dynamic memory allocation in MATLAB functions (Simulink)。

## 版本历史

**在 R2025a 中引入**

## 描述

检查两个凸碰撞几何体是否发生碰撞

Check Collision 模块检查两个凸碰撞几何体之间的碰撞，并额外输出碰撞几何体之间的分离距离和相应的见证点。
