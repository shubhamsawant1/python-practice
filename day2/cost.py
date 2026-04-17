#Enter cost of 3 items from the user (using float data type) -a pencil a pen and an eraser> you have to output the total cost of the items back to the user as their bill.

pencil = float(input("Enter your pencil price: "))
pen = float(input("Enter your pen price: "))
eraser = float(input("Enter your eraser price: "))

gst = (1 + 18 / 100)

costofitems = pencil + pen + eraser 
<<<<<<< HEAD
 
=======

>>>>>>> f288d80 (update)
totalprice = costofitems * gst

print("total price(with gst)", totalprice)