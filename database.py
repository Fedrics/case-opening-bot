from sqlalchemy import Column, Integer, String, Float, DateTime, Boolean, JSON, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine
from datetime import datetime
import config

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True)
    telegram_id = Column(Integer, unique=True, index=True)
    username = Column(String, nullable=True)
    first_name = Column(String, nullable=True)
    last_name = Column(String, nullable=True)
    balance = Column(Float, default=0.0)
    total_spent = Column(Float, default=0.0)
    total_won = Column(Float, default=0.0)
    cases_opened = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.utcnow)
    last_activity = Column(DateTime, default=datetime.utcnow)
    is_active = Column(Boolean, default=True)
    
    # Relationships
    case_openings = relationship("CaseOpening", back_populates="user")
    transactions = relationship("Transaction", back_populates="user")

class CaseOpening(Base):
    __tablename__ = "case_openings"
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    case_type = Column(String)
    case_price = Column(Float)
    reward_name = Column(String)
    reward_value = Column(Float)
    reward_rarity = Column(String)
    opened_at = Column(DateTime, default=datetime.utcnow)
    
    # Relationship
    user = relationship("User", back_populates="case_openings")

class Transaction(Base):
    __tablename__ = "transactions"
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    transaction_type = Column(String)  # 'deposit', 'case_purchase', 'reward'
    amount = Column(Float)
    payment_method = Column(String, nullable=True)  # 'stars', 'cryptobot'
    payment_id = Column(String, nullable=True)
    status = Column(String, default="pending")  # 'pending', 'completed', 'failed'
    description = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    completed_at = Column(DateTime, nullable=True)
    
    # Relationship
    user = relationship("User", back_populates="transactions")

class PaymentInvoice(Base):
    __tablename__ = "payment_invoices"
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    invoice_id = Column(String, unique=True)
    amount = Column(Float)
    currency = Column(String)
    status = Column(String, default="pending")
    payment_method = Column(String)  # 'stars', 'cryptobot'
    created_at = Column(DateTime, default=datetime.utcnow)
    paid_at = Column(DateTime, nullable=True)
    
    # Additional fields for Telegram Stars
    stars_amount = Column(Integer, nullable=True)
    
    # Additional fields for CryptoBot
    crypto_invoice_id = Column(Integer, nullable=True)
    crypto_hash = Column(String, nullable=True)

# Database engine and session
engine = create_engine(config.DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def create_tables():
    """Create all database tables"""
    Base.metadata.create_all(bind=engine)

def get_db():
    """Get database session"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Initialize database
if __name__ == "__main__":
    create_tables()
    print("Database tables created successfully!")