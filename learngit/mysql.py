查看引擎
SHOW TABLE STATUS from ideas_testing_automation where Name='Tasks'

查看版本
select version()

alter table prototype1.machine  add label varchar(50) NOT NULL DEFAULT '0';
    alter table test_service.tasks  add summary_level varchar(50) NOT NULL DEFAULT 'white';
	alter table test_service.subtasks  add ignored varchar(10) NOT NULL DEFAULT 'count';

ALTER TABLE prototype1.major_task  CHANGE task_name task_name varchar(100);

alter table machine rename machines;

mysqldump -h163.184.167.19 -uroot -pStereo888 --opt --compress test_service --skip-lock-tables | mysql -h localhost -uroot -ppassword test_service

$ mysqldump -u root -p database_name table_name > dump.txt
$ mysql -u root -p database_name < dump.txt

大概是振幅越高，频率越低，幅度谱亮点周围都是振幅高的--即低频分量，除去之后剩高频分量