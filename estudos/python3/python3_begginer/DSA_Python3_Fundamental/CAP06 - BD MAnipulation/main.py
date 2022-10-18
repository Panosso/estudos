import DSA_sqlite as dsasql
import os
os.remove("school.db") if os.path.exists("school.bd") else None

if __name__ == '__main__':
    dsasql.examples()

