
# Chmod the other files
chmod +x ~/.work-env/sync.sh
chmod +x ~/.work-env/enterbash.sh

# Set the aliases
echo "" >> ~/.bashrc
echo "# For Work-env" >> ~/.bashrc
echo "alias enter=~/.work-env/enterbash.sh"  >> ~/.bashrc
echo "alias sync=~/.work-env/sync.sh" >> ~/.bashrc
echo "alias cli=\"python3 ~/.work-env/scripts/cli.py\"" >> ~/.bashrc
echo "WORK_ENV_BRANCH=\"master\"" >> ~/.bashrc
