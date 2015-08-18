# Couchbase Market Basket Analysis with N1QL
This repository is companion code for a blog post on our site: ADD.

This project is an all in one environment that sets up a Vagrant machine with Couchbase installed with a fresh bucket and primary index for running N1QL. It has a Python script that employs an example N1QL query for gathering product recommendations on the fly for a given product ID.

Sample data taken from:

	Brijs T., Swinnen G., Vanhoof K., and Wets G. (1999), The use of association rules for product
	assortment decisions: a case study, in: Proceedings of the Fifth International Conference on
	Knowledge Discovery and Data Mining, San Diego (USA), August 15-18, pp. 254-260. ISBN:
	1-58113-143-7.
	
Can be found under the 'retail' link here: http://fimi.ua.ac.be/data/

Prerequisites
-------------
1. Install Virtualbox: https://www.virtualbox.org/wiki/Downloads

2. Install Vagrant: http://www.vagrantup.com/downloads.html

3. Install necessary Vagrant plugins:

```sh
vagrant plugin install vagrant-hostmanager
vagrant plugin install vagrant-cachier
```

4. Install Ansible

```sh
brew install ansible
```

Getting Started
------
Start by bringing up the Vagrant machine, it is configured to install everything you need to run the analysis

```sh
vagrant up
```

Load the sample data by SSHing into the machine and running the tocb.py script.

```sh
vagrant ssh
cd /vagrant
python tocb.py
```

Once the data is in Couchbase, you can run the Python script to gether recommendations for a specific ID.

```sh
python query.py 39
```

You can access the Couchbase UI at retail.vagrant:8091 with credentials: couchbase//couchbase