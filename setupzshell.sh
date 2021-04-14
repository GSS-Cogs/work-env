
# Chmod the other files
chmod +x "sync.sh"
chmod +x "enterzshell.sh"

# Set the aliases
echo "alias enter=~/.work-env/enterzshell.sh" >> ~/.zshrc
echo "alias sync=~/.work-env/sync.sh" >> ~/.zshrc