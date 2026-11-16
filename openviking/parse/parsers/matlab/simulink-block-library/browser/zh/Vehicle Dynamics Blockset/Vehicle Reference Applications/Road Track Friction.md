---
type: simulink-block
title: 'Road Track Friction'
family: 'vdynblks'
product_id: 'vdynblks'
product_name: 'Vehicle Dynamics Blockset'
documentation_release: R2025b
official_category: 'Vehicle Reference Applications'
documentation_page: 'roadtrackfriction'
documentation_source_path: 'ref/roadtrackfriction.html'
language: zh-CN
chinese_source: worker-translation
---

# Road Track Friction

## 端口

### 输入

### **XWhl** — 沿 X 轴的车轮位移 4-by-1 数组

沿地球固定 X 轴的车轮位移，指定为 4-by-1 数组。

### **YWhl** — 沿 Y 轴的车轮位移 4-by-1 数组

沿地球固定 Y 轴的车轮位移，指定为 4-by-1 数组。

### **Cg** — 车辆 CG 3-by-1 数组

车辆 cg，沿地球固定轴，指定为 3-by-1 数组。

### 输出

### **FricCoeffLambda** — 应用于车轮的摩擦系数 4-by-1 数组

车轮摩擦系数，指定为 4-by-1 数组。

## 参数

### **表面类型** — 摩擦 `Split friction coefficient scaling factor`（默认） | `Constant friction coefficient scaling factor`

- `Constant friction coefficient scaling factor` —
  操纵期间恒定的表面摩擦
- `Split friction coefficient scaling factor` — 两个
  摩擦系数

  选择此选项可为 split-mu 制动测试指定摩擦缩放系数。使用启用的参数设置地面摩擦和矩形表面摩擦系数缩放因子。

### **地面摩擦系数的缩放因子，lambda\_g** — 缩放因子 `.6`（默认） | `scalar`

地面摩擦系数的缩放因子。

### **矩形表面摩擦系数的缩放因子，lambda\_r** — 缩放因子 `.8`（默认） | `scalar`

矩形表面摩擦系数的缩放因子。

#### 依赖项

要启用此参数，请将 **表面/赛道类型** 设置为 `Split friction coefficient scaling factor`。

### **矩形表面左下角的 X 坐标，r\_x0** — X 坐标 `175`（默认） | `scalar`

矩形表面左下角的 X 坐标，位于地球固定坐标系中，单位为 m。

#### 依赖项

要启用此参数，请将 **表面/赛道类型** 设置为 `Split friction coefficient scaling factor`。

### **矩形表面左下角的 Y 坐标，r\_y0** — X 坐标 `-100`（默认） | `scalar`

矩形表面左下角的 Y 坐标，位于地球固定坐标系中。

#### 依赖项

要启用此参数，请将 **表面/赛道类型** 设置为 `Split friction coefficient scaling factor`。

### **矩形表面在 X 方向的宽度，r\_xw** — 矩形表面 `1000`（默认） | `scalar`

矩形表面在 X 方向的宽度，单位为 m。

#### 依赖项

要启用此参数，请将 **表面/赛道类型** 设置为 `Split friction coefficient scaling factor`。

### **矩形表面在 Y 方向的宽度，r\_yw** — 矩形表面 `500`（默认） | `scalar`

矩形表面在 Y 方向的宽度，单位为 m。

#### 依赖项

要启用此参数，请将 **表面/赛道类型** 设置为 `Split friction coefficient scaling factor`。

## 所属库

未在 R2025b 中记录。

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2021a 中引入**

## 描述

配置用于制动测试的道路

Road Track Friction 模块为制动测试实现道路，包括摩擦。使用 **表面类型** 参数指定摩擦系数缩放因子：

- `Constant friction coefficient scaling factor` — 操纵期间恒定的
  表面摩擦
- `Split friction coefficient scaling factor` — 两个摩擦
  系数

  选择此选项可为 split-mu 制动测试指定摩擦缩放系数。使用启用的参数设置地面摩擦和矩形表面摩擦系数缩放因子。
