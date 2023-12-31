Version: _1.0_ Author: _Naveen Kumar_

## Use Case: The Purpose of this Azure Function is to send Prisma Cloud Alerts to Customer on-premises SIEM/Syslog Server using webhook integration.

**Function Architecture:** Setup Azure Function in App Service Plan to integrate Azure Function with Virtual Network.  

Prisma Cloud – > Webhook (Azure Function) – > Vnet Integration – > Route traffic to on-premise data center syslog server.

#### Step 1: Azure Function Setup

Create a Function App

*   Publish: Code
*   Runtime stack: Python
*   Version: 3.11

![](https://33333.cdn.cke-cs.com/kSW7V9NHUXugvhoQeFaf/images/6d5be81749397327b17a97c7c4458855bec0be2d225b39a0.png)

![](https://33333.cdn.cke-cs.com/kSW7V9NHUXugvhoQeFaf/images/b44ee10d3da87fc0b6e40a02e6b2f823e89af040432639b2.png)

**Step 2: Azure Function integration with Azure VNET**

Open Function Networking setting:

![](https://33333.cdn.cke-cs.com/kSW7V9NHUXugvhoQeFaf/images/5adcd15d06be9328a1900c95af1881fff8f8fe02efc43e6a.png)

Click, Outbound Traffic configuration - Virtual Network Integration

![](https://33333.cdn.cke-cs.com/kSW7V9NHUXugvhoQeFaf/images/b91313d3733481a03c2776f464c6fb0b8c3017ea29757f7b.png)

Click, Add virtual network integration

![](https://33333.cdn.cke-cs.com/kSW7V9NHUXugvhoQeFaf/images/9e43aad094e296bb7ea0a20a205ab18c3babe4991d712eba.png)

Select VNET and Subnet and click Connect. \[This integration will be used to route traffic from Azure Function to SIEM/Syslog Server\]

![](https://33333.cdn.cke-cs.com/kSW7V9NHUXugvhoQeFaf/images/074457d57d0bca06382a1750dfc624821ba64832d02c2e38.png)

You might need to update route table to route traffic depending on your environment.

**Step 3: Deploy Azure Function**

Open Azure Function and Click **Create** 

![](https://33333.cdn.cke-cs.com/kSW7V9NHUXugvhoQeFaf/images/5435a0aab9ee7c367ce8740fd710f4eff579b31e59842c9d.png)

Select HTTP Trigger and click **Create**

![](https://33333.cdn.cke-cs.com/kSW7V9NHUXugvhoQeFaf/images/13f752ec7292de01baacad0efa0f7afec9c5f05d88381e86.png)

Open function. Click Function name “http\_trigger”

![](https://33333.cdn.cke-cs.com/kSW7V9NHUXugvhoQeFaf/images/2312922b852b659e3b7be9db9f4a9085a7623c5d5b617c63.png)

Click Code+Test

![](https://33333.cdn.cke-cs.com/kSW7V9NHUXugvhoQeFaf/images/aa0f28213bc20dfeeb3f2dad72d7eace0b28bcb741857da9.png)

![](https://33333.cdn.cke-cs.com/kSW7V9NHUXugvhoQeFaf/images/d507f4dddcdc1da2d74191adf71d21d6d584a1d5ed36bdb6.png)

Delete Default Code with Azure Function Code and Click on Save.

IMP: SYSLOG\_HOST is your Syslog server IP address

IMP: SYSLOG\_PORT is syslog server port number

Update variables with your syslog server ip address and port number.

![](https://33333.cdn.cke-cs.com/kSW7V9NHUXugvhoQeFaf/images/aeba4dbb9f42464e8ab84d15f7c61bf38cd482f3e5b880d8.png)

Click on Get function URL and copy function URL. This function URL is Prisma Cloud webhook address.

Follow Prisma Cloud documentation link to configure webhook integration in Prisma Cloud console.
