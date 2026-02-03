# Project: Linux File Permissions & Audit Log Analysis

## Scenario
As a Security Analyst, I was tasked with auditing a research team's Linux directory. The goal was to ensure the "Principle of Least Privilege" was being followed—making sure no one has access to files they don't need for their job.

## Part 1: Managing File Permissions
I discovered several files with incorrect permissions. Below are the commands I used to secure them:

### 1. Checking Existing Permissions
I used the `ls -la` command to view all files, including hidden ones, and their current permission strings.
```bash
ls -la /home/researcher/projects
