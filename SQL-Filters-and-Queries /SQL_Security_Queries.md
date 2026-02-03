# SQL Project: Investigating Unauthorized Access

### Scenario:
I need to identify security events that occurred outside of business hours or from unauthorized machines.

### 1. Finding Failed Login Attempts
I used this query to find any login attempts that failed (status '0') to identify potential brute-force attacks:
```sql

SELECT * FROM log_in_attempts 
WHERE login_time > '18:00' AND success = 0;

SELECT * FROM employees 
WHERE ip_address LIKE '192.168.1%';

SELECT device_id, department 
FROM machines 
WHERE department = 'Marketing';


