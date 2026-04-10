import subprocess
import os
from datetime import datetime


timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
backup_path = f"./backups/backup_{timestamp}"
os.makedirs("backups", exist_ok=True)


cmd = f"mongodump --uri=mongodb://localhost:27017 --db=mydatabase --out={backup_path}"
print(f"Backup: {backup_path}")
subprocess.run(cmd, shell=True)

# 2. RESTORE (розкоментуйте для відновлення)
# restore_path = f"{backup_path}/school"
# cmd_restore = f"mongorestore --uri=mongodb://localhost:27017 --db=school --drop {restore_path}"
# subprocess.run(cmd_restore, shell=True)

print("Done!")
