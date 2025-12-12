def build_sales_log(sales_list):
    new_dict={}
    for i in sales_list:
        cleaned_list=i.split("|")
        employee_id=cleaned_list[0]
        if employee_id not in new_dict:
            new_dict[employee_id]=0
        price=float(cleaned_list[2])
        new_dict[employee_id]+=price
       
    return new_dict

def find_top_performer(sales_dict):
    highest_sales=0
    id_top=None
    
    for employee_id, price in sales_dict.items():
        if price>highest_sales:
            highest_sales=price
            id_top=employee_id
    return id_top, highest_sales
sales_list = [
    "E101|Laptop|1200.00",
    "E102|Mouse|25.50",
    "E101|Monitor|300.00",
    "E103|Headphones|150.00",
    "E102|Keyboard|50.00",
    "E103|Laptop|1000.00",
    "E101|Mousepad|15.00"
]
print("Sales report:")
sales_dict=build_sales_log(sales_list)
for employee, amount in sales_dict.items():
    print(f"{employee}: ${amount:.2f}")

print("---------------------")
top_id, top_amo = find_top_performer(sales_dict)
print(f"Top Performer is {top_id} with ${top_amo:.2f}")

