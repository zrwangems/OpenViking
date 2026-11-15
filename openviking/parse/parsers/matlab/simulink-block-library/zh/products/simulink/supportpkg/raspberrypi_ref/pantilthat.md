---
type: simulink-block
title: 'Pan Tilt Hat'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Raspberry Pi Hardware / Modeling / Basic'
documentation_page: 'pantilthat'
documentation_source_path: 'supportpkg/raspberrypi_ref/pantilthat.html'
language: zh-CN
chinese_source: worker-translation
---

# Pan Tilt Hat

## 端口

### 输入

### **pan angle** — pan 和 tilt 硬件模块的 pan 角度 `[-90, 90]` | integer

模块从 pan 和 tilt 硬件模块接收的 pan 角度。

**数据类型：** `double`

### **tilt angle** — pan 和 tilt 硬件模块的 tilt 角度 `[-90, 90]` | integer

模块从 pan 和 tilt 硬件模块接收的 tilt 角度。

**数据类型：** `double`

## 参数

### **操作模式** — pan 和 tilt 硬件模块的操作模式 `Pan and tilt`（默认）| `Pan` | `Tilt`

选择 pan 和 tilt 硬件模块的操作模式。

- `Pan and tilt` — pan 和 tilt 硬件沿水平轴和垂直轴移动。
- `Pan` — pan 和 tilt 硬件沿水平轴移动。
- `Tilt` — pan 和 tilt 硬件沿垂直轴移动。

### **PWM 频率 (Hz)** — pan 和 tilt 伺服电机的 PWM 频率 `50`（默认）| `25` | `75` | `100` | `125` | `150` | `175` | `200` | `225` | `250` | `275` | `300` | `325` | `350` | `375`

选择 pan 和 tilt 伺服电机的 PWM 频率。

### **采样时间** — 模块接收 pan 和 tilt 角度的时间间隔 `0.1`（默认）| scalar

输入模块从 pan 和 tilt 硬件模块接收 pan 和 tilt 角度的时间间隔。

### Pan 伺服

### **通道** — 用于驱动 pan 伺服电机的 PWM 通道 `1`（默认）| `0` | [`2` to `16`]

输入用于驱动 pan 伺服电机的 PCA9685 PWM 通道。

### **脉冲持续时间 [min max]** — 发送到 pan 伺服电机的 PWM 脉冲持续时间 `[500e-6, 2500e-6]`（默认）| positive scalar

输入 PCA9685 驱动程序发送到 pan 伺服电机的最小和最大 PWM 脉冲持续时间。

### Tilt 伺服

### **通道** — 用于驱动 tilt 伺服电机的 PWM 通道 `0`（默认）| [`1` to `16`]

输入用于驱动 tilt 伺服电机的 PCA9685 PWM 通道。

### **脉冲持续时间 [min max]** — 发送到 tilt 伺服电机的 PWM 脉冲持续时间 `[500e-6, 2500e-6]`（默认）| positive scalar

输入 PCA9685 驱动程序发送到 tilt 伺服电机的最小和最大 PWM 脉冲持续时间。

## 所属库

Simulink Support Package for Raspberry Pi Hardware / Basic

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2022a 中引入**

## 描述

使用基于 PCA9685 的 PWM 驱动程序控制 pan 和 tilt 运动

使用 Pan Tilt Hat 模块，通过基于 PCA-9685 的 PWM I2C 驱动程序控制硬件的 pan 和 tilt 运动。此模块接受 –90 到 90 degrees 范围内的 pan 和 tilt 角度。PCA9685 驱动程序控制 pan 和 tilt 硬件模块在两个自由度 (DoF) 上的运动，即分别沿水平轴和垂直轴。

### 激活、加载和验证 PCA9685 内核模块

按照以下步骤在 Raspberry Pi® 硬件上激活并加载 PCA9685 内核模块，然后在 Simulink® 模型中使用 Pan Tilt Hat 模块。

1. 在 MATLAB® 命令窗口中执行以下命令以打开 Raspberry Pi 终端。

   ```
   r=raspberrypi('<Raspberry Pi IP address>','<Raspberry Pi username>','<Raspberry Pi password>');
   r.openShell
   ```
2. 在文本编辑器中打开 `/boot/config.txt` 文件。
3. 要激活 PCA9685 内核模块，请将以下代码添加到 `/boot/config.txt` 文件中。

   ```
   dtoverlay=i2c-pwm-pca9685a
   ```
4. 保存并关闭 `/boot/config.txt` 文件。
5. 重新启动 Raspberry Pi。
6. 要在 Raspberry Pi 上加载 PCA9685 内核模块，请在 Raspberry Pi 终端中执行以下代码。

   ```
   sudo modprobe pwm-pca9685
   ```
7. 要验证是否已在 Raspberry Pi 硬件上成功加载 PCA9685 模块，请在 Raspberry Pi 终端中执行以下代码。

   ```
   i2cdetect -y <i2c bus number>
   ```

   例如，

   ```
   i2cdetect -y 1
   ```

   观察 PCA9685 内核模块为 pan tilt 硬件保留 I2C 地址 `0x40`，由 **UU** 指示。I2C 总线上正在使用的 PCA9685 Kernel Module
