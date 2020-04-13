-- todo_schema.sql

-- Schema for to-do application examples.

-- books are my books info DB

create table books (
    id          integer primary key autoincrement not null,
    chi_title   text,
    eng_title   text,
    author      text,
    language    text default 'Chinese',
    volume      integer default 1,
    price       real,
    publisher   text
);

