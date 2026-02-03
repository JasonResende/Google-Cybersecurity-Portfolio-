# Project: Linux File Permissions & Audit Log Analysis

## Scenario
As a Security Analyst, I was tasked with auditing a research team's Linux directory. The goal was to ensure the "Principle of Least Privilege" was being followed—making sure no one has access to files they don't need for their job.

## Part 1: Managing File Permissions
I discovered several files with incorrect permissions. Below are the commands I used to secure them:

### 1. Checking Existing Permissions
I used the `ls -la` command to view all files, including hidden ones, and their current permission strings.
```bash
ls -la /home/researcher/projects

## 2. Removing 'Write' Access for 'Other' Users
## The file project_k.txt allowed "others" to write to it. I removed this to prevent unauthorized changes.

chmod o-w project_k.txt

## 3. Securing Hidden Files
## A hidden archive file .project_x.txt was accessible to the public. I changed it so only the User and Group could read it, and no one could write to it.

chmod 640 .project_x.txt
'''bash 

## Part 2: Analyzing System Logs
## I reviewed the system logs to identify failed login attempts that might indicate a brute-force attack.

## 1. Searching for Authentication Failures
##I used grep to filter the auth.log file for any failed password attempts.

grep "Failed password" /var/log/auth.log

## 2. Identifying the Target Account
## I narrowed the search to see which specific username was being targeted the most.

grep "Failed password" /var/log/auth.log | awk '{print $9}' | sort | uniq -c
