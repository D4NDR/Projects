#initialising variables
VAT = 0.2
customer_total = 0
customer_items = ""

#Item descriptions
oculusQuest2_description = "Oculus Quest 2\nVR Headset. A standalone VR headset.\n"
razerDeathadder_description = "Razer DeathAdder\nGaming mouse. A high-performance gaming mouse.\n"
corsairK100RGB_description = "Corsair K100 RGB\nGaming Keyboard. A customisable gaming keyboard.\n"
steelSeriesArctis7_description = "SteelSeries Arctis 7\n Gaming Headset. A comfortable wireless gaming headset.\n"
dxRacerFormulaSeries_description = "DX Racer Formula Series\nGaming chair. An ergonomic gaming chair.\n"
asusROGSwiftPg279Q_description = "Asus ROG Swift PG279Q\nGaming monitor. A 27-inch gaming monitor with high refresh rate and low input lag.\n"
msiGe75Raider_description = "MSI GE75 Raider\nGaming laptop. A high-performance gaming laptop.\n"
nvidiaGeforceRtx3080_description = "Nvidia GeForce RTX3080\nGraphics card. A high-end graphics card for PC gaming.\n"
xboxEliteWirelessController_description = "Xbox Elite Wireless Controller\nGamepad. A high-end gamepad for Xbox and PC gaming.\n"
arozziVeronaPro_description = "Arozzi Verona Pro\nGaming desk. A spacious and ergonomic gaming desk.\n"

#Item prices
oculusQuest2_price = 299.00
razerDeathadder_price = 50.00
corsairK100RGB_price = 110.00
steelSeriesArctis7_price = 150.00
dxRacerFormulaSeries_price = 300.00
asusROGSwiftPg279Q_price = 700.00
msiGe75Raider_price = 1500.00
nvidiaGeforceRtx3080_price = 700.00
xboxEliteWirelessController_price = 180.00 
arozziVeronaPro_price = 300.00

#Items purchased
customer_total += oculusQuest2_price
customer_items += oculusQuest2_description

customer_total += razerDeathadder_price
customer_items += razerDeathadder_description

customer_total += corsairK100RGB_price
customer_items += corsairK100RGB_description

#VAT calculation
customer_VAT = round(customer_total * VAT, 2)
customer_subtotal = round(customer_total - customer_VAT, 2)

#Customer receipt
print("Items Purchased:\n" + customer_items)
print("Subtotal: " + str(customer_subtotal))
print("VAT: " + str(customer_VAT))
print("Total: " + str(customer_total))
print("Thank you for shopping with us, please come again!")