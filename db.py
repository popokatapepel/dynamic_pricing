# coding: utf-8
from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, Table, Text
from sqlalchemy.sql.sqltypes import NullType
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Industry(Base):
    __tablename__ = 'industries'

    id = Column(Integer, primary_key=True)
    name = Column(Integer, nullable=False)


class ProductGroup(Base):
    __tablename__ = 'product_groups'

    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)


t_sqlite_sequence = Table(
    'sqlite_sequence', metadata,
    Column('name', NullType),
    Column('seq', NullType)
)


class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    name = Column(Integer, nullable=False)
    industry_id = Column(ForeignKey('industries.id'))

    industry = relationship('Industry')


class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)
    product_group_id = Column(ForeignKey('product_groups.id'))

    product_group = relationship('ProductGroup')


class Sale(Base):
    __tablename__ = 'sales'

    id = Column(Integer, primary_key=True)
    amount = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)
    product_id = Column(ForeignKey('products.id'), nullable=False)
    customer_id = Column(ForeignKey('customers.id'), nullable=False)
    date = Column(DateTime, nullable=False)

    customer = relationship('Customer')
    product = relationship('Product')
