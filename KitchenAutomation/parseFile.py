import csv
from tkinter import *






def loadInventory(fileName):
    with open(fileName) as dataFile:
        reader = csv.DictReader(dataFile)
        stockItems = []
        for row in reader:
            stockItems.append({"product":row["product_name"],
             "stockQty":int(row["stock_quantity"]),"reorderAmt":int(row["reorder_level"])})
    return stockItems
def checkStock(stockItems):
    reorderList = []
    for item in stockItems:
        if item["stockQty"] <= item["reorderAmt"]:
            print(f'{item["product"]} is low! Quantity: {item["stockQty"]}( Reorder level: {item["reorderAmt"]}')
            reorderList.append(f'{item["product"]},{item["stockQty"]}, {item["reorderAmt"]}')
        else:
            print(f'{item["product"]} is sufficient, Quantity: {item["stockQty"]}(Reorder level:{item["reorderAmt"]}')
    return reorderList
def runInventoryAutomation():
    inventory = loadInventory("Kitchen_Inventory.csv")
    toReorder = checkStock(inventory)

    with open("reorderAlerts.csv","w") as newFile:
        fieldNames = ["item"]
        writer = csv.DictWriter(newFile,fieldnames=["item","stockQty","reorderAmt"])
        writer.writeheader()
        for product in toReorder:
            writer.writerow({"item":product})
    print("\nReorder list saved to reorderAlerts.csv")
if __name__ == "__main__":
    runInventoryAutomation()





def on_check_stock():
    """Fill the listbox using your existing functions."""
    items = loadInventory("Kitchen_Inventory.csv")
    to_reorder = checkStock(items)         # list like "Name,Qty,Reorder"
    lb.delete(0, END)
    for line in to_reorder:
        lb.insert(END, line)
    count_label.config(text=f"{len(to_reorder)} item(s) need restock")

def on_export_csv():

    runInventoryAutomation()
    count_label.config(text="Exported to reorderAlerts.csv")

# ---------- UI ----------
window = Tk()
window.geometry("600x690")
window.title("Kitchen Inventory")

btn_check = Button(window, text="Check Stock", font=("Arial", 12), command=on_check_stock)
btn_check.pack(pady=8)

lb = Listbox(window, width=70, height=22)
lb.pack(pady=6)

exportButton = Button(window, text="Export CSV (reuse code)", font=("Arial", 12), command=on_export_csv)
exportButton.pack(pady=8)

count_label = Label(window, text="", font=("Arial", 10))
count_label.pack(pady=4)




window.mainloop()














