import matplotlib.pyplot as plt

# E-Commerce Graphs
# Graph 1: Line Chart
sales = [20000, 25000, 30000, 28000, 35000, 40000]
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
plt.plot(months, sales, marker='o', color='orange')
plt.xlabel("Months")
plt.ylabel("Sales Revenue ($)")
plt.title("Monthly Sales Trends")
plt.grid(True)
plt.show()
plt.savefig("E_LineGraph.png")

# Graph 2: Bar Chart (Horizontal)
products = ["Laptop", "Phone", "Shoes", "Watch", "Bag"]
units_sold = [150, 200, 250, 180, 220]
plt.barh(products, units_sold, color='cyan')
plt.xlabel("Units Sold")
plt.ylabel("Products")
plt.title("Top 5 Best-Selling Products")
plt.show()
plt.savefig("E_BarChart.png")

# Graph 3: Pie Chart
categories = ["Electronics", "Clothing", "Home Appliances", "Books", "Accessories"]
orders = [300, 500, 200, 150, 250]
plt.pie(orders, labels=categories, autopct="%1.1f%%", colors=["blue", "green", "red", "purple", "orange"])
plt.title("Orders by Category")
plt.show()
plt.savefig("E_PieChart.png")