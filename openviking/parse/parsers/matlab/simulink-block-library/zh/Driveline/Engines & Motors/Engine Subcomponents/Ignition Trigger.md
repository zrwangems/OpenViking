---
type: simulink-block
title: 'Ignition Trigger'
family: 'sdl'
product_id: 'sdl'
product_name: 'Driveline'
documentation_release: R2025b
official_category: 'Engines & Motors / Engine Subcomponents'
documentation_page: 'ignitiontrigger'
documentation_source_path: 'ref/ignitiontrigger.html'
language: zh-CN
chinese_source: worker-translation
---

# Ignition Trigger

## 端口

### 输入

### **Cam** — 曲轴位置，deg 物理信号

与 720 度循环中的曲轴位置相关联的物理信号输入。

### **Sw** — 点火器开关输入信号，二值物理信号

与点火器开关输入信号相关联的物理信号输入，其中 `0` 关闭点火器，`1` 打开点火器。

### **SA** — 点火提前角输入，deg 物理信号

与上止点前的点火提前角相关联的物理信号输入，单位为度。

### 输出

### **Trig** — 异步触发报告，二值物理信号

与该模块生成的异步火花触发事件相关联的物理信号输出，其中 `0` 关闭触发，`1` 打开触发。

## 参数

### **Number of cylinders** — 总气缸数 `Single Cylinder`（默认）| `Two Cylinders` | `Three Cylinders` | `Four Cylinders`

火花点火气缸的数量。

## 所属库

Simscape / Driveline / Engines & Motors / Engine Subcomponents

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2022a 中引入**

## 描述

火花点火式内燃机触发系统

Ignition Trigger 模块表示内燃机模型的抽象点火触发系统。该模块在端口 **SA** 接收点火提前角作为输入，并在曲轴位置越过点火提前角时在端口 **Trig** 生成异步事件触发输出。该模块忽略点火系统的动态特性。

将 Crankshaft 模块连接到 **Cam** 端口。
