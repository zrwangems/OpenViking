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
language: en
---

# Magnetometer

## Ports

### Output

### **Port\_1** — Strength of magnetic field around Android device vector

The block outputs the strength of the magnetic field as a
`1`-by-`3` vector. The elements of
the vector represent the measurements of the magnetic field in
`μT` along the X, Y, and Z axes of the magnetometer
sensor on the Android
device.

**Data Types:** `single`

## Parameters

### **Sample time** — How often the block reads data `0.1` (default) | `-1` | any positive integer

Specify how often the block reads data from the magnetometer, measured in
seconds. When you specify this parameter as `-1`,
Simulink® determines the best sample time for the block based on the
block context within the model.

### Read Magnetic Field Strength from Android Device

This example shows how to read the strength of the magnetic field around an
Android device.

This Simulink model includes a Magnetometer block and a Data Display block. The Magnetometer
block reads the strength of the magnetic field from the built-in magnetometer sensor
on your Android device. The block outputs the
magnetic field as a 1-by-3 vector. The Data Display block accepts the
vector and displays the values on your Android device.

To run the model:

1. Connect an Android device to your
   computer with a USB cable.
2. Install the Simulink Support Package for Android Devices as described in Install Support for Android Devices.
3. In the **Modeling** tab of the toolstrip, select
   **Model Settings**.
4. In the Configuration Parameters dialog box, select **Hardware
   Implementation**.
5. Set the **Hardware board** parameter to `Android
   Device`. This selection automatically populates the parameters
   in the **Hardware board settings** with the default values
   for Android.
6. From the **Groups** list under **Target hardware
   resources**, select **Device options**.
7. From the **Device** list, select your Android device. If
   your device is not listed, click **Refresh**.

   **Note**

   If your device is not listed even after clicking the
   **Refresh** button, ensure that you have enabled
   the **USB debugging** option on your device. To enable
   **USB debugging**, enter
   `androidhwsetup` in the MATLAB® Command Window and follow the onscreen
   instructions.
8. Click **Apply** to save your changes. Click
   **OK**.
9. On the Simulink editor toolbar, click the Build Model button . The model is loaded and starts running on the device.
   The values from the magnetometer are displayed on the device screen. Move
   your Android device and observe the
   change in the magnetic strength along all three axes.

## Libraries

Simulink Support Package for Android Devices / Sensors

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2018a**

## Description

Measure magnetic field along X, Y, and Z axes

The Magnetometer block reads the strength of the magnetic field around
an Android™ device. The built-in magnetometer sensor
on the Android device measures the magnetic field
along the X, Y, and Z axes. The block outputs the magnetic field as a 1-by-3 vector in
microtesla (μT).

This illustration shows the orientation of the X, Y, and Z axes for a typical
Android mobile phone.

This illustration shows the orientation of the X, Y, and Z axes for a typical
Android tablet.

**Note**

During simulations without hardware, this block outputs zeros. For more
information, see Block Produces Zeros or Does Nothing in Simulation.
