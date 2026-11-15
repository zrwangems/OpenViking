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
language: en
---

# Pan Tilt Hat

## Ports

### Input

### **pan angle** — Pan angle of pan and tilt hardware module `[-90, 90]` | integer

Pan angle that the block receives from the pan and tilt hardware module.

**Data Types:** `double`

### **tilt angle** — Tilt angle of pan and tilt hardware module `[-90, 90]` | integer

Tilt angle that the block receives from the pan and tilt hardware module.

**Data Types:** `double`

## Parameters

### **Mode of operation** — Mode of operation of pan and tilt hardware module `Pan and tilt` (default) | `Pan` | `Tilt`

Select the operating mode of the pan and tilt hardware module.

- `Pan and tilt` — Pan and tilt hardware moves along
  horizontal and vertical axes.
- `Pan` — Pan and tilt hardware moves along horizontal
  axis.
- `Tilt` — Pan and tilt hardware moves along vertical
  axis.

### **PWM frequency (Hz)** — PWM frequency of pan and tilt servo motors `50` (default) | `25` | `75` | `100` | `125` | `150` | `175` | `200` | `225` | `250` | `275` | `300` | `325` | `350` | `375`

Select the PWM frequency of the pan and tilt servo motors.

### **Sample time** — Interval at which block receives pan and tilt angles `0.1` (default) | scalar

Enter the time interval at which the block receives the pan and tilt angles from the
pan and tilt hardware module.

### Pan Servo

### **Channel** — PWM channel to drive pan servo motor `1` (default) | `0` | [`2` to `16`]

Enter the PCA9685 PWM channel to drive the pan servo motor.

### **Pulse duration [min max]** — PWM pulse duration sent to pan servo motor `[500e-6, 2500e-6]` (default) | positive scalar

Enter the minimum and maximum PWM pulse duration that the PCA9685 driver sends to
the pan servo motor.

### Tilt Servo

### **Channel** — PWM channel to drive tilt servo motor `0` (default) | [`1` to `16`]

Enter the PCA9685 PWM channel to drive the tilt servo motor.

### **Pulse duration [min max]** — PWM pulse duration sent to tilt servo motor `[500e-6, 2500e-6]` (default) | positive scalar

Enter the minimum and maximum PWM pulse duration that the PCA9685 driver sends to
the tilt servo motor.

## Libraries

Simulink Support Package for Raspberry Pi Hardware / Basic

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2022a**

## Description

Control pan and tilt motions using PCA9685-based PWM driver

Use the Pan Tilt Hat block to control the pan and tilt motions of hardware
using the PCA-9685-based PWM I2C driver. This block accepts pan and
tilt angles in the range –90 to 90 degrees. The PCA9685 driver controls the movement of the
pan and tilt hardware module in two degree of freedom (DoF), namely along the horizontal and
vertical axes, respectively.

### Activate, Load, and Verify PCA9685 Kernel Module

Follow these steps to activate and load the PCA9685 kernel module on your Raspberry Pi® hardware and then use the Pan Tilt Hat block in your
Simulink® model.

1. Execute these commands on the MATLAB® Command Window to open the Raspberry Pi
   terminal.

   ```
   r=raspberrypi('<Raspberry Pi IP address>','<Raspberry Pi username>','<Raspberry Pi password>');
   r.openShell
   ```
2. Open the `/boot/config.txt` file in a text editor.
3. To activate the PCA9685 kernel module, add this code to the
   `/boot/config.txt`
   file.

   ```
   dtoverlay=i2c-pwm-pca9685a
   ```
4. Save and close the `/boot/config.txt` file.
5. Reboot your Raspberry Pi.
6. To load the PCA9685 kernel module on your Raspberry Pi, execute this code in the Raspberry Pi
   terminal.

   ```
   sudo modprobe pwm-pca9685
   ```
7. To verify whether you have successfully loaded the PCA9685 module on your
   Raspberry Pi hardware, execute this code in the Raspberry Pi
   terminal.

   ```
   i2cdetect -y <i2c bus number>
   ```

   For example,

   ```
   i2cdetect -y 1
   ```

   Observe that the PCA9685 kernel module reserves an I2C
   address `0x40` for the pan tilt hardware, indicated by **UU**.PCA9685 Kernel Module in use on I2C bus
