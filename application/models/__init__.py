from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

from models.billing import Billing
from models.class_has_costumer import ClassHasCostumer
from models.class_has_employee import ClassHasEmployee
from models.customer import Customer
from models.employee import Employee
from models.gym_class import Gymclass
from models.membership import Membership
from models.people import People
from models.physical_assessment import PhysicalAssessment
from models.place_has_products import PlaceHasProducts
from models.place import Place
from models.products import Products
from models.purchase_has_products import PurchaseHasProducts
from models.purchase import Purchase
from models.workout_plan import WorkoutPlan

