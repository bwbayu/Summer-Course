import statistics
infected_patients = [174, 335, 278, 214, 422, 513, 737, 672, 489, 412, 1301, 1105, 1123, 1376, 1502, 894, 665, 1704, 1656, 1342]

print(f"minimum {min(infected_patients)}")
print(f"maximum {max(infected_patients)}")
print(f"range {max(infected_patients) - min(infected_patients)}")
print(f"mean {statistics.mean(infected_patients)}")
print(f"median {statistics.median(infected_patients)}")
print(f"variance {statistics.variance(infected_patients)}")
print(f"standard deviation {statistics.pstdev(infected_patients)}")