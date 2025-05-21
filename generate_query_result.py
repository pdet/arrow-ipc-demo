import duckdb

con = duckdb.connect()

con.execute("INSTALL tpch")

con.execute("LOAD tpch")


con.execute("CALL dbgen(sf=1)")


con.execute("INSTALL arrow FROM community")

con.execute("LOAD arrow")


# Store Query 01 result in an Arrow file
con.execute('''COPY (SELECT
    l_returnflag,
    l_linestatus,
    sum(l_quantity) AS sum_qty,
    sum(l_extendedprice) AS sum_base_price,
    sum(l_extendedprice * (1 - l_discount)) AS sum_disc_price,
    sum(l_extendedprice * (1 - l_discount) * (1 + l_tax)) AS sum_charge,
    avg(l_quantity) AS avg_qty,
    avg(l_extendedprice) AS avg_price,
    avg(l_discount) AS avg_disc,
    count(*) AS count_order
FROM
    lineitem
WHERE
    l_shipdate <= CAST('1998-09-02' AS date)
GROUP BY
    l_returnflag,
    l_linestatus
ORDER BY
    l_returnflag,
    l_linestatus
) TO \'q01.arrows\'''')
