create or replace package std is



    procedure new_student(
                            nameStudent OUT VARCHAR2,
                            status out varchar2,
                            nameStudentIn in USER1.name%TYPE,
                            ageStudentIn in USER1.age%TYPE

                            );
end std;


create or replace package body std is

    procedure new_student(
                            nameStudent OUT VARCHAR2,
                            status out varchar2,
                            nameStudentIn in USER1.name%TYPE,
                            ageStudent in USER1.age%TYPE

                            ) is
                            begin
                            BEGIN
                            insert into student(name,age) values(namestudentIn,agestudentIn)
                            RETURNING name
                            INTO nameStudent;
                            COMMIT;
                            status:='ok';
                            EXCEPTION
                                WHEN DUP_VAL_ON_INDEX THEN
                                    status:='user already exists';
                                WHEN OTHERS THEN
                                    status:=SQLERRM;
                            END;
                            end new_student;
