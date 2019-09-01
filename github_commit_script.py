import os
import subprocess
from datetime import datetime, timedelta

# Initialize a new Git repository or use an existing one
repo_path = '/Users/malcolmdecuire/decuresolutions_archive'
os.chdir(repo_path)

# Ensure the git repository is initialized (optional if already cloned)
subprocess.run(['git', 'init'])

# Function to run a git command
def run_git_command(command):
    subprocess.run(command, shell=True)

# Start and end dates for the commits
start_date = datetime(2019, 9, 1)
end_date = datetime.now()

# Generate commits from start_date to end_date
current_date = start_date
while current_date <= end_date:
    # Create a dummy file for the commit
    filename = f'file_{current_date.strftime("%Y%m%d")}.txt'
    with open(filename, 'w') as file:
        file.write(f'Git commit experiment {current_date.strftime("%Y-%m-%d")}\n')

    # Add the file to the staging area
    run_git_command('git add .')

    # Commit the file with a backdated commit date
    commit_message = f'Commit for {current_date.strftime("%Y-%m-%d")}'
    commit_date = current_date.strftime('%Y-%m-%dT%H:%M:%S')
    run_git_command(f'git commit -m "{commit_message}" --date="{commit_date}"')

    # Move to the next day (or other interval)
    current_date += timedelta(weeks=1)

print('Commit history generated successfully.')
