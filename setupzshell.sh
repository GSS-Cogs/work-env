
# Chmod the other files
chmod +x ~/.work-env/sync.sh
chmod +x ~/.work-env/enterzshell.sh

# Set the aliases
echo "" >> ~/.zshrc
echo "# For Work-env" >> ~/.zshrc
echo "alias enter=~/.work-env/enterzshell.sh" >> ~/.zshrc
echo "alias sync=~/.work-env/sync.sh" >> ~/.zshrc
echo "alias cli=\"python3 ~/.work-env/scripts/cli.py\"" >> ~/.zshrc
echo "WORK_ENV_BRANCH=\"master\"" >> ~/.zshrc