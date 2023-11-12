use academia;
set autocommit = false;

/* insere um novo funcionario no banco de dados, se houver algum erro nao há commit */ 
delimiter $$
    create procedure insert_employee(in nome varchar(45), in cpf varchar(11), in phone varchar(11), in birth_date date, in position varchar(45), in salary decimal(8,2), in place_id smallint(4))
        begin

			declare person_id smallint(3);
            declare sql_erro int default false;
            declare continue handler for sqlexception set sql_erro = true;

            start transaction;
                insert into people (person_name, cpf, phone, birth_date) values
                    (nome, cpf, phone, birth_date);
                    
                set person_id = (select last_insert_id());

                insert into employee (id, position, salary, place_id) values
                    (person_id, position, salary, place_id);
            if(sql_erro = false)then
                commit;
            else
                rollback;
            end if;
            
        end $$
delimiter ;

/*Retorna os gastos salariais de determinada academia, caso algum erro ocorra no loop a transaction volta para antes dele.*/
delimiter $$
    create procedure salary_spendings(in gym varchar(100))
        begin

            declare break smallint(1) default 0;
            declare placeholder decimal(8,2);
            declare gastos decimal (10,2) default 0;
			declare sql_error int default false;
            declare iterator cursor for select salary from employee where place_id = (select id from place where place_name = gym);
            declare continue handler for not found set break = 1;
            declare continue handler for sqlexception set sql_error = true;

            open iterator;
            start transaction;
                savepoint before_loop;
                while(break = 0)do
                    fetch iterator into placeholder;
                    set gastos = gastos + placeholder;
                end while;
            if(sql_error = false)then
                commit;
                select gym, gastos;
            else
                rollback to before_loop;
            end if;
        end $$
delimiter ;

-- Insere um novo cliente no banco de dados com todas as suas informações (treino, exame, aulas).
start transaction;
    insert into people (person_name, cpf, phone, birth_date) values 
        ("Claudair", "00000000055", "41999845127", "1945-10-10");
    insert into workout_plan (exercises, start_date, days, customer_id, employee_id) values 
        ("Treino A(Costas e biceps) B(Perna) C(Peito, triceps e ombro)", "2023-01-01", 40, 1, 4);
    insert into physical_assessment (height, weight, assessment_date, physical_problems, customer_id, employee_id) values 
        (1.90, 95.0, now(), "Joelho ruim", 40, 6);
    insert into class (class_datetime, class_type, price) values 
        ("2023-12-01 09:00:00", "spinning", 250.00);
    insert into membership (price, membership_type, customer_id) values
        (150.00, "mensal", 40),
commit;