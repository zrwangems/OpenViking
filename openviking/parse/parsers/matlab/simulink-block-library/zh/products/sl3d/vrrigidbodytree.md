---
type: simulink-block
title: 'VR RigidBodyTree'
family: 'sl3d'
product_id: 'sl3d'
product_name: 'Simulink 3D Animation'
documentation_release: R2025b
official_category: 'Classic Virtual Reality World'
documentation_page: 'vrrigidbodytree'
documentation_source_path: 'vrrigidbodytree.html'
language: zh-CN
chinese_source: worker-translation
---

# VR RigidBodyTree

## 端口

### 输入

### **Input 1** — Joint Positions 标量 | 向量

求解所需末端执行器位姿的机器人配置，指定为向量。机器人配置是 `rigidBodyTree` 模型的关节位置向量。位置数等于 `rigidBodyTree` 参数中非固定关节的数量。

**数据类型：** `single` | `double`

## 参数

### **关联 VRML 文件** — 3D World 3D 世界文件名

指定要在其中可视化 `rigidBodyTree` 的虚拟世界

### **父节点（对于根节点留空）** — 场景层次结构位置 character vector | string

指定 `rigidBodyTree` 对象在场景层次结构中的位置。

### **刚体树** — 机器人位姿 `rigidBodyTree`

指定要在虚拟世界中使用的 Robotics System Toolbox `rigidBodyTree` 对象的名称。如果虚拟世界中已存在同名机器人，则默认使用该机器人进行可视化。

您可以启用 **始终使用 RigidBodyTree 对象中的机器人定义** 参数，以使用 `rigidBodyTree` 对象指定的机器人覆盖现有机器人（如果存在）。

### **始终使用 RigidBodyTree 对象中的机器人定义** — 创建机器人 `‘off’`（默认） | `’on’`

启用此参数可始终根据 **刚体树** 参数指定的 `rigidBodyTree` 对象创建机器人。

默认情况下，如果存在同名机器人，虚拟世界会使用该现有机器人。

### **采样时间** — 用于仿真的模块采样时间 0.1（默认） | 标量 | 向量

指定模块的采样时间，或指定 `-1` 以继承采样时间。

### **确保仿真期间查看器窗口处于打开状态** — 打开 3D 世界查看器 `‘off’`（默认） | `’on’`

启用此参数可确保仿真期间 Simulink 3D Animation Viewer 处于打开状态。

## 所属库

Simulink 3D Animation

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

实际的数据类型或功能支持取决于模块实现。

## 版本历史

**在 R2018b 中引入**

### R2025a: 警告

`VR RigidBodyTree` 模块将在未来版本中移除。Simulink 3D Animation Viewer 已被移除，因此 `VR RigidBodyTree` 不会打开虚拟世界。有关替代功能，请参阅将虚拟现实世界过渡到 Unreal Engine 3D 环境。

### R2023b: 将被移除

`VR RigidBodyTree` 运行时不会发出警告，并将在未来版本中移除。

## 描述

（将被移除）在 Simulink 中可视化 Robotics System Toolbox rigidBodyTree 对象

使用 VR RigidBodyTree 模块在 Simulink® 3D Animation™ 查看器中可视化来自 Robotics System Toolbox™ 的 `rigidBodyTree` 对象。
