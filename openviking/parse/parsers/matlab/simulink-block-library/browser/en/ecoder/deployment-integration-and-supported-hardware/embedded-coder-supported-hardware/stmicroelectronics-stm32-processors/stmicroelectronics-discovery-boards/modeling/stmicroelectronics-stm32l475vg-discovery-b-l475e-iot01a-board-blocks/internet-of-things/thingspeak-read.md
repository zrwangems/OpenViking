---
type: simulink-block
title: 'ThingSpeak Read'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / STMicroelectronics STM32 Processors / STMicroelectronics Discovery Boards / Modeling / STMicroelectronics STM32L475VG-Discovery (B-L475E-IOT01A) Board Blocks / Internet of Things'
documentation_page: 'thingspeakread'
documentation_source_path: 'stmicroelectronicsstm32f4discovery/ref/thingspeakread.html'
language: en
---

# ThingSpeak Read

## Ports

### Output

### **Data** — Data read from specified field of ThingSpeak channel scalar

At each time step, the port outputs the data read from the field specified in the
**Field Number** parameter.

**Data Types:** `single`

### **Status** — Status of each read request scalar

The port outputs the status of each read request as mentioned in the following
table:

**Return status codes**

| **Status** | Description |
| --- | --- |
| 200 | OK or Success |
| -301 | Failed to connect to ThingSpeak |
| -303 | No response/ Unable to parse response from ThingSpeak |

#### Dependencies

This port appears only when you select the **Output
Status** parameter.

**Data Types:** `single`

## Parameters

### **Channel ID** — Channel ID from which block reads data `65531` (default) | `positive integer`

Specify the channel ID from which the block reads data.

If you do not know the channel ID of your channel:

1. Sign In to
   ThingSpeak using your MathWorks® Account.
2. Select **Channels** > **My Channels**.
3. Select the channel from which to read data.
4. Click the **Channel Settings** tab.
5. Copy the channel ID from the **Channel ID** parameter.
6. Open the ThingSpeak Read block in your model and paste the copied
   ID to the **Channel ID** parameter.

### **Channel access** — Sharing settings of channel `Public` (default) | `Private`

Specify if your channel is private or public.

If you do not know the sharing settings of your channel:

1. Sign In to
   ThingSpeak using your MathWorks Account.
2. Select **Channels** > **My Channels**.
3. Select the channel to get the sharing status.
4. Click the **Sharing** tab. Use the option selected in the tab
   to set **Channel Access**.

   - **Keep channel view private**: Set **Channel
     Access** to `Private`. Only you can view the
     channel data.
   - **Share channel view with everyone**: Set **Channel
     Access** to `Public`. Anyone browsing the
     ThingSpeak website can view the channel data.
   - **Share channel view only with the following users**: Set
     **Channel Access** to `Private`.
     Users who have access to shared channels can see only the private view of a
     channel; they cannot add channels, see alerts, or see license
     information.

### **Field number** — Field from which block reads data `1` (default) | integer between 1 and 8

Select a field of the ThingSpeak channel from which the block reads data.

### **Output Status** — Enable output status `off` (default) | `on`

When you select the **Output Status** parameter, the block
configures an output port, **Status**. The port outputs the status
message.

### **Sample time** — Interval at which block reads data `20` (default) | `-1` | `nonnegative integer`

Specify how often the block reads data from the ThingSpeak channel.

When you set this parameter to `-1`, Simulink® determines the best sample time for the block based on the block context
within the model.

## Libraries

Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32L475VG-Discovery (B-L475E-IOT01A) Simulink Coder Support Package for STMicroelectronics Nucleo Boards / STM32F7 Simulink Coder Support Package for STMicroelectronics Nucleo Boards / STM32H7 Simulink Support Package for Arduino Hardware / Ethernet Shield

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2021a**

## Description

Read data stored in ThingSpeak channel

The ThingSpeak Read block reads data from the ThingSpeak™ channel on the ThingSpeak.com
website.

ThingSpeak is an IoT analytics platform service that allows you to aggregate, visualize,
and analyze live data streams in the cloud. You can send data to ThingSpeak from your devices, create instant visualizations of live data, and send alerts
using web services. With MATLAB® analytics inside ThingSpeak, you can write and execute MATLAB code to perform preprocessing, visualizations, and analyses.

For more information on how to use ThingSpeak, see Apps, Plugins, or Tutorials.
