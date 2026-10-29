import csv
import logging
logging.basicConfig(
    filename="analyzer.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s -  %(message)s"
)

log_file="sample_auth.log"

try:
    with open(log_file, "r") as file:
        logs = file.readlines()
except FileNotFoundError:
    print("Error: Log file not found")
    logging.error("Log file not found")
    raise SystemExit()
except OSError as e:
    print("File error: ",e)
    logging.error(f"File error: {e}")
    raise SystemExit()

print("Total log entries: ",len(logs))

for log in logs:
    print(log.strip())

failed_count=0
for log in logs:
    if "Failed password" in log:
        failed_count +=1

print("Total Failed login attempts: ",failed_count)

success_count=0

for log in logs:
    if "Accepted password" in log:
        success_count +=1

print("Total Accepted login attempts: ",success_count)

ip_counts={}
for log in logs:
    if "Failed password" in log:
        ip=log.split("from ")[1].split(" ")[0]
        if ip in ip_counts:
            ip_counts[ip]+=1
        else:
            ip_counts[ip]=1

print("Failed Login attempts by IP: ")
for ip,count in ip_counts.items():
    print(ip,": ",count)

for ip,count in ip_counts.items():
    if count>=3:
        print("Suspicious IP addresses: ")
        print(ip,"-",count,"failed attempts")

print("Failed login activity: ")

for log in logs:
    if "Failed password" in log:
        timestamp=" ".join(log.split()[:3])
        print("Time: ",timestamp)

with open("failed_logins.csv","w",newline="") as file:
    writer=csv.writer(file)
    writer.writerow(["IP Address","Failed Login Count","Status"])

    for ip,count in ip_counts.items():
        if count>=3:
            status="suspicious"
        else:
            status="normal"
        writer.writerow([ip,count,status])

print("CSV report generated Successfully")


logging.info(f"Total log entries: {len(logs)} ")
logging.info(f"Failed login attempts: {failed_count} ")
logging.info(f"Successful login attempts: {success_count} ")

for ip,count in ip_counts.items():
    logging.info(f"{ip} - {count} failed login attempts")

logging.info("Log analysis completed Successfully")


