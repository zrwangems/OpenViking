---
type: simulink-block
title: '3D Engine'
family: 'vdynblks'
product_id: 'vdynblks'
product_name: 'Vehicle Dynamics Blockset'
documentation_release: R2025b
official_category: 'Vehicle Reference Applications'
documentation_page: '3dengine'
documentation_source_path: 'ref/3dengine.html'
language: zh-CN
chinese_source: worker-translation
---

# 3D Engine

## 端口

### 输入

### **VehFdbk** — 车辆反馈 `Bus`

包含车辆反馈信号的 Bus，包括速度、加速度和方向盘扭矩。

## 参数

#### 3D Engine

### **3D Engine** — 启用 3D 可视化 `off` (default) | `on`

启用 3D 可视化。

### **Scene** — 3D 场景 `Straight road` | `Curved road` | `Parking lot` | `Double lane change` | `Open surface` | `US city block` | `US highway` | `Virtual Mcity` | `Large parking lot`

指定 3D 场景的名称。

### **Engine frame rate, dt3D** — 图形 `.03` (default)

图形帧率，单位为 s。图形帧率是采样时间的倒数。

### **Recommended for scene** — 初始车辆位置 `on` (default) | `off`

使用场景推荐的车辆位置。

### **User-specified** — 初始车辆位置 `off` (default) | `on`

指定以设置您自己的初始车辆位置值。

### **Initial longitudinal position, X\_o** — 初始纵向位置 `off` (default) | `on`

车辆 CG 沿地球固定 *X* 轴的初始位置，单位为 m。

### **Initial lateral position, Y\_o** — 初始横向位置 `off` (default) | `on`

车辆 CG 沿地球固定 *Y* 轴的初始位置，单位为 m。

### **Initial vertical position, Z\_o** — 初始垂直位置 `off` (default) | `on`

车辆 CG 沿地球固定 *Z* 轴的初始位置，单位为 m。

### **Initial roll angle, phi\_o** — 侧倾 `off` (default) | `on`

车辆固定坐标系绕地球固定 *X* 轴的旋转（侧倾），单位为 rad。

### **Initial pitch angle, theta\_o** — 俯仰 `off` (default) | `on`

车辆固定坐标系绕地球固定 *Y* 轴的旋转（俯仰），单位为 rad。

### **Initial yaw angle, psi\_o** — 横摆 `off` (default) | `on`

车辆固定坐标系绕地球固定 *Z* 轴的旋转（横摆），单位为 rad。

## 所属库

R2025b 中未记录。

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2019a 中引入**

## 描述

在参考应用中配置场景

3D Engine 模块实现 3D 仿真环境。Vehicle Dynamics Blockset™ 将 3D 仿真环境与 Simulink® 集成，以便您可以查询车辆周围的世界，从而虚拟测试感知、控制和规划算法。

要在场景中定位车辆：

1. 选择位置初始化方法：

   - **Recommended for scene** — 将初始车辆位置设置为场景推荐的值
   - **User-specified** — 设置您自己的初始车辆位置
2. 点击 **使用初始值更新模型工作区**，以将应用的值覆盖模型工作区中的初始车辆位置。
