



def calculate_total(file_name):
    total_spent=0.0
    total_items=0
    with open("expenses.txt","r") as file:
        
        for line in file:
            try:
                expense=float(line.strip())
                total_spent+=expense
                total_items+=1
            except ValueError:
                print("Skipping invalid line ")
                
    print("---------")
    print(f"Total Items: {total_items}")
    print(f"Total Spent: ${total_spent:.2f}")

calculate_total("expenses.txt")

