from couchbase.bucket import Bucket
from couchbase.n1ql import N1QLQuery
import sys

# Check for expected number of arguments
if len(sys.argv) > 2:
    print "Too many arguments."
    sys.exit(1)
elif len(sys.argv) < 2:
    print "Specify Product ID."
    sys.exit(1)

# Ensure that the argument given is an int
try:
    product_id = int(sys.argv[1])
except ValueError:
    print "Product ID must be an Integer."
    sys.exit(1)

# Open the Couchbase bucket
bucket = Bucket("couchbase://localhost/retail")

# Create our parameterized query
query_string = """select item, count(*) as cnt
                  from retail
                  unnest items as item
                  where item != $id and $id in retail.items
                  group by item
                  order by cnt desc
                  limit 3;
               """
query = N1QLQuery(query_string, id=product_id)

# Run the query and print the results
for row in bucket.n1ql_query(query):
	print row

