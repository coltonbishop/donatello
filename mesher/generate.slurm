#!/bin/bash
#SBATCH --gres=gpu:4
#SBATCH --mem=16384
#SBATCH --time=1:01:00
source /n/fs/donatello/temp/anaconda2/bin/activate myenv; python demo.py --image image.png
