#! /bin/bash

# Make shure that the directory ./local/bin is executable

localbin=$HOME/.local/bin
scripts=$HOME/T-scripts/Scripts

echo "export PATH=$PATH:$localbin" >> ~/.bashrc
echo "export PATH=$PATH:$localbin" >> ~/.zshrc

# installing scripts
cp -r $scripts/* $localbin
