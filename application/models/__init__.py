from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

from models.people import People
from models.gym_class import GymClass
from models.products import Products
from models.place import Place
from models.place_has_products import PlaceHasProducts
from models.customer import Customer
from models.purchase import Purchase
from models.membership import Membership
from models.class_has_customer import ClassHasCustomer
from models.employee import Employee
from models.class_has_employee import ClassHasEmployee
from models.billing import Billing
from models.workout_plan import WorkoutPlan
from models.purchase_has_products import PurchaseHasProducts
from models.physical_assessment import PhysicalAssessment
