---
type: simulink-block
title: 'ThingSpeak Write'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / STMicroelectronics STM32 Processors / STMicroelectronics Discovery Boards / Modeling / STMicroelectronics STM32L475VG-Discovery (B-L475E-IOT01A) Board Blocks / Internet of Things'
documentation_page: 'thingspeakwrite'
documentation_source_path: 'stmicroelectronicsstm32f4discovery/ref/thingspeakwrite.html'
language: en
---

# ThingSpeak Write

## Ports

### Input

### **Var1** — Send data to specified field of ThingSpeak channel scalar

The input port from which the block sends data to the ThingSpeak channel field you specify in the Fields parameter. If you do not specify
a field, the block sends data to all the fields in the channel in a sequential
manner.

**Data Types:** `single`

## Parameters

### Main

### **Channel ID** — Channel ID to which block writes data `65531` (default) | `any positive integer`

Specify the ThingSpeak channel to which you want to write data.

If you do not know the channel ID of your channel:

1. Sign In to
   ThingSpeak using your MathWorks® Account.
2. Select **Channels** > **My Channels**.
3. Select the channel to which to you want to write data.
4. Click the **Channel Settings** tab.
5. Copy the channel ID from the **Channel ID** parameter.

   ThingSpeak Channel Settings
6. Open the ThingSpeak Write block in your model and paste the
   copied ID to the **Channel ID** parameter.

### **Write API key** — Write API key of ThingSpeak channel `ABCDEFGHIJK` (default)

Specify the write API key of the ThingSpeak channel. Get the **Write API Key** parameter from your
channel in ThingSpeak.com.

After creating a ThingSpeak channel for your target hardware:

1. In the ThingSpeak.com
   website, select **Channels** > **My Channels**.
2. Under the channel that you created for this target hardware, click
   **Settings**.
3. Click the **API Keys** tab.
4. Copy the key from **Write API Key** parameter.
5. Open the ThingSpeak Write block in your model and paste the API
   key into **Write API key** parameter.

### **Number of variables** — Set number of variables to write `1` (default) | `Integer between 1 to 8`

Set the number of variables to write.

### **Set Minimum Update Interval** — Enable minimum update interval `off` (default) | `on`

Enable to set the minimum update interval.

### **Minimum update interval** — Specify minimum update interval `15` (default) | `Nonnegative value`

Specify the minimum update interval time in seconds.

### Optional

### **Send location information** — Option to send location information `off` (default) | `on`

Enable to send location information. Specify the `location
source` and `location`.

### **Location source** — Select location source `Block dialog` (default) | `Input port`

Select the source of the location. When location source is set to:

- `Input port` - specify the location using a signal
  that is connected to the **location** block input.
- `Block dialog` - specify the location using the
  **Location (latitude, longitude, altitude)**
  parameter.

In both cases, specify the location as a cell array of three elements:

```
[latitude,longitude,altitude]
```

Use decimal degrees notation to specify latitude and longitude. Use meters to
specify altitude. For example:

- The lowest human-sized point underground, the TauTona Mine in
  Carletonville, South Africa:
  `[-26.416111,27.4275,-3900]`
- The highest point measured from sea level, the summit of Mount Everest in
  Nepal: `[27.988056,86.925278,8848]`

### **Location** — Specify the location as a cell array of three elements `[ 42.29971, -71.350719, 69.29 ]` (default) | `three-element cell array`

Specify the location as a cell array of three elements:

```
[latitude,longitude,altitude]
```

#### Dependencies

To enable this parameter, set **Location source** parameter to
`Block dialog`.

### **Enable field selection** — Enable to select the fields to send data `off` (default) | `on`

Enable this parameter if you want to specify the fields to send data. If this
parameter is not enabled, the data is sent to the fields in a sequential order.

### **Fields** — Field to which block sends data `[1]` (default) | `Array of positive integer ranging between 1 to 8`

Specify the fields of the ThingSpeak channel to which the block sends data.

#### Dependencies

To enable this parameter, select **Enable field selection**
parameter.

## Libraries

Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32L475VG-Discovery (B-L475E-IOT01A) Simulink Coder Support Package for STMicroelectronics Nucleo Boards / STM32F7 Simulink Coder Support Package for STMicroelectronics Nucleo Boards / STM32H7 Simulink Support Package for Arduino Hardware / Ethernet Shield

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2021a**

## Description

Publish data to Internet of Things using ThingSpeak

Use this block publish data from your target hardware to the Internet of Things using
ThingSpeak™.

ThingSpeak is an IoT analytics platform service that allows you to aggregate, visualize,
and analyze live data streams in the cloud. You can send data to ThingSpeak from your devices, create instant visualizations of live data, and send alerts
using web services. With MATLAB® analytics inside ThingSpeak, you can write and execute MATLAB code to perform preprocessing, visualizations, and analyses.

For more information on how to use ThingSpeak, see Apps, Plugins, or Tutorials.
