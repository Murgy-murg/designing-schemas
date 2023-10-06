CREATE TABLE posts(
    id SERIAL PRIMARY KEY,
    title text,
    contents text
);
CREATE TABLE comments(
    id SERIAL PRIMARY KEY,
    content text,
    auther text,
    post_id int,
    constraint fk_cohort foreign key(post_id) references posts(id) on delete cascade
);

