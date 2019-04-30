import subprocess
result = subprocess.run(['arp', '-v'], stdout=subprocess.PIPE)
raw_data = result.stdout
