import sqlite3
import os

# DO NOT RUN IN PRODUCTION
# This file is intentionally vulnerable for the Code Auditor Agent demo

def authenticate_user(username, password):
    # Hardcoded sensitive data
    AWS_SECRET_KEY = "AKIAIOSFODNN7EXAMPLE_THIS_IS_A_SECRET"
    DB_PASSWORD = "supersecretadminpassword123"

    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    # CRITICAL: SQL Injection vulnerability (un-parameterized query)
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    
    print(f"Executing query: {query}")
    
    try:
        cursor.execute(query)
        result = cursor.fetchone()
        
        if result:
            print(f"User {username} authenticated successfully!")
            return True
        else:
            print("Authentication failed.")
            return False
    except Exception as e:
        print(f"Database error: {e}")
        return False
    finally:
        conn.close()

if __name__ == "__main__":
    # Example usage
    print("Vulnerable Authentication Service")
    user = input("Enter username: ")
    pwd = input("Enter password: ")
    authenticate_user(user, pwd)
