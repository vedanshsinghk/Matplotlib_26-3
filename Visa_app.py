import matplotlib.pyplot as plt

# Visa Graphs

# Graph 1: Bar Chart
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
applications = [120, 150, 180, 200, 170, 190]
plt.bar(months, applications, color='blue')
plt.xlabel("Months")
plt.ylabel("Applications")
plt.title("Visa Applications Per Month")
plt.show()
plt.savefig("V_BarChart.png")

# Graph 2: Pie Chart
labels = ["Approved", "Rejected"]
counts = [450, 50]
plt.pie(counts, labels=labels, autopct="%1.1f%%", colors=["green", "red"])
plt.title("Visa Approval vs. Rejection Rate")
plt.show()
plt.savefig("V_PieChart.png")

# Graph 3: Line Chart
visa_types = ["Tourist", "Business", "Student", "Work"]
processing_days = [10, 15, 30, 45]
plt.plot(visa_types, processing_days, marker='o', color='purple')
plt.xlabel("Visa Type")
plt.ylabel("Processing Time (Days)")
plt.title("Average Processing Time by Visa Type")
plt.grid(True)
plt.show()
plt.savefig("V_LineChart.png")