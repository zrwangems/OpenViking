---
type: simulink-block
title: 'Magnetometer'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Android Devices / Modeling / Sensors'
documentation_page: 'magnetometer'
documentation_source_path: 'supportpkg/android_ref/magnetometer.html'
language: zh-CN
chinese_source: worker-translation
---

# Magnetometer

## 端口

### 输出

### **Port\_1** — Android 设备周围磁场强度向量

该模块将磁场强度输出为 `1`×`3` 向量。该向量的元素表示沿 Android 设备上磁力计传感器的 X、Y 和 Z 轴以 `μT` 为单位的磁场测量值。

**数据类型：** `single`

## 参数

### **采样时间** — 模块读取数据的频率 `0.1`（默认） | `-1` | 任意正整数

指定该模块从磁力计读取数据的频率，以秒为单位。当您将此参数指定为 `-1` 时，Simulink® 会根据模型中的模块上下文确定该模块的最佳采样时间。

### 从 Android 设备读取磁场强度

此示例显示如何读取 Android 设备周围的磁场强度。

此 Simulink 模型包含一个 Magnetometer 模块和一个 Data Display 模块。Magnetometer 模块从您的 Android 设备上的内置磁力计传感器读取磁场强度。该模块将磁场输出为 1×3 向量。Data Display 模块接受该向量并在您的 Android 设备上显示这些值。

要运行该模型：

1. 使用 USB 线将 Android 设备连接到计算机。
2. 按照“安装 Android 设备支持”中的说明安装 Simulink Support Package for Android Devices。
3. 在工具条的 **建模** 选项卡中，选择 **模型设置**。
4. 在“配置参数”对话框中，选择 **硬件实现**。
5. 将 **硬件板卡** 参数设置为 `Android Device`。此选择会自动使用 Android 的默认值填充 **硬件板卡设置** 中的参数。
6. 在 **目标硬件资源** 下的 **组** 列表中，选择 **设备选项**。
7. 从 **设备** 列表中，选择您的 Android 设备。如果您的设备未列出，请单击 **刷新**。

      **注意**

      如果您的设备在单击 **刷新** 按钮后仍未列出，请确保您已在设备上启用 **USB 调试** 选项。要启用 **USB 调试**，请在 MATLAB® 命令窗口中输入 `androidhwsetup`，然后按照屏幕上的说明操作。
8. 单击 **应用** 以保存更改。单击 **确定**。
9. 在 Simulink 编辑器工具栏上，单击构建模型按钮 。模型将加载并开始在设备上运行。来自磁力计的值会显示在设备屏幕上。移动您的 Android 设备，并观察沿所有三个轴的磁场强度变化。

## 所属库

Simulink Support Package for Android Devices / Sensors

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2018a 中引入**

## 描述

测量沿 X、Y 和 Z 轴的磁场

Magnetometer 模块读取 Android™ 设备周围的磁场强度。Android 设备上的内置磁力计传感器测量沿 X、Y 和 Z 轴的磁场。该模块将磁场输出为以微特斯拉 (μT) 为单位的 1×3 向量。

此图显示了典型 Android 手机的 X、Y 和 Z 轴方向。

此图显示了典型 Android 平板的 X、Y 和 Z 轴方向。

**注意**

在没有硬件的仿真期间，此模块输出零。有关详细信息，请参阅“模块在仿真中产生零或不执行任何操作”。
