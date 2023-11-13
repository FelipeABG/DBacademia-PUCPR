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

/Retorna os gastos salariais de determinada academia, caso algum erro ocorra no loop a transaction volta para antes dele./
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


DELIMITER $$
CREATE PROCEDURE register_customer_class_and_purchase(IN person_name VARCHAR(45), IN cpf VARCHAR(11), IN phone VARCHAR(11), IN birth_date DATE,
                                                      IN class_id INT, IN product_id INT)
BEGIN
    START TRANSACTION;

    -- Inserir um novo cliente
    INSERT INTO people (person_name, cpf, phone, birth_date) VALUES 
        (person_name, cpf, phone, birth_date);
    SET @customer_id := LAST_INSERT_ID();

    -- Registrar participação em uma aula
    INSERT INTO class_has_customer (class_id, customer_id) VALUES
        (class_id, @customer_id);

    -- Comprar um produto
    INSERT INTO purchase (price, customer_id) VALUES
        (20.00, @customer_id);
    SET @purchase_id := LAST_INSERT_ID();

    INSERT INTO purchase_has_products (purchase_id, product_id) VALUES
        (@purchase_id, product_id);

    COMMIT;
END $$

DELIMITER ;


DELIMITER $$

-- Insere um novo produto no banco de dados.
CREATE PROCEDURE insert_product(IN product_name VARCHAR(256), IN product_type ENUM('suplemento', 'comida', 'bebida'), IN price DECIMAL(8,2), IN amount SMALLINT(5))
BEGIN
    START TRANSACTION;
    INSERT INTO products (product_name, product_type, price, amount) VALUES
        (product_name, product_type, price, amount);
    COMMIT;
END $$

DELIMITER ;

--Atualiza o salário de um funcionário.
DELIMITER $$

CREATE PROCEDURE update_employee_salary(IN employee_id INT, IN new_salary DECIMAL(8,2))
BEGIN
    START TRANSACTION;
    UPDATE employee SET salary = new_salary WHERE id = employee_id;
    COMMIT;
END $$

DELIMITER ;

--Registra a participação de um cliente em uma aula.
DELIMITER $$

CREATE PROCEDURE register_customer_for_class(IN class_id INT, IN customer_id INT)
BEGIN
    START TRANSACTION;
    INSERT INTO class_has_customer (class_id, customer_id) VALUES
        (class_id, customer_id);
    COMMIT;
END $$

DELIMITER ;

-- Tenta inserir um cliente sem fornecer CPF (vai falhar e dar rollback).
DELIMITER $$

CREATE PROCEDURE try_insert_customer_without_cpf(IN person_name VARCHAR(45), IN phone VARCHAR(11), IN birth_date DATE)
BEGIN
    START TRANSACTION;
    -- Esta inserção deve falhar devido à restrição NOT NULL no campo cpf
    INSERT INTO people (person_name, phone, birth_date) VALUES
        (person_name, phone, birth_date);
    ROLLBACK;
END $$

DELIMITER ;

-- Tenta atualizar o preço de uma aula para um valor negativo (vai falhar e dar rollback).
DELIMITER $$

CREATE PROCEDURE try_update_class_price_negative(IN class_id INT, IN new_price DECIMAL(5,2))
BEGIN
    START TRANSACTION;
    -- Esta atualização deve falhar devido ao valor negativo
    UPDATE class SET price = new_price WHERE id = class_id;
    ROLLBACK;
END $$

DELIMITER ;

-- Tenta comprar um produto sem fornecer um cliente (vai falhar e dar rollback).
DELIMITER $$

CREATE PROCEDURE try_purchase_without_customer(IN product_id INT)
BEGIN
    START TRANSACTION;
    -- Esta inserção deve falhar devido à restrição de chave estrangeira
    INSERT INTO purchase_has_products (purchase_id, product_id) VALUES
        (1, product_id);
    ROLLBACK;
END $$

DELIMITER ;

-- Inserir um cliente, salvar um ponto antes da compra e tentar inserir uma compra sem produtos (falha e da rollback ao savepoint).
DELIMITER $$

CREATE PROCEDURE insert_customer_and_try_purchase_without_products(IN person_name VARCHAR(45), IN cpf VARCHAR(11), IN phone VARCHAR(11), IN birth_date DATE)
BEGIN
    START TRANSACTION;
    INSERT INTO people (person_name, cpf, phone, birth_date) VALUES 
        (person_name, cpf, phone, birth_date);
    SAVEPOINT before_purchase;
    -- A próxima inserção deve falhar devido à restrição de chave estrangeira
    INSERT INTO purchase (price, customer_id) VALUES
        (50.00, LAST_INSERT_ID());
    ROLLBACK TO before_purchase;
    ROLLBACK;
END $$

DELIMITER ;