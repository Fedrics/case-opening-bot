"""
Database initialization script with proper BigInteger for telegram_id
"""
from sqlalchemy import create_engine, text
import config
from database import Base, create_tables

def init_database():
    """Initialize database with proper schema"""
    engine = create_engine(config.DATABASE_URL)
    
    # Drop existing tables if they exist (for fresh start)
    try:
        with engine.connect() as conn:
            conn.execute(text("DROP TABLE IF EXISTS payment_invoices CASCADE;"))
            conn.execute(text("DROP TABLE IF EXISTS transactions CASCADE;"))
            conn.execute(text("DROP TABLE IF EXISTS case_openings CASCADE;"))
            conn.execute(text("DROP TABLE IF EXISTS users CASCADE;"))
            conn.commit()
            print("Dropped existing tables")
    except Exception as e:
        print(f"Error dropping tables (might not exist): {e}")
    
    # Create all tables with new schema
    Base.metadata.create_all(bind=engine)
    print("Created tables with BigInteger telegram_id")
    
    return engine

if __name__ == "__main__":
    init_database()