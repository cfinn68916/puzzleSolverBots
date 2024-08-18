import concurrent.futures
import subprocess

def solve(task):
    ad=subprocess.run(['./main_opt'],input=(task+'\n20').encode(), capture_output=True)
    ans=ad.stdout.decode('ascii').strip('\n')
    return ans


ppe=concurrent.futures.ThreadPoolExecutor(max_workers=16)
futures=[]
with open("q1000", 'r') as f:
    for line in f:
        futures.append(ppe.submit(solve, line))
with open("ans1000", 'w') as f:
    for future in futures:
        f.write(future.result()+'\n')
