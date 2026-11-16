---
type: simulink-block
title: '5x5 LED Matrix'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / BBC micro:bit / Modeling / LED'
documentation_page: '5x5ledmatrix'
documentation_source_path: 'microbit/ref/5x5ledmatrix.html'
language: zh-CN
chinese_source: worker-translation
---

# 5x5 LED Matrix

## 端口

### 输入

### **Matrix** — 输入信号矩阵

该端口接受一个 5x5 矩阵，其中所有元素均为 `0` 或 `1`。当元素值大于 0 时，对应的 LED 点亮。否则，它会熄灭。

**数据类型：** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `single` | `double`

## 参数

R2025b 中未记录。

## 所属库

Simulink Coder Support Package for BBC micro:bit/ LED

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2018a 中引入**

## 描述

在开发板上输出 5x5 LED 图像

5x5 LED Matrix 模块在开发板上的内置 5x5 LED 矩阵上输出 5x5 LED 图像。该模块有一个输入端口 Matrix。Matrix 端口接受一个 5x5 矩阵，其中所有元素均为 `0` 或 `1`。

### 使用 5x5 LED Matrix

BBC micro:bit 使用 x、y 坐标来标识 5x5 矩阵中的特定 LED。坐标从矩阵左上角的 `0` 开始。

将开发板水平放置在桌面上，LED 朝上。水平线表示 x 坐标，垂直线表示 y 坐标。

假设您将值为 `[1 0 0 0 1;0 1 0 1 0;0 0 1 0 0;0 1 0 1 0;1 0 0 0 1]` 的矩阵作为输入发送到该模块。所有值为 `1` 的元素对应的 LED 都会点亮。
