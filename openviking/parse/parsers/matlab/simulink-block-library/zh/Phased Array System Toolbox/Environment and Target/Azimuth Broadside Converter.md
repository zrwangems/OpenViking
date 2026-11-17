---
type: simulink-block
title: 'Azimuth Broadside Converter'
family: 'environment-and-target'
product_id: 'phased'
product_name: 'Phased Array System Toolbox'
documentation_release: R2025b
official_category: 'Environment and Target'
documentation_page: 'azimuthbroadsideconverter'
documentation_source_path: 'ref/azimuthbroadsideconverter.html'
language: zh-CN
chinese_source: worker-translation
---

# Azimuth Broadside Converter

## 端口

### 输入

### **az** — 方位角 标量 | 实数值向量

方向的方位角，指定为标量或实数值向量。单位为 degrees。当 `az` 为向量时，`az` 和 `el` 的维度必须匹配。

#### 依赖项

要启用此端口，请将 **Conversion Mode** 设置为 **azimuth -> broadside**。

**Data Types:** `double`

### **bsd** — 侧射角 标量 | 实数值向量

方向的侧射角，指定为标量或实数值向量。单位为 degrees。当 `bsd` 为向量时，`bsd` 和 `el` 的维度必须匹配。

#### 依赖项

要启用此端口，请将 **Conversion Mode** 设置为 **broadside -> azimuth**。

**Data Types:** `double`

### **el** — 俯仰角 标量 | 实数值向量

方向的俯仰角，指定为标量或实数值向量。单位为 degrees。`el` 的维度必须与 `az` 和 `bsd` 的维度匹配。

**Data Types:** `double`

### 输出

### **az** — 方位角 标量 | 实数值向量

方向的方位角，返回为标量或实数值向量。单位为 degrees。

#### 依赖项

要启用此端口，请将 **Conversion Mode** 设置为 **broadside -> azimuth**。

**Data Types:** `double`

### **bsd** — 侧射角 标量 | 实数值向量

方向的侧射角，返回为标量或实数值向量。单位为 degrees。

#### 依赖项

要启用此端口，请将 **Conversion Mode** 设置为 **azimuth -> broadside**。

**Data Types:** `double`

## 参数

### **Conversion mode** — 角度转换类型 **broadside -> azimuth**（默认）| **azimuth -> broadside**

角度转换类型，指定为

|  |  |
| --- | --- |
| **broadside -> azimuth** | 将以侧射角和俯仰角表示的方向转换为方位角和俯仰角。 |
| **azimuth -> broadside** | 将以方位角和俯仰角表示的方向转换为侧射角和俯仰角。 |

## 所属库

Phased Array System Toolbox / Environment and Target

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2014b 中引入**

## 描述

将方位角转换为侧射角，或将侧射角转换为方位角

Azimuth Broadside Converter 模块将按侧射角表示的角度方向转换为等效方位角，或将方位角转换为等效侧射角。在这两种情况下，都必须指定俯仰角。
