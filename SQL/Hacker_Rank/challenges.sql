create table hackers (hacker_id integer , name varchar(15));

create table challenges (challenge_id integer , hacker_id integer);


insert into hackers values (5077,"Rose");
insert into hackers values (21283,"Angela");
insert into hackers values (62743,"Frank");
insert into hackers values (88255,"Patrick");
insert into hackers values (96196,"Lisa");

insert into challenges values (61654,5077);
insert into challenges values (58302,21283);
insert into challenges values (40587,88255);
insert into challenges values (29477,5077);
insert into challenges values (1220,21283);
insert into challenges values (69514,21283);
insert into challenges values (46561,62743);
insert into challenges values (58077,62743);
insert into challenges values (18483,88255);
insert into challenges values (76766,21283);
insert into challenges values (52382,5077);
insert into challenges values (74467,21283);
insert into challenges values (33625,96196);
insert into challenges values (26053,88255);
insert into challenges values (42665,62743);
insert into challenges values (12859,62743);
insert into challenges values (70094,21283);
insert into challenges values (34599,88255);
insert into challenges values (54680,88255);
insert into challenges values (61881,5077);

=========================================================================

select max(counts) from (
select hacker_id , 
       count(challenge_id)counts
from challenges 
group by hacker_id)a;

with set_a as (
    select hacker_id , 
           count(challenge_id)counts
    from challenges 
    group by hacker_id
)
select a.hacker_id , b.name , a.counts from set_a a
inner join hackers b
on a.hacker_id = b.hacker_id
order by a.counts desc ,
         b.name  
         

with set_a as (
    select hacker_id , 
           count(challenge_id)counts
    from challenges 
    group by hacker_id
)
select count(hacker_id) from set_a group by counts;