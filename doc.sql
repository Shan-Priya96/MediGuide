 create database doc;
 use doc; 
 create table doctors(name varchar(100), location varchar(100), contact int(10), timings varchar(100), rating varchar(10));
 alter table doctors add column specialisation varchar(100);
 alter table doctors add column reg_id int(5);
 alter table doctors add primary key(reg_id);
