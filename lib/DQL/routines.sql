use academia;

/* insere um novo funcionario no banco de dados */ 
delimiter $$
    create procedure insert_employee(in nome varchar(45), in cpf varchar(11), in phone varchar(11), in birth_date date, in position varchar(45), in salary decimal(8,2), in place_id smallint(4))
        begin
			
            declare person_id smallint(3);

            insert into people (person_name, cpf, phone, birth_date) values
                (nome, cpf, phone, birth_date);
				
			set person_id = (select last_insert_id());

            insert into employee (id, position, salary, place_id) values
                (person_id, position, salary, place_id);

        end $$
delimiter ;

/*Retorna os gastos salariais de determinada academia*/
delimiter $$
    create procedure salary_spendings(in gym varchar(100))
        begin
			
            declare break smallint(1) default 0;
            declare placeholder decimal(8,2);
            declare gastos decimal (10,2) default 0;
            declare iterator cursor for select salary from employee where place_id = (select id from place where place_name = gym);
            declare continue handler for not found set break = 1;

            open iterator;

            while(break = 0)do
                fetch iterator into placeholder;
                set gastos = gastos + placeholder;
            end while;

        select gym, gastos;

        end $$
delimiter ;


/* retorna os estabelecimentos com alugueis acima do determinado */
delimiter $$
    create procedure check_rent_price(in price decimal(8,2))
        begin

            select place_name, rent_price
                from place
                where rent_price > price;

        end $$
delimiter ;




/* Funcao que determinar se uma peessoa é maior de idade. */
delimiter $$
    create function is_legal_age(cpf varchar(11))
    returns boolean deterministic
        begin

            declare age varchar(100);
            declare birth date;
			
            set birth = (select birth_date from people where people.cpf = cpf);
            set age = year(now()) - year(birth);

			if(age >= "18")then
				return True;
            else
				return False;
            end if;

        end $$
delimiter ;

/* Função que retorna a situação do cliente baseado em seu IMC */
delimiter $$
    create function imc(client_id int)
    returns varchar(40) deterministic
        begin

            declare result varchar(40);
            declare imc decimal(5,2);
            declare person_weight decimal(5,2);
            declare person_height decimal(5,2);

            set person_weight = (select weight from physical_assessment where customer_id = client_id);
            set person_height = (select height from physical_assessment where customer_id = client_id);

            set imc = person_weight / (person_height * person_height);

            set result = (select case when
                            imc < 17 then "Muito abaixo do peso"
                            when imc >= 17 and imc <= 18.49 then "Abaixo do peso"
                            when imc > 18.49 and imc <= 24.99 then "Peso Normal"
                            when imc > 18.49 and imc <=29.99 then "Acima do peso"
                            when imc > 29.99 then "Obeso" end);
            return result;

        end $$
delimiter ;

/* Função que retorna a quantidade de treinos que um cliente possui */
delimiter $$
    create function workouts(person_id int)
    returns int deterministic
        begin

            return (select count(customer_id) from workout_plan where customer_id = person_id);

        end $$
delimiter ;



/* Adiciona automaticamente a data de vencimento como o ultimo dia do ano na tabela billing */
create trigger add_date before insert on billing
    for each row 
        set new.due_datetime = concat_ws("-", convert(year(new.billing_datetime), char), "12-31 23:59:59");

/* Deleta o Treino e a avaliação física do cliente sendo deletado*/ 
delimiter $$
	create trigger delete_data before delete on customer 
		for each row begin
			
            delete from workout_plan where customer.id = old.id;
            delete from physical_assessment where customer.id = old.id;
            
        end $$
delimiter ;

/* Atualiza todos os salarios quando um salario é modificado */ 
create trigger change_salary before update on employee
    for each row
        update employee
            set salary = new.salary
        where position = new.position;
