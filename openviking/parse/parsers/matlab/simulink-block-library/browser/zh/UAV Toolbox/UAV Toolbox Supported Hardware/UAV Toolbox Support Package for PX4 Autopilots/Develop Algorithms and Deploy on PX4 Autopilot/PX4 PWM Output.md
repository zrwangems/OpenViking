---
type: simulink-block
title: 'PX4 PWM Output'
family: 'uav'
product_id: 'uav'
product_name: 'UAV Toolbox'
documentation_release: R2025b
official_category: 'UAV Toolbox Supported Hardware / UAV Toolbox Support Package for PX4 Autopilots / Develop Algorithms and Deploy on PX4 Autopilot'
documentation_page: 'px4pwmoutput'
documentation_source_path: 'px4/ref/px4pwmoutput.html'
language: zh-CN
chinese_source: worker-translation
---

# PX4 PWM Output

## 端口

### 输入

### **Arm** — 使 PX4 飞控解锁 `0`（默认）| `1`

用于使 PX4 飞控解锁的使能信号。

**数据类型：** `Boolean`

### **Set failsafe** — 为 PX4 飞控强制执行失效保护 `0`（默认）| `1`

即使失效保护条件可能已发生或可能尚未发生，也强制执行失效保护值。您可以在 Simulink 的 Configuration Parameters 对话框中指定失效保护值。

**注意**

如果使用 PX4 固件 1.12.3，并且将 AUX 通道用于 PWM，则 `Set failsafe` 输入端口处的值无效。

**数据类型：** `Boolean`

### **Ch *`x`*** — 接受 PWM ON 值的输入 `0`（默认）| `1`

将 Ch `x` 输入连接到表示 PWM ON 值（in microseconds）的信号

#### 依赖关系

所需的 `Ch` 输入通过 **PWM Channels** 参数选择。

**数据类型：** `uint16`

## 参数

#### Main 选项卡

### **Select PWM Device** — 用于标识您将要选择的通道的通道类别 Main（默认）| Aux

选择类别（Main 或 AUX）以标识并选择相应的通道。选择此类别后，您可以分别在参数列表中选择 Main 和 AUX 的通道。

### **PWM Channels** — 要将 PWM ON 时间值发送到的通道 通道编号

选择要将 PWM ON 时间值发送到的通道（即连接伺服电机或 ESC 的通道）。模块的 `Ch` 输入将根据此参数列表中的选择出现。

**注意**

确保选择属于同一通道组的所有通道。如果需要连接到不同组中的 PWM 通道，请选择所有所需组中的所有通道。整个 Simulink 模型中，每个通道类别（Main 或 AUX）仅允许有一个 PX4 PWM Output 模块。

**提示**

要识别 Pixhawk Series 飞控板中的通道组，请在主机上使用 QGroundControl 应用程序：

1. 打开 QGroundControl。
2. 将 Pixhawk Series 飞控板连接到主机的 USB 端口。
3. 在 QGroundControl 中，转到 **Mavlink Console**，然后执行以下操作：

   - 要识别 Main 通道及其组，请输入命令 `pwm info`。
   - 要识别 Aux 通道及其组，请输入命令 `pwm info -d /dev/pwm_output1`

## 所属库

UAV Toolbox Support Package for PX4 Autopilots / PX4 Utility Blocks

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2018b 中引入**

### R2024b：将在未来版本中删除

PX4 PWM Output 功能将在未来版本中删除。请改用 PX4 Actuator Write 模块。

有关将 Simulink 模型中的 PX4 PWM Output 转换为 PX4 Actuator Write 模块的信息，请参阅 Convert PX4 PWM Output Block to PX4 Actuator Write Block。

## 描述

为伺服电机和 ESC 控制配置 PWM 输出

PX4 PWM Output 模块可帮助您配置来自 PX4® 飞控板的 PWM 输出。该模块接受表示特定通道的 PWM 信号 ON 周期的时间值（in microseconds），并将其传递到板上相应的 PWM 通道。

PX4 PWM Output 模块还接受用于使飞控解锁的信号。

在 Connected IO 仿真期间，此模块会将数据写入硬件的外设。

**配置执行器**

对于固件版本 1.14，需要先在 QGroundControl 中配置 PWM & AUX 引脚，然后才能在 Simulink 中使用 PWM Output 模块。为此，需要 QGroundControl 版本 4.2.8，可从该位置下载。

**注意**

对于 Hardware-in-the-loop 或 PX4 Host Target 仿真，不需要配置执行器。

要配置执行器，请执行以下步骤。

1. 对您的 Autopilot 执行 Hardware setup 过程。
2. 启动 QGroundControl 4.2.8 (QGC)，并允许其连接到您的 Autopilot。
3. QGC 连接后，转到 **Vehicle Setup** -> **Actuators** 选项卡。

   硬件板

4. 为每个 Main 通道分配以下电机顺序。

   硬件板

   建议将每个通道的 Minimum PWM value 更改为 1000，并将 Maximum PWM value 更改为 2000。

5. 为每个 AUX 通道分配以下电机顺序。

   硬件板
