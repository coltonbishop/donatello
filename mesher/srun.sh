#!/bin/bash

srun \
  --job-name=test \
  --mail-user=cmbishop@cs.princeton.edu \
  --mail-type=FAIL \
  --ntasks=1 \
  --cpus-per-task=2 \
  --mem=16384 \
  --gres=gpu:1 \
  --time=01-00:00:00 \
  --pty bash
