print("--- Welcome to our Cafe ---")
print("------- Menu ---------")
print("Appetizer-5$")
print("Entree-6$")
print("Dessert-6.5$")

total=0
while True:   
      food=input("Enter food name:")

      if food=="done".lower():
         print(f"Your total is:{total}$")
         break
      else:
         if food =="appetizer":
                total=total+5
                print(f"Your current total is:{total}$")
         elif food=="entree":
                total=total+6
                print(f"Your current total is:{total}$")
          
         elif food=="dessert":
                total=total+7
                
                print(f"Your current total is:{total}$")
         else:
                print("Enter from menu,please!")


print("=== Order Summary ===")
print(f"Subtotal:{total}$")
if total>=35:
    total=total-4.5
    print(f"Combo Deal Discount:{total}$")
print("Thank you for your order!")





