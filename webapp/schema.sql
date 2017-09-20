drop table if exists votes;
create table votes (
  id integer primary key autoincrement,
  filename text not null,
  count integer not null
);
