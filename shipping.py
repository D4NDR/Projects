weight = 8.4

#Ground shipping charges
if weight <= 2.0:
  ground_shipping = (weight * 1.5) + 20
elif weight <= 6.0:
  ground_shipping = (weight * 3.0) + 20
elif weight <= 10.0:
  ground_shipping = (weight * 4.0) + 20
else: 
  ground_shipping = (weight * 4.75) + 20

#Premium ground shipping charges
premium_ground_shipping = 125


#Drone shipping charges
if  weight <= 2.0:
  drone_shipping = weight * 4.5
elif weight <= 6.0:
  drone_shipping = weight * 9
elif weight <= 10.0:
  drone_shipping = weight * 12
else: 
  drone_shipping = weight * 14.25

#Print options
print("Ground Shipping: " + str(ground_shipping))
print("Premium Ground Shipping: " + str(premium_ground_shipping))
print("Drone Shipping: " + str(round(drone_shipping)))

#Check for lowest price
if ground_shipping < premium_ground_shipping and ground_shipping < drone_shipping:
  best_price = ground_shipping
elif premium_ground_shipping < ground_shipping and premium_ground_shipping < drone_shipping:
  best_price = premium_ground_shipping
elif drone_shipping < ground_shipping and drone_shipping < premium_ground_shipping:
  best_price = drone_shipping

#Print lowest price
if best_price == ground_shipping:
  print("Your best option is: Ground Shipping @ " + str(best_price))
elif best_price ==  premium_ground_shipping:
  print("Your best option is: Premium Ground Shipping @ " + str(best_price))
elif best_price == drone_shipping:
  print("Your best option is: Drone Shipping @ " + str(best_price)) 