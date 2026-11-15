---
type: simulink-block
title: 'Direction Cosine Matrix ECEF to NED'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Standard Workflow Procedures / Coordinate Systems / Axes Transformations / Geodetic Transformations'
documentation_page: 'directioncosinematrixeceftoned'
documentation_source_path: 'directioncosinematrixeceftoned.html'
language: zh-CN
chinese_source: worker-translation
---

# Direction Cosine Matrix ECEF to NED

## 端口

### 输入

### **μl** — 大地纬度和经度 2×1 向量

大地纬度和经度，指定为 2×1 向量，以 degrees 为单位。纬度和经度值可以是任意值。但是，由于极点处的奇异性，纬度值 +90 和 -90 可能返回意外值。

**数据类型：** `double`
### 输出

### **DCMef** — 方向余弦矩阵 3×3 矩阵

DCM，用于将 ECEF 轴中的向量坐标变换为 NED 轴中的向量，以 3×3 矩阵返回。

**数据类型：** `double`

## 参数

R2025b 中未记录。

## 所属库

Aerospace Blockset / Utilities / Axes Transformations

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**R2006a 之前引入**

## 描述

将大地纬度和经度转换为方向余弦矩阵

Direction Cosine Matrix ECEF to NED 模块将大地纬度和经度转换为 3×3 方向余弦矩阵 (DCM)。该 DCM 矩阵执行将地心地球固连 (ECEF) 轴中的向量转换为北-东-地 (NED) 轴中的向量的坐标变换。有关方向余弦矩阵的详细信息，请参阅算法。

ECEF 坐标系的实现假设原点位于行星中心，*x* 轴与格林尼治子午线和赤道相交，*z* 轴是行星的平均自转轴，正向朝北，*y* 轴构成右手系统。有关详细信息，请参阅 ECI 和 ECEF 坐标。
