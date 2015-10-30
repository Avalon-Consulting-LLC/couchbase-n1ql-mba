from couchbase.bucket import Bucket

bucket = Bucket("couchbase://localhost/retail")
f = open('retail.txt','r')
count = 1
inserts = dict()

for line in f:
    items = map(int, line.strip().split(" "))
    inserts["order::%d" % count] = {'type': 'order', 'items': items}
    count += 1
    if count % 1000 == 0:
        bucket.upsert_multi(inserts)
        inserts = dict()
        print "Inserted %d docs" % count
bucket.upsert_multi(inserts)
print
print "Finished inserting %d total documents." % count
