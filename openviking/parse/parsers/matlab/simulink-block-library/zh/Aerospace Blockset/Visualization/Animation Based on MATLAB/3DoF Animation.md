---
type: simulink-block
title: '3DoF Animation'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Visualization / Animation Based on MATLAB'
documentation_page: '3dofanimation'
documentation_source_path: '3dofanimation.html'
language: zh-CN
chinese_source: worker-translation
---

# 3DoF Animation

## 端口

### 输入

### **xtzt** — 目标下靶程位置和高度（向下为正）二元向量

目标的下靶程位置和高度（向下为正），指定为二元向量。

**数据类型：** `double`

### **xeze** — 飞行器下靶程位置和高度（向下为正）二元向量

飞行器的下靶程位置和高度（向下为正），指定为二元向量。

**数据类型：** `double`

### **θ** — 飞行器姿态 1×1 标量

飞行器的姿态，指定为 1×1 标量，单位为 radians。

**数据类型：** `double`

## 参数

### **坐标轴范围 [xmin xmax ymin ymax zmin zmax]** — 坐标轴范围 `[0 5000 -2000 2000 -5050 -3050]`（默认）| 六元素向量

要查看的三维空间，指定为六元素向量。

#### 程序化用法

|  |
| --- |
| **模块参数**: `u1` |
| **类型**: character vector |
| **值**: 六元素向量 |
| **默认值**: `'[0 5000 -2000 2000 -5050 -3050]'` |

### **更新之间的时间间隔** — 时间间隔 `0.05`（默认）| 标量

重绘动画的时间间隔，指定为 double 标量。

#### 程序化用法

|  |
| --- |
| **模块参数**: `u2` |
| **类型**: character vector |
| **值**: double scalar |
| **默认值**: `'0.05'` |

### **显示的飞行器大小** — 比例因子 `1.0`（默认）| 标量

用于调整飞行器和目标大小的比例因子，指定为 double 标量。

#### 程序化用法

|  |
| --- |
| **模块参数**: `u3` |
| **类型**: character vector |
| **值**: double scalar |
| **默认值**: `'1.0'` |

### **进入视图** — 入口视图 `Fixed position`（默认）| `Cockpit` | `Fly alongside`

预设入口视图，指定为：

- `Fixed position`
- `Cockpit`
- `Fly alongside`

这些预设视图由图窗坐标轴的 MATLAB Graphics 参数 **CameraTarget** 和 **CameraUpVector** 指定。

**提示**

要自定义所选视图的位置和视野，请使用 **相机位置** 和 **视角** 参数。

#### 程序化用法

|  |
| --- |
| **模块参数**: `u5` |
| **类型**: character vector |
| **值**: `Fixed position` | `Cockpit` | `Fly alongside` |
| **默认值**: `'Fixed position'` |

### **相机位置 [xc yc zc]** — 相机位置 `[2000 500 -3150]`（默认）| 三元素向量

相机位置，使用图窗坐标轴的 MATLAB Graphics 参数 CameraPosition 指定为三元素向量。用于除 Cockpit 视图之外的所有情况。

#### 程序化用法

|  |
| --- |
| **模块参数**: `u6` |
| **类型**: character vector |
| **值**: 三元素向量 |
| **默认值**: `'[2000 500 -3150]'` |

### **视角** — 视角 `10`（默认）| 标量

视角，使用图窗坐标轴的 MATLAB Graphics 参数 CameraViewAngle 以 degrees 为单位指定为 double 标量。

#### 程序化用法

|  |
| --- |
| **模块参数**: `u7` |
| **类型**: character vector |
| **值**: double scalar |
| **默认值**: `'10'` |

### **启用动画** — 显示动画 `on`（默认）| `off`

要在仿真期间显示动画，请选中此复选框。如果未选中，则不显示动画。

#### 程序化用法

|  |
| --- |
| **模块参数**: `u8` |
| **类型**: character vector |
| **值**: `on` | `off` |
| **默认值**: `'on'` |

## 所属库

Aerospace Blockset / Animation / MATLAB-Based Animation

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前引入**

## 描述

创建三自由度对象的三维 MATLAB Graphics 动画

3DoF Animation 模块使用 MATLAB® Graphics 显示三自由度（3DoF）飞行器、其轨迹及其目标的三维动画视图。

3DoF Animation 模块使用输入值和对话框参数来创建并显示动画。

此模块不生成可部署代码，但您可以将其作为 SimViewingDevice 与 Simulink® Coder™ 外部模式一起使用。
