---
type: simulink-block
title: '6DoF Animation'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Visualization / Animation Based on MATLAB'
documentation_page: '6dofanimation'
documentation_source_path: '6dofanimation.html'
language: zh-CN
chinese_source: worker-translation
---

# 6DoF Animation

## 端口

### 输入

### **xe** — 下射程位置、横程位置和高度（向下为正）三元素向量

飞行器的下射程位置、横程位置和高度（向下为正），指定为三元素向量。

**数据类型：** `double`

### **φ θ ψ** — 欧拉角三元素向量

飞行器的欧拉角，指定为三元素向量。

**数据类型：** `double`

## 参数

### **坐标轴范围 [xmin xmax ymin ymax zmin zmax]** — 坐标轴范围 `[0 4000 -2000 2000 -5000 -3000]`（默认）| 六元素向量

要查看的三维空间，指定为六元素向量。

#### 编程用法

|  |
| --- |
| **模块参数**: `u1` |
| **类型**: character vector |
| **值**: 六元素向量 |
| **默认值**: `'[0 4000 -2000 2000 -5000 -3000]'` |

### **更新之间的时间间隔** — 时间间隔 `0.1`（默认）| 标量

重绘动画的时间间隔，指定为 double scalar。

#### 编程用法

|  |
| --- |
| **模块参数**: `u2` |
| **类型**: character vector |
| **值**: double scalar |
| **默认值**: `'0.1'` |

### **显示的飞行器大小** — 缩放因子 `1.0`（默认）| 标量

用于调整飞行器和目标大小的缩放因子，指定为 double scalar。

#### 编程用法

|  |
| --- |
| **模块参数**: `u3` |
| **类型**: character vector |
| **值**: double scalar |
| **默认值**: `'1.0'` |

### **静态对象位置 [xp yp zp]** — 静态对象位置 `[4000 0 -5000]`（默认）| 三元素向量

目标的高度、横程位置和下射程位置，指定为三元素向量。

#### 编程用法

|  |
| --- |
| **模块参数**: `u4` |
| **类型**: character vector |
| **值**: 三元素向量 |
| **默认值**: `'[4000 0 -5000]'` |

### **进入视图** — 入口视图 `Fixed position`（默认）| `Cockpit` | `Fly alongside`

预设入口视图，指定为：

- `Fixed position`
- `Cockpit`
- `Fly alongside`

这些预设视图由图窗坐标轴的 MATLAB Graphics 参数 **CameraTarget** 和 **CameraUpVector** 指定。

**提示**

要自定义所选视图的位置和视场，请使用 **相机位置** 和 **视角** 参数。

#### 编程用法

|  |
| --- |
| **模块参数**: `u5` |
| **类型**: character vector |
| **值**: `Fixed position` | `Cockpit` | `Fly alongside` |
| **默认值**: `'Fixed position'` |

### **相机位置 [xc yc zc]** — 相机位置 `[2000 500 -3150]`（默认）| 三元素向量

相机位置，使用图窗坐标轴的 MATLAB Graphics 参数 CameraPosition 指定为三元素向量。除 **进入视图** 设置为 `Cockpit` 外，所有情况下均使用。

#### 编程用法

|  |
| --- |
| **模块参数**: `u6` |
| **类型**: character vector |
| **值**: 三元素向量 |
| **默认值**: `'[2000 500 -3150]'` |

### **视角** — 视角 `10`（默认）| 标量

图窗坐标轴的 MATLAB Graphics 参数 CameraViewAngle 的视角，以 degrees 为单位，指定为 double scalar。

#### 编程用法

|  |
| --- |
| **模块参数**: `u7` |
| **类型**: character vector |
| **值**: double scalar |
| **默认值**: `'10'` |

### **启用动画** — 显示动画 `on`（默认）| `off`

是否在仿真期间显示动画。如果未选中，则不显示动画。

#### 编程用法

|  |
| --- |
| **模块参数**: `u8` |
| **类型**: character vector |
| **值**: `on` | `off` |
| **默认值**: `'on'` |

## 所属库

Aerospace Blockset / Animation / MATLAB-Based Animation

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前引入**

## 描述

创建六自由度对象的三维 MATLAB Graphics 动画

6DoF Animation 模块使用 MATLAB® Graphics 显示六自由度 (6DoF) 飞行器、其轨迹及其目标的三维动画视图。

6DoF Animation 模块使用输入值和模块参数创建并显示动画。**坐标轴范围**、**静态对象位置** 和 **相机位置** 参数的长度单位与输入参数相同。

此模块不生成可部署代码，但您可以将其与 Simulink® Coder™ 外部模式一起用作 SimViewingDevice。
