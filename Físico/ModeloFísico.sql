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

create table billing(
    id int primary key auto_increment not null,
    payment_method enum('credit card', 'debit card', 'pix') not null,
    total decimal(8,2) not null,
    billing_datetime datetime not null,
    due_datetime datetime not null,
    employee_id int,

);
