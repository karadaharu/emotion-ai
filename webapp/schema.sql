drop table if exists votes;
create table votes (
  id integer primary key autoincrement,
  filename text unique not null,
  yes_count integer not null default 0,
  no_count integer not null default 0
);
