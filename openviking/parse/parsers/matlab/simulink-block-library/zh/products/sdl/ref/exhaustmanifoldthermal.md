---
type: simulink-block
title: 'Exhaust Manifold Thermal'
family: 'sdl'
product_id: 'sdl'
product_name: 'Simscape Driveline'
documentation_release: R2025b
official_category: 'Engines & Motors / Engine Subcomponents'
documentation_page: 'exhaustmanifoldthermal'
documentation_source_path: 'ref/exhaustmanifoldthermal.html'
language: zh-CN
chinese_source: worker-translation
---

# Exhaust Manifold Thermal

## 端口

### 输入

### **Qeng** — 气体能量流，W 物理信号

与气体能量流关联的物理信号输入端口，单位为 W。将此端口连接到 SI Combustion Cylinder 模块上的 **Weo** 物理信号输出端口。
### 输出

### **Texh** — 排气歧管温度，K 物理信号

与集总参数排气歧管温度关联的物理信号输出端口，单位为 K。

## 参数

### **排气端口数量** — 排气端口数量 `1`（默认） | 正标量

SI Combustion Cylinder 模块的数量。

### **环境温度** — 参考温度 `298.15` `K`（默认） | 正标量

进入进气口的空气温度。

### **排气壁表面积** — 排气壁表面积 `pi * ((1.5 / 2) ^ 2)` `m^2`（默认） | 正标量

排气壁的表面积。
这只是与排气接触的内壁表面积。

### **排气壁质量** — 排气壁总质量 `5` `kg`（默认） | 正标量

排气壁的质量。

### **排气壁热容** — 排气壁热容 `100` `J/(K*kg)`（默认） | 正标量

排气壁的热容。

### **排气热流时间常数** — 排气热流时间常数 `10` `s`（默认） | 正标量

排气热流速率的时间常数。

### **排气外侧对流换热系数** — 排气外部对流换热系数 `100` `W/(K*m^2)`（默认） | 正标量

排气外侧的对流换热系数。

### **辐射常数** — 排气辐射常数 `0.3`（默认） | 正标量

排气的辐射常数。

### **Stefan-Boltzmann 常数** — 排气 Stefan-Boltzmann 常数 `5.7e-8` `W/(K^4*m^2)`（默认） | 正标量

总排气的 Stefan-Boltzmann 常数。

## 所属库

Simscape / Driveline / Engines & Motors / Engine Subcomponents

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2022a 中引入**

## 描述

内燃机排气歧管热力学

Exhaust Manifold Thermal 模块表示内燃机排气歧管的抽象热力学。该模块与 SI Combustion Cylinder 模块集成。

### 方程

该模块从 SI Combustion Cylinder 模块获取排气气体流量，并计算排气歧管温度 *Texh*，该模块在端口 **Texh** 输出此温度。该模块使用集总参数模型计算输出，使得

CexhMexhddtTexh=hexh−hx,

其中

- *Cexh* 是 **排气壁热容** 参数。
- *Mexh* 是 **排气壁质量** 参数。
- *hexh* 是排气歧管处的热流。
- *hx* 是排气气体与环境之间的热交换。

该模块按如下方式计算 *hx*：

hx=Sexh(hconvec(Texh−Tamb)−kraσ(Texh4−Tamb4)),

其中

- *Sexh* 是 **排气壁表面积** 参数。
- *hconvec* 是 **排气外侧对流换热系数** 参数。
- *kra* 是 **辐射常数** 参数。
- *σ* 是 **Stefan-Boltzmann 常数** 参数。
- *Tamb* 是 **环境温度** 参数。

该模块按如下方式求得 *hexh*：

kgasddthexh=hin−hexh,

其中 *kgas* 是 **排气热流时间常数** 参数，*hin* 是从发动机排气出口到排气歧管的瞬时热流。瞬时热流是排气出口处各个瞬时热流 *hi* 的总和，使得

hin=∑i=1Nportshi,

其中 *Nports* 是 **排气端口数量** 参数。
