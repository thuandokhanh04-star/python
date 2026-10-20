from app.core.db_check import check_database_connection


if check_database_connection():
    print("Ket noi PostgreSQL thanh cong!")