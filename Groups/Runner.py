import subprocess
import time

# List of Python scripts to run in order
scripts_to_run = [
    'ALPHV.py',
    'Babuk_leak_site.py',
    'BB_Auction.py',
    'Bianlian.py',
    'Black_Basta_Blog.py',
    'Cuba.py',
    'D#nuts.py',
    'Daixin_Team.py',
    'Everest_Rnsr_Group.py',
    'LockBIT_Leaked.py',
    'LockBIT_BLOG.py',
    'Lorenz.py',
    'Mallox_Blog.py',
    'Medusa_Blog.py',
    'Omega_Blog.py',
    'MONTI_Leak_site.py',
    'Quantum_Blog.py',
    'Ragnar_Locker.py',
    'Snatch.py',
]

# Loop through the list and run each script with a 1-minute delay
for script in scripts_to_run:
    try:
        print(f"Running {script}...")
        subprocess.run(['python', script], check=True)
        print(f"{script} executed successfully")
    except subprocess.CalledProcessError as e:
        print(f"Error running {script}: {e}")

    # Introduce a 1-minute delay
    time.sleep(60)

print("All scripts have been executed.")
