use aula;

create table aluno(
    id int primary key auto_increment,
    nome varchar(200) not null,
    telefone varchar(20),
    email varchar(200)
);

select * from aluno;

insert aluno(nome, telefone, email)
values('Isabella Nunes', '11912345678', 'isa.bela@aprendendodoinicio.com.br'),
('Vilma Nunes', '11987654321', 'vilma.nunes@aprendendodoinicio.com.br'),
('Osvaldo', '11965432187', 'osvaldo@pro.fecaf.com.br'),
('Nelson', '11963258741', 'nelson@fecaf.com.br'),
('Daniel Xavier', '11987456321', 'daniel@pro.fecaf.com.br'),
('Luis', '11932145698', 'luis@pro.fecaf.com.br');