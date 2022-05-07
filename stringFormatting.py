itemQty = 4
items = ["apples", "oranges", "grapes", "mangos"]
qtys = [3, 5, 2, 1]
units = ["pounds", "pounds", "pounds", "pounds"]
rates = [2, 3, 2, 5]

sum = 0
result = "Invoice:\n"
result += "==============================================================\n"
result += "Sl.No\tItems\t\t  Qty\t\tRate\t\tAmount\n"
result += "==============================================================\n"

for i in range(itemQty):
    text = "  {}\t{}\t\t{} {}\t${}\t-\t${}\n"
    result += text.format(i+1, items[i], qtys[i],
                          units[i], rates[i], qtys[i]*rates[i])
    sum += qtys[i]*rates[i]
result += "==============================================================\n"
result += "\t\t\t\t\tTotal:\t\t${}\n".format(sum)
result += "==============================================================\n"
print(result)
