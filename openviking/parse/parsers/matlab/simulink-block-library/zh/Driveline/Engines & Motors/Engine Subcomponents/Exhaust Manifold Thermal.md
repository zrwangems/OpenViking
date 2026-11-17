---
type: simulink-block
title: 'Exhaust Manifold Thermal'
family: 'sdl'
product_id: 'sdl'
product_name: 'Driveline'
documentation_release: R2025b
official_category: 'Engines & Motors / Engine Subcomponents'
documentation_page: 'exhaustmanifoldthermal'
documentation_source_path: 'ref/exhaustmanifoldthermal.html'
language: zh-CN
chinese_source: worker-translation
---

# Exhaust Manifold Thermal

## 端口
```yaml
ports:
- name: Qeng
  summary: 气体能量流，W 物理信号
  direction: input
- name: Texh
  summary: 排气歧管温度，K 物理信号
  direction: output
```

### 输入

### **Qeng** — 气体能量流，W 物理信号

与气体能量流相关联的物理信号输入端口，单位为 W。将此端口连接到 SI Combustion Cylinder 模块上的 **Weo** 物理信号输出端口。
### 输出

### **Texh** — 排气歧管温度，K 物理信号

与集总参数排气歧管温度相关联的物理信号输出端口，单位为 K。
## 参数
```yaml
parameters:
- name: Number of exhaust ports
  summary: 排气端口数量 1（默认）| 正标量
  group: ''
- name: Ambient temperature
  summary: 参考温度 298.15 K（默认）| 正标量
  group: ''
- name: Surface area of exhaust wall
  summary: 排气壁表面积 pi * ((1.5 / 2) ^ 2) m^2（默认）| 正标量
  group: ''
- name: Mass of exhaust wall
  summary: 排气壁总质量 5 kg（默认）| 正标量
  group: ''
- name: Heat capacity of exhaust wall
  summary: 排气壁热容量 100 J/(K*kg)（默认）| 正标量
  group: ''
- name: Time constant of exhaust heat flow
  summary: 排气热流时间常数 10 s（默认）| 正标量
  group: ''
- name: Convective heat transfer coefficient for the outer side of exhaust
  summary: 排气外侧对流换热系数 100 W/(K*m^2)（默认）| 正标量
  group: ''
- name: Radiation constant
  summary: 排气辐射常数 0.3（默认）| 正标量
  group: ''
- name: Stefan-Boltzmann constant
  summary: 排气 Stefan-Boltzmann 常数 5.7e-8 W/(K^4*m^2)（默认）| 正标量
  group: ''
```

### **Number of exhaust ports** — 排气端口数量 `1`（默认）| 正标量

SI Combustion Cylinder 模块的数量。

### **Ambient temperature** — 参考温度 `298.15` `K`（默认）| 正标量

进入进气口的空气温度。

### **Surface area of exhaust wall** — 排气壁表面积 `pi * ((1.5 / 2) ^ 2)` `m^2`（默认）| 正标量

排气壁的表面积。
这仅是与排气接触的内壁的表面积。

### **Mass of exhaust wall** — 排气壁总质量 `5` `kg`（默认）| 正标量

排气壁的质量。

### **Heat capacity of exhaust wall** — 排气壁热容量 `100` `J/(K*kg)`（默认）| 正标量

排气壁的热容量。

### **Time constant of exhaust heat flow** — 排气热流时间常数 `10` `s`（默认）| 正标量

排气热流速率的时间常数。

### **Convective heat transfer coefficient for the outer side of exhaust** — 排气外侧对流换热系数 `100` `W/(K*m^2)`（默认）| 正标量

排气外侧的对流换热系数。

### **Radiation constant** — 排气辐射常数 `0.3`（默认）| 正标量

排气的辐射常数。

### **Stefan-Boltzmann constant** — 排气 Stefan-Boltzmann 常数 `5.7e-8` `W/(K^4*m^2)`（默认）| 正标量

整个排气系统的 Stefan-Boltzmann 常数。
## 所属库

Simscape / Driveline / Engines & Motors / Engine Subcomponents

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2022a 中引入**

## 描述

内燃机排气歧管的热力学

Exhaust Manifold Thermal 模块表示内燃机排气歧管的抽象热力学。该模块与 SI Combustion Cylinder 模块集成。

### 方程

该模块从 SI Combustion Cylinder 模块获取排气气体流量，并计算排气歧管温度 *Texh*，该模块在端口 **Texh** 输出该温度。该模块使用集总参数模型计算输出，使得

CexhMexhddtTexh=hexh−hx，

其中

- *Cexh* 是 **Heat capacity of exhaust wall** 参数。
- *Mexh* 是 **Mass of exhaust wall** 参数。
- *hexh* 是排气歧管处的热流。
- *hx* 是排气气体与环境之间的热交换。

该模块将 *hx* 计算为

hx=Sexh(hconvec(Texh−Tamb)−kraσ(Texh4−Tamb4))，

其中

- *Sexh* 是 **Surface area of exhaust wall** 参数。
- *hconvec* 是 **Convective heat transfer coefficient for the outer side of exhaust** 参数。
- *kra* 是 **Radiation constant** 参数。
- *σ* 是 **Stefan-Boltzmann constant** 参数。
- *Tamb* 是 **Ambient temperature** 参数。

该模块将 *hexh* 计算为

kgasddthexh=hin−hexh，

其中 *kgas* 是 **Time constant of exhaust heat flow** 参数，*hin* 是从发动机排气出口到排气歧管的瞬时热流。瞬时热流是排气出口处各个瞬时热流 *hi* 的总和，使得

hin=∑i=1Nportshi，

其中 *Nports* 是 **Number of exhaust ports** 参数。
