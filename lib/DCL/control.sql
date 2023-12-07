-- Cria role admin que garante administração completa do banco de dados e da essa permissão ao usuario admin.
create role "admin";

grant all on *.* to "admin" with grant option;

create user "admin"@"localhost" identified by "admin";

grant "admin" to "admin"@"localhost";


-- Cria role manager que garante administração completa do banco de dados da academia e da essa permissão ao usuario manager.
create role "manager";

grant all on academia.* to "manager" with grant option;

create user "manager"@"localhost" identified by "manager";

grant "manager" to "manager"@"localhost";


-- Cria role customer que garante acesso de leitura ao treino, as aulas, e o exames médicos e da essa permissão a 2 usuários.
create role "customer";

grant select on academia.workout_plan to "customer";
grant select on academia.physical_assessment to "customer";
grant select on academia.class_has_customer to "customer";

create user "customer"@"localhost" identified by "customer";
create user "customer2"@"localhost" identified by "customer";

grant "customer" to "customer"@"localhost";


-- Cria role instructor que garante acesso de leitura e escrita ao treino, as aulas, e o exames médicos e da essa permissão ao usuario instructor.
create role "instructor";

grant select, insert, update, delete on academia.workout_plan to "instructor";
grant select, insert, update, delete on academia.physical_assessment to "instructor";
grant select, insert, update, delete on academia.class_has_customer to "instructor";

create user "instructor"@"localhost" identified by "instructor";

grant "instructor" to "instructor"@"localhost";


-- Cria role accountant que garante acesso de leitura e escrita ao pagamentos, produtos e planos de assinatura, e da essa permisson ao usuario accountant.
create role "accountant";

grant select, insert, update, delete on academia.billing to "accountant";
grant select, insert, update, delete on academia.purchase to "accountant";
grant select, insert, update, delete on academia.membership to "accountant";
grant select, insert, update, delete on academia.purchase_has_products to "accountant";

create user "accountant"@"localhost" identified by "accountant";

grant "accountant" to "accountant"@"localhost";