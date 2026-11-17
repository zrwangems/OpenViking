---
type: simulink-block
title: 'Battery'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Dashboard / Automotive Indicator Lamps'
documentation_page: 'battery'
documentation_source_path: 'supportpkg/legomindstormsev3_ref/battery.html'
language: zh-CN
chinese_source: worker-translation
---

# Battery

## 端口

### 输出

### **voltage** — EV3 主机电池电压标量

该模块以毫伏为单位输出 LEGO MINDSTORMS EV3 主机的电池电压。

**数据类型：** `uint16`

## 参数

### **Sample time** — 模块读取 EV3 主机电池电压的时间间隔 `0.1`（默认）| 正整数

指定模块读取 EV3 主机电池值的频率。较短的采样时间（例如 `0.01`）可能会产生不可靠的测量结果。

较小的采样时间要求处理器在更短的时间内完成相同数量的指令，这可能导致任务超限。

## 所属库

Simulink Support Package for LEGO MINDSTORMS EV3 Hardware

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2012a 中引入**

## 描述

测量 EV3 主机中电池的电压水平

使用 Battery 模块以毫伏为单位测量 LEGO® MINDSTORMS® EV3 主机中电池的电压。例如，当六节 1.5 伏电池完全充满时，输出值约为 `9000` 毫伏。

在没有硬件的仿真过程中，该模块输出零。请参阅 Block Produces Zeros or Does Nothing in Simulation。
