---
type: simulink-block
title: 'ThingSpeak Write'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Android Devices / Modeling / Communications'
documentation_page: 'thingspeakwrite'
documentation_source_path: 'supportpkg/android_ref/thingspeakwrite.html'
language: en
---

# ThingSpeak Write

## Ports

### Input

### **fieldn** — Data published to nth variable of ThingSpeak channel [`1` x *N*] vector, where *N* ranges from `1` to `8`

The block publishes the data read from this port to the nth variable on the
ThingSpeak channel at each time step. The number of data channels at the block
input depends on the number of variables you select in the **Number of fields** parameter. For example, if you set the **Number of fields** parameter to `3`, the block
enables three input ports with names `field1`,
`field2`, and `field3`.

**Data Types:** `single`

### **location** — Send location data three-element numeric vector

Specify location data as a three-element numeric vector of the form
[*latitude*, *longitude*,
*altitude*]. The block then publishes the location data to
ThingSpeak.

#### Dependencies

To enable this port, on the **Optional** tab, select
**Send location information** and set the **Location
source** parameter to `Input port`.

**Data Types:** `single` | `double`

## Parameters

### Main

### **Channel ID** — ThingSpeak channel ID `12397` (default) | positive integer

Enter the unique identification number of the ThingSpeak channel from which the block publishes data.

Follow these steps to get the ThingSpeak channel identification number.

1. Sign in to ThingSpeak using your MATLAB account.
2. Select **Channels** > **My Channels**.
3. Select the channel to get the write API key.
4. Click the **Channel Settings** tab and copy the channel ID
   from the **Channel ID** parameter.ThingSpeak Channel ID
5. Open the ThingSpeak Write block in your model and paste the
   copied ID to the **Channel ID** parameter.

### **Write API key** — Write API key of ThingSpeak channel character vector

Enter the 16-digit write API key of the ThingSpeak channel.

Follow these steps to get the API key for your ThingSpeak channel:

1. Sign in to ThingSpeak using your MATLAB account.
2. Select **Channels** > **My Channels**.
3. Select the channel to get the ThingSpeak write API key.
4. Click the **API Keys** tab and copy the key from the
   **Write API Keys** parameter.ThingSpeak Write API Key
5. Open the ThingSpeak Write block in your model and paste the
   copied API key in the **Write API key** parameter.

### **Number of fields** — Number of ThingSpeak fields to publish data `1` (default) | `2` | `3` | `4` | `5` | `6` | `7` | `8`

Select the field(s) of the ThingSpeak channel to which the block writes the data. For example, if you set this
parameter to `3`, the block has three input ports
`field1`, `field2`, and `field3`.
If you set this parameter to `1`, the block has only one input port
`field1`.

### **Update interval (seconds)** — Data update interval `60` (default) | nonnegative scalar

Specify the time interval at which the input data is updated on the ThingSpeak channel.

### Optional

### **Send location information** — Send location information off (default) | on

Select this parameter to send the location information to the ThingSpeak channel.

### **Location source** — Source of location data `Block dialog` (default) | `Input port`

Select the source of the location data as one of the following:

- `Block dialog` — Specify the location using the
  **Location (latitude, longitude, altitude)**
  parameter.
- `Input port` — Specify the location using the
  **location** input port.

Use decimal degrees notation to specify *latitude* and
*longitude* and use meters to specify *altitude*.
For example:

- The lowest human-sized point underground, the TauTona Mine in Carletonville,
  South Africa, is [`-26.416111,27.4275,-3900`].
- The highest point measured from sea level, the summit of Mount Everest in
  Nepal, is [`27.988056,86.925278,8848`].

### **Location (latitude, longitude, altitude)** — Location information [`42.29971`, `-71.350719`, `69.29`] (default) | three-element numeric vector

Enter the location information as a three-element numeric vector of the form
[*latitude*, *longitude*,
*altitude*] to publish location information to the ThingSpeak channel.

#### Dependencies

To enable this parameter, set **Location source** to
`Block dialog`.

## Libraries

Simulink Support Package for Android Devices / Communication

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2016b**

## Description

Publish data to Internet of Things using ThingSpeak

The ThingSpeak Write block publishes data from target hardware to the
Internet of Things (IoT) using ThingSpeak™.

ThingSpeak is an open IoT platform with
MATLAB® analytics that allows you to collect and store sensor data in the cloud and
develop IoT applications. The ThingSpeak IoT platform provides applications that allow you to analyze and visualize your
data in MATLAB and then act on the data. For more information on how to use ThingSpeak, see ThingSpeak
Apps, Plugins, and Tutorials.
