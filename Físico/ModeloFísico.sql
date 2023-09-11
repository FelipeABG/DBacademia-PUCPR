drop database if exists academia;
create database if not exists academia;

use academia;

create table people(
    id int primary key auto_increment not null,
    person_name varchar(45) not null,
    cpf varchar(11) not null unique,
    phone varchar(11) not null,
    birth_date date not null
);

create table place(
    id int primary key auto_increment not null,
    place_name varchar(45) not null,
    rent_price decimal(8,2) not null,
    cep varchar(10) not null, 
    phone_number smallint(4) not null,
    city varchar(20) not null,
    neighborhood varchar(45) not null,
    street varchar(100) not null,
    place_state varchar(2) not null
);

create table employee(
    id int primary key,
    position varchar(45) not null,
    salary decimal(8,2) not null,
    place_id int,
    foreign key(place_id) references place(id),
    foreign key(id) references people(id)
);

create table customer(
	id int primary key,
    foreign key(id) references people(id)
);

create table workout_plan(
    exercises varchar(150) not null,
    start_date date not null,
    days smallint(3) not null,
    customer_id int,
    employee_id int,
    foreign key(customer_id) references customer(id),
    foreign key(employee_id) references employee(id)
);


create table physical_assessment(
    height decimal(3,2) not null,
    weight decimal(4,2) not null,
    assessment_date datetime not null,
    physical_problems varchar(300),
    customer_id int,
    employee_id int,
    foreign key(customer_id) references customer(id),
    foreign key(employee_id) references employee(id)
);

create table purchase(
    id int primary key auto_increment not null,
    price decimal(8,2) not null,
    customer_id int,
    foreign key(customer_id) references customer(id)
);

create table class(
    id int primary key auto_increment not null,
    class_datetime datetime not null,
    class_type enum('spinning', 'zumba', 'pilates') not null,
    price decimal(5,2) not null
);

create table membership(
    id int primary key auto_increment not null,
    price decimal(8,2) not null,
    membership_name varchar(45) not null,
    membership_type enum('mensal', 'trimestral', 'semestral', 'anual') not null,
    customer_id int,
    foreign key(customer_id) references customer(id)
);

create table billing(
    id int primary key auto_increment not null,
    payment_method enum('credit card', 'debit card', 'pix') not null,
    total decimal(8,2) not null,
    billing_datetime datetime not null,
    due_datetime datetime not null,
    employee_id int,
    class_id int,
    purchase_id int,
    membership_id int,
    foreign key(employee_id) references employee(id),
    foreign key(class_id) references class(id),
    foreign key(purchase_id) references purchase(id),
    foreign key(membership_id) references membership(id)
);

create table products(
    id int primary key auto_increment not null,
    product_name varchar(256) not null,
    product_type enum('suplemento', 'comida', 'bebida') not null,
    price decimal(8,2) not null,
    amount smallint(5) not null
);

create table class_has_employee(
    class_id int,
    employee_id int,
    foreign key(class_id) references class(id),
    foreign key(employee_id) references employee(id),
    primary key(class_id, employee_id)
);

create table class_has_customer(
    class_id int,
    customer_id int,
    foreign key(class_id) references class(id),
    foreign key(customer_id) references customer(id),
	primary key(class_id, customer_id)
);

create table place_has_products(
    place_id int,
    product_id int,
    aquisition_date datetime not null,
    foreign key(place_id) references place(id),
    foreign key(product_id) references products(id),
    primary key(place_id, product_id)
);

create table purchase_has_products(
    purchase_id int,
    product_id int,
    foreign key(purchase_id) references purchase(id),
    foreign key(product_id) references products(id),
    primary key(purchase_id, product_id)
);
