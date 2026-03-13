GitHub Setup

    1. Create a GitHub repository
    2. Make 1_FastAPI_App folder as local git
    3. Push local to remote

git config --global user.name "vaibhavk26"
git config --global user.email "your-email@example.com"  # Use the email associated with your GitHub account

New Setup 
    1. Fork the trainer repo outskill-git/GenAIEngineering-Cohort5: Cohort %
        a. Click on Fork
        b. Create a New Fork
        c. Append your initials to the Fork Repo name "-VK"
        d. Click Create fork 
        e. Your repo is created with name vaibhavk26/GenAIEngineering-Cohort5-VK: Cohort 5 Vaibhav Repo
    2. Check origin connection using "git remote -v"
        a. PS C:\Users\vaibh\OneDrive\Vaibhav\GenAIEngineering-Cohort5> git remote -v
        origin  https://github.com/outskill-git/GenAIEngineering-Cohort5.git (fetch)
        origin  https://github.com/outskill-git/GenAIEngineering-Cohort5.git (push)
        b. If origin is connected to trainer repo, remove it 
        >> git remote remove origin
        c. Now connect your fork
        >> git remote add origin https://github.com/vaibhavk26/GenAIEngineering-Cohort5-VK.git
    3. Add Trainer repo as upstream 
        a. git remote add upstream https://github.com/outskill-git/GenAIEngineering-Cohort5.git
        b. Now check remote connection (it should show origin as your fork and upstream as trainer repo)
        $ git remote -v
        origin  https://github.com/vaibhavk26/GenAIEngineering-Cohort5-VK.git (fetch)
        origin  https://github.com/vaibhavk26/GenAIEngineering-Cohort5-VK.git (push)
        upstream        https://github.com/outskill-git/GenAIEngineering-Cohort5.git (fetch)
        upstream        https://github.com/outskill-git/GenAIEngineering-Cohort5.git (push)
        
    4. Push to your fork repo
        >> Git push origin main
    5. Every week pull the trainer repo
        >> git pull upstream main

