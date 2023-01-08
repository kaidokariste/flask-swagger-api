-- From https://andmed.stat.ee/et/stat/majandus__hinnad/IA02/table/tableViewLayout2
CREATE TABLE tarbijahinnaindeks
(
    id                                  SERIAL PRIMARY KEY,
    order_date                          DATE NOT NULL,
    year                                INTEGER,
    month                               VARCHAR,
    index_value                         NUMERIC,
    change_to_previous_month            NUMERIC,
    change_to_previous_month_in_percent NUMERIC
);

SELECT * FROM tarbijahinnaindeks;

ALTER TABLE tarbijahinnaindeks
    ADD CONSTRAINT index_unique UNIQUE (year, month);

-- Insert base value of 1997 - 100pts manually
INSERT INTO tarbijahinnaindeks(order_date, year, month, index_value                               )
VALUES
    ('1998-02-01', 1998, 'Veebruar', 106.59);


----------------------------------------------------------------------
-- Create trigger

CREATE OR REPLACE FUNCTION public.insert_thi_index_change() RETURNS TRIGGER AS
$$
DECLARE
    previous_value               NUMERIC;
    var_change_to_previous_month NUMERIC;
    var_change_in_percentage     NUMERIC(20, 2);
BEGIN
    IF TG_OP IN ('INSERT') THEN
        previous_value := (SELECT index_value
                           FROM tarbijahinnaindeks
                           WHERE DATE_TRUNC('month', order_date) =
                                 DATE_TRUNC('month', NEW.order_date - INTERVAL '1 month'));

        var_change_to_previous_month := NEW.index_value - previous_value;
        var_change_in_percentage := (var_change_to_previous_month / previous_value) * 100;

        UPDATE tarbijahinnaindeks
        SET change_to_previous_month            = var_change_to_previous_month,
            change_to_previous_month_in_percent = var_change_in_percentage
        WHERE order_date = NEW.order_date;
    END IF;
    RETURN new;


END;
$$ LANGUAGE plpgsql;

	CREATE TRIGGER update_thi_change_in_table
	AFTER INSERT
	ON public.tarbijahinnaindeks
	FOR EACH ROW
	EXECUTE PROCEDURE public.insert_thi_index_change();