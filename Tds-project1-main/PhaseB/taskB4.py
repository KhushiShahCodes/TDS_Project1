import os
import subprocess
import datetime

repo_url = "https://github.com/KhushiShahCodes/TDS_Project1"  # Public repo URL

def run_command(command, cwd=None):
    """Helper function to run a shell command and capture the output."""
    result = subprocess.run(command, shell=True, cwd=cwd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error: {result.stderr}")
    else:
        print(result.stdout)

def clone_and_commit(repo_url, local_path="TDS_Project1/Tds-project1-main", file_to_modify="requirements.txt", commit_message="Updated requirements.txt with new content"):
    """Clone a Git repo, make a commit, and push changes."""
    if not repo_url:
        raise ValueError("Repository URL is required")
    
    # Ensure Git is installed
    run_command("git --version")

    # Configure Git user (if needed for commits)
    run_command('git config --global user.name "Khushi Shah"') 
    run_command('git config --global user.email "23f2005471@ds.study.iitm.ac.in"')

    cwd = os.getcwd()

    try:
        # 1. Clone the repository if it doesn't exist locally
        if os.path.exists(local_path):
            print("Repository already exists. Pulling latest changes.")
            run_command("git pull", cwd=local_path)
        else:
            # Clone the repository
            print(f"Cloning repository from {repo_url} to {local_path}...")
            run_command(f"git clone {repo_url} {local_path}")
        
        # 2. Change to the repo directory
        os.chdir(local_path)

        # 3. Make changes (e.g., modify a file)
        print("Making changes...")
        now = datetime.datetime.now()
        with open(file_to_modify, "a") as f:
            f.write(f"{now.isoformat()}: This is an automated commit.\n")

        # 4. Commit the changes
        print("Committing changes...")
        run_command("git add .")  # Stage the changes
        run_command(f'git commit -m "{commit_message}"')  # Commit with a message

        # 5. Push the changes
        print("Pushing changes...")
        run_command("git push")

    except Exception as e:
        print(f"Error occurred: {e}")
    finally:
        os.chdir(cwd)

    return "Changes committed and pushed successfully!"

clone_and_commit(repo_url)


