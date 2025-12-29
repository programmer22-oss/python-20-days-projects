error_count = 0
warning_count = 0

with open("sample.log", "r") as file:
    for line in file:
        if "ERROR" in line:
            error_count += 1
        elif "WARNING" in line:
            warning_count += 1

print("📊 Log Analysis Report")
print("Errors:", error_count)
print("Warnings:", warning_count)
print("✅ Analysis Complete")