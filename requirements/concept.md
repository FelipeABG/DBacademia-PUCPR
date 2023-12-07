# Objective

Our fitness centers has multiple establishments. Each establishment has its own staff and students, and we also sell products. The staff members are responsible for conducting classes, creating workout plans, performing physical assessments, handling billing, and selling products. Students have access to the gym, including workout plans and a mandatory physical assessment, and they can enroll in classes such as spinning, Zumba, etc.

## Database Requirements Analysis (Fitness Center)

### 1 - Students
- Name.
- Date of birth.
- CPF (Brazilian individual taxpayer registry identification).
- Phone number.
- ID.

_Relationships:_
- Have physical assessments.
- Have workout plans.
- Perform billing.
- Participate in classes.
- Can purchase products.

### 2 - Staff Members
- Name.
- Date of birth.
- CPF.
- Phone number.
- Position.
- Salary.
- ID.

_Relationships:_
- Conduct classes.
- Create workout plans.
- Perform physical assessments.
- Sell products.
- Handle billing.
- Belong to an establishment.

### 3 - Billing
- Amount.
- Billing date.
- Due date.
- Payment method.
- Status.
- ID.

### 4 - Workout Plan
- Exercises.
- Start date.
- Number of days.

### 5 - Establishment
- Name.
- Address.
- Rent.
- ID.

_Relationships:_
- Has products.

### 6 - Classes
- Type of class.
- Schedule.
- Date.
- ID.

_Relationships:_
- Have instructors.
- Attended by students.

### 7 - Physical Assessment
- Weight.
- Height.
- Medical issues.
- Date.

_Relationships:_
- Belong to students.
- Conducted by staff members.

### 8 - Products
- Name.
- Type.
- Price.
- Quantity.
- ID.

### 9 - Plans:
- Name.
- Price.
- Type.
- ID.

_Relationships:_
- Sold by staff members.
- Can be purchased by customers.
- Belong to the establishment.

# Functional Requirements:
- Average salary per position in the network.
- Monthly salary expenditure in the network.
- Total monthly expenditure per establishment.
- Revenue per establishment.
- Profit per establishment.
- Average age of students per establishment.
- Average weight of students per establishment.
- Number of students per plan per establishment.
- Average age of staff members per establishment.
- Total revenue per payment method per month per establishment.
- Monthly salary expenditure per establishment.
- Revenue per type of product sold per establishment.
- Number of students per class per establishment.
- Number of students per establishment.
- Number of overdue bills per establishment.
- Number of staff members per position per establishment.
- Number of staff members in an establishment.
- Number of products per type.
- Number of products per establishment.
- Number of products sold per establishment.

