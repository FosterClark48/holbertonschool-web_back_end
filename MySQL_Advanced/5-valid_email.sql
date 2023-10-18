-- script that creates a trigger that resets the attribute valid_email only when the email has been changed
-- Good for email validation
DROP TRIGGER IF EXISTS  email_update;

DELIMITER //
CREATE TRIGGER email_update
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
    IF NEW.email <> OLD.email THEN
        SET NEW.valid_email = 0;
    END IF;
END;
//
DELIMITER ;
