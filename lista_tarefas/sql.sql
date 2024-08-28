CREATE DATABASE lista_tarefas;

USE lista_tarefas;

CREATE TABLE tarefas
(
    data varchar(255),
    tarefa varchar(255)
);

CREATE TABLE tarefas_concluidas
(
    data varchar(255),
    tarefa varchar(255)
);