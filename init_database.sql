-- Date: 2021-06-06 15:00:00
-- Database: sqlite
-- Author: murali krishnan
-- Description: This is a sample database schema for an e-commerce website

create table users(
    user_id integer primary key autoincrement,
    username varchar(255) NOT NULL,
    fullname varchar(255) NOT NULL,
    password varchar(255) NOT NULL,
    active bool default 1
);

create table roles(
    role_id integer primary key autoincrement,
    role_name varchar(255) NOT NULL,
    description text,
    active bool default 1
);

create table permissions( 
    permission_id integer primary key autoincrement,
    permission_name varchar(255) NOT NULL,
    description text,
    active bool default 1
);

create table role_permissions(
    role_permission_id integer primary key autoincrement,
    role_id integer,
    permission_id integer,
    foreign key (role_id) references roles(role_id),
    foreign key (permission_id) references permissions(permission_id)
);

create table users_roles(
    user_role_id integer primary key autoincrement,
    user_id integer,
    role_id integer,
    foreign key (user_id) references users(user_id),
    foreign key (role_id) references roles(role_id)
);

create table categories (
    category_id integer primary key autoincrement,
    category_name varchar(255) NOT NULL,
    category_desc text,
    active bool default 1
);

create table products(
    product_id integer primary key autoincrement,
    category_id integer, 
    product_name varchar(255) NOT NULL,
    prod_desc text,
    price decimal(10,2),
    active bool default 1,
    foreign key (category_id) references categories(category_id)
);

create table cart(
    cart_id integer primary key autoincrement,
    user_id integer,
    payment_done bool default 0
);

create table cart_items(
    cart_item_id integer primary key autoincrement,
    cart_id integer,
    product_id integer NOT NULL,
    quantity integer,
    price decimal(10,2),
    foreign key (cart_id) references cart(cart_id),
    foreign key (product_id) references products(product_id)
);

create table payment_modes(
    payment_mode_id integer primary key autoincrement,
    payment_mode_name varchar(255) NOT NULL,
    description text,
    active bool default 1
);

insert into payment_modes(payment_mode_name, description) values ('credit_card', 'Credit Card');
insert into payment_modes(payment_mode_name, description) values ('debit_card', 'Debit card');
insert into payment_modes(payment_mode_name, description) values ('net_banking', 'Netbanking');
insert into payment_modes(payment_mode_name, description) values ('upi', 'UPI');

insert into categories (category_name, category_desc) values ('Footwear','Shoes, slippers, sandals');
insert into categories (category_name, category_desc) values ('Household','daily household items');
insert into categories (category_name, category_desc) values ('Toys', 'kids toys');
insert into categories (category_name, category_desc) values ('Sports', 'sports items');

insert into products(category_id, product_name, prod_desc, price) values (1, 'tshirt', 'round neck tshirt', 500);
insert into products(category_id, product_name, prod_desc, price) values (1, 'shirt', 'formal shirt', 1000);
insert into products(category_id, product_name, prod_desc, price) values (1, 'jeans', 'jeans pant', 1500);
insert into products(category_id, product_name, prod_desc, price) values (2, 'shoes', 'sports shoes', 2000);
insert into products(category_id, product_name, prod_desc, price) values (2, 'slippers', 'slippers', 500);
insert into products(category_id, product_name, prod_desc, price) values (2, 'sandals', 'sandals', 1000);
insert into products(category_id, product_name, prod_desc, price) values (3, 'soap', 'dove soap', 50);
insert into products(category_id, product_name, prod_desc, price) values (3, 'shampoo', 'clinic plus shampoo', 100);
insert into products(category_id, product_name, prod_desc, price) values (3, 'toothpaste', 'colgate toothpaste', 50);
insert into products(category_id, product_name, prod_desc, price) values (4, 'barbie', 'barbie doll', 500);
insert into products(category_id, product_name, prod_desc, price) values (4, 'car', 'remote control car', 1000);
insert into products(category_id, product_name, prod_desc, price) values (4, 'teddy', 'teddy bear', 500);
insert into products(category_id, product_name, prod_desc, price) values (5, 'bat', 'cricket bat', 500);
insert into products(category_id, product_name, prod_desc, price) values (5, 'ball', 'cricket ball', 50);
insert into products(category_id, product_name, prod_desc, price) values (5, 'gloves', 'cricket gloves', 500);


insert into users(username, fullname, password) values ('murali','Murali krishnan', 'abc123');
insert into users(username, fullname, password) values ('archana','Archana', 'abc123');
insert into users(username, fullname, password) values ('pappu','Prathyu', 'abc123');
insert into users(username, fullname, password) values ('vpk','VPK', 'abc123');

insert into roles(role_name, description) values ('admin', 'admin role');
insert into roles(role_name, description) values ('user', 'user role');

-- admin permissions

-- product permissions
insert into permissions(permission_name, description) values ('create_product', 'create permission');
insert into permissions(permission_name, description) values ('update_product', 'update permission');
insert into permissions(permission_name, description) values ('delete_product', 'delete permission');
insert into permissions(permission_name, description) values ('view_product', 'view permission');
-- category permissions
insert into permissions(permission_name, description) values ('create_category', 'create category permission');
insert into permissions(permission_name, description) values ('update_category', 'update category permission');
insert into permissions(permission_name, description) values ('delete_category', 'delete category permission');
insert into permissions(permission_name, description) values ('view_category', 'view category permission'); 

-- user permissions

-- cart permissions
insert into permissions(permission_name, description) values ('add_to_cart', 'add to cart permission');
insert into permissions(permission_name, description) values ('remove_from_cart', 'remove from cart permission');
insert into permissions(permission_name, description) values ('view_cart', 'view cart permission');
insert into permissions(permission_name, description) values ('checkout', 'checkout permission');

-- admin role permissions
insert into role_permissions(role_id, permission_id) values (1, 1);
insert into role_permissions(role_id, permission_id) values (1, 2);
insert into role_permissions(role_id, permission_id) values (1, 3);
insert into role_permissions(role_id, permission_id) values (1, 4);
insert into role_permissions(role_id, permission_id) values (1, 5);
insert into role_permissions(role_id, permission_id) values (1, 6);
insert into role_permissions(role_id, permission_id) values (1, 7);
insert into role_permissions(role_id, permission_id) values (1, 8);

-- users role permissions
insert into role_permissions(role_id, permission_id) values (2, 4);
insert into role_permissions(role_id, permission_id) values (2, 8);
insert into role_permissions(role_id, permission_id) values (2, 9);
insert into role_permissions(role_id, permission_id) values (2, 10);
insert into role_permissions(role_id, permission_id) values (2, 11);
insert into role_permissions(role_id, permission_id) values (2, 12);

insert into users_roles(user_id, role_id) values (1, 2);
insert into users_roles(user_id, role_id) values (2, 2);
insert into users_roles(user_id, role_id) values (3, 1);
insert into users_roles(user_id, role_id) values (4, 1);

-- Queries

-- To get the username and his corresponding roles

--  select u.fullname, r.role_name from users_roles as ur INNER JOIN users as u ON ur.user_id = u.user_id INNER JOIN roles as r ON ur.role_id = r.role_id ;

-- to obtain all permissions of all roles of all users

--  select u.fullname, r.role_name, p.permission_name from users_roles as ur INNER JOIN users as u ON ur.user_id = u.user_id INNER JOIN roles as r ON ur.role_id = r.role_id INNER JOIN role_permissions as rp ON r.role_id = rp.role_id INNER JOIN permissions as p ON rp.permission_id = p.permission_id ;

-- get permissions of a particular user

-- select u.fullname, r.role_name, p.permission_name from users_roles as ur INNER JOIN users as u ON ur.user_id = u.user_id INNER JOIN roles as r ON ur.role_id = r.role_id INNER JOIN role_permissions as rp ON r.role_id = rp.role_id INNER JOIN permissions as p ON rp.permission_id = p.permission_id  where u.user_id = 1;