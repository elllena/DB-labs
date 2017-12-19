-- змінні 
CREATE TABLE mypoint(id INT, point TINYINT, PRIMARY KEY (`id`));

INSERT INTO mypoint VALUES (0,0) --вкл/викл тригер
INSERT INTO mypoint VALUES (1,0) --подія

-- процедура
-- кліентам, у яких кредитний ліміт більше вартості квитка, встановлюється що вони оплатили квиток 
DELIMITER $$ ; 
CREATE PROCEDURE my_proc()
UPDATE mypoint, main, card, ticket SET main.paid=mypoint.point WHERE main.card_id=card.id 
AND main.ticket_id=ticket.id AND ticket.cost<card.card_limit AND mypoint.id=1  AND main.paid=0;
$$
DELIMITER ; $$ 


-- тригер(ввімкненя/вимкнення з інтерфейсу користувача)
-- виклик процедури при додані нового кліента
DROP TRIGGER IF EXISTS `Main_Trigger`

CREATE TRIGGER  `Main_Trigger` BEFORE INSERT ON `main`
FOR EACH ROW BEGIN
  SET NEW.paid = 1;
END
-- подія(налаштування часових параметрав через інтерфейс користувача)
SET GLOBAL event_scheduler=on;

DELIMITER $$ ; 
DROP EVENT IF EXISTS my_event$$
CREATE EVENT `my_event`
  ON SCHEDULE EVERY 1 WEEK STARTS CURRENT_TIMESTAMP
  ON COMPLETION NOT PRESERVE
  ENABLE
  COMMENT ''  DO
call my_proc();
$$
DELIMITER ; $$ 

ALTER EVENT 'my_event' ON SCHEDULE EVERY 1 WEEK;

-- транзакції 
SHOW VARIABLES LIKE '%tx_isolation%'; --REPEATABLE READ

SET TRANSACTION ISOLATION LEVEL READ UNCOMMITTED;
SET TRANSACTION ISOLATION LEVEL REPEATABLE READ;

START TRANSACTION;

INSERT INTO main(paid, client_id, ticket_id, airline_id, card_id) VALUES(0,1,1,1,1);

SELECT * FROM main;

COMMIT;
