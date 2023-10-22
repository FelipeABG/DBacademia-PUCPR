use academia;

/* Média salarial por cargo na rede*/
    select position as Cargo, avg(salary) as "Média salarial"
        from employee
        group by position;

/* Gasto salarial por cargo na rede */
    select position as Cargo, sum(salary) as "Gasto salarial"
        from employee
        group by position;

/* Gasto total mensal por estabelecimento */
    select place_name ,sum(salary) + rent_price as "Gasto total"
        from place
        join employee
        where employee.place_id = place.id
        group by place.id;

/* Receita por estabelecimento */
    select place_name, (sum(purchase.price) + ( sum(class.price)* count(class_has_customer.customer_id) ) + ( sum(membership.price) * count(membership.id)) ) as "Receita total"
        from billing
        join employee
        on employee.id = billing.employee_id
        join place
        on place.id = employee.place_id
        join purchase
        on purchase.id = billing.purchase_id
        join class
        on class.id = billing.class_id
        join class_has_customer
        on class_has_customer.class_id = class.id
        join membership
        on membership.id = billing.membership_id
        group by place.id;

/* Lucro por estabelecimento */
    select place_name, (sum(purchase.price) + (sum(class.price)* count(class_has_customer.customer_id)) + (sum(membership.price) * count(membership.id))) - (place.rent_price + sum(employee.salary)) as "Lucro total"
        from billing
        join employee
        on employee.id = billing.employee_id
        join place
        on place.id = employee.place_id
        join purchase
        on purchase.id = billing.purchase_id
        join class
        on class.id = billing.class_id
        join class_has_customer
        on class_has_customer.class_id = class.id
        join membership
        on membership.id = billing.membership_id
	    group by place.id;


/* Idade média dos alunos por estabelecimento */
    select place_name, avg(year(now()) - year(birth_date)) as "Média de idade"
        from place
        join employee
        on place.id = employee.place_id
        join workout_plan
        on workout_plan.employee_id = employee.id
        join customer
        on customer.id = workout_plan.customer_id
        join people
        on people.id = customer.id
        group by place.id
        order by avg(year(now()) - year(birth_date)) asc;

/* Peso médio dos alunos por estabelecimento */
    select place_name, avg(weight) as "Peso médio"
        from place
        join employee
        on place.id = employee.place_id
        join physical_assessment
        on physical_assessment.employee_id = employee.id
        group by place.id;

/* Quantidade de alunos por plano por estabelecimento */
    select place_name, membership_type as "Plano", count(customer.id) as "Quantidade de alunos"
        from membership
        join customer
        on customer.id = membership.customer_id
        join workout_plan 
        on customer.id = workout_plan.customer_id
        join employee
        on employee.id = workout_plan.employee_id
        join place
        on place.id = employee.place_id
        group by place.id, membership_type;
    
/* Idade média dos funcionários por estabelecimento */
    select place_name ,avg(year(now()) - year(birth_date)) as "Média de idade"
        from place
        join employee
        on place.id = employee.place_id
        join people
        on people.id = employee.id
        group by place.id
        order by avg(year(now()) - year(birth_date)) asc;

/* Receita total por forma de pagamento por mês por estabelecimento*/
    select place_name, payment_method as "Forma de pagamento", sum(total) as "Receita"
        from billing 
        join employee
        on billing.employee_id = employee.id
        join place
        on place.id = employee.place_id 
        group by place.id, payment_method;

/* Gasto salarial mensal por estabelecimento */
    select place_name, sum(salary) as "Gasto salarial mensal"
        from place
        join employee
        on place.id = employee.place_id
        group by place.id;
    
/* Receita por tipo de produto vendido por estabelecimento */ 
    select place_name, product_type as tipo, sum(price) as "Receita por tipo"
        from purchase_has_products
        join place_has_products
        on purchase_has_products.product_id = place_has_products.product_id
        join place
        on place.id = place_has_products.place_id
        join products
        on products.id = purchase_has_products.product_id
        group by product_type, place.id;

/* Quantidade de alunos por aula por estabelecimento*/
    select place_name, class_type ,count(customer_id)
        from class
        join class_has_customer
        on class.id = class_has_customer.class_id
        join class_has_employee
        on class_has_employee.class_id = class.id
        join employee
        on employee.id = class_has_employee.employee_id
        join place
        on place.id = employee.place_id
        group by place.id, class_type;

/* Quantidade de alunos por estabelecimento */
    select place_name, count(workout_plan.customer_id) as "Quantidade de alunos"
        from place
        join employee
        on employee.place_id = place.id
        join workout_plan 
        on workout_plan.employee_id = employee.id
        group by place.id;
    

/* Quantidade de cobranças em atraso por estabelecimento*/
select place_name, count(billing.id) as "Quantidade de cobranças atrasadas"
	from billing 
	join employee
	on employee.id = billing.employee_id 
	join place 
	on place.id = employee.place_id
    where due_datetime < now()
    group by place.id;
		

/* Quantidade de funcionários por cargo por estabelecimento */ 
    select place_name, position as "Cargo" ,count(position) as "Quantidade de funcionários"
        from employee
        join place
        on place.id = employee.place_id
        group by position, place.id;

/* Quantidade de funcionários de um estabelecimento */
    select place_name ,count(employee.id) "Quantidade de funcionários"
        from place
        join employee
        on employee.place_id = place.id
        group by place.id;

/* Quantidade de produtos por tipo na rede */
    select product_type, sum(amount) as "Quantidade de produtos" 
        from products
        group by product_type
        order by sum(amount) asc;

/* Quantidade de produtos por estabelecimento */
    select place_name, sum(amount) as "Quantidade total de produtos"
        from place
        join place_has_products
        on place.id = place_has_products.place_id
        join products
        on products.id = place_has_products.product_id
        group by place.id;

/* Quantidade de produtos vendidos por estabelecimento*/
    select place_name, count(purchase_has_products.product_id) "Quantidade de produtos vendidos"
        from purchase 
        join purchase_has_products
        on purchase.id = purchase_has_products.purchase_id
        join billing
        on billing.purchase_id = purchase.id
        join employee
        on employee.id = billing.employee_id
        join place
        on place.id = employee.place_id
        group by place.id;




/* View do lucro de cada estabelecimento */
    create view lucro as 
        select place_name, (sum(purchase.price) + ( sum(class.price)* count(class_has_customer.customer_id) ) + ( sum(membership.price) * count(membership.id)) ) - (place.rent_price + sum(employee.salary)) as "Receita total"
            from billing
            join employee
            on employee.id = billing.employee_id
            join place
            on place.id = employee.place_id
            join purchase
            on purchase.id = billing.purchase_id
            join class
            on class.id = billing.class_id
            join class_has_customer
            on class_has_customer.class_id = class.id
            join membership
            on membership.id = billing.membership_id
            group by place.id;

/* View de receita de cada estabelecimento */
    create view receita as
        select place_name, (sum(purchase.price) + ( sum(class.price)* count(class_has_customer.customer_id) ) + ( sum(membership.price) * count(membership.id)) ) as "Receita total"
        from billing
            join employee
            on employee.id = billing.employee_id
            join place
            on place.id = employee.place_id
            join purchase
            on purchase.id = billing.purchase_id
            join class
            on class.id = billing.class_id
            join class_has_customer
            on class_has_customer.class_id = class.id
            join membership
            on membership.id = billing.membership_id
            group by place.id;

/* view de gasto totais de cada estabelecimento */
    create view gastos as 
        select place_name ,sum(salary) + rent_price as "Gasto total"
            from place
            join employee
            where employee.place_id = place.id
            group by place.id;